# Useful-Scripts-Qualys-&-TenableIO
Collection of Useful Scripts To Automate Some Basic Tasks In Qualys, Tenable IO
<br> Bulk-Asset-Group-Creation-Via-QualysAPI.py - Automatically creates asset groups in bulk with CSV Inputs.
<br> Bulk-Removal-Remediation-Tickets-Via-QualysAPI.py - Removing 20000 Remediation tickets at once, from the UI you are limited to 500.

# Usage
<br> python Bulk-Asset-Group-Creation-Via-QualysAPI.py
<br> python Bulk-Removal-Remediation-Tickets-Via-QualysAPI.py

# Things to modify before execution
url = " " # Replace with your Qualys Cloud Platform URL

# Basic authorization is used in the script:
<br> Replace dXNlcm5hbWU6cGFzc3dvcmQ= with your Qualys Cloud Platform Credentials in username:password base64 encoded format.
<br> Example: 
<br> if your username is prasad and password is qualys then you have to encode prasad:qualys in base64 and then use that encoded string instead of dXNlcm5hbWU6cGFzc3dvcmQ= in the code.
