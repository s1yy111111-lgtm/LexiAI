from dictionary import load_dictionary, search_word
from ai import ask_ai


# =========================
# 1. 加载词典
# =========================

dictionary = load_dictionary()

print("LexiAI 词典加载完成！")


# =========================
# 2. 主查询循环
# =========================

while True:

    word = input(
        "\n请输入单词（输入 exit 退出）："
    ).strip().lower()


    # 退出
    if word == "exit":
        print("程序结束")
        break


    # =========================
    # 3. 查询单词
    # =========================

    data = search_word(
        dictionary,
        word
    )


    # 没找到
    if data is None:

        print("\n没有找到这个单词。")

        continue


    # =========================
    # 4. 显示基础信息
    # =========================

    print("\n单词：", data["word"])
    print("音标：", data["phonetic"])
    print("释义：", data["translation"])
    print("词性：", data["pos"])
    print("范围：", data["tag"])


    # =========================
    # 5. AI选择
    # =========================

    choice = input(
        "\n输入1查看基础释义，输入2查看AI深度解释："
    )


    if choice == "2":

        print("\nAI正在解释...")


        answer = ask_ai(
            word,
            data
        )


        print("\n===== AI解释 =====")
        print(answer)