#!/usr/bin/env python3
"""
GitHub Profile README Generator
This script helps generate dynamic content for your GitHub profile README.
"""

import json
import requests
from datetime import datetime
from typing import Dict, List

class GitHubProfileGenerator:
    """Generate dynamic content for GitHub profile README"""
    
    def __init__(self, username: str):
        """
        Initialize the generator with a GitHub username
        
        Args:
            username: GitHub username
        """
        self.username = username
        self.api_base = "https://api.github.com"
    
    def get_user_stats(self) -> Dict:
        """
        Fetch user statistics from GitHub API
        
        Returns:
            Dictionary containing user stats
        """
        try:
            response = requests.get(f"{self.api_base}/users/{self.username}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching user stats: {e}")
            return {}
    
    def get_repositories(self) -> List[Dict]:
        """
        Fetch user's repositories
        
        Returns:
            List of repository dictionaries
        """
        try:
            response = requests.get(
                f"{self.api_base}/users/{self.username}/repos",
                params={"sort": "updated", "per_page": 100}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []
    
    def get_language_stats(self) -> Dict[str, int]:
        """
        Calculate language statistics from all repositories
        
        Returns:
            Dictionary with language names and their byte counts
        """
        repos = self.get_repositories()
        language_stats = {}
        
        for repo in repos:
            if repo.get("fork"):
                continue
            
            try:
                response = requests.get(repo["languages_url"])
                response.raise_for_status()
                languages = response.json()
                
                for lang, bytes_count in languages.items():
                    language_stats[lang] = language_stats.get(lang, 0) + bytes_count
            except requests.RequestException:
                continue
        
        return language_stats
    
    def generate_stats_markdown(self) -> str:
        """
        Generate markdown content with statistics
        
        Returns:
            Markdown formatted string
        """
        user_stats = self.get_user_stats()
        
        if not user_stats:
            return "<!-- Stats unavailable -->"
        
        markdown = f"""
## 📈 Statistics

- **Public Repositories**: {user_stats.get('public_repos', 0)}
- **Followers**: {user_stats.get('followers', 0)}
- **Following**: {user_stats.get('following', 0)}
- **Profile Created**: {user_stats.get('created_at', 'N/A')[:10]}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
"""
        return markdown
    
    def generate_top_languages(self, top_n: int = 5) -> str:
        """
        Generate markdown list of top languages
        
        Args:
            top_n: Number of top languages to display
            
        Returns:
            Markdown formatted string
        """
        lang_stats = self.get_language_stats()
        
        if not lang_stats:
            return "<!-- Language stats unavailable -->"
        
        # Sort by byte count
        sorted_langs = sorted(lang_stats.items(), key=lambda x: x[1], reverse=True)
        top_langs = sorted_langs[:top_n]
        
        total_bytes = sum(lang_stats.values())
        
        markdown = "\n## 🔤 Top Languages\n\n"
        for lang, bytes_count in top_langs:
            percentage = (bytes_count / total_bytes) * 100
            markdown += f"- **{lang}**: {percentage:.1f}%\n"
        
        return markdown
    
    def generate_badge_urls(self) -> Dict[str, str]:
        """
        Generate shield.io badge URLs for the profile
        
        Returns:
            Dictionary of badge names and their URLs
        """
        badges = {
            "followers": f"https://img.shields.io/github/followers/{self.username}?style=social",
            "stars": f"https://img.shields.io/github/stars/{self.username}?style=social",
            "profile_views": f"https://komarev.com/ghpvc/?username={self.username}",
        }
        return badges


def main():
    """Main function to demonstrate the generator"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python profile_generator.py <github_username>")
        sys.exit(1)
    
    username = sys.argv[1]
    generator = GitHubProfileGenerator(username)
    
    print(f"Generating profile statistics for {username}...")
    print("\n" + "="*50)
    
    # Generate and display stats
    stats_md = generator.generate_stats_markdown()
    print(stats_md)
    
    langs_md = generator.generate_top_languages()
    print(langs_md)
    
    print("\n" + "="*50)
    print("\nBadge URLs:")
    badges = generator.generate_badge_urls()
    for name, url in badges.items():
        print(f"{name}: {url}")


if __name__ == "__main__":
    main()
