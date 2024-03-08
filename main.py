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
    english_word TEXT NOT NULL UNIQUE,
    translated_word TEXT NOT NULL
)
''')
conn.commit()

# Dodanie slow do bazy danych
words_to_add = [('apple', 'jablko'), ('pear', 'gruszka')]
for word_pair in words_to_add:
    c.execute('SELECT *FROM words WHERE english_word=?', (word_pair[0],))
    if not c.fetchone():
        try:
            c.executemany('INSERT INTO words (english_word, translated_word) VALUES (?, ?)', words_to_add)
            conn.commit()
        except sqlite3.IntegrityError:
            print("te slowa juz istnieja w bazie ")
        except Exception as e:
            print(f"wystapil blad{e}")

# Wyswietlanie danych z bazy
c.execute('SELECT *FROM words')
rows = c.fetchall()
for row in rows:
    print(row)

# Tworzenie okna glownego
root = tk.Tk()
root.geometry("600x300")
root.title('Aplikacja do Nauki')
tree = tkinter.ttk.Treeview(root, columns=('ID', 'English', 'Translated'), show='headings')
tree.heading('ID', text='ID')
tree.column('ID',anchor='center')
tree.heading('English', text='Angielskie slowa')
tree.column('English',anchor='center')
tree.heading('Translated', text='Tlumaczenie')
tree.column('Translated',anchor='center')
tree.pack(expand=True, fill='both')
load_button = tk.Button(root, text='Laduj slowa', command=zaladuj_dane)
load_button.pack(pady=10)

root.mainloop()
