from flask import Flask, request, redirect, render_template, session, make_response
from flask_session import Session

import json
import boto3
import uuid
from datetime import datetime

AWSKEY = ''
AWSSECRET = ''

def get_dynamo_table(DYNAMOTABLE):
    dynamo = boto3.resource(service_name='dynamodb',
                            region_name='us-east-1',
                            aws_access_key_id=AWSKEY,
                            aws_secret_access_key=AWSSECRET)
    table = dynamo.Table(DYNAMOTABLE)
    return table

def login(form):
    email = form.get('email')
    password = form.get('password')

    if email == '' or password == '':
        return {'result':'Bad Login'}

    table = get_dynamo_table('Users')
    item = table.get_item(Key={'email':email})
    if 'Item' not in item:
        return {'result': 'Email not found'}

    user = item['Item']
    if password != user['password']:
        return {'result':'Password not valid'}
    # at this point, the email and password are correct
    session['email'] = user['email']
    return {'result':'OK'}


def uploadfile(form):
    table = get_dynamo_table('Blog')
    title = form.get("title")
    blogID = str(uuid.uuid4())
    description = form.get('description')
    date = datetime.now()
    time = date.strftime('%Y-%m-%d %H:%M:%S')
    email = session.get('email')



    table.put_item(Item={
        'BlogID': blogID,
        'title': title,
        'description': description,
        'time': time,
        'email': email

        })
    return { 'results': 'OK' }

def listfiles():
    table = get_dynamo_table('Blog')
    items = table.scan()['Items']

    output = []
    for item in items:
        d = {'ID': item['BlogID'],
             'title': item['title'],
             'description': item['description'],
             'time': item['time'],
             'email': item.get('email', 'unknown')
             }

        output.append(d)
    output.sort(key=lambda x: x['time'],reverse=True)

    return {'items': output}

def deletefile(form):
    table = get_dynamo_table('Blog')
    id = form.get('ID')
    table.delete_item(Key={"BlogID":id})
    return {'results':'OK'}
