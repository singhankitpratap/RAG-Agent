from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Agent for web-related information
web_assistant = Agent(
    name="Web Assistant",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Provide a concise summary of recent updates with trusted sources."],
    show_tool_calls=True,
    markdown=True
)

# Agent for financial data analysis
finance_assistant = Agent(
    name="Finance Assistant",
    role="Deliver financial insights and data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True
        )
    ],
    instructions=["Present financial data in easy-to-read tables."],
    show_tool_calls=True,
    markdown=True,
)

# Combined agent team
assistant_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_assistant, finance_assistant],
    instructions=[
        "Ensure all outputs are backed by credible sources.",
        "Use tables for presenting financial data and structured Markdown for clarity."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Task execution using the team of agents
assistant_team.print_response(
    "Provide a summary of analyst recommendations and the latest news for TSLA (Tesla Inc.)",
    stream=True
)
