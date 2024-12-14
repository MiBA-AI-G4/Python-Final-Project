import math
import json
import pickle

# Load the model and scaler
try:
    with open('/opt/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('/opt/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    raise e

def lambda_handler(event, context):
    """
    Lambda function to compute predictions using logistic regression.
    """
    try:
        # Extract features from query parameters
        query_params = event.get('queryStringParameters', {})
        if not query_params:
            raise ValueError("Missing queryStringParameters in the event.")

        # Parse the input features
        lead_time = float(query_params.get('lead_time', 0))
        previous_cancellations = float(query_params.get('previous_cancellations', 0))
        days_in_waiting_list = float(query_params.get('days_in_waiting_list', 0))
        booking_changes = float(query_params.get('booking_changes', 0))

        # Manual preprocessing (z-score normalization)
        mean_std_map = {
            "lead_time": (103.919214, 106.852343),
            "previous_cancellations": (0.086774, 0.844402),
            "days_in_waiting_list": (2.339360, 17.738206),
            "booking_changes": (0.220831, 0.651776)
        }
        z_lead_time = (lead_time - mean_std_map["lead_time"][0]) / mean_std_map["lead_time"][1]
        z_previous_cancellations = (previous_cancellations - mean_std_map["previous_cancellations"][0]) / mean_std_map["previous_cancellations"][1]
        z_days_in_waiting_list = (days_in_waiting_list - mean_std_map["days_in_waiting_list"][0]) / mean_std_map["days_in_waiting_list"][1]
        z_booking_changes = (booking_changes - mean_std_map["booking_changes"][0]) / mean_std_map["booking_changes"][1]

        # Logistic regression coefficients and intercept
        coef = [0.56924606, 1.43345832, -0.00177538, -0.47313005]
        intercept = -0.53776839

        # Compute log-odds (linear combination)
        log_odds = (
            intercept
            + coef[0] * z_lead_time
            + coef[1] * z_previous_cancellations
            + coef[2] * z_days_in_waiting_list
            + coef[3] * z_booking_changes
        )

        # Convert log-odds to probability
        probability = 1 / (1 + math.exp(-log_odds))

        # Convert probability to prediction (threshold = 0.5)
        prediction = 1 if probability >= 0.5 else 0

        # Return the response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "log_odds": log_odds,
                "probability": probability,
                "prediction": prediction
            })
        }

    except Exception as e:
        # Return error response
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
