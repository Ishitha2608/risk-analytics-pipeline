Enterprise Risk Monitoring Pipeline:

This module demonstrates a data analytics pipeline for monitoring operational and compliance risks. The pipeline transforms issue tracking data into structured analytics models used to monitor risk signals and SLA breaches.

Risk Monitoring Architecture: Jira API → Python ingestion script → BigQuery raw tables→ SQL transformation → Risk scoring model → Dashboard

What the Risk Pipeline Does:-

The pipeline performs the following tasks:

-extracts issue data from Jira using the REST API
-loads the data into BigQuery
-transforms operational issue data into analytics tables
-calculates weighted risk scores
-enables dashboards for monitoring risk signals
This mirrors how organizations transform operational issue tracking systems into continuous risk monitoring platforms.

Data Pipeline Components:

1. Jira Data Ingestion
2. jira_to_bigquery.py
3. Python script that extracts issue data from the Jira REST API and loads it into BigQuery.
Example fields ingested: issue_id status created_date last_updated due_date summary

BigQuery Tables:

-jira_issues_raw - Raw issue data extracted directly from Jira.
-issues_raw - Governance metadata used for risk evaluation.
-issues_joined - Combined dataset that joins Jira operational data with governance metadata. This dataset allows issue monitoring across products, teams, and regulatory categories.
-issues_scored_final - Final analytics dataset used by the monitoring dashboard.

** Risk Scoring Model**

The risk scoring model prioritizes issues based on severity, sensitivity, and aging.

Risk Score Formula -> (severity_weight × 2) + (sensitivity_weight × 2) + (aging_weight × 1)

Security & Risk Dashboard:-

The Looker Studio dashboard provides two monitoring views:

Access Provisioning Monitoring: Tracks identity access activity and provisioning trends.

Enterprise Risk Monitoring: Tracks operational risks, SLA breaches, and risk score distributions.

These dashboards demonstrate how security teams can build continuous monitoring systems for operational risk and access governance.

Technologies Used

Python Pandas REST APIs SQL Google BigQuery Google Sheets Looker Studio GitHub
