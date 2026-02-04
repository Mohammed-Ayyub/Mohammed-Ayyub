# Quick Reference Card

## 🚀 Quick Commands

### Setup
```bash
# Clone repository
git clone https://github.com/Mohammed-Ayyub/Mohammed-Ayyub.git
cd Mohammed-Ayyub

# Install dependencies
pip install -r requirements.txt
```

### Generate Stats
```bash
# Generate profile statistics
python profile_generator.py Mohammed-Ayyub
```

### Update Profile
```bash
# Make changes to README.md
nano README.md

# Commit and push
git add .
git commit -m "Update profile"
git push origin main
```

## 📋 File Structure

```
Mohammed-Ayyub/
├── README.md                  # Your profile (displays on GitHub)
├── profile_generator.py       # Stats generator script
├── requirements.txt           # Python dependencies
├── DOCUMENTATION.md           # Full documentation
├── EXAMPLES.md               # Usage examples
├── QUICK_REFERENCE.md        # This file
├── .gitignore                # Git ignore rules
└── .github/
    └── workflows/
        └── update-profile.yml # Auto-update workflow
```

## 🎨 Popular Themes

| Theme | Preview |
|-------|---------|
| `radical` | Dark with pink/purple |
| `dark` | Classic dark theme |
| `tokyonight` | Tokyo night colors |
| `dracula` | Dracula color scheme |
| `onedark` | Atom One Dark |
| `cobalt` | Blue cobalt theme |
| `synthwave` | Retro synthwave |
| `gruvbox` | Gruvbox colors |

**Usage**: Change `theme=radical` in README.md badge URLs

## 🏷️ Badge Templates

### Tech Badges
```markdown
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
```

### Social Badges
```markdown
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](URL)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](URL)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:EMAIL)
```

## 📊 Stats Cards

### GitHub Stats
```markdown
![Stats](https://github-readme-stats.vercel.app/api?username=USERNAME&show_icons=true&theme=radical)
```

### Top Languages
```markdown
![Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=USERNAME&layout=compact&theme=radical)
```

### Streak Stats
```markdown
![Streak](https://github-readme-streak-stats.herokuapp.com/?user=USERNAME&theme=radical)
```

### Profile Trophies
```markdown
![Trophies](https://github-profile-trophy.vercel.app/?username=USERNAME&theme=radical&row=1&column=7)
```

### Profile Views
```markdown
![Views](https://komarev.com/ghpvc/?username=USERNAME&label=Profile%20Views&color=0e75b6&style=flat)
```

## 🔧 Customization Cheat Sheet

### Change Colors
Replace hex colors in badge URLs:
- Blue: `0077B5`
- Green: `00C853`
- Red: `E53935`
- Purple: `9C27B0`
- Orange: `FF6F00`

### Badge Styles
- `style=flat` - Flat style
- `style=flat-square` - Square flat
- `style=for-the-badge` - Large bold
- `style=plastic` - Plastic look
- `style=social` - Social media style

### Layout Options
Stats cards support:
- `hide=stars,commits,prs,issues` - Hide specific stats
- `show_icons=true` - Show icons
- `include_all_commits=true` - Include all commits
- `count_private=true` - Count private repos

## 🔄 Workflow Commands

### Manual Trigger
```bash
# Via GitHub CLI
gh workflow run update-profile.yml

# Via web interface
# Go to Actions tab → Update Profile README → Run workflow
```

### Schedule Syntax
```yaml
# Daily at midnight
- cron: '0 0 * * *'

# Every 6 hours
- cron: '0 */6 * * *'

# Weekly on Monday
- cron: '0 0 * * 1'

# Monthly on 1st
- cron: '0 0 1 * *'
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Stats not showing | Check username in URLs, verify service is up |
| Badges broken | Verify badge URL syntax, check image links |
| Workflow fails | Check Actions logs, verify syntax |
| Rate limited | Add GITHUB_TOKEN, reduce API calls |
| Images not loading | Check internet connection, try different CDN |

## 📱 Social Media Links

| Platform | Badge Template |
|----------|----------------|
| LinkedIn | `[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](URL)` |
| Twitter | `[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](URL)` |
| Instagram | `[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](URL)` |
| YouTube | `[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](URL)` |
| Medium | `[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](URL)` |
| Dev.to | `[![Dev.to](https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](URL)` |

## 🌐 Useful URLs

- **Profile**: `https://github.com/USERNAME`
- **Actions**: `https://github.com/USERNAME/USERNAME/actions`
- **Settings**: `https://github.com/USERNAME/USERNAME/settings`
- **Edit README**: `https://github.com/USERNAME/USERNAME/edit/main/README.md`

## 💡 Pro Tips

1. **Update Regularly**: Keep skills and projects current
2. **Use Cache Busting**: Add `?v=1` to force refresh
3. **Test Mobile**: Check appearance on phones
4. **Keep Simple**: Don't overload with widgets
5. **Check Performance**: Too many external calls slow loading
6. **Version Control**: Always commit before major changes
7. **Preview First**: Use GitHub's preview before committing

## 🔗 Important Links

- [Full Documentation](DOCUMENTATION.md)
- [Usage Examples](EXAMPLES.md)
- [GitHub Profile README Guide](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)

---

**Made with ❤️ by Mohammed Ayyub**
