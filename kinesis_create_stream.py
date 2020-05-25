import boto3
from settings import *
import json
import uuid


class Aws:
    def __init__(self):
        pass

    def connection_aws(self, service):
        return boto3.client(service, region_name=AWS_REGION,
                            aws_access_key_id=AWS_ACCESS_KEY,
                            aws_secret_access_key=AWS_SECRET_KEY)


class Kinesis(Aws):
    def __init__(self):
        super(Kinesis, self).__init__()
        self.kinesis = self.connection_aws(service="kinesis")

    def get_status(self):
        r = self.kinesis.describe_stream(StreamName=AWS_KINESIS_STREAM_NAME)
        return r

    def create_stream(self, stream_name, shard_count):
        try:
            self.kinesis.create_stream(StreamName=stream_name,
                                       ShardCount=shard_count)

            print('stream {} created in region {}'.format(stream_name, AWS_REGION))
        except self.kinesis.exceptions.ResourceInUseException:
            print('stream {} already exists in region {}'.format(stream_name, AWS_REGION))

    def remove_stream(self, stream_name):
        return self.kinesis.delete_stream(StreamName=stream_name)

    def put_to_stream(self, payload, stream_name, partitionKey="auto"):
        if partitionKey == "auto":
            partitionKey = uuid.uuid4().hex

        put_response = self.kinesis.put_record(
            StreamName=stream_name,
            Data=json.dumps(payload),
            PartitionKey=partitionKey)

        return put_response
