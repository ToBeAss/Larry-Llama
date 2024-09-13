# Larry-Llama
A personalised chatbot based on Meta Llama3.1, using RAG to get personal data.

## Instructions

### Ollama
* Download Ollama: https://ollama.com/download

* Open a new terminal window and start Ollama
```sh
ollama serve
```
You can check if Ollama is running on: http://localhost:11434

* Open a new terminal window and pull the model from Ollama
```sh
ollama pull llama3.1
```

### Installation
* Clone and enter the repository

* Create a virtual environment in python
```sh
python -m venv venv
```

* Activate the virtual environment

Windows
```sh
venv\Scripts\activate.bat
```
MacOS
```sh
source venv/bin/activate
```

* Download the required packages
```sh
pip install -r requirements.txt
```
