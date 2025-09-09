import requests
from typing import Dict, Any

class MCPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def check_health(self) -> Dict[str, Any]:
        response = requests.get(f"{self.base_url}/health")
        return response.json()

    async def get_status(self) -> Dict[str, Any]:
        response = requests.get(f"{self.base_url}/status")
        return response.json()

class LogHandler:
    @staticmethod
    def log_error(message: str):
        print(f"ERROR: {message}")

    @staticmethod
    def log_info(message: str):
        print(f"INFO: {message}")

    @staticmethod
    def log_warning(message: str):
        print(f"WARNING: {message}")