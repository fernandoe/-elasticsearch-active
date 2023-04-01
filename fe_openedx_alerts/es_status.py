#!/usr/bin/env python
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
whatsapp_number = os.environ['TWILIO_WHATSAPP_NUMBER']
my_number = os.environ['MY_NUMBER']

def get_current_status(fixed_str=None):
    if fixed_str == 'ok':
        with open("./es-status-ok.txt", "r") as result:
            return result.read()
    elif fixed_str == 'ko':
        with open("./es-status-not-ok.txt", "r") as result:
            return result.read()
    return ''


def execute():
    output = get_current_status('ko')
    print(output)
    if 'Active: active (running)' not in output:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="ATENÇÃO: O serviço do Elastic Search parou de funcionar!",
            from_=f"{whatsapp_number}",
            to=f"{my_number}"
        )
        print(f"Mensagem enviada com sucesso! SID: {message.sid}")


if __name__ == '__main__':
    execute()

