from tkinter import messagebox


class usuario:
    def __init__(self,email, senha):
        self.email = email
        self.senha = senha
           
    def validar(self): 
        
        if "@" not in self.email:
            messagebox.showerror("Erro", "Email inválido")
        else:
            pass
                       
        if len(self.senha) < 8:
            messagebox.showerror("Erro", "Sua senha deve ter 8 caracteres ou mais")
        else:
            with open ("senhas.json", "w", encoding="utf-8") as arquivo:
                pass
        