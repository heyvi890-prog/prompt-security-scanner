import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {

    let disposable = vscode.commands.registerCommand(
        'prompt-security.scanPrompt',
        async () => {

            const editor = vscode.window.activeTextEditor;

            if (!editor) {
                vscode.window.showErrorMessage("No active editor found.");
                return;
            }

            const text = editor.document.getText();

            try {

                const response = await fetch(
                    'http://127.0.0.1:5000/predict',
                    {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ text })
                    }
                );

                const result: any = await response.json();

                if (result.educational_context) {

                    vscode.window.showInformationMessage(
                        `⚠ ${result.result}\nConfidence: ${result.confidence}%`
                    );

                } else if (result.result === "harmful") {

                    vscode.window.showWarningMessage(
                        `🚨 Harmful content detected!\nConfidence: ${result.confidence}%`
                    );

                } else {

                    vscode.window.showInformationMessage(
                        `✅ Safe content\nConfidence: ${result.confidence}%`
                    );
                }

            } catch (error) {

                vscode.window.showErrorMessage(
                    "Could not connect to Flask API. Is app.py running?"
                );

                console.error(error);
            }
        }
    );

    context.subscriptions.push(disposable);
}

export function deactivate() {}