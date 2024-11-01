from src.chat import ask

def test_connectionToLLM():
    result = ask("Hei, er det noen der?")
    assert result