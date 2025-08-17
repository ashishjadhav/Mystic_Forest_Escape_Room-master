# Mystic Forest Escape Room Chatbot - RASA Project

## Project Overview
Welcome to the Mystic Forest Escape Room Chatbot, a RASA-based project that brings the excitement of an escape room adventure to the virtual world. This chatbot is designed to guide users through a thrilling and mysterious journey within the Mystic Forest, where they will encounter challenges, solve puzzles, and ultimately escape.

---

## Key Features
- **Dialog Management:**  
  The chatbot employs RASA NLU and Core for effective dialogue management, understanding user intents, and generating appropriate responses.
  
- **Story Flow:**  
  Users will follow a captivating storyline within the Mystic Forest, facing challenges and making decisions that influence the outcome of their escape.

- **User Guidance:**  
  The chatbot provides hints, clues, and guidance to help users progress through the escape room adventure.

---

## Setup Instructions

### 1. Install UV (Astral) Package Manager
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create virtual environment
```bash
uv venv --python 3.10
source .venv/bin/activate   # Mac/Linux

.venv\Scripts\activate    # Windows
```
### 3. Install Rasa Pro in the activated environement
```bash
uv pip install rasa-pro
```
### 4. Setup liscence key and check the version
```bash
export RASA_PRO_LICENSE=YOUR_LICENSE_KEY
rasa --version
```
### 5. Run train command to create model in the /models directory and start playing
```bash
rasa train
rasa shell
```

