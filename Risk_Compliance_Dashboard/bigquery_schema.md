# BigQuery Schema

Dataset: risk_analysis

## Tables

### jira_issues_raw
Stores issue data ingested from Jira API.

Columns:
- issue_id
- issue_type
- status
- summary
- created_date
- last_updated
- due_date

### issues_raw
Metadata table containing security and compliance attributes.

Columns:
- issue_id
- product_area
- issue_type
- severity
- data_sensitivity
- regulation
- owner_team
- detected_via
- open_days
- created_date
- last_updated_date

### issues_joined
Joined dataset combining metadata with operational Jira issue data.

### issues_scored_final
Final analytics table used for risk monitoring dashboards.
