📘 Tema: Compactador de arquivos<br>

📝 Descrição<br>
Programa em Python com interface gráfica (Tkinter) para compactação de arquivos nos formatos ZIP, TAR e TAR.GZ.

⚙️ Tecnologias e Ferramentas Utilizadas <br>
• Python 3<br>
• Tkinter (GUI)<br>
» Bibliotecas nativas: zipfile, tarfile, os<br>

💻 Como Rodar o Projeto<br>
Instruções passo a passo para executar o projeto localmente:<br>
```bash
# Clone o repositório
git clone https://github.com/Leandro-Callado/Compactador-de-arquivos

# Acesse a pasta
cd Compactador-de-arquivos

# Execute o projeto
python main.py

```
🐧 Instruções para Linux
```bash
#Verifique se o Python 3 está instalado:
python3 --version

#Se não aparecer a versão, instale:
sudo apt update && sudo apt install python3 python3-tk -y

#(No Ubuntu/Debian. Para Fedora/Arch, o pacote tkinter pode variar: sudo dnf install python3-tkinter ou sudo pacman -S tk)

#Clone o repositório e entre na pasta:

git clone https://github.com/Leandro-Callado/Compactador-de-arquivos
cd Compactador-de-arquivos

#Dê permissão de execução (opcional, se quiser rodar direto):
chmod +x main.py

#Execute o projeto:
python3 main.py

#ou, se deu permissão:
./main.py

#(Opcional) Criar atalho no sistema:
#Edite o arquivo .desktop em ~/.local/share/applications/compactador.desktop:

[Desktop Entry]
Name=Compactador de Arquivos
Exec=python3 /caminho/para/Compactador-de-arquivos/main.py
Icon=utilities-file-archiver
Type=Application
Categories=Utility;
```
👥 Colaboradores<br>
[@Lucas](https://github.com/GabVP)<br>
[@Leandro](https://github.com/Leandro-Callado)<br>

📄 Licença<br>
Este projeto está licenciado sob a MIT License.<br>
