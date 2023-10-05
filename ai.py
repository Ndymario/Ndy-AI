from langchain.llms import Ollama
from langchain.tools import Tool

# DuckDuckGo Tool
from langchain.tools import DuckDuckGoSearchResults
from langchain.agents import AgentType

from langchain.agents import initialize_agent, load_tools

llm = Ollama(model="llama2")
search = DuckDuckGoSearchResults()
tools = []

duckduckgo_tool = Tool(
        name = "DuckDuckGo Search",
        func = search.run,
        description="Only use if you do not have information on the question asked to you and need to search the internet for more information."
    )

tools.append(duckduckgo_tool)

duckduckgo_agent = initialize_agent(tools=tools,
                         llm=llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=False,
                         max_iterations = 3,
                         handle_parsing_errors="Clearly state what the final answer is")