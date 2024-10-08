import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()


class SimpleClient:

    def __init__(self) -> None:
        self.url = "http://127.0.0.1:8000/request/"
        self.token = os.getenv("API_AUTH_TOKEN", "")

    def simple_client_post(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        payload = {
            'message': 'This is a confirmation message.'
        }


        response = requests.post(
            self.url, headers=headers, json=payload, allow_redirects=False
        )

        return response



if __name__ == "__main__":        
    response = SimpleClient().simple_client_post()
    pprint(response.json())
