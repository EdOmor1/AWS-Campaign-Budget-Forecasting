import json
from forecast_model import generate_forecast

def lambda_handler(event, context):
    forecast = generate_forecast()
    return {
        'statusCode': 200,
        'body': json.dumps(forecast)
    }
