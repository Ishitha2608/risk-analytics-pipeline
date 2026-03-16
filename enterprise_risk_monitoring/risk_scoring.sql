-- Enterprise Risk Scoring Model

SELECT
  issue_id,
  product_area,
  issue_type,
  severity,
  data_sensitivity,
  regulation,
  owner_team,
  detected_via,

  
  jira_status AS status,
  DATE(jira_created_date) AS created_date,
  DATE(jira_last_updated) AS last_updated_date,
  due_date,
  summary,

  
  DATE_DIFF(CURRENT_DATE(), DATE(jira_created_date), DAY) AS open_days,

  
  CASE
    WHEN severity = "S1" THEN 3
    WHEN severity = "S2" THEN 2
    WHEN severity = "S3" THEN 1
    ELSE 1
  END AS severity_weight,

  
  CASE
    WHEN data_sensitivity = "HIGH" THEN 3
    WHEN data_sensitivity = "MEDIUM" THEN 2
    WHEN data_sensitivity = "LOW" THEN 1
    ELSE 1
  END AS sensitivity_weight,

  
  CASE
    WHEN DATE_DIFF(CURRENT_DATE(), DATE(jira_created_date), DAY) < 60 THEN 1
    WHEN DATE_DIFF(CURRENT_DATE(), DATE(jira_created_date), DAY) <= 120 THEN 2
    ELSE 3
  END AS aging_weight,

  -- Final risk score
  (
    (
      CASE
        WHEN severity = "S1" THEN 3
        WHEN severity = "S2" THEN 2
        WHEN severity = "S3" THEN 1
        ELSE 1
      END * 2
    )
    +
    (
      CASE
        WHEN data_sensitivity = "HIGH" THEN 3
        WHEN data_sensitivity = "MEDIUM" THEN 2
        WHEN data_sensitivity = "LOW" THEN 1
        ELSE 1
      END * 2
    )
    +
    (
      CASE
        WHEN DATE_DIFF(CURRENT_DATE(), DATE(jira_created_date), DAY) < 60 THEN 1
        WHEN DATE_DIFF(CURRENT_DATE(), DATE(jira_created_date), DAY) <= 120 THEN 2
        ELSE 3
      END * 1
    )
  ) AS risk_score

FROM `noogler-2026.risk_analysis.issues_joined`;
