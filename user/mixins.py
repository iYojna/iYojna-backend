from email import message
from twilio.rest import Client

account_sid = "ACf9b47deca688d4b5a0bb2c0689cd2863"
auth_token = "948602a4cc649d8b4ba02fc027374e64"
twilio_phone = "+17472943310"


class MessageHandler:
    
    phone_number = None
    otp = None
    
    def __init__(self,phone_number,otp):
        self.phone_number= phone_number
        self.otp = otp
        
    def send_otp_on_phone(self):
        client = Client(account_sid, auth_token)
        
        message=   client.messages.create(
                     body=f'Your verification code is "+{self.otp}',
                     from_=twilio_phone,
                     to=self.phone_number
                 )
        print(message.sid)