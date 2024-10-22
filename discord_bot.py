import os
from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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
    allow_origins=["*"],  # In production, replace with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active websocket connections
active_connections: Dict[str, Set[WebSocket]] = {}

# Add health check endpoints
@app.get("/")
async def root():
    return {
        "status": "online",
        "bot_user": str(bot.user) if bot.user else "Not connected",
        "active_connections": {
            channel: len(connections) 
            for channel, connections in active_connections.items()
        }
    }

@app.get("/health")
async def health_check():
    if not bot.is_ready():
        raise HTTPException(status_code=503, detail="Discord bot not ready")
    return {
        "status": "healthy",
        "discord_latency": f"{bot.latency * 1000:.2f}ms"
    }

# Rest of your bot code remains the same...
