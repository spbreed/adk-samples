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

"""Geopolitical agent for FOMC Research Agent."""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from ..config import LITELLM_MODEL
from ..shared_libraries.callbacks import rate_limit_callback, add_continue_button
from ..tools.store_state import store_state_tool
from . import geopolitical_agent_prompt

GeopoliticalAgent = Agent(
    model=LiteLlm(model=LITELLM_MODEL),
    name="geopolitical_agent",
    description=(
        "Analyze local and regional geopolitical developments and their potential impact on real estate investments."
    ),
    instruction=geopolitical_agent_prompt.PROMPT,
    tools=[
        store_state_tool,
    ],
    before_model_callback=rate_limit_callback,
    after_model_callback=add_continue_button,
)
