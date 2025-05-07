#!/bin/bash

# Step 1: Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 2: Upgrade pip
pip install --upgrade pip

# Step 3: Install required packages
pip install -r requirements.txt

# Step 4: Set environment variables (example format)
# Update these values in your local .env file manually or automate below
cat <<EOT >> .env
GOOGLE_CLIENT_SECRET=your-google-client-secret.json
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TIMEZONE=America/Chicago
CALENDAR_ID=primary
EOT

# Step 5: Provide reminder to activate the environment
printf "✅ Setup complete. Run 'source venv/bin/activate' before starting your app.\n"

You can run this file with:
chmod +x setup.sh
./setup.sh
