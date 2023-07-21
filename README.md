# sast2023 word game

## 环境配置

第三方库 streamlit

## 使用设置

运行CLI界面游戏：python main-CLI.py
运行GUI界面游戏：streamlit run main_GUI.py
进行出题：streamlit run new_example.py

CLI中约定以下参数：

--file  -f  接文章的路径
--confirm -c 接int值，0表示不指定文章，!0表示指定文章
--which -w 接int值，表示指定文章的序号（从1开始）

文章使用 JSON 存储，的格式如下：

{
    language:"",//语言
    articles:[
        {
            "title":"xxx",//标题
            "article":"xxx",//文章内容
            "hints":[
                "xxx","yyy",...
            ]//提示
        }
        {...}
        ...
    ]//文集
}

## 游戏功能

基础功能：可以进行填词游戏，题库包括中英德西四种语言

拓展功能：实现了CLI与GUI双版本，GUI界面中增加了将所得到的文章保存为Markdown格式的功能；支持进行出题操作（在GUI界面中进行）
