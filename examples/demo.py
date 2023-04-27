#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : demo
# @Time         : 2021/9/4 下午3:26
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :


from meutils.pipe import *

from chatllm.utils import llm_load
from chatllm._his._chatllm import ChatLLM
from chatllm._his.FaissANN import FaissANN
from chatllm._his._qa import QA

model, tokenizer = llm_load("/Users/betterme/PycharmProjects/AI/CHAT_MODEL/chatglm")
glm = ChatLLM()
glm.chat_func = partial(model.chat, tokenizer=tokenizer)
# glm.chat_func = partial(model.stream_chat, tokenizer=tokenizer)

texts = []
metadatas = []
for p in Path('//examples/Chinese-LangChain/docs').glob('*.txt') | xlist:
    texts.append(p.read_text())
    metadatas.append({'source': p})

faissann = FaissANN()
faissann.add_texts(texts, metadatas)

qa = QA(glm, faiss_ann=faissann.faiss_ann)

qa.get_knowledge_based_answer('周杰伦在干吗')
qa.get_knowledge_based_answer('姚明住哪里')
