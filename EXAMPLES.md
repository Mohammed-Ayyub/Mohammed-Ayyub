# Example Usage Guide

This guide shows practical examples of using the GitHub Profile Application.

## Quick Start

### 1. View Your Profile
After pushing changes to the main branch, visit:
```
https://github.com/Mohammed-Ayyub
```

Your enhanced profile README will be displayed on your profile page.

## 2. Generate Statistics Locally

### Basic Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Generate stats for your profile
python profile_generator.py Mohammed-Ayyub
```

### Example Output
```
Generating profile statistics for Mohammed-Ayyub...

==================================================

## 📈 Statistics

- **Public Repositories**: 15
- **Followers**: 42
- **Following**: 30
- **Profile Created**: 2020-05-15
- **Last Updated**: 2024-02-04

## 🔤 Top Languages

- **Python**: 45.2%
- **JavaScript**: 28.7%
- **Java**: 15.3%
- **HTML**: 7.8%
- **CSS**: 3.0%

==================================================

Badge URLs:
followers: https://img.shields.io/github/followers/Mohammed-Ayyub?style=social
stars: https://img.shields.io/github/stars/Mohammed-Ayyub?style=social
profile_views: https://komarev.com/ghpvc/?username=Mohammed-Ayyub
```

## 3. Customize Your Profile

### Change Theme
Edit `README.md` and change the `theme` parameter in badge URLs:

```markdown
<!-- Dark theme -->
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mohammed-Ayyub&show_icons=true&theme=dark)

<!-- Tokyo Night theme -->
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mohammed-Ayyub&show_icons=true&theme=tokyonight)

<!-- Dracula theme -->
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mohammed-Ayyub&show_icons=true&theme=dracula)
```

### Add Custom Badges
Add your own badges to the Tech Stack section:

```markdown
![Your Tech](https://img.shields.io/badge/YourTech-HexColor?style=for-the-badge&logo=yourlogo&logoColor=white)
```

Popular badges:
```markdown
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
```

### Update Projects Section
Replace placeholder projects with your actual repositories:

```markdown
## 📌 Featured Projects

### 🔥 [Awesome Web App](https://github.com/Mohammed-Ayyub/awesome-web-app)
A full-stack web application built with React and Node.js that helps users manage their tasks efficiently.

### 💻 [Python Data Tool](https://github.com/Mohammed-Ayyub/python-data-tool)
Data analysis toolkit for processing large datasets with pandas and visualizing results.

### 🌟 [Mobile App](https://github.com/Mohammed-Ayyub/mobile-app)
Cross-platform mobile application built with React Native for iOS and Android.
```

## 4. Automated Updates

### Manual Trigger
Go to Actions tab in GitHub:
```
https://github.com/Mohammed-Ayyub/Mohammed-Ayyub/actions
```
1. Click on "Update Profile README" workflow
2. Click "Run workflow"
3. Select branch and click "Run workflow"

### Scheduled Updates
The workflow automatically runs daily at midnight UTC. No action needed!

### View Workflow Logs
1. Go to Actions tab
2. Click on a workflow run
3. View the execution logs

## 5. Advanced Customization

### Add Spotify Now Playing
```markdown
[![Spotify](https://spotify-github-profile.vercel.app/api/view?uid=YOUR_SPOTIFY_ID&cover_image=true&theme=default)](https://spotify-github-profile.vercel.app/api/view?uid=YOUR_SPOTIFY_ID&redirect=true)
```

### Add WakaTime Stats
```markdown
[![WakaTime Stats](https://github-readme-stats.vercel.app/api/wakatime?username=YOUR_WAKATIME_USERNAME)](https://wakatime.com/@YOUR_WAKATIME_USERNAME)
```

### Add Activity Graph
```markdown
[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Mohammed-Ayyub&theme=radical)](https://github.com/ashutosh00710/github-readme-activity-graph)
```

### Add Latest Blog Posts
Use [gautamkrishnar/blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow) action:

1. Add to `.github/workflows/update-profile.yml`:
```yaml
- name: Update Blog Posts
  uses: gautamkrishnar/blog-post-workflow@master
  with:
    feed_list: "https://your-blog.com/feed.xml"
```

2. Add placeholder in README.md:
```markdown
## 📝 Latest Blog Posts
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
```

## 6. Testing Changes

### Preview Locally
Use a Markdown preview tool or GitHub's preview feature when editing README.md.

### Test Script
```bash
# Dry run - see what would be generated
python profile_generator.py Mohammed-Ayyub

# Verify badge URLs work
curl -I https://img.shields.io/github/followers/Mohammed-Ayyub?style=social
```

## 7. Common Issues and Solutions

### Issue: Stats Cards Not Loading
**Solution**: Check if external services are accessible. Try different theme or refresh cache by adding `?v=1` to URL.

### Issue: Workflow Not Running
**Solution**: 
1. Check Actions is enabled: Settings → Actions → General
2. Verify workflow file syntax
3. Check workflow logs for errors

### Issue: Rate Limiting
**Solution**: Add GitHub token to environment:
```bash
export GITHUB_TOKEN="your_token_here"
```

## 8. Best Practices

1. **Regular Updates**: Keep your skills and projects current
2. **Mobile Testing**: Preview on mobile devices
3. **Performance**: Don't add too many heavy images
4. **Accessibility**: Use alt text for images
5. **Privacy**: Don't share sensitive information
6. **Simplicity**: Keep it clean and professional

## 9. Resources and Inspiration

- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/)
- [Shields.io](https://shields.io/) - For custom badges
- [Simple Icons](https://simpleicons.org/) - For logo icons

## 10. Contributing Back

If you create unique features or improvements:
1. Fork this repository
2. Make your changes
3. Share your version with the community
4. Consider creating a blog post about your customizations

---

**Need Help?** Check [DOCUMENTATION.md](DOCUMENTATION.md) for detailed information.
