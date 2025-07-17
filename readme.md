LangGraph Agentic Models Practice
Author: Harsh Srivastava
Handle: horus-bot
Purpose: Practice repository for LangGraph agentic model implementations

📖 Overview
This repository contains various implementations of AI agents using LangGraph, demonstrating different patterns and use cases for building intelligent, tool-enabled conversational systems. Each project explores different aspects of agentic AI development, from basic chatbots to sophisticated RAG (Retrieval-Augmented Generation) systems.

🏗️ Project Structure
🚀 Key Features
1. Mathematical Tools Agent (toolsChatbot.ipynb)
Performs arithmetic operations (addition, subtraction, multiplication)
Demonstrates tool calling with LangGraph state management
Uses ChatGroq with Llama-3.3-70b-versatile model
2. RAG System (rag/ragModel.ipynb)
Document-based question answering
PDF processing with vector embeddings
ChromaDB for persistent vector storage
Contextual search with citation support
3. Email Automation Agent (emailAgent.ipynb)
Automated email composition and sending
SMTP integration with Gmail
Natural language email generation
4. Conditional Routing (2nd_level_contion.ipynb)
Multi-level decision trees
Complex workflow orchestration
Dynamic routing based on user input
🛠️ Technology Stack
Component	Technology
Framework	LangGraph
LLM Provider	ChatGroq (Llama-3.3-70b-versatile)
Vector Database	ChromaDB
Embeddings	HuggingFace (all-MiniLM-L6-v2)
Document Processing	PyPDF, LangChain
Email	SMTP, aiosmtplib
📋 Installation
Prerequisites
Environment Setup
Create a .env file in the root directory:

🎯 Quick Start
1. Mathematical Tools Agent
2. RAG System
3. Email Agent
🔧 Core Patterns
State Management
All agents use consistent state management:

Tool Integration
Tools are defined using LangChain's @tool decorator:

Conditional Routing
Agents use conditional edges for decision making:

📊 Example Workflows
Basic Chatbot Flow
Tool-Enhanced Agent Flow
RAG System Flow
🎓 Learning Objectives
This repository demonstrates:

LangGraph Fundamentals: State graphs, nodes, and edges
Tool Integration: Seamless LLM-tool interaction
State Management: Message handling and conversation flow
Conditional Logic: Dynamic routing and decision making
Error Handling: Robust system design
RAG Implementation: Document-based AI systems
🔍 Key Concepts Explored
State Graphs: Building complex AI workflows
Tool Calling: Extending LLM capabilities
Conditional Routing: Dynamic decision making
Vector Databases: Efficient document retrieval
Multi-turn Conversations: Context preservation
Error Handling: Graceful failure management
🚨 Common Issues & Solutions
Module Import Errors
API Key Issues
Ensure .env file is in the correct location
Verify API key validity
Check environment variable loading
Tool Execution Errors
Validate tool function signatures
Check tool registration with LLM
Verify tool call arguments
🤝 Contributing
This is a personal learning repository. Feel free to:

Fork and experiment
Submit improvements
Share feedback and suggestions
Add new agent patterns
📚 Resources
LangGraph Documentation
LangChain Documentation
ChatGroq API
ChromaDB Documentation
📄 License
Educational and research use. Please follow respective API terms of service.

Happy Coding! 🚀
Building the future of AI agents with LangGraph

Last updated: January 2025