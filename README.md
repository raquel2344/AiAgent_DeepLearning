# AiAgent_DeepLearning

This repository contains the exported JSON for an AI Agent built using the [n8n](https://n8n.io/) automation platform. The agent is capable of managing Google Calendar events, handling contact information, storing user preferences, and responding intelligently through OpenAI’s language model integration.

---

## 📁 Workflow File

- `ai-agent-workflow.json`: The exported n8n workflow file.

---

## 🔧 How to Import the Workflow

### Option 1: Using the n8n UI

1. Open your [n8n instance](https://n8n.io/) (either hosted or self-hosted).
2. Go to the **"Workflows"** tab.
3. Click the **plus icon ➕** or "New Workflow".
4. Click the **gear icon ⚙️** (top right) > **"Import from file"**.
5. Upload the `ai-agent-workflow.json` file from this repository.
6. Click **"Activate"** if you want the workflow to run automatically.

---

### Option 2: Using the CLI (Self-Hosted Only)

If you're running n8n locally or via Docker:

```bash
n8n import:workflow --input=./ai-agent-workflow.json
