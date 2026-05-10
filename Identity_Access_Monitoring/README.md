#Security & Risk Monitoring Platform

This project demonstrates a lightweight security monitoring platform that combines:

->Access provisioning monitoring ->Enterprise risk analytics ->Security dashboards

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
Access Provisioning Monitoring:

This module simulates monitoring of identity access provisioning across security systems. The script pulls identity records from an API, assigns access roles and statuses, and generates monitoring metrics used by dashboards. This mirrors how organizations monitor IAM provisioning workflows and system integrations.

Access Monitoring Architecture: Identity API → Python Access Monitor → Monitoring Dataset → Dashboard

Access Monitoring Script:-

security_application_monitor/access_provisioning_monitor.py

The script performs the following steps:

-Retrieves user records from an API
-Assigns simulated access roles
-Generates access provisioning statuses
-Measures integration health metrics
-Exports the monitoring dataset
** Access Monitoring Metrics**

The dataset produced by the script includes metrics such as:

-Total access requests
-Access status distribution (Approved, Pending, Rejected, Revoked)
-Access by role (Employee, Contractor, Admin)
-API response time
-API status code
-Records processed
These metrics simulate monitoring of identity provisioning pipelines and security integrations.

Access Monitoring Dashboard:-

The dashboard visualizes identity activity including:

-total access requests
-access status distribution
[access by role -system integration health metrics
This demonstrates how security teams track access governance and identity lifecycle events.

** Dashboard export: security_application_monitor/security_access_monitoring_dashboard.pdf
