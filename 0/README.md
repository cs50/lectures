# CS50x Lecture 0

This directory contains source code from CS50's Lecture 0, which introduces the fundamental concepts of computer science and computational thinking using Scratch, a visual, block-based language
To give you taste of what is to come, we could program our own chatbot called chat.py


## Overview

Lecture 0 serves as an introduction to CS50, covering the fundamentals of working with AI and LLMs through practical examples. Students learn how to interact with language models programmatically and understand key concepts like prompts, system instructions, and API usage.

## Contents

### `/src0` Directory

The `src0` directory contains a progressive series of Python chatbot examples that build upon each other:

#### **chat0.py**
- **Concept**: Hardcoded Prompts
- Basic chatbot that sends a fixed prompt ("In one sentence, what is CS50?") to the OpenAI API
- Demonstrates the simplest form of LLM interaction
- Uses the GPT-5 model

#### **chat1.py**
- **Concept**: User Input
- Extends chat0 by allowing the user to enter their own prompt
- Takes user input and sends it to the API
- Shows how to make the chatbot interactive

#### **chat2.py**
- **Concept**: System Prompts
- Introduces the concept of system prompts (also called instructions)
- Demonstrates how to constrain model behavior ("Limit your answer to one sentence")
- Shows the difference between user prompts and system instructions

#### **chat3.py**
- **Concept**: Advanced System Prompts
- Further demonstrates system prompts with more complex constraints
- Example: "Limit your answer to one sentence. Pretend you're a cat."
- Shows how system prompts can control tone, style, and behavior

## Learning Objectives

By studying this progression, students understand:
1. ✅ How to make API calls to language models
2. ✅ The importance of well-crafted prompts
3. ✅ The role of system prompts in guiding AI behavior
4. ✅ How to create interactive AI applications
5. ✅ Best practices for prompt engineering

## Prerequisites

- Python 3.x
- OpenAI API key
- `openai` Python library

## Setup

```bash
pip install openai
export OPENAI_API_KEY="your-api-key-here"
