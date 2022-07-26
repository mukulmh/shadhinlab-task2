import mysql.connector

def lambda_handler(event, context):
    
    print(event)

    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                                database='0SvQ34JYQz',
                                                user='0SvQ34JYQz',
                                                password='P1GVwRXVKP')

        inptoken = event['authorizationToken']

        sql_select_Query = "select * from token where token = %s"
        mycursor = connection.cursor()
        mycursor.execute(sql_select_Query,(inptoken,))
        # get records
        records = mycursor.fetchone()
        
        if records:
            auth = 'Allow'
        else:
            auth = 'Deny'
    
    except:
        auth = 'Deny'
    
    authResponse = { "principalId": inptoken, "policyDocument": { "Version": "2012-10-17", "Statement": [{"Action": "execute-api:Invoke", "Resource": ["arn:aws:execute-api:ca-central-1:618758721119:jk8ikfnt3i/*/*"], "Effect": auth}] }}
    
    return authResponse