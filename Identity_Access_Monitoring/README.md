# Identity & Access Provisioning Monitoring

This module simulates how security teams monitor user access provisioning across enterprise systems. It focuses on tracking access requests, role assignments, and system integration health using automated data pipelines and dashboards.

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

---

## Overview

The goal of this module is to replicate real-world Identity and Access Management (IAM) monitoring by:

- Tracking user access requests  
- Monitoring provisioning status  
- Evaluating system integration performance  
- Generating metrics for security visibility  

---

## Architecture

Identity API → Python Monitoring Script → Monitoring Dataset → Dashboard

---

## Implementation

**Script Location:**  
`Identity_Access_Monitoring/access_provisioning_monitor.py`

---

## What the Script Does

- Retrieves user access records from an API  
- Assigns simulated roles (Employee, Contractor, Admin)  
- Generates provisioning statuses (Approved, Pending, Rejected, Revoked)  
- Measures API response time and system health  
- Exports processed data for dashboard visualization  

---

## Key Metrics

The system generates:

- Total access requests  
- Access status distribution  
- Access by role  
- API response time  
- API status codes  
- Total records processed  

---

## Dashboard Insights

The dashboard provides visibility into:

- Access request trends  
- Provisioning status distribution  
- Role-based access patterns  
- System integration performance  

---

## Why This Matters

This module demonstrates how organizations:

- Monitor IAM provisioning workflows  
- Detect delays or failures in access requests  
- Track system reliability and integrations  
- Build real-time visibility into access control processes  

---

            
