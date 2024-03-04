#tkinter
#SQLite

import tkinter

slownik=\
    {
    "chicken":"kurczak",
        "dog":"pies",
    }

def Tlumacz():
    #pobiera slowo z lebela ktory jest w gornej czesci programu
    slowo_angielskie=entry.get()
    #przypisuje do zmiennej tlumaczenie wartosc sprawdzona z wartosciami ze slownika zapisana aktualenie w etykiecie
    tlumaczenie=slownik.get(slowo_angielskie)
    #jesli slowo znajduje sie w slowniku zwrace tlumaczenie
    if tlumaczenie:
        slowo.config(text=tlumaczenie)
    else:
        slowo.config(text="Brak slowa "+slowo_angielskie.upper()+" w slowniku")

def dodajznane():
   wartosc=entry.get()
   ZnaneSlowa.append(wartosc)
   print("dodano do listy")
   for element in ZnaneSlowa:
       print(element)
ZnaneSlowa=[]
root=tkinter.Tk()
root.geometry("400x400")
slowo=tkinter.Label(root, text="")
slowo.pack()

entry=tkinter.Entry(root)
entry.pack()
znane=tkinter.Button(root,text="Znane",background="green",foreground="white",command=dodajznane)
znane.place(x=280,y=200)
#znane.pack()
nieznane=tkinter.Button(root,text="Nie znane",bg="red",fg="white")
nieznane.place(x=70,y=200)
#nieznane.pack()
tlumacz=tkinter.Button(root,text="tlumacz",command=Tlumacz)
tlumacz.place(x=190,y=200)
#tlumacz.pack()


root.mainloop()