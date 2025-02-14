import json
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os  # Para manipulação de arquivos

class JSONEditor:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.current_index = 0

        # Carregar o índice salvo, se existir
        self.config_file = "config.json"
        self.load_last_index()

        # Configuração da interface
        self.root.title("Editor de JSON")
        self.root.geometry("600x400")

        # Labels e campos de texto
        self.label_url = tk.Label(root, text="URL:")
        self.label_url.pack()
        self.entry_url = tk.Entry(root, width=80)
        self.entry_url.pack()

        self.label_title = tk.Label(root, text="Title:")
        self.label_title.pack()
        self.entry_title = tk.Entry(root, width=80)
        self.entry_title.pack()

        self.label_description = tk.Label(root, text="Description:")
        self.label_description.pack()
        self.entry_description = tk.Text(root, width=80, height=10)
        self.entry_description.pack()

        # Botões
        self.button_delete = tk.Button(root, text="Apagar (Ctrl+E)", command=self.delete_item)
        self.button_delete.pack(side=tk.LEFT, padx=10)

        self.button_previous = tk.Button(root, text="Anterior (Ctrl+Q)", command=self.previous_item)
        self.button_previous.pack(side=tk.LEFT, padx=10)

        self.button_next = tk.Button(root, text="Próximo (Ctrl+W)", command=self.next_item)
        self.button_next.pack(side=tk.LEFT, padx=10)

        self.button_save = tk.Button(root, text="Salvar Alterações", command=self.save_changes)
        self.button_save.pack(side=tk.RIGHT, padx=10)

        self.button_open_url = tk.Button(root, text="Abrir URL (Ctrl+O)", command=self.open_url)
        self.button_open_url.pack(side=tk.LEFT, padx=10)

        # Atalhos de teclado
        self.root.bind("<Control-e>", lambda event: self.delete_item())  # Ctrl+E para apagar
        self.root.bind("<Control-q>", lambda event: self.previous_item())  # Ctrl+Q para anterior
        self.root.bind("<Control-w>", lambda event: self.next_item())  # Ctrl+W para próximo
        self.root.bind("<Control-y>", lambda event: self.open_url())  # Ctrl+O para abrir URL

        # Carregar o item atual
        self.load_item()

    def load_last_index(self):
        """Carrega o último índice salvo do arquivo de configuração."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self.current_index = config.get("last_index", 0)
            except Exception as e:
                print(f"Erro ao carregar o índice salvo: {e}")
                self.current_index = 0
        else:
            self.current_index = 0

    def save_last_index(self):
        """Salva o índice atual no arquivo de configuração."""
        config = {"last_index": self.current_index}
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"Erro ao salvar o índice: {e}")

    def load_item(self):
        """Carrega os dados do item atual na interface."""
        if self.current_index < len(self.data):
            item = self.data[self.current_index]
            self.entry_url.delete(0, tk.END)
            self.entry_url.insert(0, item["url"])
            self.entry_title.delete(0, tk.END)
            self.entry_title.insert(0, item["title"])
            self.entry_description.delete(1.0, tk.END)
            self.entry_description.insert(1.0, item["description"])
        else:
            messagebox.showinfo("Fim", "Todos os itens foram revisados.")
            self.root.destroy()

    def delete_item(self):
        """Remove o item atual da lista."""
        if self.current_index < len(self.data):
            del self.data[self.current_index]
            self.save_last_index()  # Salva o índice atual
            self.load_item()
        else:
            messagebox.showinfo("Fim", "Todos os itens foram revisados.")

    def previous_item(self):
        """Volta para o item anterior."""
        if self.current_index > 0:
            self.current_index -= 1
            self.save_last_index()  # Salva o índice atual
            self.load_item()
        else:
            messagebox.showinfo("Início", "Este já é o primeiro item.")

    def next_item(self):
        """Passa para o próximo item."""
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.save_last_index()  # Salva o índice atual
            self.load_item()
        else:
            messagebox.showinfo("Fim", "Todos os itens foram revisados.")

    def save_changes(self):
        """Salva as alterações no arquivo JSON."""
        with open("competicoes_com_metadados.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        self.save_last_index()  # Salva o índice atual
        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")
        self.root.destroy()

    def open_url(self):
        """Abre a URL do item atual no navegador."""
        if self.current_index < len(self.data):
            url = self.data[self.current_index]["url"]
            webbrowser.open(url)  # Abre a URL no navegador padrão
        else:
            messagebox.showinfo("Fim", "Todos os itens foram revisados.")


# Carregar o arquivo JSON
try:
    with open("competicoes_com_metadados.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    messagebox.showerror("Erro", "Arquivo 'competicoes_com_metadados.json' não encontrado.")
    exit()

# Iniciar a interface gráfica
root = tk.Tk()
app = JSONEditor(root, data)
root.mainloop()