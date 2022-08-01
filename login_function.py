# Mehedy Hassan Mukul

import mysql.connector
import json
import uuid

def lambda_handler(event, context):
    # Establish the connection
    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                            database='0SvQ34JYQz',
                                            user='0SvQ34JYQz',
                                            password='P1GVwRXVKP')
    except:
        result = {
            "message": "Connection Error!"
        }

    # get an user details
    def get_user(inp_email):
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM user WHERE email = %s", (inp_email,))
        record = mycursor.fetchone()
        return record

    # check user login
    def login_check(inp_email,inp_password):
        record =  get_user(inp_email)

        if record:
            password = record[3]
            user_id = record[0]

            if inp_password == password:
                token = str(uuid.uuid1())
                mycursor = connection.cursor()
                mycursor.execute('insert into token (user_id, token) values(%s, %s)', (user_id,token,))
                connection.commit()
                data = {
                    "message" : "Login Success",
                    "token": token
                }
                return data
                
            else:
                return "Incorrect Password"
        else :
            return "No user found!"

    try:
        body = json.loads(event['body'])
        inp_email = body['email']
        inp_password = body['password']
        result =  login_check(inp_email,inp_password)
    except:
        result = {
            "message": "Please provide both email and password!"
        }
    
    return{
        'statusCode': 200,
        'body': json.dumps(result)
    }
