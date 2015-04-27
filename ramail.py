'''
  Created By    : Ryan Alexander
  Date          : 4/17/2015
  FileName      : ramail.py
  Description   : A program to send message via Mailgun API
'''
import requests
from argparse import ArgumentParser
from keys.keys import kApiKey

def send_simple_message(address, subject):
    return requests.post(
        "https://api.mailgun.net/v3/ryan-alex.com/messages",
        auth=("api", kApiKey),
        files=[("attachment", open("_attachments/RyanResume.docx")),
        ("attachment", open("_attachments/RyanResume.pdf"))],
        data={"from": "Ryan <ryan@ryan-alex.com>",
            "to": address,
            "subject": subject,
            "html": open("_ready/stage.html") })

def main(): 
  parser = ArgumentParser(description="""\
Send the contents of an html file as a request to the Mailgun API. 
A recipient email address using the -a flag and a subject using the
-s flag must be set. 
""")
  parser.add_argument('-a', '--address', required=True,
                        help="""Set a recipient email address to send
                        this message to.""")
  parser.add_argument('-s', '--subject', required=True,
                        help="""Set a subject to send with this message.""")
  
  args = parser.parse_args()
  address = args.address
  subject = args.subject
  send_simple_message(address, subject)

if __name__ == "__main__":
    main()