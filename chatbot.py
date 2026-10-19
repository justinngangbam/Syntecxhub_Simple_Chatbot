import re
import random
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self, log_file="chat_history_log.txt"):
        self.bot_name = "SyntecxBot"
        self.log_file = log_file
        self.conversation_history = []

        # 1. Intents: Greeting, Help, Small Talk, and Farewell
        self.intents = {
            "greeting": {
                "patterns": [r"\b(hi|hello|hey|greetings|good morning|good afternoon|good evening)\b"],
                "responses": [
                    "Hello! I am SyntecxBot. How can I help you today?",
                    "Hi there! Ask me anything about Artificial Intelligence, or type 'help' to see what I can do.",
                    "Hey! Welcome. What would you like to chat about today?"
                ]
            },
            "help": {
                "patterns": [r"\b(help|support|what can you do|options|commands|menu)\b"],
                "responses": [
                    "I can help you with:\n"
                    "  1. General conversation & small talk (e.g., 'How are you?', 'Who are you?')\n"
                    "  2. Domain questions on AI (ask about 'AI', 'Machine Learning', 'Deep Learning', 'NLP', 'A* Search', or 'Python')\n"
                    "  3. Commands: Type 'history' to see our chat log, or 'exit' to quit."
                ]
            },
            "small_talk_status": {
                "patterns": [r"how are you", r"how is it going", r"how do you do", r"what's up"],
                "responses": [
                    "I'm running smoothly on Python code! How are you doing?",
                    "I'm doing great and ready to answer your questions! How about you?",
                    "All systems operational! How is your day going?"
                ]
            },
            "small_talk_identity": {
                "patterns": [r"who are you", r"what is your name", r"are you a bot", r"are you human"],
                "responses": [
                    "I am SyntecxBot, a rule-based conversational AI built for the Syntecxhub Internship!",
                    "My name is SyntecxBot! I use pattern matching and a knowledge base to chat with you."
                ]
            },
            "small_talk_thanks": {
                "patterns": [r"\b(thanks|thank you|appreciate it|helpful)\b"],
                "responses": [
                    "You're very welcome! Let me know if you have more questions.",
                    "Happy to help! Anything else you'd like to know?",
                    "Anytime! Feel free to ask another question."
                ]
            }
        }

        # 2. Domain Knowledge Base (Artificial Intelligence & Tech)
        self.knowledge_base = {
            r"\b(what is ai|artificial intelligence|\bai\b)\b": (
                "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, "
                "especially computer systems. It includes learning, reasoning, problem-solving, and perception."
            ),
            r"\b(machine learning|\bml\b)\b": (
                "Machine Learning (ML) is a subset of AI that allows software applications to become more accurate "
                "at predicting outcomes from data without being explicitly programmed for every rule."
            ),
            r"\b(deep learning|\bdl\b|neural network)\b": (
                "Deep Learning is a subset of Machine Learning based on artificial neural networks with multiple layers. "
                "It powers advanced tasks like image recognition and large language models."
            ),
            r"\b(nlp|natural language processing)\b": (
                "Natural Language Processing (NLP) is a branch of AI that gives computers the ability to understand, "
                "interpret, and generate human language—just like how we are chatting right now!"
            ),
            r"\b(a\*|a star|astar|pathfinding)\b": (
                "A* (A-Star) Search is an informed pathfinding algorithm that finds the shortest path between nodes "
                "using the cost function f(n) = g(n) + h(n), combining exact distance and a heuristic estimate."
            ),
            r"\b(expert system|forward chaining|rule-based)\b": (
                "A Rule-Based Expert System is an AI program that emulates the decision-making ability of a human expert "
                "using 'if-then' rules and an inference engine over a knowledge base."
            ),
            r"\b(python)\b": (
                "Python is the most popular programming language for AI and Data Science due to its clean syntax "
                "and rich ecosystem of libraries like Scikit-Learn, TensorFlow, and PyTorch."
            ),
            r"\b(syntecxhub)\b": (
                "Syntecxhub is a forward-thinking company that bridges learning with practical experience through "
                "hands-on internship projects in AI, Data Science, Web Development, and more."
            )
        }

        # Fallback responses when no pattern matches
        self.fallback_responses = [
            "I'm not sure I understand that yet. Try asking me about 'AI', 'Machine Learning', 'NLP', or type 'help'!",
            "Could you rephrase that? You can type 'help' to see the topics in my knowledge base.",
            "Hmm, that's outside my current rules. Ask me a question about Artificial Intelligence or Python!"
        ]

    def log_interaction(self, sender, message):
        """Records every message with a timestamp in memory and saves it to a text file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {sender}: {message}"
        self.conversation_history.append(log_entry)

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(log_entry + "\n")

    def get_response(self, user_input):
        """Matches user input against the knowledge base first, then general intents."""
        cleaned_input = user_input.lower().strip()

        # 1. Check the Domain Knowledge Base first for specific topic questions
        for pattern, answer in self.knowledge_base.items():
            if re.search(pattern, cleaned_input):
                return answer

        # 2. Check General Conversational Intents (Greeting, Help, Small Talk)
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data["patterns"]:
                if re.search(pattern, cleaned_input):
                    return random.choice(intent_data["responses"])

        # 3. Return a fallback message if no rules match
        return random.choice(self.fallback_responses)

    def show_history(self):
        """Displays the logged conversation history in the console."""
        print("\n" + "=" * 55)
        print("                 CONVERSATION HISTORY")
        print("=" * 55)
        if not self.conversation_history:
            print("No conversation history recorded yet.")
        else:
            for entry in self.conversation_history:
                print(entry)
        print("=" * 55 + "\n")

    def start_chat(self):
        """Runs the interactive console loop."""
        print("=" * 60)
        print(f" Welcome to {self.bot_name} - Simple Rule-Based AI Chatbot")
        print(" Type 'help' for options, 'history' for logs, or 'exit' to quit.")
        print("=" * 60)

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                # Log the user's input
                self.log_interaction("User", user_input)

                # Check for exit command
                if re.search(r"\b(exit|quit|bye|goodbye)\b", user_input.lower()):
                    farewell_msg = "Goodbye! Thanks for chatting with me. Have a great day!"
                    print(f"{self.bot_name}: {farewell_msg}")
                    self.log_interaction(self.bot_name, farewell_msg)
                    print(f"\n[System] Chat history saved to '{self.log_file}'.")
                    break

                # Check for history command
                if user_input.lower() in ["history", "show history", "log"]:
                    self.show_history()
                    continue

                # Generate, print, and log the bot's response
                bot_response = self.get_response(user_input)
                print(f"{self.bot_name}: {bot_response}")
                self.log_interaction(self.bot_name, bot_response)

            except (KeyboardInterrupt, EOFError):
                print(f"\n{self.bot_name}: Session ended. Goodbye!")
                break

if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start_chat()