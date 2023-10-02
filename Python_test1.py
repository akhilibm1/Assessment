import io
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('akhil_storage1')
blob = bucket.blob('Test File.txt')
data = blob.download_as_string()
print(data.decode('utf-8'))