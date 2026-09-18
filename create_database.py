import sqlite3
import csv


conn = sqlite3.connect("lexicon.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
    word TEXT,
    phonetic TEXT,
    translation TEXT,
    definition TEXT,
    pos TEXT
)
""")


with open("ecdict.csv", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        cursor.execute(
            """
            INSERT INTO words
            (word, phonetic, translation, definition, pos)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                row["word"],
                row["phonetic"],
                row["translation"],
                row["definition"],
                row["pos"]
            )
        )


conn.commit()