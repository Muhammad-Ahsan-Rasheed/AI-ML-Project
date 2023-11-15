import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer
import ast

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-10-23-19-23-41-638'

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    # Instantiate a Predictor
    predictor = sagemaker.Predictor(ENDPOINT)

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image, initial_args={'ContentType': 'image/png'})

    # We return the data back to the Step Function    
    inferences_str = inferences.decode('utf-8')
    
    event['body']["inferences"] = ast.literal_eval(inferences_str)
    
    return {
        'statusCode': 200,
        'body': event['body']
    }

