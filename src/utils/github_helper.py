"""
GitHub API Helper Functions
Provides reusable functions for GitHub integrations
"""

import requests
from typing import Dict, Optional

def post_pr_comment(
    repo_full_name: str,
    pr_number: int,
    comment_body: str,
    github_token: str,
    timeout: int = 10
) -> Optional[Dict]:
    """
    Posts a comment to a GitHub Pull Request
    
    Args:
        repo_full_name: Format "owner/repo"
        pr_number: PR number (integer)
        comment_body: Markdown-formatted comment text
        github_token: GitHub Personal Access Token
        timeout: Request timeout in seconds
    
    Returns:
        Dict with comment data if successful, None if failed
    """
    url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"
    
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {"body": comment_body}
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=timeout)
        
        if response.status_code == 201:
            return response.json()
        else:
            print(f"GitHub API Error: {response.status_code}")
            print(response.text)
            return None
            
    except Exception as e:
        print(f"Error posting comment: {str(e)}")
        return None