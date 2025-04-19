# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration for the Real Estate Investment Analysis Agent."""

import os
import logging
import litellm

logger = logging.getLogger(__name__)


# Configure litellm with AWS credentials
litellm.aws_bedrock_credentials = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "aws_region_name": os.getenv("AWS_REGION_NAME")
} 

# For GCP models, make sure to run 'gcloud auth application-default login' first
# Get model name from environment

MODEL = os.getenv("GOOGLE_GENAI_MODEL")
# MODEL = os.getenv("AWS_GENAI_MODEL")
if not MODEL:
    MODEL = "gemini-1.5-flash-002"

# For AWS Bedrock, prepend with "bedrock/" if needed
if "anthropic" in MODEL and not MODEL.startswith("bedrock/"):
    LITELLM_MODEL = f"bedrock/{MODEL}"
else:
    LITELLM_MODEL = MODEL

logger.debug("Using MODEL: %s", MODEL)
logger.debug("Using LITELLM_MODEL: %s", LITELLM_MODEL)
