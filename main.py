import os
import socket
import json
from typing import Optional
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Devil's Host - AI Orchestrator API",
    description="A secure translation engine to orchestrate hosting configurations using natural language syntax.",
    version="1.1.0"
)

# CORS Rules
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEVIL_API_KEY = os.getenv("DEVIL_API_KEY", "devil-default-secure-secret-key")
DEVIL_SOCKET_PATH = "/var/run/devil2.sock"

class CommandPayload(BaseModel):
    instruction: str
    context: Optional[dict] = None

# API Key Validation
async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != DEVIL_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized key pair.")
    return x_api_key

def send_to_devil_socket(payload: dict) -> dict:
    """
    Establishes connection to the UNIX daemon socket server to process hosting tasks.
    """
    if not os.path.exists(DEVIL_SOCKET_PATH):
        # Local mocking fallbacks for sandbox environments
        return {"status": "mock", "message": f"Simulated socket transmission success for command sequence payload."}
        
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.connect(DEVIL_SOCKET_PATH)
            client.sendall(json.dumps(payload).encode("utf-8"))
            response = client.recv(4096)
            return json.loads(response.decode("utf-8"))
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Socket interface unreachable: {str(e)}")

def parse_instruction_with_ai(instruction: str) -> dict:
    """
    Decodes structured operations from plain instructions. 
    In live production environments, this can connect to LLMs to yield standard JSON execution definitions.
    """
    text = instruction.lower()
    
    if "proxy" in text or "reverse" in text:
        # Extract arbitrary port sequences for mapping
        port = "3000"
        for word in text.split():
            if word.isdigit():
                port = word
                break
        return {
            "action": "vhost-gen",
            "type": "reverse_proxy",
            "port": port,
            "domain": "devil-app.local"
        }
        
    elif "db" in text or "database" in text or "sql" in text:
        return {
            "action": "database",
            "type": "mysql_create",
            "db_name": "devil_db_inst",
            "user": "devil_user"
        }
        
    elif "list" in text or "vhost" in text:
        return {
            "action": "system_info",
            "query": "list_vhosts"
        }
        
    # Standard fallback schema mapping
    return {
        "action": "generic_shell",
        "command_fallback": "vhost-gen --help"
    }

@app.post("/api/v1/orchestrate")
async def orchestrate_hosting(payload: CommandPayload, api_key: str = Depends(verify_api_key)):
    """
    Receives prompt, transforms intent using parser engine, and dispatches to Devil UNIX core socket.
    """
    parsed_config = parse_instruction_with_ai(payload.instruction)
    
    # Merge instruction metadata
    execution_payload = {
        "orchestrated_from": "AI Engine",
        "instruction": payload.instruction,
        "config": parsed_config
    }
    
    socket_response = send_to_devil_socket(execution_payload)
    
    return {
        "status": "success",
        "parsed_intent": parsed_config,
        "socket_feedback": socket_response
    }

@app.get("/api/v1/health")
async def check_health():
    socket_active = os.path.exists(DEVIL_SOCKET_PATH)
    return {
        "status": "online",
        "socket_path": DEVIL_SOCKET_PATH,
        "socket_active": socket_active
    }
