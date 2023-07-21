import argparse
import json
import sys
import re

def parser_data():

    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-c", "--confirm",type = int, help="是否指定文件", required=True)
    parser.add_argument("-w", "--which", type = int, default = 0, help="指定的文件序号")
    
    args = parser.parse_args()
    return args



def read_articles(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data



def get_inputs(hints, lang):
    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        input_str = input()
        if input_str == '':
            input_str = ' '
            print("你没有输入任何字符！")
        keys.append(input_str)

    return keys


def replace(article, keys):
    for i in range(len(keys)):
        pattern = "\{\{" + str(i+1) + "\}\}"
        repl = keys[i]
        article = re.sub(pattern,repl,article)
    return article


if __name__ == "__main__":
    args = parser_data()
    # 根据参数或随机从 articles 中选择一篇文章并获取相关信息
    if args.confirm and args.which :
        num = args.which - 1
    elif (not args.confirm):
        num = 0
    else:
        print("参数错误噢，再来一遍吧！\n")
        sys.exit(1)
    data = read_articles(args.file)
    articles = data["articles"]
    lang = data["language"]
    actual_hints = articles[num]["hints"]
    actual_artiale = articles[num]["article"]

    # 给出合适的输出，提示用户输入
    print(articles[num]["title"],":\n") 
    keys = get_inputs(actual_hints, lang)
    
    # 获取用户输入并进行替换
    article = replace(actual_artiale,keys)
    
    # 给出结果
    print("以下是你产生的文章:\n",article)

    
    



