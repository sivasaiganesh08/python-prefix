import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--prefix', help="Prefix")
parser.add_argument('--folder_name', help="folder name")
parser.add_argument('--bucket_name', help="bucket name")
parser.add_argument('--key_id', help="key id")
parser.add_argument('--secret_key', help="secret key")
args = parser.parse_args()

s3 = boto3.client('s3', 
                      aws_access_key_id = args.key_id, 
                      aws_secret_access_key = args.secret_key, 
                      region_name = "us-east-1"
                      )

s3.put_object(Bucket=args.bucket_name, Key=(args.prefix+'/'+args.folder_name+'/'))
