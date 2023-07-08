import boto3
region = 'eu-central-1'
def lambda_handler(event,contex):
    
    instances = get_instance_id()
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=[instances])

    print('stopped your instances: ' + str(instances))
    return {
        'message': 'EC2 instance stopped successfully'
    }

def get_instance_id():
  session = boto3.Session()
  client = session.client('ec2')

  response = client.describe_instances()

  for instance in response['Reservations'][0]['Instances']:
    if instance['ImageId'] == 'ami-0749e2c902c836c08':
      return instance['InstanceId']

lambda_handler()