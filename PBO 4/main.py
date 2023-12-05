import tkinter as tk
from tkinter import END, Frame, Entry, Label, Button, W
from Fungsi import hitung_luas_Bola,hitung_Volume, hitung_luas_Permukaan, hitung_luas_Selimut,hitung_Volumep,hitung_volume,hitung_luas,hitung_volume_segitiga

#bola

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Volume Bola")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label jari Jari

Qr = Label (frame, text="Jari Jari: ")
Qr.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Jari Jari

textjarijari = Entry (frame)
textjarijari.grid(row=0, column=1)

# Button

def hitung():
    hasil_luas = hitung_luas_Bola(textjarijari.get())
    hasil_volume = hitung_Volume(textjarijari.get())
    txtLuasBola.delete(0,END)
    txtLuasBola.insert(END,hasil_luas)
    txtVolume.delete(0,END)
    txtVolume.insert(END,hasil_volume)
  
hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Bola

luasBola = Label (frame, text="Luas Selimut:") 
luasBola.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Bola

txtLuasBola = Entry(frame)
txtLuasBola.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output label Volume

Volume = Label (frame, text="Volume: ") 
Volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtVolume = Entry (frame)
txtVolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)


app.mainloop()







#kerucut




app = tk. Tk()
app.title("Kalkulator Luas dan Volume Kerucut")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label jari Jari

jarijari = Label (frame, text="Jari Jari: ")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Jari Jari

teksjarijari = Entry (frame)
teksjarijari.grid(row=0, column=1)

# Label Tinggi

tinggi= Label (frame, text="Tinggi: ")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi

tekstinggi = Entry (frame)
tekstinggi.grid(row=1, column=1)

# Label Pelukis

garispelukis = Label (frame, text="Garis Pelukis: ")
garispelukis.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox Pelukis

teksgarispelukis = Entry (frame)
teksgarispelukis.grid(row=2, column=1)

# Button
def hitung():
    hasil_Luas_selimut = hitung_luas_Selimut(teksjarijari.get(),teksgarispelukis.get())
    hasil_Luas_permukaan = hitung_luas_Permukaan(teksjarijari.get(),teksgarispelukis.get())
    hasil_Volume = hitung_Volumep(teksjarijari.get(),tekstinggi.get())
    txtLuasSelimut.delete(0, END)
    txtLuasSelimut.insert(END, hasil_Luas_selimut) 
    txtLuasPermukaan.delete(0, END)
    txtLuasPermukaan.insert(END, hasil_Luas_permukaan) 
    txtVolume.delete(0, END)
    txtVolume.insert(END,hasil_Volume)

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut

luasSelimut = Label (frame, text="Luas Selimut:") 
luasSelimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut

txtLuasSelimut = Entry(frame)
txtLuasSelimut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output label Luas Permukaan

LuasPermukaan = Label (frame, text="Luas Permukaan: ") 
LuasPermukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtLuasPermukaan = Entry (frame)
txtLuasPermukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output label Volume

Volume = Label (frame, text="Volume: ") 
Volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtVolume = Entry (frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)


app.mainloop()





#limassegitiga



app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan volume Limas Segi 4")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label Ls1

QLs1 = Label (frame, text="Luas Sisi 1: ")
QLs1.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls1

LuasSisi1 = Entry (frame)
LuasSisi1.grid(row=0, column=1)

# Label Ls2

QLs2 = Label (frame, text="Luas Sisi 2: ")
QLs2.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls2

LuasSisi2 = Entry (frame)
LuasSisi2.grid(row=1, column=1)

# Label Ls3

QLs3 = Label (frame, text="Luas Sisi 3: ")
QLs3.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox lebar

LuasSisi3 = Entry (frame)
LuasSisi3.grid(row=2, column=1)

# Label Ls4

QLs4 = Label (frame, text="Luas Sisi 4: ")
QLs4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Ls4

LuasSisi4 = Entry (frame)
LuasSisi4.grid(row=3, column=1)


# Label La

QLa = Label (frame, text="Luas Alas: ")
QLa.grid(row=5, column=0, sticky=W, padx=5, pady=5)


# Textbox La

LuasAlas = Entry (frame)
LuasAlas.grid(row=5, column=1)

