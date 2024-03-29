import tkinter


ventana = tkinter.Tk()
ventana.title("Hola mundo")
ventana.geometry("700x500")
ventana.configure(background="#B3B3B3")


Titulo = tkinter.Label(ventana, text="Descargador de Videos de YouTube", font=("Arial", 20, "bold", "italic",), background="#B3B3C2")
Titulo.pack(padx=30, pady=10, ipadx=50, ipady=40)

Descripción = tkinter.Label(ventana, text="Descarga qualquier video de YouTube de forma gratis y legal (creo)", font=("Arial", 13, "normal", "italic",), background="#B3B3C2")
Descripción.pack(ipadx=30, ipady=20)

ventana.mainloop()