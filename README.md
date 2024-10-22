# Discord Channel Web Viewer

A real-time Discord channel viewer that shows messages from your Discord server on a webpage. Uses a Discord bot for real-time message streaming and WebSocket connections for instant updates.

## 🏗️ Architecture

This project consists of two parts:
1. **Backend**: A Discord bot + WebSocket server (hosted on Render)
2. **Frontend**: A static webpage (can be hosted on GitHub Pages)

```
Discord Server <-> Discord Bot (Render) <-> WebSocket <-> Webpage
```

## 🚀 Setup Guide

### 1. Discord Bot Setup

1. Create a Discord Application:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to "Bot" section
   - Click "Add Bot"
   - Copy the bot token (you'll need this later)

2. Enable Required Intents:
   - In the Bot section, enable:
     - Presence Intent
     - Server Members Intent
     - Message Content Intent

3. Invite Bot to Your Server:
   - Go to OAuth2 > URL Generator
   - Select scopes:
     - bot
     - applications.commands
   - Select permissions:
     - Read Messages/View Channels
     - Read Message History
   - Use the generated URL to invite the bot

### 2. Backend Deployment (Render)

1. Fork this repository

2. Sign up on [Render](https://render.com)

3. Create New Web Service:
   - Connect your GitHub repository
   - Select the repository
   - Fill in details:
     - Name: `discord-channel-bot` (or your preference)
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python discord_bot.py`

4. Add Environment Variable:
   - Key: `DISCORD_BOT_TOKEN`
   - Value: Your Discord bot token

5. Deploy the service

### 3. Frontend Setup

1. Get your channel information:
   - Enable Developer Mode in Discord (User Settings > App Settings > Advanced)
   - Right-click your channel and "Copy ID"
   - Note your channel name (without the #)

2. Update the WebSocket URL in index.html:
   ```javascript
   const wsUrl = `wss://YOUR-RENDER-SERVICE.onrender.com/ws/${channelId}`;
   ```

3. Host the frontend:
   - GitHub Pages (recommended)
   - Any static hosting service
   - Local file system

## 🔧 Configuration

### Backend Environment Variables
- `DISCORD_BOT_TOKEN`: Your Discord bot token
- `PORT`: (Optional) Port for the WebSocket server (defaults to 8000)

### Frontend Configuration
Enter in the web interface:
- Channel ID: Your Discord channel ID
- Channel Name: The channel name (without #)

## 📡 API Endpoints

- `GET /`: Bot status and connection information
- `GET /health`: Health check endpoint with Discord connection status
- `WS /ws/{channel_id}`: WebSocket endpoint for real-time messages

## 🔍 Monitoring

Check your bot's status:
1. Visit `https://YOUR-SERVICE.onrender.com/`
2. Check the health endpoint: `https://YOUR-SERVICE.onrender.com/health`

## 🐛 Troubleshooting

1. **WebSocket Not Connecting**:
   - Check if the bot is online in Discord
   - Verify your channel ID
   - Check the Render service logs

2. **No Messages Showing**:
   - Ensure bot has correct permissions
   - Verify the channel ID is correct
   - Check browser console for errors

3. **Render Deployment Issues**:
   - Verify environment variables are set
   - Check build and start logs
   - Ensure requirements.txt is present

## 📚 Development

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with `DISCORD_BOT_TOKEN=your_token`
4. Run: `python discord_bot.py`

### Testing WebSocket
```javascript
// Browser console test
const ws = new WebSocket('wss://YOUR-SERVICE.onrender.com/ws/CHANNEL_ID');
ws.onmessage = (event) => console.log(JSON.parse(event.data));
```

## 🔐 Security Notes

- Keep your bot token secret
- Use environment variables for sensitive data
- Consider adding authentication for production use

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

Made with ❤️ for the Discord community
