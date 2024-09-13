# Larry-Llama
A personalised chatbot based on Meta Llama3.1, using RAG to get personal data.

## Instructions

### Ollama
* Download Ollama: https://ollama.com/download

* Start Ollama via the desktop app or:
```sh
ollama serve
```
You can check if Ollama is running on: http://localhost:11434

* Pull the model from Ollama
```sh
ollama pull llama3.1
```

You can stop Ollama from running in the task manager (Windows) or using the icon in the menu bar (MacOS), or:

Windows:
```sh
Get-Process | Where-Object {$_.ProcessName -like '*ollama*'} | Stop-Process
```

If you started it using ollama serve it will stop running once you close the window

### Installation
* Clone and enter the repository

* Create a virtual environment in python
```sh
python -m venv venv
```

* Activate the virtual environment
  * Windows
```sh
venv\Scripts\activate.bat
```
  * MacOS
```sh
source venv\bin\activate
```

* Download the required packages
```sh
pip install -r requirements.txt
```
