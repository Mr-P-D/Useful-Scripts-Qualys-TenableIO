import base64
import subprocess
import time
 
# Base64-encoded credentials provided
base64_credentials = "dXNlcm5hbWU6cGFzc3dvcmQ="
 
# Decode the Base64 credentials to plain text
decoded_credentials = base64.b64decode(base64_credentials).decode('utf-8')
 
# Extract username and password
username, password = decoded_credentials.split(":")
 
# Prompt the user for ticket values
since_ticket = input("Enter the 'since_ticket' value: ")
until_ticket = input("Enter the 'until_ticket' value: ")
 
# Define the API endpoint
url = f"https://qualysapi.qg1.apps.qualys.ae/msp/ticket_delete.php?since_ticket_number={since_ticket}&until_ticket_number={until_ticket}"
 
# Prepare the curl command
curl_command = [
    "curl", "-k", "-u", f"{username}:{password}",
    "-H", "X-Requested-With: Curl",
    "-X", "GET", url
]

# Record the start time
start_time = time.time()
 
# Execute the curl command using subprocess
result = subprocess.run(curl_command, capture_output=True, text=True)
 
# Record the end time
end_time = time.time()
 
# Calculate the time taken
execution_time = end_time - start_time
 
# Print the output and time taken
print(f"Status Code: {result.returncode}")
#print(f"Response: {result.stdout}")
print(f"Time taken for execution: {execution_time:.2f} seconds")