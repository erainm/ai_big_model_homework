# Created by erainm on 2025/7/22 21:19.
# @Author erainm
# @Project: study_python
# @Description: TODO: ollama调用大模型工具类
"""
底层有client，默认使用本地ollama
修改远程ollama，new_ollama = ollama.Client(host="thhp://地址:11434")
"""

import ollama

new_allama = ollama.Client(host="http://127.0.0.1:11434")

def ask_ollama(message):
    response = ollama.chat(
        model="deepseek-r1:7b",
        messages=message
    )
    return response["message"]["content"]

