import mysql.connector
import json
import uuid

def lambda_handler(event, context):
    
    token = ""
    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                            database='0SvQ34JYQz',
                                            user='0SvQ34JYQz',
                                            password='P1GVwRXVKP')

        body = json.loads(event['body'])

        email = body['email']
        inp_password = body['password']
        inp_email = (email,)

        sql_select_Query = "select * from user where email = %s"
        mycursor = connection.cursor()
        mycursor.execute(sql_select_Query,inp_email)
        # get records
        records = mycursor.fetchone()
        
        if records:
            password = records[3]
            user_id = records[0]
        
            if inp_password == password:
                token = str(uuid.uuid1())
                mycursor.execute('insert into token (user_id, token) values(%s, %s)', (user_id,token,))
                connection.commit()
                message = "Login Success"
            else:
                message = "Incorrect Passowrd"
        else:
            message = "No user found!!"
        
    except :
        message = "Something Went Wrong!"
    
    if token:
        data = {
            "message" : message,
            "token" : token
        }
    else:
        data = {
            "message" : message
        }
    

    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }