# Prompt Security VS Code Extension

## Overview

Prompt Security is a VS Code extension that detects potentially harmful prompts using a fine-tuned DistilBERT model. The extension scans user prompts and warns users about harmful or suspicious content directly inside VS Code.

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
