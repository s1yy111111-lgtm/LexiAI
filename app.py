from flask import Flask, render_template, request

from dictionary import load_dictionary
from ai import ask_ai


# =========================
# 1. 创建网页程序
# =========================

app = Flask(__name__)


# =========================
# 2. 加载词典
# =========================

dictionary = load_dictionary()

print("LexiAI 词典加载完成！")


# =========================
# 3. 网页主页
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    answer = None
    data = None
    word = None


    # 用户点击查询
    if request.method == "POST":


        # 获取网页输入的单词
        word = request.form["word"]


        # 去词典查找


        if not word:
            answer = "请输入要查询的单词"

        elif word in dictionary:
            data = dictionary[word]
            answer = ask_ai(word, data)

        else:
            answer = "没有找到这个单词"


    return render_template( 
                "index.html",
                 word=word,
                 data=data,
                 answer=answer
         
    )


# =========================
# 4. 启动网页
# =========================

if __name__ == "__main__":

    app.run(debug=True)