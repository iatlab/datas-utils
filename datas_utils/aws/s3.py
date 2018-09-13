import json
from boto3.session import Session

class S3(object):

    ENCODING = 'utf-8'

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.session = Session(
                               aws_access_key_id     = aws_access_key_id,
                               aws_secret_access_key = aws_secret_access_key,
                               region_name           = region_name,
        )
    
    def get(self, bucketname, keyname):
        obj = self._get_bucket_object(bucketname, keyname)
        response = obj.get()['Body']
        return response

    def list(self, bucketname, prefix):
        s3 = self.session.resource('s3')
        bucket = s3.Bucket(bucketname)
        for obj in bucket.objects.filter(Prefix=prefix):
            yield obj.key

    def put(self, bucketname, keyname, content, content_type):
        if isinstance(content, str):
            content = content.encode(self.ENCODING)
        if not isinstance(content, bytes):
            content = json.dumps(content).encode(self.ENCODING)

        obj = self._get_bucket_object(bucketname, keyname)
        response = obj.put(
            Body=content,
            ContentEncoding=self.ENCODING,
            ContentType=content_type,
        )
        return response

    def _get_bucket_object(self, bucketname, keyname):
        s3 = self.session.resource('s3')
        bucket = s3.Bucket(bucketname)
        obj = bucket.Object(keyname)
        return obj

