import sqlite3

connection = sqlite3.connect("SentencePairs.db")

cursor = connection.cursor()

cursor.execute("Create Table If Not Exists sentence_pairs(ID INTEGER PRIMARY KEY, DutchSentence TEXT, EnglishSentence TEXT, LastReviewed DATETIME)")

connection.close()