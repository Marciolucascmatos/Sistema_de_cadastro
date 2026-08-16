from tkinter import messagebox

from Sistema_cadastro import email_entry, senha_entry

senha = senha_entry.get()
email = email_entry.get()

class usuario:
    def __init__(self,email, senha):
        self.email = email
        self.senha = senha   
    def validar():
          global  senha, email
          if len(senha) < 8:
              messagebox.showerror("Erro", "Sua senha deve ter 8 caracteres")
          else:
              pass
          
          if "@" not in email:
              messagebox.showerror("Erro", "Email inválido")
          else:
              pass
        