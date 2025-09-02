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
            
arquivos_selecionados = []

def selecionar_arquivos():
    """Abre a janela para selecionar um ou mais arquivos e os guarda na lista global."""
    global arquivos_selecionados
    
    arquivos = filedialog.askopenfilenames(title="Selecione um ou mais arquivos")
    
    if arquivos:
        arquivos_selecionados = list(arquivos) 
        label_status.config(text=f"{len(arquivos_selecionados)} arquivo(s) selecionado(s).")
        zip_button.config(state="normal")
        tar_button.config(state="normal")
        targz_button.config(state="normal")
    else:
        # Se o usuário cancelou, limpa a lista e desativa os botões
        arquivos_selecionados = []
        label_status.config(text="Nenhum arquivo selecionado.")
        zip_button.config(state="disabled")
        tar_button.config(state="disabled")
        targz_button.config(state="disabled")


def iniciar_compactacao(formato):
    """Inicia o processo de compactação baseado no formato escolhido."""
    # Verifica se há arquivos na lista para compactar
    if not arquivos_selecionados:
        messagebox.showwarning("Atenção", "Por favor, selecione os arquivos primeiro!")
        return

    tipos_de_arquivo = {
        'zip': [("Arquivo ZIP", "*.zip")],
        'tar': [("Arquivo TAR", "*.tar")],
        'targz': [("Arquivo TAR.GZ", "*.tar.gz")]
    }
    extensao_padrao = f".{formato.replace('targz', 'tar.gz')}"

    # Abre a janela "Salvar como" para o usuário escolher o nome e local do arquivo final
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

arquivos_selecionados = []

def selecionar_arquivos():
    """Abre a janela para selecionar um ou mais arquivos e os guarda na lista global."""
    global arquivos_selecionados
    
    # Abre o seletor de arquivos e permite múltiplas seleções
    arquivos = filedialog.askopenfilenames(title="Selecione um ou mais arquivos")
    
    if arquivos:
        arquivos_selecionados = list(arquivos) # Converte a tupla para lista
        # Atualiza o texto do label para mostrar quantos arquivos foram selecionados
        label_status.config(text=f"{len(arquivos_selecionados)} arquivo(s) selecionado(s).")
        # Ativa os botões de compactação
        zip_button.config(state="normal")
        tar_button.config(state="normal")
        targz_button.config(state="normal")
    else:
        # Se o usuário cancelou, limpa a lista e desativa os botões
        arquivos_selecionados = []
        label_status.config(text="Nenhum arquivo selecionado.")
        zip_button.config(state="disabled")
        tar_button.config(state="disabled")
        targz_button.config(state="disabled")


def iniciar_compactacao(formato):
    """Inicia o processo de compactação baseado no formato escolhido."""
    # Verifica se há arquivos na lista para compactar
    if not arquivos_selecionados:
        messagebox.showwarning("Atenção", "Por favor, selecione os arquivos primeiro!")
        return

    # Define os tipos de arquivo para a janela "Salvar como"
    tipos_de_arquivo = {
        'zip': [("Arquivo ZIP", "*.zip")],
        'tar': [("Arquivo TAR", "*.tar")],
        'targz': [("Arquivo TAR.GZ", "*.tar.gz")]
    }
    extensao_padrao = f".{formato.replace('targz', 'tar.gz')}"

    # Abre a janela "Salvar como" para o usuário escolher o nome e local do arquivo final
    caminho_saida = filedialog.asksaveasfilename(
        title=f"Salvar arquivo {formato.upper()} como...",
        defaultextension=extensao_padrao,
        filetypes=tipos_de_arquivo[formato]
    )

    # Se o usuário não cancelou a janela de salvar
    if caminho_saida:
        try:
            # Chama a função de compactação correta
            if formato == 'zip':
                compactar_zip(arquivos_selecionados, caminho_saida)
            elif formato == 'tar':
                compactar_tar(arquivos_selecionados, caminho_saida)
            elif formato == 'targz':
                compactar_tar_gz(arquivos_selecionados, caminho_saida)
            
            # Mostra uma mensagem de sucesso
            messagebox.showinfo("Sucesso!", f"Arquivos compactados com sucesso em:\n{caminho_saida}")
        except Exception as e:
            messagebox.showerror("Erro!", f"Ocorreu um erro durante a compactação:\n{e}")

window = tk.Tk()
window.title("Compactador by Leandro & Lucas")
window.geometry("400x300")
# ---------------------- GIF animado ----------------------
# Carrega todos os frames do GIF
frames = []
i = 0
while True:
    try:
        frame = tk.PhotoImage(file='fundogif.gif', format=f'gif -index {i}')
        frames.append(frame)
        i += 1
    except tk.TclError:
        break  # Sai do loop quando não houver mais frames

label_fundo = tk.Label(window)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

def animar_gif(ind=0):
    frame = frames[ind]
    label_fundo.configure(image=frame)
    label_fundo.image = frame  # mantém referência
    window.after(100, animar_gif, (ind+1) % len(frames))  # muda frame a cada 100ms

animar_gif()  # inicia a animação

fundo = tk.PhotoImage(file="fundogif.gif")

# Coloca a imagem como label de fundo
label_fundo = tk.Label(window, image=fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

label_status = tk.Label(
    text="Selecione os arquivos para compactar: ",
    fg="black",
    bg="#ffffff"
)
selecionar_arquivos_button = tk.Button(
    text="Selecionar Arquivos",
    fg="black",
    command=selecionar_arquivos,
)

label_escolha = tk.Label(
    text="Escolha o formato da compactação: ",
    fg="black",
)

zip_button = tk.Button(
    text="Compactar em ZIP",
    width=20,
    height=3,
    bg="white",
    fg="black",
    command=lambda: iniciar_compactacao('zip'),
)
tar_button = tk.Button(
    text="Compactar em TAR",
    width=20,
    height=3,
    bg="white",
    fg="black",
    command=lambda: iniciar_compactacao('tar'),
)
targz_button = tk.Button(
    text="Compactar em TAR.GZ",
    width=20,
    height=3,
    bg="white",
    fg="black",
    command=lambda: iniciar_compactacao('targz'),
)
label_status.pack(pady=10)
selecionar_arquivos_button.pack(pady=2)
label_escolha.pack(pady=10)
zip_button.pack(pady=2)
tar_button.pack(pady=2)
targz_button.pack(pady=2)

# Exibir na interface
label = tk.Label(window, image=fundo)
label.pack()
window.mainloop()