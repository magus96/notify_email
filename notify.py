import asyncio
import aio_msgpack_rpc
import requests
import json
import time

MAILTM_HEADERS = {   
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MDIxOTA0NTAsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJhZGRyZXNzIjoicW94aWFoeWFlemJnbmdsQHdpcmVjb25uZWN0ZWQuY29tIiwiaWQiOiI2NTc1NWFjM2VlMjI4MjdiOTIwYzA0ZTMiLCJtZXJjdXJlIjp7InN1YnNjcmliZSI6WyIvYWNjb3VudHMvNjU3NTVhYzNlZTIyODI3YjkyMGMwNGUzIl19fQ.3fERxqurdN3J6qEArz8glbvtvBd5OeO33aFRZmRRjcanxVV3bR9iBYSlPLeZCTALoKbGuVmUKVmSshHEIFh2Vg"
}

messages_path = "https://api.mail.tm/messages"

def read_email():
    resp = requests.get(messages_path, headers = MAILTM_HEADERS)
    try:
        response_body = resp.json()
    except:
        response_body = {}
    return response_body

def get_headers(emails_resp):
    headers = []
    n_mails = emails_resp.get('hydra:totalItems', 0)
    emails = emails_resp.get('hydra:member')
    for i in range(n_mails):
        headers.append(emails[i])
        
    return headers

async def main():
    client = aio_msgpack_rpc.Client(*await asyncio.open_connection("localhost", 18000))
    while True:
        emails_response = read_email()
        headers = get_headers(emails_response)
        for i in range(len(headers)):
            ids
            if headers[i].get('seen', '') == True:
                continue
            else:
                title = headers[i].get('subject', '')
                body = headers[i].get('intro', '')
                id = headers[i].get('id', '')
                msg_path = f'https://api.mail.tm/messages/{id}'
                r = requests.patch(msg_path, headers = MAILTM_HEADERS)
                print(r.json())
                await client.notify("on_new_mail", title, body)




        




asyncio.run(main())