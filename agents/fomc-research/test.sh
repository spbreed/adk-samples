MODEL_ID="gemini-2.0-flash-001"
ACCESS_TOKEN=$(gcloud auth application-default print-access-token)

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  "https://aiplatform.googleapis.com/v1/publishers/google/models/${MODEL_ID}:streamGenerateContent" -d \
  $'{
    "contents": {
      "role": "user",
      "parts": [
        {
        "fileData": {
          "mimeType": "image/png",
          "fileUri": "gs://generativeai-downloads/images/scones.jpg"
          }
        },
        {
          "text": "Describe this picture."
        }
      ]
    }
  }'
