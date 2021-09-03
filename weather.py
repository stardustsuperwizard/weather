import boto3
import datetime
import gzip
import json
import os
import requests
import uuid

from botocore.exceptions import ClientError

DATA_BUCKET = os.environ['DATA_BUCKET']


def get_locations():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('weather-locations')
    
    data = []

    try:
        response = table.scan()
    except Exception as err:
        print(err)
        return []
    else:
        data.extend(response['Items'])

    while response.get('LastEvaluatedKey'):
        try:
            response = table.scan(ExclusiveStartKey=last_key)
        except Exception as err:
            print(err)
            break
        else:
            data.extend(response['Items'])
    
    return data


def get_weather_forecast(office, grid_x, grid_y, user_agent):
    headers = {
        'Accept': 'application/geo+json',
        'User-Agent': user_agent
    }

    response = requests.get(url=f'https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast', headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def put_data_s3(data_string, s3_key, client):
    data_object = bytes(data_string, 'utf-8')
    data_object = gzip.compress(data_object)
    
    try:
        response = client.put_object(Bucket=DATA_BUCKET, Body=data_object, Key=s3_key)
    except ClientError as err:
        print(err)
        return None
    except Exception as err:
        print(err)
        return None
    else:
        return response
    return None


def lambda_handler(event, context):
    print(json.dumps(event))

    now = datetime.datetime.now().strftime("%Y/%m/%d")
    s3 = boto3.client('s3')

    locations = get_locations()
    for location in locations:
        data = get_weather_forecast(location['office'], location['grid_x'], location['grid_y'], os.environ['headers'])
        if data:
            s3_key = f"data/{now}/{location['name'].replace(' ','')}-{uuid.uuid4()}.json.gz"
            print(s3_key)
            response = put_data_s3(json.dumps(data), s3_key, s3)
            print(response)
    return
