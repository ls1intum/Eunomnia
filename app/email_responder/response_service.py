import logging

import requests

from app.common.environment import config


class ResponseService:
    def __init__(self):
        self.angelos_url = config.ANGELOS_URI
        self.port = config.ANGELOS_PORT
        self.api_url = f"{self.angelos_url}:{self.port}/api/v1/question/ask"
        self.session = requests.Session()
        self.api_key = config.ANGELOS_APP_API_KEY
        self._set_authorization_header()

    def _set_authorization_header(self):
        """Helper function to set the authorization header."""
        self.headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}

    def get_response(self, payload):
        """Send a request to the API endpoint with the given payload."""
        try:
            logging.info(f"Sending POST request to {self.api_url}")
            response = self.session.post(self.api_url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise
