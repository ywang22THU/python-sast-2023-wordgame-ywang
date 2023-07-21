import streamlit as st 
import json 

st.title("大家来出题！")
with open ("rule.txt","r",encoding="utf-8") as rule_:
    rule = rule_.read()
st.write(rule)
lang = st.radio("请选择你的语言,依次为德语、英语、西班牙语、中文",("de","en","es","zh"))
json_file = {}
with open (f"example_{lang}.json",'r',encoding="utf-8") as f:
    json_file = json.load(f)

new_title = ''
new_article = ''
new_hints = []

if lang == "de":
    new_title = st.text_input("Title:")
    new_article = st.text_input("Artikel:")
    new_hints_str = st.text_input("Hinweise:")
    new_hints = new_hints_str.split()

if lang == "en":
    new_title = st.text_input("Title:")
    new_article = st.text_input("Article:")
    new_hints_str = st.text_input("Hints:")
    new_hints = new_hints_str.split()
    
if lang == "es":
    new_title = st.text_input("Título:")
    new_article = st.text_input("Artículo:")
    new_hints_str = st.text_input("Pistas:")
    new_hints = new_hints_str.split()
    
if lang == "zh":
    new_title = st.text_input("标题：")
    new_article = st.text_input("文章内容：")
    new_hints_str = st.text_input("提示语：")
    new_hints = new_hints_str.split()

new_example = {
    "title": new_title,
    "article": new_article,
    "hints": new_hints 
}

if st.button("出题，完成！"):
    json_file["articles"].append(new_example)
    with open(f"example_{lang}.json","w",encoding="utf-8") as file:
        json.dump(json_file,file)