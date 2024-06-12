import subprocess
import json

def run_aws_cli(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
        return None
    return json.loads(result.stdout)

def regions():
    command = "aws ec2 describe-regions --query 'Regions[].RegionName' --output json"
    return run_aws_cli(command)

def services_supported():
    return [
        'ec2', 's3', 'lambda', 'sns', 'sqs', 'cloudformation', 'cloudwatch', 'iam'
    ]

def cli_command(region, service):
    service_commands = {
        'ec2': f"aws ec2 describe-instances --region {region} --query 'Reservations[].Instances[]' --output json",
        's3': f"aws s3api list-buckets --region {region} --query 'Buckets' --output json",
        'lambda': f"aws lambda list-functions --region {region} --query 'Functions' --output json",
        'sns': f"aws sns list-topics --region {region} --query 'Topics' --output json",
        'sqs': f"aws sqs list-queues --region {region} --output json",
        'cloudformation': f"aws cloudformation list-stacks --region {region} --query 'StackSummaries' --output json",
        'cloudwatch': f"aws cloudwatch describe-alarms --region {region} --query 'MetricAlarms' --output json",
        'iam': "aws iam list-users --query 'Users' --output json"
    }

    if service not in service_commands:
        print(f"Service {service} is not supported.")
        return None

    command = service_commands[service]
    return run_aws_cli(command)

def main():
    available_regions = regions()
    if available_regions is None:
        return

    print("Available regions:")
    for i, region in enumerate(available_regions, start=1):
        print(f"{i}. {region}")
    
    region_choice = int(input("Select a region by entering the corresponding number: "))
    selected_region = available_regions[region_choice - 1]

    services = services_supported()
    print("\nAvailable services:")
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")
    
    service_choice = int(input("Select a service by entering the corresponding number: "))
    selected_service = services[service_choice - 1]

    # Fetch and print the details for the selected service and region
    print(f"\nFetching details for {selected_service} in region {selected_region}...")
    service_details = cli_command(selected_region, selected_service)

    # Print the details
    if service_details:
        print(f"\nService: {selected_service} in Region: {selected_region}")
        print(json.dumps(service_details, indent=2))

if __name__ == "__main__":
    main()
