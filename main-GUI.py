import json
import re
import streamlit as st

def read_articles(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data



def get_inputs(hints):
    keys = []
    for hint in hints:
        answer = st.text_input(f"请输入{hint}:",key = hint)
        keys.append(answer)
    return keys


def replace(article, keys):
    for i in range(len(keys)):
        pattern = "\{\{" + str(i+1) + "\}\}"
        repl = f"<span style = \"color:red\">{keys[i]}</span>"
        article = re.sub(pattern,repl,article)
    return article


if __name__ == "__main__":
    # 基础格式
    st.title("猜词游戏")
    file_list = ["example_de.json","example_en.json","example_es.json","example_zh.json"]
    filename = st.radio("请选择题库文件",file_list)
    data = read_articles(filename)
    articles = data["articles"]
    titles = []
    for i in range(len(articles)):
        titles.append(articles[i]["title"])
    
    # 根据参数或随机从 articles 中选择一篇文章并获取相关信息
    confirm = st.radio("请选择是否选择文章",("是","否"))
    if (confirm == "是"):
        if len(titles)==0:
            st.markdown("<div style=\"color:red\">该题库下没有题目噢！</div>",unsafe_allow_html=True)
        else:
            which = st.radio("请选择文章",titles)
            num = titles.index(which)
    else:
        num = 0 
    actual_title = articles[num]["title"] 
    actual_artiale = articles[num]["article"]
    actual_hints = articles[num]["hints"] 

    # 给出合适的输出，提示用户输入
    answers = get_inputs(actual_hints)
    # 获取用户输入并进行替换
    final_article = replace(actual_artiale,answers)
    # 给出结果
    if st.button("练习完成！"):
        output = f"<div style=\"border: 1px solid black; padding: 10px\">{final_article}</div>"
        st.markdown(output,unsafe_allow_html=True)
    # 保存文件
    if st.button("保存文件"):
        with open(f"output\{actual_title}.md",'w',encoding='utf-8') as f:
            f.write(final_article)