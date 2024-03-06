import sqlite3
import tkinter as tk
import tkinter.ttk
from tkinter import ttk


def przenies():
    # Laczenie z baza danych i pobieranie rekordow
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    c.execute('SELECT *FROM words')
    rows = c.fetchall()
    conn.close()
    return rows


def zaladuj_dane():
    # Czyszczenie tabeli
    for i in tree.get_children():
        tree.delete(i)
    # Pobieranie i dodawanie danych do tebeli
    for row in przenies():
        tree.insert('', 'end', values=row)


conn = sqlite3.connect('words.db')
c = conn.cursor()

# Tworzenie tabeli
c.execute(''' CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    english_word TEXT NOT NULL,
    translated_word TEXT NOT NULL
)
''')
conn.commit()


#Do poprawy
words_to_add = [('apple', 'jablko'), ('pear', 'gruszka')]
c.executemany('INSERT INTO words (english_word, translated_word) VALUES (?, ?)', words_to_add)

conn.commit()
for word_pair in words_to_add:
    c.execute('SELECT *FROM words WHERE english_word=?', (word_pair[0],))
    existing_word = c.fetchone()
    if existing_word is None:
        c.execute('INSERT INTO words (english_word, translated_word) VALUES (?, ?)', word_pair)

c.execute('SELECT *FROM words')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()





# Tworzenie okna glownego
root = tk.Tk()
root.geometry("400x400")
root.title('Aplikacja do Nauki')
tree = tkinter.ttk.Treeview(root, columns=('ID', 'English', 'Translated'), show='headings')
tree.heading('ID', text='ID')
tree.heading('English', text='Angielskie slowa')
tree.heading('Translated', text='Tlumaczenie')
tree.pack(expand=True, fill='both')
load_button = tk.Button(root, text='Laduj slowa', command=zaladuj_dane)
load_button.pack(pady=10)

root.mainloop()
