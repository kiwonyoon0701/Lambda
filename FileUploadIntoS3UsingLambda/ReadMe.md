Reference : https://beomi.github.io/2017/12/15/Direct-upload-to-S3-with-Lambda/


s3-upload-using-lambda-kiwony

https://yr5udx91c1.execute-api.us-east-1.amazonaws.com/live

Creaate S3 Bucket

```
kiwony@kiwonymac.com:/Users/kiwony> aws s3 mb s3://s3-upload-using-lambda-kiwony --region us-east-1
kiwony@kiwonymac.com:/Users/kiwony> aws s3api put-public-access-block --bucket s3-upload-using-lambda-kiwony  --public-access-block-configuration  "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

kiwony@kiwonymac.com:/Users/kiwony/Documents/GitHub/Lambda/FileUploadIntoS3UsingLambda> cat cors.json
{
    "CORSRules": [
        {
            "AllowedOrigins": ["*"],
            "AllowedMethods": ["GET"],
            "AllowedHeaders": ["Authorization"],
            "MaxAgeSeconds":3000
        },
        {
            "AllowedOrigins": ["*"],
            "AllowedMethods": ["POST"],
            "AllowedHeaders": ["Authorization"],
            "MaxAgeSeconds":3000
        }
    ]
}

kiwony@kiwonymac.com:/Users/kiwony/Documents/GitHub/Lambda/FileUploadIntoS3UsingLambda> aws s3api put-bucket-cors --bucket s3-upload-using-lambda-kiwony --cors-configuration file://cors.json
 

```

Create IAM User

```
kiwony@kiwonymac.com:/Users/kiwony/Documents/GitHub/Lambda/FileUploadIntoS3UsingLambda> aws iam create-user --user-name s3-upload-using-lambda-kiwony


kiwony@kiwonymac.com:/Users/kiwony/Documents/GitHub/Lambda/FileUploadIntoS3UsingLambda> cat s3-upload-using-lambda-kiwony-policy.json 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "s3UploadsGrant",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::s3-upload-using-lambda-kiwony/uploads/*"
            ]
        }
    ]
}

Create user and attached required permission


```




"BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
aws s3api put-public-access-block --bucket s3-upload-using-lambda-kiwony  --public-access-block-configuration  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"


<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>POST</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>

{
    "CORSRules": [
        {
            "AllowedOrigins": ["*"],
            "AllowedMethods": ["GET"],
            "AllowedHeaders": ["Authorization"],
            "MaxAgeSeconds":3000 
        },
        {
            "AllowedOrigins": ["*"],
            "AllowedMethods": ["POST"],
            "AllowedHeaders": ["Authorization"],
            "MaxAgeSeconds":3000 
        },
    ]
}
