# -*- coding: utf-8 -*-
import httplib2
import base64
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail api client'
SENDER = 'steetzvv@gmail.com'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, None)
    return credentials


class MessageSender(object):
    def __init__(self):
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('gmail', 'v1', http=http)

    def _send_message(self, message):
        try:
            message = (self.service.users().messages().send(userId='me', body=message)
                       .execute())

            return message
        except Exception as ex:
            print('An error occurred: %s' % ex)

    def send(self, recipient, subject, body):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['To'] = recipient
        msg['From'] = SENDER

        msg.attach(MIMEText(body, 'html'))
        raw = base64.urlsafe_b64encode(msg.as_bytes())
        raw = raw.decode()
        self._send_message({'raw': raw})