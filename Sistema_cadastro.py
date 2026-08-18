import tkinter

from Validador import usuario

janela_principal = tkinter.Tk()
janela_principal.geometry("1000x600")
janela_principal.title("Cadastro")
janela_principal.maxsize(1000, 600)
janela_principal.minsize(1000, 600)

Frame_inserção = tkinter.Frame(janela_principal, bg = "gray", bd = 2, relief= "solid",width=300,  height = 400)
Frame_inserção.place(x = 350, y = 100)

titulo = tkinter.Label(Frame_inserção, font=("Arial", 20, "bold"), text="Cadastro")
titulo.place(x = 85, y = 30)

email_label = tkinter.Label(Frame_inserção, font=("Arial", 12, "bold"), text="Email" )
email_label.place(x = 20, y = 100)

senha_label = tkinter.Label(Frame_inserção, font=("Arial", 12, "bold"), text="Senha" )
senha_label.place(x = 20, y = 200)

email_entry = tkinter.Entry(Frame_inserção, font=("Arial", 12))
email_entry.place(x = 20, y = 150, height=35, width=250)

senha_entry = tkinter.Entry(Frame_inserção, font=("Arial", 12), show="•")
senha_entry.place(x = 20, y = 250, height=35, width=250)

def cadastrar():
    usuario_fic = usuario(email_entry.get(), senha_entry.get())
    usuario_fic.validar()
    email_entry.delete(0, "end")
    senha_entry.delete(0, "end")
    
enviar = tkinter.Button(Frame_inserção, text="Enviar", font=("Arial", 20, "bold"), command=cadastrar)
enviar.place(height=50, width=285, x= 5, y= 340)

janela_principal.mainloop()


        
    