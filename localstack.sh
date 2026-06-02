#!/bin/bash
echo "Initializing LocalStack infrastructure..."

# Create the bucket (fails silently if it exists)
awslocal s3 mb s3://bucket || true

# Apply Global CORS policy
CORS_CONFIG='{
    "CORSRules": [
        {
            "AllowedOrigins": ["*"],
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
            "ExposeHeaders": ["ETag", "Location"]
        }
    ]
}'

# Apply to all existing buckets
for bucket in $(awslocal s3api list-buckets --query "Buckets[].Name" --output text); do
    echo "Applying CORS to bucket: $bucket"
    awslocal s3api put-bucket-cors --bucket "$bucket" --cors-configuration "$CORS_CONFIG"
done