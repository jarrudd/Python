# post_login_api.py
import requests

class APIClient:
    @staticmethod
    def login(api_url, user_input, pass_input):
        data = {'email': user_input, 'password': pass_input}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url + "/api/login", json=data, headers=headers)
        return response