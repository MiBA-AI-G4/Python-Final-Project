import math

def z_score(value, mean, std):
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

        return {
            'statusCode': 200,
            'body': str({
                'probability': probability,
                'prediction': prediction
            })
        }
    except KeyError as ke:
        return {
            'statusCode': 400,
            'body': f"Error: Missing required parameter: {str(ke)}"
        }
    except ValueError as ve:
        return {
            'statusCode': 400,
            'body': f"Error: Invalid parameter value: {str(ve)}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
