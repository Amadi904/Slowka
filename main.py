import  sqlite3
import tkinter

conn=sqlite3.connect('words.db')
c=conn.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    english_word TEXT NOT NULL,
    translated_word TEXT NOT NULL
)
''')
conn.commit()
words_to_add=[('apple','jablko'),('pear','gruszka')]
c.executemany('INSERT INTO words (english_word, translated_word) VALUES (?, ?)', words_to_add)

conn.commit()
c.execute('SELECT *FROM words')
rows=c.fetchall()
for row in rows:
    print(row)
conn.close()



root = tkinter.Tk()
root.geometry("400x400")
root.title('Aplikacja do Nauki')



root.mainloop()
