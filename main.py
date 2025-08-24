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

