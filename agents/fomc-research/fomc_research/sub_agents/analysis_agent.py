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

"""Analyze real estate investments based on ESG and geopolitical factors."""

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from ..config import LITELLM_MODEL
from ..shared_libraries.callbacks import rate_limit_callback, add_continue_button
from . import analysis_agent_prompt
from .esg_analyst_agent import ESGAnalystAgent
from .geopolitical_agent import GeopoliticalAgent
from .market_data_agent import MarketDataAgent

AnalysisAgent = Agent(
    model=LiteLlm(model=LITELLM_MODEL),
    name="analysis_agent",
    description=(
        "Analyze real estate investment opportunities using all three analytical perspectives: market data, ESG factors, and geopolitical considerations."
    ),
    instruction=analysis_agent_prompt.PROMPT,
    sub_agents=[
        ESGAnalystAgent,
        GeopoliticalAgent,
        MarketDataAgent,
    ],
    before_model_callback=rate_limit_callback,
    after_model_callback=add_continue_button,
)
