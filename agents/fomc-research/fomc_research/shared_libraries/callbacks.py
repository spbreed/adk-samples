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

"""Callback functions for the Real Estate Investment Analysis Agent."""

import logging
import time
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


def rate_limit_callback(*args, **kwargs) -> Dict[str, Any]:
    """Callback function to rate limit API calls.

    Helps avoid 429 errors by adding a delay between calls.

    Args:
        *args: Positional arguments
        **kwargs: Keyword arguments

    Returns:
        The original request or response, unmodified
    """
    time.sleep(2)
    
    # Return the first argument if available (likely the request)
    if args and isinstance(args[0], dict):
        return args[0]
    
    # If no positional arguments, check for llm_request in kwargs
    if 'llm_request' in kwargs and isinstance(kwargs['llm_request'], dict):
        return kwargs['llm_request']
    
    # Last resort - return an empty dict to avoid errors
    return {}


def add_continue_button(*args, **kwargs) -> Dict[str, Any]:
    """Callback function to add a continue button to agent responses.

    This function modifies the agent's response to include a UI button
    that allows users to continue the conversation without typing.

    Args:
        *args: Positional arguments
        **kwargs: Keyword arguments

    Returns:
        The modified response with a continue button
    """
    # Extract the response from args or kwargs
    response = None
    
    if args and isinstance(args[0], dict):
        response = args[0]
    elif 'response' in kwargs and isinstance(kwargs['response'], dict):
        response = kwargs['response']
    
    # If we couldn't find a valid response, return empty dict
    if not response:
        return {}
    
    # Add the continue button if appropriate
    if "text" in response and isinstance(response["text"], str):
        text = response["text"]
        
        # Don't add the button if this is a final response or a question to the user
        if ("In conclusion" in text or 
            "final recommendation" in text or 
            "?" in text or
            "Please provide" in text):
            return response
            
        # Preserve the original text
        original_text = text
        
        # Add the continue button UI element (using a special syntax that the UI will recognize)
        continue_button = "\n\n<continue_button>Continue Analysis</continue_button>"
        response["text"] = original_text + continue_button
    
    return response
