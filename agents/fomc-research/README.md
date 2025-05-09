#  Real Estate Investment Analysis Agent

The Real Estate Investment Analysis Agent uses a multi-agent architecture to generate
detailed analysis reports for real estate investors based on market data, ESG (Environmental, Social, and Governance) 
factors, and geopolitical considerations for specific locations and organizations. This agent 
provides location-specific insights to support informed investment decisions.

## Overview

Investors increasingly consider historical market performance, ESG and geopolitical factors when making real estate investment 
decisions. These factors can significantly impact property values, development opportunities, 
rental income potential, and overall investment risk.

This agent demonstrates how a multi-agent architecture can be used to generate comprehensive 
real estate investment analysis reports. The agent collects information about a specific location 
(zipcode or address) and relevant organizations, then leverages specialized sub-agents to analyze 
historical price trends, ESG factors, and geopolitical considerations before synthesizing a final investment recommendation.

## Agent Details
The key features of the Real Estate Investment Analysis Agent include:

| Feature | Description |
| --- | --- |
| *Interaction Type* | Workflow |
| *Complexity* | Advanced |
| *Agent Type* | Multi Agent |
| *Components* | Tools, AgentTools |
| *Vertical* | Real Estate Investment |

### Agent Architecture

The agent architecture consists of a root agent that coordinates specialized sub-agents working through the analysis agent:

### Key Features

##### Agents
* **root_agent:** Entry point for the agent workflow. Collects location and organization information from the user and coordinates the analysis.
* **analysis_agent:** Coordinates the specialized analysis sub-agents and synthesizes their findings into a comprehensive investment recommendation.
* **market_data_agent:** Analyzes historical real estate price trends and market metrics for the specified location over the past 5 years, providing data on appreciation rates, market cycles, and future projections.
* **esg_analyst_agent:** Analyzes ESG (Environmental, Social, and Governance) factors related to the specified location and organizations, focusing on sustainability metrics, green building certifications, community initiatives, and governance practices relevant to real estate investment.
* **geopolitical_agent:** Evaluates local and regional political developments, regulatory environments, demographic trends, and economic factors that could impact real estate investments in the specified location.

##### Tools
* **store_state_tool**: Stores location and organization information in the ToolContext.

##### Callbacks
* **rate_limit_callback**: Implements request rate limiting to minimize `429: Resource Exhausted` errors.
* **add_continue_button**: Adds a UI button that allows users to continue the analysis without typing.

## Setup and Installation

### Quick Start

