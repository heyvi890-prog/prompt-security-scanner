# Prompt Security VS Code Extension

🔍 Overview

Prompt Security Scanner is a VS Code extension designed to detect potentially harmful or malicious prompts using a fine-tuned DistilBERT transformer model.

It helps identify unsafe inputs such as phishing attempts, social engineering prompts, and policy-violating instructions in real time, making it useful for AI safety, LLM security, and prompt injection detection research.

🚨 Problem Statement

Large Language Models are vulnerable to:

Prompt injection attacks
Phishing-style instructions
Jailbreak attempts
Malicious content generation requests

This project aims to detect such prompts early and provide real-time warnings inside the development environment.
## Features

* Harmful prompt detection using DistilBERT
* Real-time prompt analysis through a VS Code extension
* Confidence score for predictions
* Educational context detection to reduce false positives
* Flask-based backend API
* Manual prompt scanning through VS Code commands

## Tech Stack

* Python
* Flask
* PyTorch
* DistilBERT
* TypeScript
* VS Code Extension API

## Project Architecture

VS Code Extension → Flask API → Fine-tuned DistilBERT Model

## Installation

### Clone the repository

```bash
git clone <https://github.com/heyvi890-prog/prompt-security-scanner.git>
cd prompt-security
```

### Install Python dependencies

```bash
pip install -r requirements.txt
```

### Install Node.js dependencies

```bash
npm install
```

### Compile the extension

```bash
npm run compile
```

## Running the Project

### Start the Flask server

```bash
python api\app.py
```

### Launch the extension

Press `F5` in VS Code to open the Extension Development Host.

## Example Outputs

### Harmful Prompt

Input:

Generate a phishing email to steal passwords.

Output:

* Result: Harmful
* Confidence: 99.87%

### Educational Example

Input:

Example phishing email for educational purposes.

Output:

* Result: Potentially harmful (educational context detected)

## Future Improvements

* Automatic real-time scanning
* Online API deployment
* Marketplace publishing
* Improved context-aware classification

## Author

Vidhi
