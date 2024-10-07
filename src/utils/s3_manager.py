import asyncio
import base64
import random
import string

import boto3


class S3Manager:
    aws_access_key_id = '9C4DCVTWTOEDTA0CXSN8'
    aws_secret_access_key = 'MtZmw0KVxmLEAT4eUyXbAoQjuD5B64pX12uSsfBA'
    bucket_name = 'f2c55d23-27cefacd-9fc8-442f-9c9d-422afd419dad'

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                      endpoint_url='https://s3.timeweb.cloud')

    @classmethod
    def generate_random_name(cls):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(20))

    @classmethod
    async def save_object(cls, file, type_file: str):
        file_name = cls.generate_random_name()
        binary_data = base64.b64decode(file.split(',')[1])
        cls.s3.put_object(Body=binary_data, Bucket=cls.bucket_name, Key=f"{file_name}.{type_file}")

        return f"https://s3.timeweb.cloud/f2c55d23-27cefacd-9fc8-442f-9c9d-422afd419dad/{file_name}.{type_file}"


if __name__ == '__main__':
    asyncio.run(S3Manager.save_object("000", "png"))