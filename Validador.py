import json
from tkinter import messagebox

armazenador = []
senhas = []

class usuario:
    def __init__(self,email, senha):
        self.email = email
        self.senha = senha
           
    def validar(self):
        global armazenador, senhas
        try:
            with open("armazenador.json", "r") as arquivo:
                armazenador = json.load(arquivo)
        except ValueError:
            with open("armazenador.json", "w") as arquivo:
                json.dump([], arquivo)
        try:
            with open("senhas.json", "r") as arquivo:
                senhas = json.load(arquivo)
        except ValueError:
            with open("senhas.json", "w") as arquivo:
                json.dump([], arquivo)
        dados_email = {
            "email": self.email,
            "senha": len(self.senha)*"•"
        }
        dados_senha = {
            "email": self.email,
            "senha": self.senha
        }
        
        if "@" not in self.email:
            messagebox.showerror("Erro", "Email inválido")
        else:
            with open("armazenador.json", "r") as arquivo:
                armazenador = json.load(arquivo)
            armazenador.append(dados_email)
            with open ("armazenador.json", "w", encoding="utf-8") as arquivo:
                json.dump(armazenador, arquivo, indent=4,ensure_ascii=False)
                       
        if len(self.senha) < 8:
            messagebox.showerror("Erro", "Sua senha deve ter 8 caracteres ou mais")
        else:
            with open("senhas.json", "r") as arquivo:
                senhas = json.load(arquivo)
            senhas.append(dados_senha)
            with open("senhas.json", "w", encoding="utf-8") as arquivo:
                json.dump(senhas, arquivo, indent=4, ensure_ascii=False)
            messagebox.showinfo("Concluído", "Seu cadastro foi finalizado\n com sucesso!!!")
            
            
        