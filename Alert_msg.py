# Mock implementation for sending alerts (example with Twilio)
# Install Twilio: !pip install twilio

from twilio.rest import Client

# Twilio credentials (replace with your credentials)
account_sid = 'Sweety'
auth_token = '48763'
client = Client(account_sid, auth_token)

def send_alert(message, to_phone_number):
    from_phone_number = '6503835249'
    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )
    return message.sid

# Example alert
alert_message = "Heatwave Alert! Temperatures are expected to exceed 30°C today. Stay hydrated and indoors."
to_phone_number = '+1234567890'  # Replace with the recipient's phone number

# Send alert (uncomment to send)
# alert_sid = send_alert(alert_message, to_phone_number)
# print(f"Alert sent with SID: {alert_sid}")
