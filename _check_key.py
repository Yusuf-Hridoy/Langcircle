import os
from langsmith import Client

client = Client(
    api_key="lsv2_pt_your_copied_key_here",
    api_url="https://eu.api.smith.langchain.com"
)

try:
    project = client.read_project(project_name="Unit")
    print(f"Success on EU endpoint! Connected to: {project.name}")
except Exception as e:
    print(f"EU endpoint failed: {e}")