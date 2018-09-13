import os
import json
from unittest import TestCase
from nose.tools import eq_, ok_, raises
from datas_utils import aws
from boto3.session import Session

class S3TestCase(TestCase):
    BUCKETNAME = 'datas-dev'
    KEY_PREFIX    = 'datas_utils_test/'
    TEST_FILE = 'test.json'
    TEST_CONTENT = {
        "a": 1,
        "b": 2,
    }
    TEST_MULTILINE_CONTENT = "ABC\nEFG"

    def setUp(self):
        self.aws_access_key_id     = os.environ["AWS_ACCESS_KEY_ID"]
        self.aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
        self.region_name           = os.environ["REGION_NAME"]

        self.s3 = aws.S3(
                         aws_access_key_id     = self.aws_access_key_id,
                         aws_secret_access_key = self.aws_secret_access_key,
                         region_name           = self.region_name,
        )

        self._delete_objects()

    def tearDown(self):
        self._delete_objects()

    def test_s3_get_put(self):
        self.s3.put(self.BUCKETNAME, 
                    self.KEY_PREFIX+self.TEST_FILE,
                    self.TEST_CONTENT,
                    "text/json")
        stream = self.s3.get(self.BUCKETNAME, 
                             self.KEY_PREFIX+self.TEST_FILE)
        content = json.load(stream)
        eq_(content, self.TEST_CONTENT)

    def test_s3_str_get_put(self):
        self.s3.put(self.BUCKETNAME, 
                    self.KEY_PREFIX+self.TEST_FILE,
                    json.dumps(self.TEST_CONTENT),
                    "text/json")
        stream = self.s3.get(self.BUCKETNAME, 
                             self.KEY_PREFIX+self.TEST_FILE)
        content = json.load(stream)
        eq_(content, self.TEST_CONTENT)

    def test_s3_bytes_get_put(self):
        self.s3.put(self.BUCKETNAME, 
                    self.KEY_PREFIX+self.TEST_FILE,
                    json.dumps(self.TEST_CONTENT).encode(),
                    "text/json")
        stream = self.s3.get(self.BUCKETNAME, 
                             self.KEY_PREFIX+self.TEST_FILE)
        content = json.load(stream)
        eq_(content, self.TEST_CONTENT)

    def test_s3_get_put_readlines(self):
        self.s3.put(self.BUCKETNAME, 
                    self.KEY_PREFIX+self.TEST_FILE,
                    self.TEST_MULTILINE_CONTENT,
                    "text/plain")
        stream = self.s3.get(self.BUCKETNAME, 
                             self.KEY_PREFIX+self.TEST_FILE)
        content = '\n'.join([line.decode() for line in stream.iter_lines()])
        eq_(content, self.TEST_MULTILINE_CONTENT)

    def test_s3_list(self):
        self.s3.put(self.BUCKETNAME, 
                    self.KEY_PREFIX+"1-"+self.TEST_FILE,
                    json.dumps(self.TEST_CONTENT).encode(),
                    "text/json")
        self.s3.put(self.BUCKETNAME, 
                    self.KEY_PREFIX+"2-"+self.TEST_FILE,
                    json.dumps(self.TEST_CONTENT).encode(),
                    "text/json")
        keys = self.s3.list(self.BUCKETNAME, self.KEY_PREFIX)
        eq_(set(keys), set([
                            self.KEY_PREFIX+"1-"+self.TEST_FILE,
                            self.KEY_PREFIX+"2-"+self.TEST_FILE,
        ]))

    def _delete_objects(self):
        session = Session(
                          aws_access_key_id     = self.aws_access_key_id,
                          aws_secret_access_key = self.aws_secret_access_key,
                          region_name           = self.region_name,
        )
        s3 = session.resource('s3')
        bucket = s3.Bucket(self.BUCKETNAME)
        for obj in bucket.objects.filter(Prefix=self.KEY_PREFIX):
            obj.delete()
