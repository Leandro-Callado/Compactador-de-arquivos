import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile, tarfile, os

# --- Funções de compactação ---
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

# --- Variável global para arquivos selecionados ---
arquivos_selecionados = []

# --- Função para selecionar arquivos ---
def selecionar_arquivos():
    global arquivos_selecionados
    arquivos = filedialog.askopenfilenames(title="Selecione um ou mais arquivos")
    
    if arquivos:
        arquivos_selecionados = list(arquivos)
        label_status.config(text=f"{len(arquivos_selecionados)} arquivo(s) selecionado(s).")
        zip_button.config(state="normal")
        tar_button.config(state="normal")
        targz_button.config(state="normal")
    else:
        arquivos_selecionados = []
        label_status.config(text="Nenhum arquivo selecionado.")
        zip_button.config(state="disabled")
        tar_button.config(state="disabled")
        targz_button.config(state="disabled")

# --- Função para iniciar compactação ---
def iniciar_compactacao(formato):
    if not arquivos_selecionados:
        messagebox.showwarning("Atenção", "Por favor, selecione os arquivos primeiro!")
        return

    tipos_de_arquivo = {
        'zip': [("Arquivo ZIP", "*.zip")],
        'tar': [("Arquivo TAR", "*.tar")],
        'targz': [("Arquivo TAR.GZ", "*.tar.gz")]
    }

    extensao_padrao = f".{formato.replace('targz', 'tar.gz')}"

    caminho_saida = filedialog.asksaveasfilename(
        title=f"Salvar arquivo {formato.upper()} como...",
        defaultextension=extensao_padrao,
        filetypes=tipos_de_arquivo[formato]
    )

    if caminho_saida:
        try:
            if formato == 'zip':
                compactar_zip(arquivos_selecionados, caminho_saida)
            elif formato == 'tar':
                compactar_tar(arquivos_selecionados, caminho_saida)
            elif formato == 'targz':
                compactar_tar_gz(arquivos_selecionados, caminho_saida)
            
            messagebox.showinfo("Sucesso!", f"Arquivos compactados com sucesso em:\n{caminho_saida}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a compactação:\n{e}")

# --- Interface gráfica ---
window = tk.Tk()
window.title("Compactador by Leandro & Lucas")
window.geometry("400x300")

label_escolha = tk.Label(window, text="Escolha os arquivos para compactar:", fg="black")
label_escolha.pack(pady=10)

btn_selecionar = tk.Button(window, text="Selecionar Arquivos", command=selecionar_arquivos)
btn_selecionar.pack(pady=10)

label_status = tk.Label(window, text="Nenhum arquivo selecionado.", fg="blue")
label_status.pack(pady=10)

zip_button = tk.Button(window, text="Compactar em ZIP", width=20, state="disabled",
                       command=lambda: iniciar_compactacao('zip'))
zip_button.pack(pady=5)

tar_button = tk.Button(window, text="Compactar em TAR", width=20, state="disabled",
                       command=lambda: iniciar_compactacao('tar'))
tar_button.pack(pady=5)

targz_button = tk.Button(window, text="Compactar em TAR.GZ", width=20, state="disabled",
                         command=lambda: iniciar_compactacao('targz'))
targz_button.pack(pady=5)

window.mainloop()
