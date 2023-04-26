#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : chatpdf_demo
# @Time         : 2023/4/26 12:22
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from chatllm.applications.chatpdf import ChatPDF

qa = ChatPDF(encode_model='nghuyong/ernie-3.0-nano-zh')
qa.load_llm4chat(model_name_or_path="/Users/betterme/PycharmProjects/AI/CHAT_MODEL/chatglm")
qa.create_ann_index('财报.pdf')
# 召回
qa.ann_find('东北证券主营业务')

for i, _ in qa(query='东北证券主营业务'):
    pass

