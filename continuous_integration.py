import requests
import json

# Define the Jenkins API URL
jenkins_url = "http://jenkins_server:8080/jenkins"

# Define the Jenkins API token for authentication
api_token = "your_api_token"

# Define the Jenkins job name
job_name = "your_jenkins_job_name"

# Trigger a build of the Jenkins job
build_url = jenkins_url + "/job/" + job_name + "/build"
response = requests.post(build_url, auth=("api_token", api_token))

# Check the build status
build_number = response.headers["Location"].split("/")[-2]
build_info_url = jenkins_url + "/job/" + job_name + "/" + build_number + "/api/json"
build_info = requests.get(build_info_url, auth=("api_token", api_token)).json()

# Get the build status
build_status = build_info["result"]
print("Build status: " + build_status)

# Check if the build is successful
if build_status == "SUCCESS":
    # Deploy the application
    deployment_command = "your_deployment_command"
    subprocess.run(deployment_command, shell=True)
    print("Application deployed successfully")
else:
    print("Build failed, deployment skipped")
