import logging
import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# get the credentials from the environment variables
endpoint = 'https://huilin.cognitiveservices.azure.com/'
key = '706cf2a1acf14de9bfc7a3a2db8b0c40'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # get the input text from the request body
    try:
        req_body = req.get_json()
        text = req_body.get('text')
    except ValueError:
        return func.HttpResponse("Invalid request body", status_code=400)
    
    # authenticate the Text Analytics client
    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    
    # perform sentiment analysis on the input text
    # documents = [text]
    documents = [{"id": "1", "text": text}]
    response = client.analyze_sentiment(documents=documents)[0]
    
    # create the response message
    if response.sentiment == 'positive':
        message = 'The text is positive'
    elif response.sentiment == 'negative':
        message = 'The text is negative'
    else:
        message = 'The text is neutral'
    
    # return the response as a JSON object
    return func.HttpResponse(
        message,
        status_code=200,
        headers={
            'Content-Type': 'application/json'
        }
    )
