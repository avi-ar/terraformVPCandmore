import boto3

def lambda_handler(event, context):
    region = 'eu-central-1'
    instances = get_instance_id()
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=[instances])

    print('started your instances: ' + str(instances))
    return {
        'message': 'EC2 instance started successfully'
    }

def get_instance_id():
  session = boto3.Session()
  client = session.client('ec2')

  response = client.describe_instances()

  for instance in response['Reservations'][0]['Instances']:
    if instance['ImageId'] == 'ami-0749e2c902c836c08':
      return instance['InstanceId']

