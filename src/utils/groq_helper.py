"""
Groq AI API Helper Functions
Provides reusable functions for Groq AI code analysis
"""

import requests
from typing import Dict, Optional, List

def analyze_code(
    pr_details: Dict,
    groq_api_key: str,
    model: str = "llama-3.1-70b-versatile",
    timeout: int = 30
) -> Optional[Dict]:
    """
    Analyzes code using Groq AI API
    
    Args:
        pr_details: Dictionary with PR info (title, description, files_changed)
        groq_api_key: Groq API key
        model: Groq model to use
        timeout: Request timeout in seconds
    
    Returns:
        Dict with analysis results if successful, None if failed
    """
    api_endpoint = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    
    review_prompt = f"""You are an expert code reviewer. Analyze this Pull Request:

PR Title: {pr_details.get('title', 'N/A')}
PR Description: {pr_details.get('description', 'N/A')}
Files Changed: {pr_details.get('files_changed', 'N/A')}

Review the code for:
1. Security issues (SQL injection, XSS, hardcoded secrets)
2. Performance problems (inefficient loops, N+1 queries)
3. Code style and best practices
4. Potential bugs (null references, logic errors)
5. Missing tests or documentation

Provide a structured review in JSON format with: summary, issues (array with type, severity, message, suggestion)."""

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert code reviewer. Provide structured feedback in JSON format."
            },
            {
                "role": "user",
                "content": review_prompt
            }
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(api_endpoint, headers=headers, json=payload, timeout=timeout)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            print(f"Groq API Error: {response.status_code}")
            print(response.text)
            return None
            
    except Exception as e:
        print(f"Error calling Groq API: {str(e)}")
        return None