'''
  Created By    : Ryan Alexander
  Date          : 4/17/2015
  FileName      : ramail.py
  Description   : A program to send SMTP message via Mailgun API
'''
import requests

from keys import kApiKey

def send_simple_message(address, subject, body):
    return requests.post(
        "https://api.mailgun.net/v3/ryan-alex.com/messages",
        auth=("api", kApiKey),
        files=[("attachment", open("RyanResume.docx"))],
        data={"from": "Ryan <ryan@ryan-alex.com>",
            "to": address,
            "subject": subject,
            "html": body })

def main(): 
  address  = raw_input("Email: ")
  subject  = raw_input("Subject: ")
  body     = raw_input("Message: ") 

  send_simple_message(address, subject, body)

if __name__ == "__main__":
    main()