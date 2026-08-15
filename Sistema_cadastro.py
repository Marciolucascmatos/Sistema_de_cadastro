import tkinter

janela_principal = tkinter.Tk()
janela_principal.geometry("1000x600")
janela_principal.title("Cadastro")
janela_principal.maxsize(1000, 600)
janela_principal.minsize(1000, 600)

Frame_inserção = tkinter.Frame(janela_principal, bg = "gray", bd = 2, relief= "solid", width = 300, height = 400)
Frame_inserção.place(x = 350, y = 100)

janela_principal.mainloop()


        
    