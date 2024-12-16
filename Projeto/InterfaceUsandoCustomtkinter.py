import customtkinter as c


# aparencia da interface do programa
c.set_appearance_mode('dark')
# criar a janela
app = c.CTk()
# Titulo da janela 
app.title('Login')
app.geometry('300x300')
# campos que serão usados
frase = c.CTkLabel(app,text=' Seja Bem-Vindo')
usuario = c.CTkLabel(app,text='Usuario')
frase.pack()
usuario.pack()
# loop da aplicação
app.mainloop()
