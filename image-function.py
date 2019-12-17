import os
import uuid
import boto3
from botocore.exceptions import ClientError

u = uuid.uuid4();
id = str(u.int)[:5]

BUCKET_NAME = 'testbucketimgloftly'
FILE_NAME, extension = os.path.splitext('pexels-photo-414612.jpeg')

VALID_EXTENSIONS = { '.png': True, '.jpeg': True, '.pdf' : True, '.webp': True}

# connect to bucket
s3 = boto3.client('s3')
if extension in VALID_EXTENSIONS:
    s3.upload_file(FILE_NAME + extension, BUCKET_NAME, 'loftly_image' + id + extension)
    print("Image Saved to S3 Bucket")
elif extenstion not in VALID_EXTENSIONS:
    raise Exception('Not Valid Image Format')

print("Done")
