from unicodedata import name
import mysql.connector
import json

def lambda_handler(event, context):
    try:
        connection = mysql.connector.connect(host='remotemysql.com',
                                            database='0SvQ34JYQz',
                                            user='0SvQ34JYQz',
                                            password='P1GVwRXVKP')
                                            
        body = json.loads(event['body'])

        inp_name = body['name']
        inp_email = body['email']
        inp_password = body['password']

        sql_select_Query = "select * from user where email = %s"
        mycursor = connection.cursor()
        mycursor.execute(sql_select_Query, (inp_email,))
        
        records = mycursor.fetchone()
        
        if not records:
        
            try:
                mycursor.execute('insert into user (name, email, password) values(%s, %s, %s)', (inp_name,inp_email,inp_password,))
                connection.commit()
                message = "Registration Success"
            except:
                message = "Soemthing Went Wrong"
        else:
            message = "Email already taken!"

    except:
        message = "Something went wrong!"

    data = {
            "message" : message
        }

    return{
        'statusCode': 200,
        'body': json.dumps(data)
    }