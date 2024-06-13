# devops-assignment

## Ideally scope of project: 

We combine all four tasks into a single requirement. Use CloudFormation to create the necessary resources for the upcoming tasks. Develop an Ansible playbook to set up a web server with SSL certificates. Create an AMI with the Ansible playbook and use this AMI to launch instances behind load balancers. Ensure the instances have a role to access an S3 bucket for image retrieval. Finally, create a script to monitor AWS resources and provide details about them.


## Scope of improvements: 

- We can streamline the entire process to automatically get the ID of resources and use them in the terraform/cloudformation for creating Scaling group. 
- Also can use terraform as well for creating all resources. 
- For the script we can use boto3 for more refined results.  


