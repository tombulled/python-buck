# import boto3
import buck.client
from rich.pretty import pprint as pp

# client = boto3.client \
# (
#     's3',
#     endpoint_url = 'http://127.0.0.1:8000',
#     config = boto3.session.Config(signature_version = 's3v4'),
# )

client = buck.client.client()

pp(client.list_buckets())
