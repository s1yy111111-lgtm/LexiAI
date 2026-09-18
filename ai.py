import os


from dotenv import load_dotenv
from openai import OpenAI


# 1. 加载 .env 文件
load_dotenv()

# 2. 获取 API Key
API_KEY = os.getenv("AGNES_API_KEY")

# 3. 创建 AI 客户端
client = OpenAI(
    api_key=API_KEY,
    base_url="https://apihub.agnes-ai.com/v1"
)

# 4. 创建 AI 查询函数
def ask_ai(word, data):

    response = client.chat.completions.create(
        model="agnes-2.5-flash",

        messages=[
            {
                "role": "user",
                "content": f"""
                你是 LexiAI 英语学习助手。

                单词：{word}
                音标：{data["phonetic"]}
                中文释义：{data["translation"]}
                英文释义：{data["definition"]}
                词性：{data["pos"]}
               

                请用简洁中文帮助用户快速理解这个词：

                1. 核心含义：一句话
                2. 常见用法：2个常用搭配
                3. 例句：1个简单自然的英文例句 + 中文翻译
                4. 易混词：如有必要，最多给2个并简要说明区别；没有则省略

                要求：简洁、不重复、不讲生僻内容，不编造词频或考试数据，不要使用 Markdown 符号（例如 **、#、-），使用普通文本和换行排版。
                """
            }
        ]
    )


    answer = response.choices[0].message.content


    return answer