import json


with open("words.json", "r", encoding="utf-8") as f:
    words = json.load(f)


while True:

    word = input("请输入单词（输入exit退出）：")


    if word == "exit":
        print("程序结束")
        break


    if word in words:
        print("单词：", word)
        print("意思：", words[word]["意思"])
        print("词性：", words[word]["词性"])
        print("等级：", words[word]["等级"])

    else:
        print("没有找到这个单词")