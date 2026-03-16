# security application - access provisioning -  integration monitoring module
# Simulates monitoring of an enterprise security application integration
# Example: HR Identity System → PIAM Access Control System

import requests
import pandas as pd
import time

# HR identity system API
url = "https://jsonplaceholder.typicode.com/users"

# Measure API response time
start_time = time.time()
response = requests.get(url)
end_time = time.time()

response_time = round(end_time - start_time, 3)

# Convert API response to dataframe
data = response.json()
df = pd.DataFrame(data)

#  security system fields
df["system"] = "PIAM_access_control"

#  access statuses
statuses = ["pending", "approved", "rejected", "revoked"]
df["access_status"] = [statuses[i % len(statuses)] for i in range(len(df))]

#  user roles
roles = ["employee", "contractor", "admin"]
df["role"] = [roles[i % len(roles)] for i in range(len(df))]

# Monitoring metrics
records_received = len(df)
api_status = response.status_code

print("Access Provisioning Integration Report")
print("--------------------------------------")
print("API Status Code:", api_status)
print("API Response Time:", response_time, "seconds")
print("Access Requests Processed:", records_received)

print("\nSample Access Provisioning Records")
print(df[["id", "name", "email", "role", "access_status", "system"]].head())
