import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import discord
from discord.ext import commands
import asyncio
import json
from typing import Dict, Set
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI and Discord bot
app = FastAPI()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active websocket connections
active_connections: Dict[str, Set[WebSocket]] = {}

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "online", "message": "Discord bot is running"}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel_id = str(message.channel.id)
    if channel_id in active_connections:
        message_data = {
            'author': message.author.name,
            'content': message.content,
            'timestamp': message.created_at.isoformat(),
            'avatar_url': str(message.author.avatar.url) if message.author.avatar else None
        }
        connections = active_connections[channel_id].copy()
        for connection in connections:
            try:
                await connection.send_json(message_data)
            except:
                active_connections[channel_id].remove(connection)

@app.websocket("/ws/{channel_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id: str):
    await websocket.accept()
    
    if channel_id not in active_connections:
        active_connections[channel_id] = set()
    active_connections[channel_id].add(websocket)
    
    try:
        channel = bot.get_channel(int(channel_id))
        if channel:
            messages = []
            async for message in channel.history(limit=50):
                messages.append({
                    'author': message.author.name,
                    'content': message.content,
                    'timestamp': message.created_at.isoformat(),
                    'avatar_url': str(message.author.avatar.url) if message.author.avatar else None
                })
            for message in reversed(messages):
                await websocket.send_json(message)
        
        while True:
            await websocket.receive_text()
            
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        if channel_id in active_connections:
            active_connections[channel_id].remove(websocket)
            if not active_connections[channel_id]:
                del active_connections[channel_id]

async def run_bot(bot_token):
    try:
        await bot.start(bot_token)
    except Exception as e:
        print(f"Bot error: {e}")

async def run_fastapi(port):
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    bot_token = os.getenv('DISCORD_BOT_TOKEN')
    if not bot_token:
        raise ValueError("Please set the DISCORD_BOT_TOKEN environment variable")
    
    # Get port from environment variable with fallback to 10000
    port = int(os.getenv('PORT', 10000))
    
    print(f"Starting server on port {port}")
    
    await asyncio.gather(
        run_bot(bot_token),
        run_fastapi(port)
    )

if __name__ == "__main__":
    import uvicorn
    asyncio.run(main())
