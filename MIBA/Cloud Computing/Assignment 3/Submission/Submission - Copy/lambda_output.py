import math
import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'hotelbucketcc3'

def z_score(value: float, mean: float, std: float) -> float:
    """Calculate the z-score for a given value."""
    return (value - mean) / std

def lambda_handler(event, context):
    intercept = -0.54485467
    coefficients = [0.60674229, 1.46157494, 0.23866557, -0.48266927]

    try:
        lead_time = float(event['queryStringParameters']['lead_time'])
        previous_cancellations = float(event['queryStringParameters']['previous_cancellations'])
        adr = float(event['queryStringParameters']['adr'])
        booking_changes = float(event['queryStringParameters']['booking_changes'])

        mean_std = {
            "lead_time": (104.01141636652986, 106.86309704798579),
            "previous_cancellations": (0.08711784906608594, 0.8443363841518937),
            "adr": (101.83112153446686, 50.5357902855456),
            "booking_changes": (0.22112404724013737, 0.6523055726747069)
        }

        lead_time = z_score(lead_time, mean_std["lead_time"][0], mean_std["lead_time"][1])
        previous_cancellations = z_score(previous_cancellations, mean_std["previous_cancellations"][0], mean_std["previous_cancellations"][1])
        adr = z_score(adr, mean_std["adr"][0], mean_std["adr"][1])
        booking_changes = z_score(booking_changes, mean_std["booking_changes"][0], mean_std["booking_changes"][1])

        log_odds = (
            intercept +
            lead_time * coefficients[0] +
            previous_cancellations * coefficients[1] +
            adr * coefficients[2] +
            booking_changes * coefficients[3]
        )
        probability = 1 / (1 + math.exp(-log_odds))

        prediction = "positive" if probability > 0.5 else "negative"

        result = {
            'probability': probability,
            'prediction': prediction
        }

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"prediction_{timestamp}.json"

        json_result = json.dumps(result)
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json_result,
            ContentType='application/json'
        )

        return {
            'statusCode': 200,
