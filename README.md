![image](https://img.shields.io/pypi/v/llm4gpt.svg) ![image](https://img.shields.io/travis/yuanjie-ai/llm4gpt.svg) ![image](https://readthedocs.org/projects/llm4gpt/badge/?version=latest)



<h1 align = "center">🔥LLM4GPT 为大模型而生🔥</h1>

---

# Install

```python
pip install -U llm4gpt
```

# [Docs](https://jie-yuan.github.io/llm4gpt/)

# Usages

```python
from meutils.pipe import *

from llm.utils import llm_load
from llm.chatllm import ChatLLM
from llm.kb.FaissANN import FaissANN
from llm.qa import QA

model, tokenizer = llm_load(model_name_or_path="THUDM/chatglm-6b", device='cpu')
glm = ChatLLM()
glm.chat_func = partial(model.chat, tokenizer=tokenizer)

texts = []
metadatas = []
for p in Path('data').glob('*.txt'):
    texts.append(p.read_text())
    metadatas.append({'source': p})

faissann = FaissANN()
faissann.add_texts(texts, metadatas)

qa = QA(glm, faiss_ann=faissann.faiss_ann)

qa.get_knowledge_based_answer('周杰伦在干吗')
qa.get_knowledge_based_answer('姚明住哪里')
```

---

# TODO

-[ ] 增加互联网搜索组件

-[ ] 增加搜索组件

-[ ] 增加本地知识库组件

-[ ] 增加知识图谱组件

-[ ] 增加微调模块



