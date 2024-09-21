import requests
from pprint import pprint


class SimpleClient:

    def __init__(self) -> None:
        self.url = "http://127.0.0.1:8000/request"
        self.token = "API_AUTH_TOKEN"

    def simple_client_post(self, parameter: str = None):
        payload = {
            "message": "Hi. This is a confirmation message."
        }

        headers = {
            "Authorization": self.token
        }

        response = requests.post(self.url, json=payload, headers=headers)
        return response


if __name__ == "__main__":        
    response = SimpleClient().simple_client_post()
    pprint(response.json())
