**#Security & Risk Monitoring Platform**

This project demonstrates a lightweight security monitoring platform that combines:

->Access provisioning monitoring
->Enterprise risk analytics
->Security dashboards

The goal is to simulate how security teams monitor identity access activity, operational risks, and system integrations using automated data pipelines and dashboards.

The platform contains two main modules: 
                
                 +-----------------------------+
                 |  Security Monitoring Module |
                 |  Access Provisioning Audit  |
                 +-------------+---------------+
                               |
                               | Access Data / Logs
                               v
                      Python Monitoring Script
                               |
                               v
                        Monitoring Dashboard


                 +-----------------------------+
                 |  Enterprise Risk Monitoring |
                 |        Analytics Module     |
                 +-------------+---------------+
                               |
                               | Jira Issues
                               v
                        Python ETL Pipeline
                        (Jira REST API)
                               |
                               v
                          BigQuery Tables
                               |
                               v
                        Risk Scoring Model
                               |
                               v
                        Risk Analytics Dashboard

                        
**Module 1 — Access Provisioning Monitoring**

This module simulates monitoring of identity access provisioning across security systems. The script pulls identity records from an API, assigns access roles and statuses, and generates monitoring metrics used by dashboards. This mirrors how organizations monitor IAM provisioning workflows and system integrations.

**Access Monitoring Architecture**
Identity API → Python Access Monitor → Monitoring Dataset → Dashboard

**Access Monitoring Script**

security_application_monitor/access_provisioning_monitor.py

The script performs the following steps:

1. Retrieves user records from an API
2. Assigns simulated access roles
3. Generates access provisioning statuses
4. Measures integration health metrics
5. Exports the monitoring dataset
   
 **  Access Monitoring Metrics**

The dataset produced by the script includes metrics such as:

- Total access requests
- Access status distribution (Approved, Pending, Rejected, Revoked)
- Access by role (Employee, Contractor, Admin)
- API response time
- API status code
- Records processed

These metrics simulate monitoring of identity provisioning pipelines and security integrations.

**Access Monitoring Dashboard**

The dashboard visualizes identity activity including:
- total access requests
- access status distribution
- access by role
 -system integration health metrics

This demonstrates how security teams track access governance and identity lifecycle events.

** Dashboard export: security_application_monitor/security_access_monitoring_dashboard.pdf

**Module 2 — Enterprise Risk Monitoring Pipeline**

This module demonstrates a data analytics pipeline for monitoring operational and compliance risks. The pipeline transforms issue tracking data into structured analytics models used to monitor risk signals and SLA breaches.

**Risk Monitoring Architecture**
Jira API → Python ingestion script → BigQuery raw tables→ SQL transformation → Risk scoring model → Dashboard

**What the Risk Pipeline Does**

The pipeline performs the following tasks:
1. extracts issue data from Jira using the REST API
2. loads the data into BigQuery
3. transforms operational issue data into analytics tables
4. calculates weighted risk scores
5. enables dashboards for monitoring risk signals

This mirrors how organizations transform operational issue tracking systems into continuous risk monitoring platforms.

**Data Pipeline Components**
- Jira Data Ingestion
- jira_to_bigquery.py
- Python script that extracts issue data from the Jira REST API and loads it into BigQuery.

Example fields ingested:
issue_id
status
created_date
last_updated
due_date
summary

**BigQuery Tables**

1. jira_issues_raw - Raw issue data extracted directly from Jira.
2. issues_raw - Governance metadata used for risk evaluation.
3. issues_joined - Combined dataset that joins Jira operational data with governance metadata. This dataset allows issue monitoring across products, teams, and regulatory categories.
4. issues_scored_final - Final analytics dataset used by the monitoring dashboard.

 **  Risk Scoring Model**

The risk scoring model prioritizes issues based on severity, sensitivity, and aging.

Risk Score Formula -> 
(severity_weight × 2) + (sensitivity_weight × 2) + (aging_weight × 1)

**Security & Risk Dashboard**

The Looker Studio dashboard provides two monitoring views:

1. Access Provisioning Monitoring:
Tracks identity access activity and provisioning trends.

2. Enterprise Risk Monitoring:
Tracks operational risks, SLA breaches, and risk score distributions.

These dashboards demonstrate how security teams can build continuous monitoring systems for operational risk and access governance.

**Technologies Used**

Python
Pandas
REST APIs
SQL
Google BigQuery
Google Sheets
Looker Studio
GitHub



