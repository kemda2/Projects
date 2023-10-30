import tkinter as tk
from tkinter import ttk
import pandas as pd

def veriyi_treeview_goster(veri, sütun_genişlikleri):
    pencere = tk.Tk()
    pencere.title("Excel Verisi")

    # Calculate the x and y position for the window to be centered
    width = 1900
    height = 900
    x = (pencere.winfo_screenwidth() - width) // 2
    y = (pencere.winfo_screenheight() - height) // 2
    

    # Set the window geometry to center it on the screen
    pencere.geometry(f"{width}x{height}+{x}+{y}")

    # Treeview için bir çerçeve oluştur
    veri_cerceve = ttk.Frame(pencere)
    veri_cerceve.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Treeview oluştur
    treeview = ttk.Treeview(veri_cerceve,height=40)

    # Treeview başlık sütunları
    basliklar = list(veri.columns)
    treeview["columns"] = basliklar
    treeview["show"] = "headings"

    # Başlık sütunları için başlık metinlerini ayarla
    for baslik in basliklar:
        treeview.heading(baslik, text=baslik)

    # Veriyi Treeview'a ekleyin
    for satir in veri.to_numpy().tolist():
        treeview.insert("", "end", values=satir)

    # Sütun genişliklerini ayarla (piksel cinsinden)
    for i, baslik in enumerate(basliklar):
        treeview.column(baslik, width=sütun_genişlikleri[i])

    # Yatay ve dikey kaydırma çubukları ekle
    yatay_scroll = ttk.Scrollbar(veri_cerceve, orient="horizontal", command=treeview.xview)
    # dikey_scroll = ttk.Scrollbar(veri_cerceve, orient="vertical", command=treeview.yview)
    treeview.configure(xscrollcommand=yatay_scroll.set)#, yscrollcommand=dikey_scroll.set)
    yatay_scroll.pack(side="bottom", fill="x")
    # dikey_scroll.pack(side="right", fill="y")

    # Treeview'ı göster
    treeview.pack()

    pencere.mainloop()

# Excel dosyasının yolunu belirtin
dosya_yolu = 'qua.xlsx'

def na_to_empty(val):
    if pd.isna(val):
        return ''
    return val

# Excel dosyasını okuyun
veri = pd.read_excel(dosya_yolu)
veri = veri.applymap(na_to_empty)

# Bütün sütunların genişliklerini elle belirleyin (piksel cinsinden)
sütun_genişlikleri = [80, 120, 70, 80, 80, 80, 80, 80, 80, 80, 0, 80, 80, 80, 80, 80, 80, 80, 80, 80,150,150]  # İstediğiniz genişlikleri bu listede belirleyebilirsiniz

# Veriyi Treeview ile göster
veriyi_treeview_goster(veri, sütun_genişlikleri)

