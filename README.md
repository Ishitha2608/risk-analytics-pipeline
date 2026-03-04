# Enterprise Risk Monitoring Pipeline

This project demonstrates a data analytics pipeline that ingests issue data from Jira, stores it in BigQuery, and supports risk monitoring dashboards.

## Architecture

Jira API  
→ Python ingestion script  
→ BigQuery raw tables  
→ SQL risk scoring model  
→ Analytics dashboard

## Technologies
- Python
- Jira REST API
- Google BigQuery
- SQL

## Key Features
- Automated ingestion of Jira issues using Python
- Data normalization and schema mapping
- Risk scoring and analytics queries
- Foundation for real-time enterprise risk dashboards

## Example Use Case
Security,Risk and compliance teams can monitor:
- High-severity issues
- SLA breaches
- Aging risks
- Ownership by product team