# Label Tinggi

QTinggi = Label (frame, text="Tinggi: ")
QTinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi

Tinggi = Entry (frame)
Tinggi.grid(row=6, column=1)


# Button

def hitung():
    hasil_luas = hitung_luas(LuasSisi1.get(),LuasSisi2.get(),LuasSisi3.get(),LuasSisi4.get())
    hasil_volume = hitung_volume(LuasAlas.get(),Tinggi.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)


hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas:") 
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Output label volume

volume = Label (frame, text="volume: ") 
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Output Textbox volume

txtvolume = Entry (frame)
txtvolume.grid(row=9, column=1, sticky=W, padx=5, pady=5)


app.mainloop()




#LIMAS SEGIEMPAT

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan volume Limas Segi 4")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label Ls1

QLs1 = Label (frame, text="Luas Sisi 1: ")
QLs1.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls1

LuasSisi1 = Entry (frame)
LuasSisi1.grid(row=0, column=1)

# Label Ls2

QLs2 = Label (frame, text="Luas Sisi 2: ")
QLs2.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls2

LuasSisi2 = Entry (frame)
LuasSisi2.grid(row=1, column=1)

# Label Ls3

QLs3 = Label (frame, text="Luas Sisi 3: ")
QLs3.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox lebar

LuasSisi3 = Entry (frame)
LuasSisi3.grid(row=2, column=1)

# Label Ls4

QLs4 = Label (frame, text="Luas Sisi 4: ")
QLs4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Ls4

LuasSisi4 = Entry (frame)
LuasSisi4.grid(row=3, column=1)

# Label Ls5

