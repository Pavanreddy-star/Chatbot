from flask import jsonify

def handle_webhook(req):
    try:
        # Log the incoming request
        print("Incoming request JSON:", req.get_json())

        # Parse the request JSON
        data = req.get_json()
        action = data.get('queryResult', {}).get('action', '')

        # Log the action being handled
        print("Action:", action)

        # Handle 'ViewUpcomingEvents' action
        if action == 'ViewUpcomingEvents':
            events = [
                {"name": "SPIE Optics Workshop", "date": "Jan 25"},
                {"name": "SPIE Annual Conference", "date": "Feb 5"}
            ]
            events_text = "Here are the upcoming SPIE events:\n"
            for event in events:
                events_text += f"{event['name']} on {event['date']}\n"

            response = {
                "fulfillmentText": events_text + "Would you like more details on any of these events?"
            }
            print("Response:", response)
            return jsonify(response)

        # Handle 'RegisterForEvent' action
        elif action == 'RegisterForEvent':
            user_name = data.get('queryResult', {}).get('parameters', {}).get('given-name')
            user_email = data.get('queryResult', {}).get('parameters', {}).get('email')

            # Simulate registration (e.g., saving user details in a database)
            print(f"Registered user: {user_name}, Email: {user_email}")

            response = {
                "fulfillmentText": f"Thank you for registering, {user_name}! You will receive a confirmation email at {user_email}."
            }
            print("Response:", response)
            return jsonify(response)

        # Default response for unrecognized actions
        else:
            response = {
                "fulfillmentText": "I'm sorry, I didn't understand that. Can you please rephrase?"
            }
            print("Response:", response)
            return jsonify(response)

    except Exception as e:
        # Log and return the exception details
        print("Error occurred:", str(e))
        response = {
            "fulfillmentText": f"An error occurred while processing your request: {str(e)}"
        }
        return jsonify(response), 500
