import csv
import difflib
import os

from dotenv import load_dotenv
from openai import OpenAI


# =========================
# 1. 读取 API Key
# =========================

load_dotenv()

api_key = os.getenv("AGNES_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://apihub.agnes-ai.com/v1"
)


# =========================
# 2. 加载 ECDICT 词典
# =========================

dictionary = {}

with open("ecdict.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        dictionary[row["word"]] = row


print("LexiAI 词典加载完成！")


# =========================
# 3. 主查询循环
# =========================

while True:

    word = input("\n请输入单词（输入 exit 退出）：").strip().lower()

    # 退出程序
    if word == "exit":
        print("程序结束")
        break


    # =========================
    # 4. 精确查询
    # =========================

    if word in dictionary:

        data = dictionary[word]


        # =========================
        # 诊断代码
        # 查看这个单词在 ECDICT 中的全部原始数据
        # =========================

        print("\n===== 诊断：完整词典数据 =====")
        print(data)
        print("=============================")


        # =========================
        # 5. 显示基础词典信息
        # =========================
        print("\n单词：", data["word"])
        print("音标：", data["phonetic"])
        print("释义：", data["translation"])
        print("词性：", data["pos"])
        print("范围：", data["tag"])
        print("常用度：", data["collins"])
        print("是否是牛津3000词：", data["oxford"])
        print("BNC排名：", data["bnc"])
        print("FRQ排名：", data["frq"])



        # =========================
        # 6. 选择是否使用 AI
        # =========================

        choice = input(
            "\n输入 1 查看基础释义，输入 2 查看 AI 深度解释："
        )


        # =========================
        # 7. AI 深度解释
        # =========================

        if choice == "2":

            print("\nAI 正在解释...")

            response = client.chat.completions.create(
                model="agnes-2.5-flash",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
你是 LexiAI 英语学习助手。

用户查询的单词：
{word}

本地词典提供的信息：

音标：
{data["phonetic"]}

中文释义：
{data["translation"]}

英文释义：
{data["definition"]}

词性：
{data["pos"]}

标签：
{data["tag"]}

请结合上面的词典数据进行解释。

要求：

1. 用中文解释这个单词最核心的意思
2. 说明这个单词常见的使用场景
3. 给出一个自然、简单的英文例句
4. 给出例句的中文翻译
5. 给出 2 到 3 个常见近义词
6. 简单说明这些近义词和这个单词的区别
7. 不要编造词典数据中不存在的信息
"""
                    }
                ]
            )

            print("\n===== AI 解释 =====")
            print(response.choices[0].message.content)


    # =========================
    # 8. 没找到 → 模糊搜索
    # =========================

    else:

        matches = difflib.get_close_matches(
            word,
            dictionary.keys(),
            n=3,
            cutoff=0.6
        )

        if matches:

            print("\n没有找到这个单词。")
            print("你是不是想找：")

            for match in matches:
                print("-", match)

        else:

            print("\n没有找到这个单词。")