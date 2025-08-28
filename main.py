import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile, tarfile, os

def compactar_zip(arquivos, saida):
    with zipfile.ZipFile(saida, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo), compress_type=zipfile.ZIP_DEFLATED)

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

 
# Teste a compactação em ZIP
print("Testando a compactação em ZIP...")
compactar_zip("teste do python.txt", "meus_arquivos.zip")
print("Arquivo meus_arquivos.zip criado com sucesso!")
