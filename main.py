import sqlite3
import tkinter as tk
import tkinter.ttk
from tkinter import ttk

current_word_index = 0
words = []

unknown_words = []


def add_unknown_words():
    global unknown_words, words, current_word_index
    if current_word_index > 0:  # Sprawdzam, czy istnieje słowo do dodania
        unknown_word = words[current_word_index - 1]  # Pobieram ostatnio wyświetlone słowo
        if unknown_word not in unknown_words:  # Dodaję słowo, jeśli jeszcze nie zostało dodane
            unknown_words.append(unknown_word)
            print(f"Dodano do nieznanych: {unknown_word}")


def show_unknown_words():
    for word in unknown_words:  # Iteracja przez listę nieznanych słów
        unknown_words_tree.insert("", "end", values=(word[1], word[2]))  # Dodawanie do Treeview


def bring_words():
    global words
    if not words:
        # Laczenie z baza danych i pobieranie rekordow
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        c.execute('SELECT *FROM words')
        words = c.fetchall()
        conn.close()
    return words


def load_data():
    global current_word_index, words
    words = bring_words()
    if current_word_index < len(words):
        # Czyszczenie tabeli
        for i in tree.get_children():
            tree.delete(i)
        # Pobieranie i dodawanie danych do tebeli
        tree.insert('', 'end', values=(words[current_word_index][1], words[current_word_index][2]))
        current_word_index += 1
    else:
        print("Osiagnieto koniec listy slow")


conn = sqlite3.connect('words.db')
c = conn.cursor()

"""""
# Tworzenie tabeli
c.execute(''' CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    english_word TEXT NOT NULL UNIQUE,
    translated_word TEXT NOT NULL
)
''')
"""""
conn.commit()
"""""
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
"""""
"""""
# Wyswietlanie danych z bazy
c.execute('SELECT *FROM words')
rows = c.fetchall()
for row in rows:
    print(row)
"""

# Tworzenie okna glownego
root = tk.Tk()
root.geometry("600x400")
root.title('Aplikacja do Nauki')
# Treeview dla znanych slow
tree = tkinter.ttk.Treeview(root, columns=('English', 'Translated'), show='headings')
tree.heading('English', text='Angielskie slowa')
tree.column('English', anchor='center')
tree.heading('Translated', text='Tlumaczenie')
tree.column('Translated', anchor='center')
tree.pack(expand=True, fill='both')
# Treview dla nieznanych slow
unknown_words_tree = ttk.Treeview(root, columns=('English', 'Translated'), show='headings')
unknown_words_tree.heading('English', text='Angielskie słowa')
unknown_words_tree.column('English', anchor='center')
unknown_words_tree.heading('Translated', text='Tłumaczenie')
unknown_words_tree.column('Translated', anchor='center')
unknown_words_tree.pack(expand=True, fill='both', pady=20)

add_unknown_button = tk.Button(root, text='Nieznane słowo', command=add_unknown_words)
add_unknown_button.pack(pady=10)

show_unknown_button = tk.Button(root, text='Wyświetl nieznane słowa', command=show_unknown_words)
show_unknown_button.pack(pady=10)

load_button = tk.Button(root, text='Ładuj słowa', command=load_data)
load_button.pack(pady=10)

root.mainloop()
