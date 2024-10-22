# Discord Channel Embed

A simple, customizable webpage that lets you embed any Discord channel using Discord's widget feature. Your server details are stored locally in your browser - no sensitive information is stored in the repository.

## 🚀 Quick Setup

1. **Enable Discord Widget in Your Server**:
   - Open Discord
   - Go to Server Settings
   - Click on "Widget"
   - Enable "Enable Server Widget"

2. **Get Your Server ID**:
   - Enable Developer Mode in Discord:
     - User Settings → App Settings → Advanced → Developer Mode
   - Right-click on your server name
   - Click "Copy Server ID"

3. **Deploy to GitHub Pages**:
   - Fork this repository
   - Go to repository Settings
   - Navigate to Pages section
   - Select main branch as source
   - Save changes
   - Your site will be available at `https://[your-username].github.io/[repo-name]/`

4. **Configure Your Embed**:
   - Visit your deployed website
   - Enter your Server ID
   - Enter your channel name (without the #)
   - Click "Save and Show Discord"
   - Your settings will be saved in your browser

## 🔒 Privacy & Security

- Your Server ID and channel settings are stored only in your browser's local storage
- No sensitive information is stored in the GitHub repository
- Settings can be updated or cleared at any time using the Edit button

## 🎨 Features

- Responsive design that works on mobile and desktop
- Discord-themed interface
- Local storage for settings
- Easy configuration form
- Edit button to update settings
- Private storage of server details
- Dark theme to match Discord's aesthetic

## 📱 Browser Support

Tested and working on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🔧 Troubleshooting

If the widget doesn't appear:
1. Verify that the Server ID is correct
2. Make sure the Discord widget is enabled in your server
3. Check that your server's widget settings allow the channel to be visible
4. Clear your browser's local storage and try setting it up again

## ⚠️ Common Issues

**Widget Not Showing**:
- Ensure "Enable Server Widget" is turned on in Discord server settings
- Server ID must be correct and widget-enabled
- At least one channel must be visible to the widget

**Settings Not Saving**:
- Make sure your browser allows local storage
- Try using a different browser if issues persist

## 🛠️ Advanced Customization

Want to customize the appearance? You can modify:
1. Open `index.html`
2. Find the `<style>` section
3. Adjust colors, sizes, and layout to match your preferences

## 📝 License

MIT License - feel free to use this code for any purpose.

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 🆘 Support

If you encounter any issues:
1. Check the [Issues](../../issues) section
2. Create a new issue if your problem isn't already reported

---

Made with ❤️ for the Discord community
