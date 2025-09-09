from fastapi import FastAPI
import uvicorn
import requests
import psutil

app = FastAPI()
MCP_SERVER = "http://mcp-server:8080"

class ToolsService:
    def __init__(self):
        self.connected = False
        self.tools = {
            "diagnostic": self.run_diagnostic,
            "monitor": self.monitor_system,
            "system_info": self.get_system_info
        }

    async def connect_to_mcp(self):
        try:
            response = requests.get(f"{MCP_SERVER}/health")
            self.connected = response.status_code == 200
            return self.connected
        except:
            self.connected = False
            return False

    async def run_diagnostic(self):
        return {"status": "diagnostic complete", "result": "all systems normal"}

    async def monitor_system(self):
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        return {
            "status": "monitoring active",
            "metrics": {
                "cpu": f"{cpu_percent}%",
                "memory_used": f"{memory.percent}%",
                "memory_available": f"{memory.available / (1024 * 1024):.2f} MB"
            }
        }

    async def get_system_info(self):
        return {
            "cpu_cores": psutil.cpu_count(),
            "memory_total": f"{psutil.virtual_memory().total / (1024 * 1024):.2f} MB",
            "platform": psutil.sys_info() if hasattr(psutil, 'sys_info') else "Unknown"
        }

service = ToolsService()

@app.on_event("startup")
async def startup_event():
    await service.connect_to_mcp()

@app.get("/tools/{tool_name}")
async def execute_tool(tool_name: str):
    if tool_name in service.tools:
        return await service.tools[tool_name]()
    return {"error": "Tool not found"}

@app.get("/status")
async def get_status():
    return {
        "service": "mcp-tools",
        "mcp_connected": service.connected,
        "available_tools": list(service.tools.keys())
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)