import boto3
from settings import *


class Aws:
    def __init__(self):
        pass

    def connection_aws(self, service):
        return boto3.client(service, region_name=AWS_REGION,
                            aws_access_key_id=AWS_ACCESS_KEY,
                            aws_secret_access_key=AWS_SECRET_KEY)
