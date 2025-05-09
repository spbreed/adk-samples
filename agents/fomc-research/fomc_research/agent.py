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

"""Real Estate Investment Analysis Agent."""

import logging
import warnings

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from . import root_agent_prompt
from .config import LITELLM_MODEL
from .shared_libraries.callbacks import rate_limit_callback, add_continue_button
from .sub_agents.analysis_agent import AnalysisAgent
from .tools.store_state import store_state_tool

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

logger = logging.getLogger(__name__)

root_agent = Agent(
    model=LiteLlm(model=LITELLM_MODEL),
    name="root_agent",
    description=(
        "Use tools and other agents provided to generate an analysis report "
        "for real estate investors based on ESG and geopolitical factors."
    ),
    instruction=root_agent_prompt.PROMPT,
    tools=[store_state_tool],
    sub_agents=[
        AnalysisAgent,
    ],
    before_model_callback=rate_limit_callback,
    after_model_callback=add_continue_button,
)
