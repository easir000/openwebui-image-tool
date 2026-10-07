import os
import urllib.parse
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Image Generation Tool Server", version="1.0.0")
EXPECTED_API_KEY = os.getenv("TOOL_SERVER_API_KEY", "super-secret-test-key-123")

class ImageRequest(BaseModel):
    prompt: str
    size: Optional[str] = "512x512"

def verify_api_key(x_api_key: str = Header(..., description="API Key for authorization")):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return x_api_key

@app.post("/generate", summary="Generate an image from a text prompt")
async def generate_image(request: ImageRequest, api_key: str = Depends(verify_api_key)):
    safe_prompt = urllib.parse.quote(request.prompt)
    width, height = ("512", "512") if request.size == "512x512" else ("1024", "1024")
    image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width={width}&height={height}&nologo=true"
    return {"status": "success", "prompt": request.prompt, "image_url": image_url}

@app.get("/health", summary="Health check endpoint")
async def health_check():
    return {"status": "healthy", "service": "image-generation-tool"}