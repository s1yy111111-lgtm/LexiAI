import sqlite3

def query_word(word):

    conn = sqlite3.connect("lexicon.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM words
        WHERE word = ?
        """,
        (word,)
    )


    result = cursor.fetchone()

    conn.close()


    if result:

        return {
            "word": result[0],
            "phonetic": result[1],
            "translation": result[2],
            "definition": result[3],
            "pos": result[4]
        }

    else:

        return None

