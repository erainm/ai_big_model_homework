# Created by erainm on 2025/7/22 21:19.
# @Author erainm
# @Project: study_python
# @Description: TODO: 使用Streamlit创建聊天页面

import streamlit as st
from ollama_utils import ask_ollama
"""
    1. 解决用户提问了才回答，不会出现None
    2. 解决保存历史记录
    3. 解决可联系上下文
"""

st.title("Ollama AI聊天机器人")
st.divider ()
if "message" not in st.session_state:
    st.session_state["message"] = []
    st.session_state["message"].append({"role":"assistant","content":"欢迎来到Ollama AI聊天机器人."})
# AI 先说话
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])
# 用户说话
prompt = st.chat_input("请输入你的问题")
# 用户提问了才回答
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role":"user","content":prompt})
    # AI回答
    result = ask_ollama(st.session_state["message"][-10:]) # 此处把最新的10条消息发送给大模型
    st.chat_message("assistant").write(result)
    st.session_state["message"].append({"role":"assistant","content":result})