# serverless-aws-sns-sender


Follow this guide to deploy this lambda to AWS: 
https://serverless.com/framework/docs/providers/aws/guide/credentials/

```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>

serverless deploy
```

Adapt sender.py to contain your aws key and secret. 

Send a post request to https://blablabla.execute-api.us-east-1.amazonaws.com/dev/send with the following body:

```
{ "number": "+49XXXXXXXXXX", "title" : "the title", "message": "Hello World!"}
```
