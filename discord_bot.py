import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import discord
from discord.ext import commands
import asyncio
import json
from typing import Dict, Set

# Initialize FastAPI and Discord bot
app = FastAPI()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active websocket connections
active_connections: Dict[str, Set[WebSocket]] = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # If there are active connections for this channel, send the message
    channel_id = str(message.channel.id)
    if channel_id in active_connections:
        message_data = {
            'author': message.author.name,
            'content': message.content,
            'timestamp': message.created_at.isoformat(),
            'avatar_url': str(message.author.avatar.url) if message.author.avatar else None
        }
        for connection in active_connections[channel_id]:
            try:
                await connection.send_json(message_data)
            except:
                # Remove dead connections
                active_connections[channel_id].remove(connection)

@app.websocket("/ws/{channel_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id: str):
    await websocket.accept()
    
    # Add this connection to active connections
    if channel_id not in active_connections:
        active_connections[channel_id] = set()
    active_connections[channel_id].add(websocket)
    
    try:
        # Fetch last 50 messages when connecting
        channel = bot.get_channel(int(channel_id))
        if channel:
            async for message in channel.history(limit=50):
                message_data = {
                    'author': message.author.name,
                    'content': message.content,
                    'timestamp': message.created_at.isoformat(),
                    'avatar_url': str(message.author.avatar.url) if message.author.avatar else None
                }
                await websocket.send_json(message_data)
        
        # Keep connection alive and handle disconnection
        while True:
            await websocket.receive_text()
            
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        active_connections[channel_id].remove(websocket)
        if not active_connections[channel_id]:
            del active_connections[channel_id]

# Run both FastAPI and Discord bot
if __name__ == "__main__":
    import uvicorn
    
    # Start the Discord bot in a separate thread
    bot_token = os.getenv('DISCORD_BOT_TOKEN')
    asyncio.create_task(bot.start(bot_token))
    
    # Run the FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000)
