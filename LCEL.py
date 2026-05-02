from langchain_ollama import ChatOllama

# LLM model
qwen = ChatOllama(model="qwen2.5:1.5b", temperature = 0.3)
dsr1 = ChatOllama(model="deepseek-r1:14b", temperature = 0.3)

# 모델에 프롬프트를 입력
response = qwen.invoke("탄소의 원자번호는 무엇인가요?")
print(response)