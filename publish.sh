#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "🚀 Starting Deployment Pipeline for Devil-Stack..."

# --- 1. ENVIRONMENT CONFIGURATION ---
export BACKEND_PORT=8000
export FRONTEND_PORT=5173
export API_SECRET_KEY=$(openssl rand -hex 32)
export PRODUCTION_DOMAIN="yourdomain.com"

echo "🔑 Generated Secure API Key for this session: $API_SECRET_KEY"

# --- 2. BACKEND SETUP (devil-api) ---
echo "⚙️ Configuring Backend (devil-api)..."
cd ../devil-api

# Create python virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

# Generate Backend Production Environment
cat <<EOF > .env
DEVIL_API_KEY="$API_SECRET_KEY"
CORS_ORIGINS="http://localhost:$FRONTEND_PORT,https://$PRODUCTION_DOMAIN"
LOG_LEVEL="INFO"
EOF

# Run database/socket migrations if required by the repo
echo "⚡ Backend successfully prepared."
deactivate
cd ../devil-web

# --- 3. FRONTEND SETUP & BUILD (devil-web) ---
echo "📦 Configuring Frontend (devil-web)..."
npm install

# Generate Frontend Production Environment 
cat <<EOF > .env
PRIVATE_DEVIL_API_URL="http://127.0.0.1:$BACKEND_PORT"
PRIVATE_DEVIL_API_KEY="$API_SECRET_KEY"
ALLOW_INSECURE_BACKEND="false"
EOF

echo "🏗️ Building SvelteKit production application..."
npm run build

# --- 4. EXECUTION / PUBLISH ---
echo "✨ Build complete! Launching process supervisors..."
echo "To publish live, map ports $BACKEND_PORT (API) and $FRONTEND_PORT (UI) via reverse proxy (Nginx)."
chmod +x publish.sh
./publish.sh