1. **Set up Python environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Linux/Mac
   # Or on Windows:
   myenv\Scripts\activate
   ```

2. **Copy the environment template**:
   ```bash
   cp .env-example .env
   ```

3. **Update the .env file** with your API keys and configuration:
   - For **AWS Bedrock**: Add your AWS access keys and select a Claude model
   - For **Google Vertex AI**: Add your GCP project details and select a Gemini model

4. **Configure authentication**:
   - For AWS Bedrock:
     ```bash
     # AWS credentials are loaded from .env file
     ```
   - For Google Cloud:
     ```bash
     gcloud auth application-default login
     gcloud services enable aiplatform.googleapis.com
     gcloud services enable bigquery.googleapis.com
     ```

5. **Load environment variables**:
   ```bash
   # On Linux/Mac
   chmod +x load_env.sh
   ./load_env.sh
   
   # On Windows PowerShell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   .\load_env.sh
   ```

6. **Install dependencies**:
   ```bash
   # Install Poetry if needed
   pip install poetry
   
   # Install all dependencies
   poetry install
   ```

7. **Switch between models**: Edit your .env file and uncomment the desired model:
   ```
   # For AWS Bedrock (Claude)
   AWS_GENAI_MODEL=us.anthropic.claude-3-sonnet-20240229-v1:0
   # GOOGLE_GENAI_MODEL=gemini-2.0-flash-001
   ```
   Or for Google Vertex AI (Gemini):
   ```
   # AWS_GENAI_MODEL=us.anthropic.claude-3-sonnet-20240229-v1:0
   GOOGLE_GENAI_MODEL=gemini-2.0-flash-001
   ```

### Additional Configuration

**For Google Cloud Deployment (Optional):**

If you plan to deploy the agent to Google Agent Engine, you'll need additional setup:

1. [Install the Google Cloud SDK](https://cloud.google.com/sdk/docs/install) and authenticate:
   ```bash
   gcloud auth login
   ```

2. For BigQuery integration, set up permissions for the Reasoning Engine Service Agent:
   ```bash
   export RE_SA="service-${GOOGLE_CLOUD_PROJECT_NUMBER}@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
   gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
       --member="serviceAccount:${RE_SA}" \
       --condition=None \
       --role="roles/bigquery.user"
   gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
       --member="serviceAccount:${RE_SA}" \
       --condition=None \
       --role="roles/bigquery.dataViewer"
   ```

3. If you want to use the sample data for testing:
   ```bash
   python bigquery_setup.py --project_id=$GOOGLE_CLOUD_PROJECT \
       --dataset_id=$GOOGLE_CLOUD_BQ_DATASET \
       --location=$GOOGLE_CLOUD_LOCATION \
       --data_file=sample_timeseries_data.csv
   ```

## Running the Agent

**Using the ADK command line:**

From the `fomc-research` directory, run this command:
```bash
adk run fomc_research
```
The initial output will include a command you can use to tail the agent log
file. The command will be something like this:
```bash
tail -F /tmp/agents_log/agent.latest.log
```

**Using the ADK Dev UI:**

From the `fomc-research` directory, run this command:
```bash
adk web .
```
It will display a URL for the demo UI. Point your browser to that URL.

The UI will be blank initially. In the dropdown at the top left, choose `fomc_research`
to load the agent.

The logs from the agent will display on the console in real time as it runs. However,
if you want to store a log of the interaction and also tail the interaction in real
time, use the following commands:

```bash
adk web . > fomc_research_log.txt 2>&1 &
tail -f fomc_research_log.txt
```

### Example Interaction

Begin the interaction by typing "Hello. What can you do for me?". After the first prompt, provide the location and organizations you want to analyze.

The interaction will look something like this:
```
$ adk run .
Log setup complete: /tmp/agents_log/agent.20250405_140937.log
To access latest log: tail -F /tmp/agents_log/agent.latest.log
Running agent root_agent, type exit to exit.
user: Hello. What can you do for me?
[root_agent]: I can help you analyze real estate investment opportunities based on market data, ESG (Environmental, Social, and Governance) factors, and geopolitical considerations. To start, please provide the location (zipcode or address) you're interested in investing in, as well as any specific organizations or companies in that area you'd like me to analyze.

user: I'm interested in investing in Austin, TX 78701 downtown area. Please analyze properties near Oracle, Tesla, and Google offices.
[analysis_agent]: I'll analyze real estate investment opportunities in downtown Austin, TX (78701) near Oracle, Tesla, and Google offices. First, I need to gather information about ESG factors for these organizations and the geopolitical considerations for this location, as well as analyze market data for this area. I'll proceed step by step with all three analyses.

[Continue Analysis]

[esg_analyst_agent]: I'm analyzing the ESG (Environmental, Social, and Governance) factors for the downtown Austin area (78701) and the specified organizations (Oracle, Tesla, and Google)...

[Continue Analysis]

[geopolitical_agent]: I'm evaluating the local political landscape, economic development factors, demographic trends, and regulatory environment in downtown Austin...

[Continue Analysis]

[market_data_agent]: I'm analyzing the real estate market trends for downtown Austin, TX (78701) over the past 5 years, including price appreciation, rental yields, and future projections...

[Continue Analysis]

[analysis_agent]: Here is my real estate investment analysis for downtown Austin, TX (78701), focusing on properties near Oracle, Tesla, and Google offices:

[Comprehensive report with sections on market data, ESG factors, and geopolitical considerations]

