# Intelligent Code Review Automation

## Overview
This workflow automatically reviews GitHub Pull Requests using Groq AI (LLaMA 3.1) and posts findings as comments.

## Architecture

GitHub PR → Webhook → Kestra → Groq API → Format Results → GitHub Comment

text

## Files
- `workflows/pr-review-workflow.yaml` - Main Kestra workflow

## Setup Required
1. **GitHub Personal Access Token** with `repo` scope
2. **Groq API Key** from [https://console.groq.com](https://console.groq.com)
3. **Kestra Secrets** (in KV Store):
   - `GITHUB_TOKEN`
   - `GROQ_API_KEY`

## How It Works

### Task Flow
1. **log_pr_info** - Logs incoming webhook data
2. **extract_pr_details** - Extracts PR number, URL, and repository info
3. **analyze_code_with_ai** - Calls Groq API for AI code analysis
4. **format_review_comment** - Formats findings into Markdown
5. **post_github_comment** - Posts comment to GitHub PR
6. **completion_summary** - Logs workflow completion

### Testing
Create a test PR:

```bash
git checkout -b test/code-review
echo "print('test')" >> test.py
git add test.py
git commit -m "test: add test file"
git push origin test/code-review

Then create a PR on GitHub and watch for the automated comment.

Troubleshooting
Webhook not triggering: Check GitHub webhook delivery logs
Groq API failing: Verify API key in Kestra KV Store
GitHub comment not posting: Check token permissions