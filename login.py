from tkinter import *
from tkinter import ttk #módulo de widgets temáticos
import ttkbootstrap as tb #biblioteca bootstrap para widgets

class Ventana(tb.Window):
    def __init__(self):
        super().__init__()
        self.ventana_login()
        # self.ventana_menu()

    def ventana_login(self):

        #alinear los widets al centro de la ventana
        self.grid_columnconfigure(0,weight=1)

        self.frame_login=Frame(master=self)
        self.frame_login.grid(row=0,column=0,sticky=NSEW) #coloca el frame posicionado en toda la ventanta
        lblframe_login=tb.LabelFrame(master=self.frame_login,text='Acceso')
        lblframe_login.pack(padx=10,pady=35)

        lbl_titulo=tb.Label(master=lblframe_login,text='Inicia Sesión o Regístrate', font=('Calibri', 17))
        lbl_titulo.pack(padx=10,pady=35)

        ent_usuario=tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        ent_usuario.pack(padx=10,pady=10)
        
        ent_clave=tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        ent_clave.pack(padx=10,pady=10)
        #mascara de entrada para ocultar el texto
        ent_clave.config(show='*')


        btn_acceso=tb.Button(master=lblframe_login,width=38,text='Iniciar Sesión', bootstyle='primary-outline', command=self.logueo_ususarios)
        btn_acceso.pack(padx=10,pady=10)

        btn_acceso=tb.Button(master=lblframe_login,width=38,text='Regístrate', bootstyle='primary-outline')
        btn_acceso.pack(padx=10,pady=10)
    def ventana_menu(self):

        #Slidebar
        self.frame_left=Frame(master=self,width=200)
        self.frame_left.grid(row=0,column=0,sticky=NSEW)

        self.frame_center=Frame(master=self,)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)

        btn_usuarios=Button(master=self.frame_left,text='Usuarios', width=15,height=2)
        btn_usuarios.grid(row=0,column=0)
    def logueo_ususarios(self):
        #cambio de ventana al loguearse
        self.ventana_menu()
        self.frame_login.destroy() #destruye al ventana loguin al ingresar



def main():
    app=Ventana()
    app.title=('Sistema Control de Stock')
    app.state('zoomed')
    tb.Style('cyborg') #tema de bootstrap

    app.mainloop()

if __name__ == '__main__':
    main()
