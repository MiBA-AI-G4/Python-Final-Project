import math
import json

def lambda_handler(event, context):
    # Extract features from the API Gateway event
    feature_1 = float(event['queryStringParameters']['lead_time'])
    feature_2 = float(event['queryStringParameters']['previous_cancellations'])
    feature_3 = float(event['queryStringParameters']['days_in_waiting_list'])
    feature_4 = float(event['queryStringParameters']['booking_changes'])

    # Preprocessing: Z-score normalization (manual implementation of StandardScaler)
    mean_1, std_1 = 103.919214, 106.852343  # lead_time
    mean_2, std_2 = 0.086774, 0.844402  # previous_cancellations
    mean_3, std_3 = 2.339360, 17.738206  # days_in_waiting_list
    mean_4, std_4 = 0.220831, 0.651776  # booking_changes


    z1 = (feature_1 - mean_1) / std_1
    z2 = (feature_2 - mean_2) / std_2
    z3 = (feature_3 - mean_3) / std_3
    z4 = (feature_4 - mean_4) / std_4
    
    # Logistic regression coefficients 
    coef_1, coef_2, coef_3, coef_4 = 0.56924606, 1.43345832, -0.00177538, -0.47313005
    intercept = -0.53776839

    # Compute log-odds (linear combination)
    log_odds = intercept + (coef_1 * z1) + (coef_2 * z2) + (coef_3 * z3) + (coef_4 * z4)

    # Convert log-odds to probability
    probability = 1 / (1 + math.exp(-log_odds))

    # Convert probability to category (threshold = 0.5)
    prediction = 1 if probability >= 0.5 else 0

    # Return API result
    return {
        "statusCode": 200,
        "body": json.dumps({
            "log_odds": log_odds,
            "probability": probability,
            "prediction": prediction
        })
    }