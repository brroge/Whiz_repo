import json
import urllib.request

API_KEY = "b8176764-449e-4671-b9ea-xxxxxxxxxxxxx"
API_URL = "https://api.balldontlie.io/v1/games?per_page=10&seasons[]=2024"

def lambda_handler(event, context):
    headers = {"Authorization": API_KEY}
    req = urllib.request.Request(API_URL, headers=headers)

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # allow S3 website to call
        },
        "body": json.dumps(data)  # must be JSON string, not dict
    }

