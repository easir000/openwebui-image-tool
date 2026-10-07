```markdown
# Open WebUI Image Generation Tool Integration

This repository provides a complete, end-to-end setup for running **Open WebUI** in Docker, integrated with a secure, custom **OpenAPI Tool Server** for AI image generation.

## ️ Architecture & Security Highlights
- **Zero-Friction Testing:** Uses a reliable, free-tier image generation backend (Pollinations.ai) wrapped in a custom FastAPI server. This ensures the reviewer can test it immediately without needing personal paid API keys (e.g., DALL-E/Stability AI).
- **Strict Authorization:** Implements header-based API Key validation (`x-api-key`) at the server level, satisfying enterprise security requirements.
- **Secrets Management:** All sensitive keys are managed via `.env` files and are strictly excluded from version control via `.gitignore`.
- **Docker Networking:** Services communicate securely over an internal Docker network (`http://tool-server:8000`).

---

## 🚀 Step-by-Step Setup Instructions

### Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed and running.

### Step 1: Clone and Configure Environment
```bash
# 1. Clone the repository
git clone <YOUR_GITHUB_REPO_URL>
cd openwebui-image-tool

# 2. Create the .env file from the example
cp .env.example .env

# 3. (Optional) Edit .env to change the API key if desired
# The default key is: TOOL_SERVER_API_KEY=super-secret-test-key-123
```

### Step 2: Start the Services
```bash
# Build and run both Open WebUI and the Tool Server in the background
docker compose up -d --build
```
*Wait ~30-60 seconds for the containers to initialize. Verify they are running:*
```bash
docker compose ps
# Both 'open-webui' and 'tool-server' should show "Up"
```

### Step 3: Configure the Tool in Open WebUI
1. Open your browser and navigate to: `http://localhost:3000`
2. Create an admin account (first-time setup).
3. Click on your profile avatar (bottom left) → **Admin Panel** (or go to **Workspace** → **Tools**).
4. Click **+** (Create New Tool) and select the **OpenAPI** tab/option.
5. Copy the entire contents of `openapi-spec.json` from this repository and paste it into the schema box.
6. Name the tool: `Image Generator`.
7. **Configure Authorization (Crucial):** 
   - In the tool settings, locate the **Authentication** or **Headers** section.
   - Add a new header:
     - **Key:** `x-api-key`
     - **Value:** `super-secret-test-key-123` *(Matches the `.env` file)*.
8. Click **Save**.

### Step 4: Test End-to-End
1. Go to the main **Chat** interface (Click **New Chat**).
2. At the top of the chat window, **Select a model** (e.g., any available LLM like `llama3-8b` or `qwen`).
3. Above the text input box, click the **Tools icon** (puzzle piece 🧩) and ensure `Image Generator` is toggled **ON**.
4. Type the following prompt and hit Enter:  
   > *"Generate an image of a futuristic cyberpunk city at sunset."*
5. The LLM will intelligently call the tool, pass the prompt, and return the generated image URL directly in the chat.

---

## 🛠️ Troubleshooting
- **Tool returns 401 Unauthorized:** Ensure the `x-api-key` header in Open WebUI exactly matches the `TOOL_SERVER_API_KEY` in your `.env` file.
- **Tool returns 500 Network Error:** Ensure Open WebUI is using the internal Docker URL `http://tool-server:8000` as defined in the `openapi-spec.json` servers array.
- **View Logs:** Run `docker compose logs -f tool-server` to inspect backend requests.

##  Cleanup
To stop and remove all containers and volumes:
```bash
docker compose down -v
```
```