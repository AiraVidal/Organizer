import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def organizar_arquivos(pasta_origem):
    pasta_destino = os.path.join(pasta_origem, "Organizados")
    os.makedirs(pasta_destino, exist_ok=True)

    arquivos = [
        nome
        for nome in os.listdir(pasta_origem)
        if os.path.isfile(os.path.join(pasta_origem, nome))
    ]

    movidos = []
    ignorados = []

    for arquivo in arquivos:
        if arquivo.lower() == "organizador.py":
            ignorados.append(arquivo)
            continue

        nome_base, extensao = os.path.splitext(arquivo)
        if not nome_base:
            ignorados.append(arquivo)
            continue

        extensao = extensao[1:].lower() if extensao else "sem_extensao"
        pasta_extensao = os.path.join(pasta_destino, extensao)
        os.makedirs(pasta_extensao, exist_ok=True)

        origem = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(pasta_extensao, arquivo)

        # Evita sobrescrever se ja existir arquivo com mesmo nome.
        if os.path.exists(destino):
            contador = 1
            while True:
                candidato = os.path.join(
                    pasta_extensao, f"{nome_base}_{contador}{os.path.splitext(arquivo)[1]}"
                )
                if not os.path.exists(candidato):
                    destino = candidato
                    break
                contador += 1

        shutil.move(origem, destino)
        movidos.append((arquivo, destino))

    return movidos, ignorados


class OrganizadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Arquivos")
        self.root.geometry("800x520")

        self.pasta_var = tk.StringVar()

        self._criar_interface()

    def _criar_interface(self):
        frame_topo = ttk.Frame(self.root, padding=12)
        frame_topo.pack(fill="x")

        ttk.Label(frame_topo, text="Pasta para organizar:").grid(
            row=0, column=0, sticky="w"
        )

        entrada = ttk.Entry(frame_topo, textvariable=self.pasta_var)
        entrada.grid(row=1, column=0, sticky="ew", padx=(0, 8), pady=(4, 0))

        btn_buscar = ttk.Button(
            frame_topo, text="Selecionar pasta", command=self._selecionar_pasta
        )
        btn_buscar.grid(row=1, column=1, pady=(4, 0))

        btn_organizar = ttk.Button(
            frame_topo, text="Organizar agora", command=self._organizar_agora
        )
        btn_organizar.grid(row=1, column=2, padx=(8, 0), pady=(4, 0))

        frame_topo.columnconfigure(0, weight=1)

        self.progresso = ttk.Progressbar(self.root, mode="indeterminate")
        self.progresso.pack(fill="x", padx=12, pady=(0, 8))

        frame_log = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        frame_log.pack(fill="both", expand=True)

        self.log = tk.Text(frame_log, height=18, wrap="word")
        self.log.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(frame_log, orient="vertical", command=self.log.yview)
        scroll.pack(side="right", fill="y")
        self.log.configure(yscrollcommand=scroll.set)

        self._escrever_log("Selecione uma pasta para iniciar.\n")

    def _escrever_log(self, texto):
        self.log.insert("end", texto)
        self.log.see("end")

    def _selecionar_pasta(self):
        pasta = filedialog.askdirectory(title="Escolha a pasta para organizar")
        if pasta:
            self.pasta_var.set(pasta)
            self._escrever_log(f"Pasta selecionada: {pasta}\n")

    def _organizar_agora(self):
        pasta = self.pasta_var.get().strip()
        if not pasta:
            messagebox.showwarning("Atenção", "Selecione uma pasta antes de organizar.")
            return

        if not os.path.isdir(pasta):
            messagebox.showerror("Erro", "A pasta selecionada não existe.")
            return

        try:
            self.progresso.start(10)
            self.root.update_idletasks()

            movidos, ignorados = organizar_arquivos(pasta)

            self._escrever_log("\n--- Resultado da organização ---\n")
            for nome, destino in movidos:
                self._escrever_log(f"Movido: {nome} -> {destino}\n")
            for nome in ignorados:
                self._escrever_log(f"Ignorado: {nome}\n")

            self._escrever_log(
                f"\nConcluído: {len(movidos)} arquivo(s) movido(s), {len(ignorados)} ignorado(s).\n"
            )
            messagebox.showinfo(
                "Concluído",
                f"Organização finalizada.\nMovidos: {len(movidos)}\nIgnorados: {len(ignorados)}",
            )
        except Exception as erro:
            messagebox.showerror("Erro ao organizar", str(erro))
        finally:
            self.progresso.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizadorApp(root)
    root.mainloop()
