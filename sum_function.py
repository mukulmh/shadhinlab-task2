import json

def numsum(num1, num2):
        try:
            sum = float(num1)+float(num2)
            message = "Success"
            data = {
                "message": message,
                "sum": sum
            }
            
        except Exception as e:
            data = {
                "message" : e
            }
        
        return{
            'statusCode': 200,
            'body': json.dumps(data)
        }

def lambda_handler(event, context):
    
    method = event['httpMethod']

    if method == "GET" :
        return numsum(event['queryStringParameters']['num1'],event['queryStringParameters']['num2'])
        
    elif method == "POST" :
        body = json.loads(event['body'])
        return numsum(body['num1'], body['num2'])

    else :
        data = {
            "message": "Supported methods are GET and POST"
        }
    
        return{
            'statusCode': 200,
            'body': json.dumps(data)
        }