import boto3

ecs_client = boto3.client('ecs')
cw_client = boto3.client('logs')

running_containers = response = ecs_client.list_container_instances(
    cluster='<cluster_name>',
    filter=attribute:ecs.name == "task-*",
    #nextToken='string',
    #maxResults=123,
    status='ACTIVE'
)

active_streams = cw-client.describe_log_streams(
    logGroupName="/aws/lambda/task-*",
    orderBy='LastEventTime'
    #limit=1
)

running_containers = running_containers['containerInstanceArns'][0]

# This need to be paginated using nextToken, assume this is list for now
active_streams = active_streams['logStreams'][0]


# Filter both lists to extract task-* name from raw output
# ...

output = list(set(active_streams) - set(running_containers))


##################################################################################################
##################################################################################################
# V2
##################################################################################################
##################################################################################################


import boto3

def get_next_stream(next_token = ""):
    stream = cw-client.describe_log_streams(
        logGroupName="/aws/lambda/task-*",
        orderBy='LastEventTime'
        limit=1,
        nextToken=next_token
    )

    return[
            stream['logStreams'][0]["logStreamName"],
            stream['nextToken']
    ]

def find_hanging_ecs:

    ecs_client = boto3.client('ecs')
    cw_client = boto3.client('logs')

    running_containers = response = ecs_client.list_container_instances(
        cluster='<cluster_name>',
        filter=attribute:ecs.name == "task-*",
        #nextToken='string',
        #maxResults=123,
        status='ACTIVE'
    )

    running_containers = [ running_containers['containerInstanceArns'][0] ]
    for i in running_containers:
        running_containers[i] = i.split(",")[1]

    active_streams = []
    stream = get_next_stream("")
    active_streams.append(stream[0])
    next_token = stream[1]

    while next_token:
        stream get_next_stream(next_token)
        active_streams.append(stream[0])
        next_token = stream[1]

    output = list(set(active_streams) - set(running_containers))
    return(output
