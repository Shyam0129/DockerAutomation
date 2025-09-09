import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()
MCP_SERVER = "http://mcp-server:8080"

class ArchestraService:
    def __init__(self):
        self.connected = False

    async def connect_to_mcp(self):
        try:
            response = requests.get(f"{MCP_SERVER}/health")
            self.connected = response.status_code == 200
            return self.connected
        except:
            self.connected = False
            return False

service = ArchestraService()

@app.on_event("startup")
async def startup_event():
    await service.connect_to_mcp()

@app.get("/status")
async def get_status():
    return {
        "service": "archestra",
        "mcp_connected": service.connected
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)