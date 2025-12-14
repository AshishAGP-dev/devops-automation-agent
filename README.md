# 🚀 PR Review Agent - DEPLOYED

**Status:** ✅ Live on Kestra Cloud
**Workflow ID:** `devopsflow.pr-review-workflow`

## Screenshots
- ✅ Kestra Flow Code (YAML deployed)
- ✅ Kestra Topology (workflow diagram)
- ✅ Kestra Execution Gantt (test run)

See `/screenshots` folder for proof of deployment.


# DevOpsFlow AI - Intelligent Code Review Agent

> **Hackathon**: AI Agents Assemble 2025  
> **Feature**: Automated PR Code Review using Kestra + Groq AI + GitHub API

## Problem Solved
Manual code reviews take 30+ minutes per PR. This automation provides instant, AI-powered code analysis in under 20 seconds.

## Features
- ✅ Automatic trigger on GitHub Pull Requests
- ✅ AI-powered code analysis using Groq LLaMA 3.1 (security, performance, style, bugs)
- ✅ Instant feedback posted as GitHub comments
- ✅ Severity-based issue grouping
- ✅ Full workflow orchestration with Kestra

## Architecture

Developer → GitHub PR → Webhook → Kestra Workflow
↓
Extract PR Data
↓
Groq AI API
↓
Format Results
↓
Post to GitHub

text

## Quick Start

### Prerequisites
- GitHub account with repository
- Kestra (running locally via Docker)
- Groq API key (free from console.groq.com)
- Python 3.8+

### Setup
1. Clone this repository
2. Copy `.env.example` to `.env` and fill in your API keys
3. Start Kestra with Docker Compose
4. Add secrets to Kestra KV Store (`GROQ_API_KEY`, `GITHUB_TOKEN`)
5. Deploy workflow to Kestra
6. Configure GitHub webhook
7. Create a test PR

Detailed setup instructions: [kestra/README.md](kestra/README.md)

## Project Structure

devops-automation-agent/
├── kestra/
│ ├── workflows/
│ │ └── pr-review-workflow.yaml # Main workflow
│ └── README.md
├── src/
│ └── utils/
│ ├── github_helper.py # GitHub API utilities
│ └── groq_helper.py # Groq AI utilities
├── docs/ # Documentation
├── .env.example # Environment template
└── README.md # This file

text

## Demo
[Link to demo video/screenshots will be added]

## Testing
Create a test PR:

```bash

git checkout -b test/feature
echo "def test(): pass" >> test.py
git add . && git commit -m "test: add test file"
git push origin test/feature
Then create a PR on GitHub and watch the automated review appear!

Results:
Before: 30+ minutes manual review

After: 15-20 seconds automated review

Improvement: 99% time reduction

Technologies Used:
Kestra - Workflow orchestration

Groq AI - LLaMA 3.1 70B for code analysis

GitHub API - PR integration

Python - Scripting and data processing

Docker - Container orchestration

 License
MIT

 Author
Ashish Patil (@AshishAutomates)

 Hackathon Submission
This project is built for the AI Agents Assemble 2025 hackathon by WeMakeDevs.

Status: Feature Complete - PR Review Agent with AI Analysis
