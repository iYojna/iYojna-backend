from email import message
from twilio.rest import Client
from decouple import Config, RepositoryEnv
DOTENV_FILE = './api/.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))

account_sid = env_config.get("account_sid")
auth_token = env_config.get("auth_token")
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