Summary of Analyses:
- Market Data Analysis: Downtown Austin has experienced a 42% price appreciation over the past 5 years with an average annual return of 7.2%. The market shows strong rental yields of 4.8% with projected continued growth due to tech sector expansion.
- ESG Analysis: All three companies demonstrate strong sustainability commitments, with Google achieving carbon neutrality and Tesla's focus on renewable energy creating positive neighborhood impacts. Oracle's community investment programs have enhanced local infrastructure.
- Geopolitical Analysis: Austin's business-friendly policies, strong tech sector growth, and infrastructure investments create a stable environment for real estate appreciation, though recent regulatory changes regarding short-term rentals should be monitored.

Based on the integration of these analyses, properties in downtown Austin near these tech campuses represent a strong investment opportunity with both appreciation and rental income potential...
```
Note that in the interaction above, the [Continue Analysis] buttons allow the user to progress through the analysis without typing commands like "please continue" or "go on."

## Deployment on Vertex AI Agent Engine

To deploy the agent to Google Agent Engine, first follow
[these steps](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up)
to set up your Google Cloud project for Agent Engine.

You also need to give BigQuery User and BigQuery Data Viewer permissions to the
Reasoning Engine Service Agent. Run the following commands to grant the required
permissions:
```bash
export RE_SA="service-${GOOGLE_CLOUD_PROJECT_NUMBER}@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
    --member="serviceAccount:${RE_SA}" \
    --condition=None \
    --role="roles/bigquery.user"
gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
    --member="serviceAccount:${RE_SA}" \
    --condition=None \
    --role="roles/bigquery.dataViewer"
```
Next, you need to create a `.whl` file for your agent. From the `fomc-research`
directory, run this command:
```bash
poetry build --format=wheel --output=deployment
```
This will create a file named `fomc_research-0.1-py3-none-any.whl` in the
`deployment` directory.

Then run the following command:
```bash
cd deployment
python3 deploy.py --create
```
When this command returns, if it succeeds it will print an AgentEngine resource
name that looks something like this:
```
projects/************/locations/us-central1/reasoningEngines/7737333693403889664
```
The last sequence of digits is the AgentEngine resource ID.

Once you have successfully deployed your agent, you can interact with it
using the `test_deployment.py` script in the `deployment` directory. Store the
agent's resource ID in an enviroment variable and run the following command:
```bash
export RESOURCE_ID=...
export USER_ID=<any string>
python test_deployment.py --resource_id=$RESOURCE_ID --user_id=$USER_ID
```
The session will look something like this:
```
Found agent with resource ID: ...
Created session for user ID: ...
Type 'quit' to exit.
Input: Hello. What can you do for me?
Response: I can create an analysis report on FOMC meetings. To start, please provide the date of the meeting you want to analyze. I need the date in YYYY-MM-DD format.

Input: 2025-01-29
Response: I have stored the date you provided. Now I will retrieve the meeting data.
...
```
Note that this is *not* a full-featured, production-ready CLI; it is just intended to
show how to use the Agent Engine API to interact with a deployed agent.

The main part of the `test_deploy.py` script is approximately this code:

```python
from vertexai import agent_engines
remote_agent = vertexai.agent_engines.get(RESOURCE_ID)
session = remote_agent.create_session(user_id=USER_ID)
while True:
    user_input = input("Input: ")
    if user_input == "quit":
      break

    for event in remote_agent.stream_query(
        user_id=USER_ID,
        session_id=session["id"],
        message=user_input,
    ):
        parts = event["content"]["parts"]
        for part in parts:
            if "text" in part:
                text_part = part["text"]
                print(f"Response: {text_part}")
```

To delete the agent, run the following command (using the resource ID returned previously):
```bash
python3 deployment/deploy.py --delete --resource_id=$RESOURCE_ID
```

## Troubleshooting

### "Malformed function call"

Occasionally the agent returns the error "Malformed function call". This is a
Gemini model error which should be addressed in future model versions. Simply
restart the UI and the agent will reset.

### Agent stops mid-workflow

Sometimes the agent will stop mid-workflow, after completing one of the
intermediate steps. When this happens, it frequently works just to tell the agent
to continue, or another instruction to continue its operation.
