# GitHub Profile Application Documentation

## Overview

This repository serves as a **special GitHub profile repository** that displays on your GitHub profile page. It includes an enhanced README with dynamic statistics, badges, and automated updates.

## Features

### 1. Enhanced Profile README
The `README.md` includes:
- **Professional Header**: Eye-catching introduction with your name and title
- **About Section**: Brief description of your interests and goals
- **Tech Stack**: Visual badges showing your skills and technologies
- **GitHub Statistics**: Dynamic stats cards showing your GitHub activity
- **GitHub Trophies**: Achievement badges
- **Featured Projects**: Showcase your best work
- **Social Links**: Connect with various platforms
- **Profile Views Counter**: Track profile visits

### 2. Profile Generator Script (`profile_generator.py`)
A Python utility that:
- Fetches GitHub user statistics via the GitHub API
- Calculates language distribution across repositories
- Generates markdown-formatted statistics
- Creates badge URLs for your profile

#### Usage
```bash
python profile_generator.py <your-github-username>
```

Example:
```bash
python profile_generator.py Mohammed-Ayyub
```

#### Requirements
```bash
pip install requests
```

### 3. Automated Profile Updates
The `.github/workflows/update-profile.yml` workflow:
- Runs daily at midnight UTC
- Can be manually triggered
- Updates your profile statistics automatically
- Commits changes if there are updates

## Setup Instructions

### Initial Setup

1. **Clone this repository** (if you haven't already):
   ```bash
   git clone https://github.com/Mohammed-Ayyub/Mohammed-Ayyub.git
   cd Mohammed-Ayyub
   ```

2. **Customize the README.md**:
   - Update your name and title
   - Add your actual skills and technologies
   - Replace placeholder project descriptions
   - Update social media links
   - Adjust the color theme (e.g., `theme=radical` can be changed to `theme=dark`, `theme=tokyonight`, etc.)

3. **Test the profile generator**:
   ```bash
   pip install requests
   python profile_generator.py Mohammed-Ayyub
   ```

4. **Commit and push your changes**:
   ```bash
   git add .
   git commit -m "feat: customize GitHub profile"
   git push origin main
   ```

### Customization Options

#### Badge Themes
The GitHub stats cards support various themes:
- `dark`, `radical`, `merko`, `gruvbox`, `tokyonight`, `onedark`, `cobalt`, `synthwave`, `highcontrast`, `dracula`

Change the theme by modifying the `theme` parameter in the image URLs:
```markdown
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mohammed-Ayyub&show_icons=true&theme=dark)
```

#### Badge Colors
You can customize badge colors using shields.io syntax:
```markdown
![Custom Badge](https://img.shields.io/badge/Label-Message-COLOR?style=for-the-badge)
```

Common colors: `blue`, `green`, `red`, `yellow`, `orange`, `purple`, `pink`, `brown`

#### Adding More Stats
Additional stats widgets available:
- **Activity Graph**: `https://github-readme-activity-graph.vercel.app/graph?username=USERNAME&theme=radical`
- **WakaTime Stats**: Show coding time statistics
- **Spotify**: Display currently playing song

### Workflow Configuration

The GitHub Actions workflow can be customized:

1. **Change update frequency**: Modify the cron expression in `.github/workflows/update-profile.yml`
   - Current: `0 0 * * *` (daily at midnight)
   - Every 6 hours: `0 */6 * * *`
   - Weekly: `0 0 * * 0`

2. **Add more automation**:
   - Fetch latest blog posts
   - Update activity feed
   - Generate contribution graphs

## File Structure

```
Mohammed-Ayyub/
├── .github/
│   └── workflows/
│       └── update-profile.yml    # Automated profile updates
├── README.md                      # Your GitHub profile (displayed on profile page)
├── profile_generator.py           # Python script for generating stats
└── DOCUMENTATION.md               # This file
```

## Advanced Features

### Using the GitHub API
The `profile_generator.py` script demonstrates how to:
- Authenticate with GitHub API (add token for higher rate limits)
- Fetch user data and repository information
- Calculate language statistics
- Generate dynamic content

### Rate Limiting
GitHub API has rate limits:
- **Unauthenticated**: 60 requests/hour
- **Authenticated**: 5,000 requests/hour

To use authentication, set the `GITHUB_TOKEN` environment variable:
```bash
export GITHUB_TOKEN="your_personal_access_token"
```

Then modify the script to use the token in request headers.

## Tips and Best Practices

1. **Keep it Updated**: Regularly update your featured projects and skills
2. **Be Authentic**: Showcase real projects and genuine interests
3. **Use Quality Images**: Ensure badges and stats load properly
4. **Test Changes**: Preview your README before committing
5. **Monitor Performance**: Check if external services (stats APIs) are responsive
6. **Add Personal Touch**: Include unique elements that represent you
7. **Mobile Friendly**: Test how your profile looks on mobile devices

## Troubleshooting

### Stats Not Loading
- Check if the external API services are up
- Verify your username is correct in the URLs
- Check browser console for CORS or loading errors

### Workflow Not Running
- Ensure GitHub Actions is enabled in repository settings
- Check if the workflow file is in the correct location
- Review workflow run logs for errors

### Script Errors
- Verify Python version (3.7+)
- Install required packages: `pip install requests`
- Check API rate limits

## Resources

- [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/)
- [GitHub README Stats](https://github.com/anuraghazra/github-readme-stats)
- [Shields.io Badge Documentation](https://shields.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Awesome GitHub Profile READMEs](https://github.com/abhisheknaiidu/awesome-github-profile-readme)

## Contributing

Feel free to fork this repository and customize it for your own profile. If you create interesting enhancements, consider sharing them!

## License

This project is open source and available for anyone to use and customize.

---

**Happy Coding! 🚀**
