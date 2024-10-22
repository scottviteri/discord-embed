# Discord Channel Embed

A simple, responsive webpage that embeds a Discord channel using Discord's widget feature. This project is designed to be hosted on GitHub Pages and provides a clean, Discord-themed interface for viewing a single Discord channel on the web.

## 🚀 Quick Setup

1. Fork or clone this repository
2. Enable Discord widget in your server:
   - Go to Server Settings > Widget
   - Enable "Enable Server Widget"
   - Copy your Server ID
3. Update `index.html`:
   - Replace `YOUR_CHANNEL_ID` with your Discord server ID
   - Update `channelName` in the config object
4. Enable GitHub Pages:
   - Go to repository Settings
   - Navigate to Pages section
   - Select main branch as source
   - Save changes

## 🛠️ Configuration

Edit the configuration in `index.html`:

```javascript
const config = {
    channelId: 'YOUR_CHANNEL_ID', // Your Discord server ID
    channelName: 'channel-name',  // Your channel name
};
```

## 🎨 Features

- Responsive design that works on mobile and desktop
- Discord-like styling for visual consistency
- Dark theme to match Discord's aesthetic
- Full-height embed that scales with viewport
- Simple configuration
- Mobile-friendly layout

## 📱 Browser Support

Tested and working on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🔧 Customization

To customize the appearance:
1. Modify the CSS in the `<style>` section of `index.html`
2. Update colors to match your branding
3. Adjust container sizes and padding as needed

## 📝 License

MIT License - feel free to use this code for any purpose.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## ⚠️ Troubleshooting

If the embed isn't working:
1. Check if Discord widget is enabled in your server
2. Verify your server ID is correct
3. Ensure your server is public or the widget is specifically enabled
4. Check browser console for any errors

## 📞 Support

If you encounter any issues:
1. Check the [Issues](../../issues) section
2. Create a new issue if your problem isn't already reported

---

Made with ❤️ for the Discord community
