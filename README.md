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
This will download the llama3.1:latest:8b model (4.7GB)

### Installation
* Clone and enter the repository
```sh
git clone https://github.com/ToBeAss/Larry-Llama.git
cd Larry-Llama
```

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

* Run the program
```sh
python main.py
```

## Resources
https://github.com/liahra/kvRAG/blob/main/query_data.py  
https://ollama.com/blog/embedding-models  
https://python.langchain.com/docs/integrations/vectorstores/chroma/  
https://python.langchain.com/docs/tutorials/rag/  
