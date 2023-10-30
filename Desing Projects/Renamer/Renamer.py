import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import locale

# Türkçe ayarlarını kullanarak yerel yapılandırmayı ayarla
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

def submit_form():

    selected_value = combobox.get()
    
    if selected_value == "Select Case":
        messagebox.showwarning("Warning", "Please Select Case!")
    
    else:
        # Dosya seçim iletişim kutusunu aç
        files = tk.filedialog.askopenfilenames(title="Select The Files To Rename")
        
        # Seçilen her dosyanın ismini yazdır
        for file in files:
            locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
            entry1_value = entry1.get()
            entry2_value = entry2.get()
            selected_value = combobox.get()
                       
            
            if checkbox_var.get() == 1:
                locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
                # Dosya adını ve uzantısını ayır
                file_dir, file_name = os.path.split(file)
                file_name, file_ext = os.path.splitext(file_name)                
                
                if selected_value == "UPPERCASE":
                    entry2_value = entry2_value.upper()
                elif selected_value == "lowercase":
                    entry2_value = entry2_value.lower()
                elif selected_value == "Sentence case":
                    entry2_value = entry2_value.capitalize()
                elif selected_value == "Title Case":
                    entry2_value = entry2_value.title()
                    
                # Dosya yolunu ve yeni dosya adını birleştir
                new_file_path = os.path.join(file_dir, entry2_value + file_ext)
                
                # Dosyayı yeniden adlandır
                os.rename(file, new_file_path)
                
            else:
                locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
                file_dir, file_name = os.path.split(file)
                file_name, file_ext = os.path.splitext(file_name)
                
                new_file_name = file_name.lower().replace(entry1_value.lower(), entry2_value.lower())
                
                if selected_value == "UPPERCASE":
                    new_file_name = new_file_name.upper()
                elif selected_value == "lowercase":
                    new_file_name = new_file_name.lower()
                elif selected_value == "Sentence case":
                    new_file_name = new_file_name.capitalize()
                elif selected_value == "Title Case":
                    new_file_name = new_file_name.title()
                
                new_file_path = os.path.join(file_dir,new_file_name+file_ext)
                
                # Dosyayı yeniden adlandır
                os.rename(file, new_file_path)
        root.destroy()
            
    print("Files are renamed.")

def checkbox_case():
    if checkbox_var.get() == 1:
        print("Checkbox is checked!")
        entry1.config(state=tk.DISABLED)
    else:
        print("Checkbox is unchecked!")
        entry1.config(state=tk.NORMAL)

def handle_selection(event):
    pass
  
def clear_form():
    # Giriş alanlarını temizle
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    combobox.set("Select Case")
    
# Ana pencereyi oluştur
root = tk.Tk()
root.title("Renamer")
root.update_idletasks()
width = root.winfo_width()+310
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# İlk etiket
label1 = tk.Label(root, text="Original:", width=30)
label1.grid(row=0, column=0, padx=10, pady=10)

# İlk giriş alanı
entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=10, pady=10)

# İkinci etiket
label2 = tk.Label(root, text="Changing:", width=30)
label2.grid(row=1, column=0, padx=10, pady=10)

# İkinci giriş alanı
entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=10, pady=10)

# İşlemleri gerçekleştiren düğmeyi oluştur
submit_button = tk.Button(root, text="Start", command=submit_form, height=2, width=30)
submit_button.grid(row=3, column=0, padx=10, pady=10)

#Giriş alanlarını temizleyen düğmeyi oluştur
clear_button = tk.Button(root, text="Clear", command=clear_form, height=2, width=30)
clear_button.grid(row=3, column=1, padx=10, pady=10)

# Create a variable to store the checkbox value
checkbox_var = tk.IntVar()

# Create the checkbox widget
checkbox = tk.Checkbutton(root, text="Rename all of them", variable=checkbox_var, command=checkbox_case, width=30)

# Set the checkbox to the unchecked state by default
checkbox.deselect()

# Place the checkbox in the window
checkbox.grid(row=2, column=0, padx=10, pady=10)

# Create a list of items for the Combobox
items = ["Uppercase", "Lowercase", "Sentence case", "Title case"]

# Create a Combobox widget
combobox = ttk.Combobox(root, values=items, width=30)

# Set an initial selection
combobox.set("Select Case")

# Bind the selection event
combobox.bind("<<ComboboxSelected>>", handle_selection)

# Place the Combobox in the window
combobox.grid(row=2, column=1, padx=10, pady=10)

# Pencereyi başlat
root.mainloop()