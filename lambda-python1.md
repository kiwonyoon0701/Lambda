
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Start*",
                "ec2:Stop*",
                "ec2:Describe*"
            ],
            "Resource": "*"
        }
    ]
}
```
Name : ResourceSchedulePolicy

**Create Role**
```
Common Use cases : Lambda
Next
Next
Role Name : ResourceScheduleRole
```

**Create Lambda**
```
Create Function

Function Name : ResourceScheduler
Runtime : Python3.8
Execution Role : ResourceSchedulerRole
```

Name ResourceScheduleRole





import boto3

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters = [{'Name'   : 'instance-state-name',
                'Values' : ['running']}])

iids = [i.id for i in instances]

def lambda_handler(event, context):
    #ec2.stop_instances(InstanceIds=instances)
    #print('stopped your instances: ' + str(instances))
    print('stopped your instances: ' + str(iids))