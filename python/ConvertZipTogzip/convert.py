import os
import boto3
import io
import zipfile
import gzip

TARGET_PREFIX = os.environ['TARGET_PREFIX']


def recompression(bucket_name, source_object_key):
    if source_object_key.endswith('.zip'):
        s3 = boto3.resource('s3')
        zip_obj = s3.Object(bucket_name=bucket_name, key=source_object_key)
        buffer = io.BytesIO(zip_obj.get()['Body'].read())

        z = zipfile.ZipFile(buffer)
        for filename in z.namelist():
            s3.meta.client.upload_fileobj(
                io.BytesIO(gzip.compress(z.read(filename))),
                Bucket=bucket_name,
                Key=f'{TARGET_PREFIX}{filename}.gz'
            )
            print(
                f'created object s3://{bucket_name}/{TARGET_PREFIX}{filename}.gz')


def lambda_handler(event, context):
    for record in event['Records']:
        eventName = record['eventName']
        if eventName.startswith('ObjectCreated:'):
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
            print(
                f'handling event {eventName} for s3://{bucket_name}/{object_key}')
            try:
                recompression(bucket_name, object_key)
            except Exception as e:
                print(
                    f'Error while recompressing s3://{bucket_name}/{object_key}: {e}')
