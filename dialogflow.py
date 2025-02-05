import os
from google.cloud import dialogflow_v2 as dialogflow

# Load Dialogflow credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/dialogflow-service-account.json'

def get_dialogflow_response(text):
    project_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    session_id = str(uuid.uuid4())  # This creates a random UUID for each session

 # Language code for the interaction (English in this case)
    language_code = 'en'

# Set up Dialogflow session client
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

     # Create the text input for the query
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
 # Detect intent from Dialogflow
    response = session_client.detect_intent(session=session, query_input=query_input)

  # Return the response text
    return response.query_result.fulfillment_text
