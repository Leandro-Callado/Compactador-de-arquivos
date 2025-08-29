import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile, tarfile, os

def compactar_zip(arquivos, saida):
    with zipfile.ZipFile(saida, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))

def compactar_tar(arquivos, saida):
    with tarfile.open(saida, "w") as tar:
        for arquivo in arquivos:
            tar.add(arquivo, arcname=os.path.basename(arquivo))

def compactar_tar_gz(arquivos, saida):
    with tarfile.open(saida, "w:gz") as tar:
        for arquivo in arquivos:
            tar.add(arquivo, arcname=os.path.basename(arquivo))

class compactadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compactador by Leandro & Lucas")

window = tk.Tk()
window.title("Compactador by Leandro & Lucas")
window.geometry("400x300")

label = tk.Label(
    text="Escolha o formato da compactação: ",
    fg="black",
    width=40,
    height=4
)
label.pack(pady=20)

Zip = tk.Button(
    text="Compactar em ZIP",
    width=20,
    height=3,
    bg="white",
    fg="black",
)
tar = tk.Button(
    text="Compactar em TAR",
    width=20,
    height=3,
    bg="white",
    fg="black",
)
targz = tk.Button(
    text="Compactar em TAR.GZ",
    width=20,
    height=3,
    bg="white",
    fg="black",
)
Zip.pack(pady=1)
tar.pack(pady=1)
targz.pack(pady=1)
window.mainloop()