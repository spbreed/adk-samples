#!/bin/bash
# Script to load environment variables from .env file

# Path to the .env file
ENV_FILE=".env"

# Check if .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: $ENV_FILE not found."
    exit 1
fi

# Export all variables from the .env file
echo "Loading environment variables from $ENV_FILE..."
set -o allexport
source "$ENV_FILE"
set +o allexport

echo "Environment variables loaded successfully."

# Print a confirmation message
echo "The following models are configured:"
echo "AWS Model: $AWS_GENAI_MODEL"
echo "Google Model: $GOOGLE_GENAI_MODEL"

# Optional: print all environment variables starting with AWS or GOOGLE
echo ""
echo "AWS Environment Variables:"
env | grep "^AWS" | sort

echo ""
echo "Google Environment Variables:"
env | grep "^GOOGLE" | sort

echo ""
echo "You can now run your agent with: adk run fomc_research"
