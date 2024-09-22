import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()


class SimpleClient:

    def __init__(self) -> None:
        self.url = "http://127.0.0.1:8000/request"
        self.token = os.getenv("API_AUTH_TOKEN", "")

    def simple_client_post(self, parameter: str = None):
        payload = {
            'message': 'This is a confirmation message.'
        }

        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.post(self.url, json=payload, headers=headers)
        return response


if __name__ == "__main__":        
    response = SimpleClient().simple_client_post()
    pprint(response.json())
