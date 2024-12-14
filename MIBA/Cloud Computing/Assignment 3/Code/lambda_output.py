import math
import json
import boto3
from uuid import uuid4
from decimal import Decimal  

dynamodb = boto3.resource('dynamodb')
table_name = 'Predictions'  
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        feature_1 = Decimal(event['queryStringParameters']['lead_time'])
        feature_2 = Decimal(event['queryStringParameters']['previous_cancellations'])
        feature_3 = Decimal(event['queryStringParameters']['days_in_waiting_list'])
        feature_4 = Decimal(event['queryStringParameters']['booking_changes'])

        mean_1, std_1 = Decimal('103.919214'), Decimal('106.852343')  # lead_time
        mean_2, std_2 = Decimal('0.086774'), Decimal('0.844402')  # previous_cancellations
        mean_3, std_3 = Decimal('2.339060'), Decimal('17.738206')  # days_in_waiting_list
        mean_4, std_4 = Decimal('0.220831'), Decimal('0.651776')  # booking_changes

        z1 = (feature_1 - mean_1) / std_1
        z2 = (feature_2 - mean_2) / std_2
        z3 = (feature_3 - mean_3) / std_3
        z4 = (feature_4 - mean_4) / std_4

        # Logistic regression coefficients
        coef_1, coef_2, coef_3, coef_4 = Decimal('0.56924606'), Decimal('1.43345832'), Decimal('-0.00177538'), Decimal('-0.47313005')
        intercept = Decimal('-0.53776839')

        # Compute log-odds (linear combination)
        log_odds = intercept + (coef_1 * z1) + (coef_2 * z2) + (coef_3 * z3) + (coef_4 * z4)

        # Convert log-odds to probability
        probability = Decimal(1) / (Decimal(1) + Decimal(math.exp(-log_odds)))

        # Convert probability to category (threshold = 0.5)
        prediction = 1 if probability >= Decimal(0.5) else 0

        # Write the result to DynamoDB
        item = {
            'id': str(uuid4()),  
            'lead_time': feature_1,
            'previous_cancellations': feature_2,
            'days_in_waiting_list': feature_3,
            'booking_changes': feature_4,
            'log_odds': log_odds,
            'probability': probability,
            'prediction': prediction
        }
        table.put_item(Item=item)

        # Return API response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Prediction saved to DynamoDB",
                "data": item
            }, default=str)  
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
