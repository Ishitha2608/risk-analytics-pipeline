import requests
from google.cloud import bigquery

# Jira credentials
JIRA_URL = "https://ishithamichael.atlassian.net"
EMAIL = "ishithamichael@gmail.com"
API_TOKEN = "YOUR_API_TOKEN"

# Jira project key
JIRA_PROJECT_KEY = "SAM1"

# BigQuery target table
BQ_TABLE = "noogler-2026.risk_analysis.jira_issues_raw"

# ------------------------
# HELPERS
# ------------------------

def jira_ts_to_rfc3339(ts: str):
    """
    Convert Jira timestamp like:
      '2026-02-20T09:42:17.755-0600'
    to RFC3339:
      '2026-02-20T09:42:17.755-06:00'
    which BigQuery accepts for TIMESTAMP fields.
    """
    if not ts:
        return None
    # Insert colon in timezone offset: -0600 -> -06:00
    if len(ts) >= 5 and (ts[-5] in ["+", "-"]) and ts[-4:].isdigit():
        return ts[:-2] + ":" + ts[-2:]
    return ts

def map_status(jira_status: str) -> str:
    """
    Map Jira statuses to your BigQuery normalized statuses.
    """
    if jira_status == "To Do":
        return "OPEN"
    if jira_status == "In Progress":
        return "IN PROGRESS"
    if jira_status == "Done":
        return "CLOSED"
    # Fallback: keep original if your Jira uses different names
    return jira_status or "OPEN"

# ------------------------
# MAIN
# ------------------------

def main():
    auth = (EMAIL, API_TOKEN)

    url = f"{JIRA_URL.rstrip('/')}/rest/api/3/search/jql"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "jira-to-bigquery-script/1.0",
    }

    payload = {
    "jql": f"project = {JIRA_PROJECT_KEY} order by created DESC",
    "maxResults": 50,
    "fields": ["summary", "status", "issuetype", "created", "updated", "duedate"],
    # optional, but safe:
    "fieldsByKeys": False
}
    response = requests.post(
        url,
        auth=auth,
        headers=headers,
        json=payload,
        timeout=30,
    )

    # Print Jira error (instead of crashing with unclear JSON errors)
    if response.status_code != 200:
        print("HTTP status:", response.status_code)
        print("Response:", response.text)
        raise SystemExit

    data = response.json()

    issues = data.get("issues", [])
    if not issues:
        print("No issues returned from Jira. (Check project key / permissions.)")
        return

    rows = []
    for issue in issues:
        f = issue.get("fields", {}) or {}

        jira_status = (f.get("status") or {}).get("name")
        status = map_status(jira_status)

        rows.append({
            "issue_id": issue.get("key"),
            "issue_type": (f.get("issuetype") or {}).get("name"),
            "status": status,
            "summary": f.get("summary"),
            "created_date": jira_ts_to_rfc3339(f.get("created")),
            "last_updated": jira_ts_to_rfc3339(f.get("updated")),
            "due_date": f.get("duedate"),  # Jira returns YYYY-MM-DD (BigQuery DATE ok)
        })

    client = bigquery.Client()
    errors = client.insert_rows_json(BQ_TABLE, rows)

    if errors:
        print("BigQuery insert errors:")
        print(errors)
    else:
        print(f"Rows inserted successfully: {len(rows)} into {BQ_TABLE}")

if __name__ == "__main__":
    main()
# BigQuery table
BQ_TABLE = "noogler-2026.risk_analysis.jira_issues_raw"

auth = (EMAIL, API_TOKEN)

url = f"{JIRA_URL.rstrip('/')}/rest/api/3/search/jql"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "jira-to-bigquery-script/1.0"
}

payload = {
    "jql": "project = SAM1 order by created DESC",
    "maxResults": 50,
    "fields": ["summary", "status", "issuetype", "created", "updated", "duedate"]
}

response = requests.post(
    url,
    json=payload,
    headers=headers,
    auth=auth,
    timeout=30
)
response.raise_for_status()
if response.status_code != 200:
    print("HTTP status:", response.status_code)
    print("Response:", response.text)
    raise SystemExit
data = response.json()

rows = []

for issue in data["issues"]:
    f = issue["fields"]

    status = (f.get("status") or {}).get("name")

    if status == "To Do":
        status = "OPEN"
    elif status == "In Progress":
        status = "IN PROGRESS"
    elif status == "Done":
        status = "CLOSED"

    rows.append({
        "issue_id": issue.get("key"),
        "issue_type": (f.get("issuetype") or {}).get("name"),
        "status": status,
        "summary": f.get("summary"),
        "created_date": f.get("created"),
        "last_updated": f.get("updated"),
        "due_date": f.get("duedate")
    })

client = bigquery.Client()

errors = client.insert_rows_json(BQ_TABLE, rows)

if errors == []:
    print("Rows inserted successfully")
else:
    print(errors)
if __name__ == "__main__":
    main()
