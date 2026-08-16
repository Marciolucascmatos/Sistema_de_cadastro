import json
from tkinter import messagebox


class usuario:
    def __init__(self,email, senha):
        self.email = email
        self.senha = senha
           
    def validar(self): 
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
            with open ("armazenador.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_email, arquivo, indent=4,ensure_ascii=False)
                       
        if len(self.senha) < 8:
            messagebox.showerror("Erro", "Sua senha deve ter 8 caracteres ou mais")
        else:
            with open("senhas.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_senha, arquivo, indent=2)
            messagebox.showinfo("Concluído", "Seu cadastro foi finalizado\n com sucesso!!!")
            
            
        