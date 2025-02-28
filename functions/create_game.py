import json
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
ROBLOX_API_KEY = os.getenv("ROBLOX_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def async_post(url: str, headers: dict, json_payload: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=json_payload)
        response.raise_for_status()
        return response.json()

def handler(event, context):
    body = json.loads(event['body'])
    theme = body.get('theme')
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Juego creado con el tema: " + theme})
    }
