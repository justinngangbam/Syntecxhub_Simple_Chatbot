Simple Rule-Based Chatbot:

Developed for Week 2 of the Artificial Intelligence Internship program at Syntecxhub, this project implements a conversational bot using pattern matching. The system interacts with users through the console, responds to common conversational intents, answers domain-specific questions on Artificial Intelligence, and logs the complete conversation history.

Core Features:

1. Pattern Matching Engine: Creates a conversational bot using regular expression pattern matching in Python to analyze and respond to user inputs.
2. Intents & Rule Responses: Supports core conversational intents including greetings, help requests, and small talk with varied rule-based responses.
3. Domain Knowledge Base: Incorporates a dedicated knowledge base so the bot can answer domain questions regarding Artificial Intelligence, Machine Learning, Deep Learning, Natural Language Processing (NLP), A* Search, Expert Systems, and Python.
4. Interactive Console & Logging: Operates interactively via the console and automatically logs the conversation history with timestamps to both the terminal session and an external chat_history_log.txt file.

How It Works:

1. Input Preprocessing: The chatbot captures user input from the console loop and normalizes the text (converting it to lowercase and stripping extra whitespace).
2. Knowledge Base Priority Matching: The engine first scans the input against its domain knowledge base patterns so technical questions are answered accurately.
3. Intent Matching & Fallbacks: If no domain topic is detected, the bot checks general conversational intents (greeting, help, small talk) and returns an appropriate rule response, or provides a helpful fallback prompt if the query is unrecognized.
4. History Tracking: Every user prompt and bot reply is formatted with a YYYY-MM-DD HH:MM:SS timestamp and appended to chat_history_log.txt. Users can also type history at any time to view the session log directly in the console.

Execution:

To run the chatbot locally, open your terminal in the project directory and run: python chatbot.py
