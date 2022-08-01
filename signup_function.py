# Mehedy Hassan Mukul

import mysql.connector
import json

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

    # register a new user
    def reg_user(inp_name, inp_email, inp_password):

        sql_select_Query = "select * from user where email = %s"
        mycursor = connection.cursor()
        mycursor.execute(sql_select_Query, (inp_email,))
        
        records = mycursor.fetchone()
        
        if not records:
            try:
                mycursor.execute('insert into user (name, email, password) values(%s, %s, %s)', (inp_name,inp_email,inp_password,))
                connection.commit()
                message ={
                    "message": "Registration Success. Now log in with your email and password."
                }
            except:
                message ={
                    "message": "Couldn't register, Please try again!"
                }
        else:
            message ={
                    "message": "User already exists!"
                }

        return message
        
    try:
        body = json.loads(event['body'])
        inp_name = body['name']
        inp_email = body['email']
        inp_password = body['password']

        result = reg_user(inp_name,inp_email,inp_password)

    except:
        result = {
            "message": "Please provide name, email & password correctly!"
        }
    
    return{
        'statusCode': 200,
        'body': json.dumps(result)
    }