QLs5 = Label (frame, text="Luas Sisi 5: ")
QLs5.grid(row=4, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls5

LuasSisi5 = Entry (frame)
LuasSisi5.grid(row=4, column=1)

# Label La

QLa = Label (frame, text="Luas Alas: ")
QLa.grid(row=5, column=0, sticky=W, padx=5, pady=5)


# Textbox La

LuasAlas = Entry (frame)
LuasAlas.grid(row=5, column=1)

# Label Tinggi

QTinggi = Label (frame, text="Tinggi: ")
QTinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi

Tinggi = Entry (frame)
Tinggi.grid(row=6, column=1)


# Button
def hitung():
    hasil_luas = hitung_luas (LuasSisi1.get(),LuasSisi2.get(),LuasSisi3.get(),LuasSisi4.get(),LuasSisi5.get()) 
    hasil_volume = hitung_volume (LuasAlas.get(),Tinggi.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas:") 
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Output label volume

volume = Label (frame, text="volume: ") 
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Output Textbox volume

txtvolume = Entry (frame)
txtvolume.grid(row=9, column=1, sticky=W, padx=5, pady=5)


app.mainloop()




#balok

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan volume balok")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label panjang

okehpanjang = Label (frame, text="panjang: ")
okehpanjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox panjang

panjang = Entry (frame)
panjang.grid(row=0, column=1)

# Label tinggi

okehtinggi = Label (frame, text="tinggi: ")
okehtinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox tinggi

tinggi = Entry (frame)
tinggi.grid(row=1, column=1)

# Label lebar

okehlebar = Label (frame, text="lebar: ")
okehlebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox lebar

lebar = Entry (frame)
lebar.grid(row=2, column=1)


# Button

def hitung():
    hasil_luas = hitung_luas(panjang.get(),lebar.get(),tinggi.get())
    hasil_volume = hitung_volume(panjang.get(),lebar.get(),tinggi.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas: ") 
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output label volume

volume = Label (frame, text="volume: ") 
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox volume

txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)


app.mainloop()








#selinder

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Volume Selinder")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label jari Jari

Qr = Label (frame, text="Jari Jari: ")
Qr.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Jari Jari

JariJari = Entry (frame)
JariJari.grid(row=0, column=1)

# Label Tinggi

QT = Label (frame, text="Tinggi: ")
QT.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi

Tinggi = Entry (frame)
Tinggi.grid(row=1, column=1)


# Button

def hitung():
    hasil_Luas_selimut = hitung_luas_Selimut(JariJari.get(),Tinggi.get())
    hasil_Luas_permukaan = hitung_luas_Permukaan(JariJari.get(),Tinggi.get())
    hasil_Volume = hitung_Volume(JariJari.get(),Tinggi.get())
    txtLuasSelimut.delete(0, END)
    txtLuasSelimut.insert(END, hasil_Luas_selimut) 
    txtLuasPermukaan.delete(0, END)
    txtLuasPermukaan.insert(END, hasil_Luas_permukaan) 
    txtVolume.delete(0, END)
    txtVolume.insert(END,hasil_Volume)


hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut

luasSelimut = Label (frame, text="Luas Selimut:") 
luasSelimut.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut

txtLuasSelimut = Entry(frame)
txtLuasSelimut.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output label Luas Permukaan

LuasPermukaan = Label (frame, text="Luas Permukaan: ") 
LuasPermukaan.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtLuasPermukaan = Entry (frame)
txtLuasPermukaan.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output label Volume

Volume = Label (frame, text="Volume: ") 
Volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtVolume = Entry (frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)


app.mainloop()


#kubus


app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan volume kubus")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label Rusuk

rusuk = Label (frame, text="rusuk: ")
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Rusuk

txtrusuk = Entry (frame)
txtrusuk.grid(row=0, column=1)


# Button

def hitung():
    hasil_luas = hitung_luas(txtrusuk.get())
    hasil_volume = hitung_volume(txtrusuk.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas: ") 
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output label volume

volume = Label (frame, text="volume: ") 
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox volume

txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)


app.mainloop()





#prisma segitiga



app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Sisi 1
sisi1 = Label(frame, text="Sisi 1:")
sisi1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 1
txtsisi1 = Entry(frame)
txtsisi1.grid(row=0, column=1)

# Label Sisi 2
sisi2 = Label(frame, text="Sisi 2:")
sisi2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 2
txtsisi2 = Entry(frame)
txtsisi2.grid(row=1, column=1)

# Label Sisi 3
sisi3 = Label(frame, text="Sisi 3:")
sisi3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 3
txtsisi3 = Entry(frame)
txtsisi3.grid(row=2, column=1)

# Label Tinggi Prisma
tinggi_prisma = Label(frame, text="Tinggi Prisma:")
tinggi_prisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi Prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=3, column=1)

# Label Alas
alas = Label(frame, text="Alas:")
alas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Alas
txtalas = Entry(frame)
txtalas.grid(row=4, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=5, column=1)

# Button

def hitung():
    hasil_volume_segitiga = hitung_volume_segitiga(txtsisi1.get(),txtsisi2.get(),txtsisi3.get(),txttinggi_prisma.get(),txtalas.get(),txttinggi.get())
    hasil_Luas_selimut = hitung_luas_Selimut(txttinggi_prisma.get(),txtvolume_segitiga.get())
    hasil_Luas_permukaan = hitung_luas_Permukaan(txtvolume_segitiga.get(),txttinggi_prisma.get(),txtalas.get(),txttinggi.get())
    hasil_Volume = hitung_volume(txttinggi_prisma.get(),txtalas.get(),txttinggi.get())
    txtvolume_segitiga.delete(0, END)
    txtvolume_segitiga.insert(END,hasil_volume_segitiga) 
    txtluas_selimut.delete(0, END)
    txtluas_selimut.insert(END, hasil_Luas_selimut) 
    txtluas_permukaan.delete(0, END)
    txtluas_permukaan.insert(END, hasil_Luas_permukaan) 
    txtVolume.delete(0, END)
    txtvolume.insert(END,hasil_Volume)


hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)


# Output volume Segitiga
volume_segitiga = Label(frame, text="volume Segitiga:")
volume_segitiga.grid(row=7, column=0, sticky=W, padx=5, pady=5)
# Textbox volume Segitiga
txtvolume_segitiga = Entry(frame)
txtvolume_segitiga.grid(row=7, column=1)

# Output Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut:")
luas_selimut.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Selimut
txtluas_selimut = Entry(frame)
txtluas_selimut.grid(row=8, column=1)

# Output Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan:")
luas_permukaan.grid(row=9, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Permukaan
txtluas_permukaan = Entry(frame)
txtluas_permukaan.grid(row=9, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)
# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=10, column=1)

app.mainloop()