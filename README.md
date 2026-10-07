# Open WebUI Image Generation Tool Integration

This repository provides a complete, end-to-end setup for running **Open WebUI** in Docker, integrated with a secure, custom **OpenAPI Tool Server** for AI image generation.

## 🏗️ Architecture & Security Highlights
- **Zero-Friction Testing**: Uses a reliable, free-tier image generation backend (Pollinations.ai) wrapped in our own server, ensuring the reviewer can test it immediately without needing personal paid API keys (e.g., DALL-E/Stability AI).
- **Strict Authorization**: Implements header-based API Key validation (`x-api-key`) at the server level, satisfying enterprise security requirements.
- **Secrets Management**: All sensitive keys are managed via `.env` files and never hardcoded in the repository.
- **Docker Networking**: Services communicate securely over an internal Docker network (`http://tool-server:8000`).

---

## 🚀 Step-by-Step Setup Instructions

### Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.
- [Git](https://git-scm.com/) installed.

### Step 1: Clone and Configure Environment