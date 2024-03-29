import tkinter
from pytube import YouTube

#Configuración básica de la ventana
ventana = tkinter.Tk()
ventana.title("Hola mundo")
ventana.geometry("700x500")
ventana.configure(background="#B3B3B3")

#Función para descargar el video
def DescargarVideo():
    try:
        URL = Url.get()
        ytObject = YouTube(URL)
        video = ytObject.streams.get_highest_resolution()
        outPath = '../Descargas'
        video.download(output_path=outPath)
    except:
        print("El link que has puesto no vale")
    print("descarga completada")


#Titulo del programa
Titulo = tkinter.Label(ventana, text="Descargador de Videos de YouTube", font=("Arial", 20, "bold", "italic",), background="#B3B3C2")
Titulo.pack(pady=30)



#Descripción del programa
Descripción = tkinter.Label(ventana, text="Descarga qualquier video de YouTube de forma gratis y legal (creo)", font=("Arial", 13, "normal", "italic",), background="#B3B3C2")
Descripción.pack()



#Fondo personalizado
frame = tkinter.Frame(ventana, width=500, height=320)
frame.place(relx=0.15, rely=0.3)
frame.config(bg="lightblue")
frame.config(bd=25, relief="solid", borderwidth=3)



#Entrada para poner el URL
Url = tkinter.Entry(ventana)
Url.place(relheight=0.08, relwidth=0.33, relx=0.5, rely=0.36)



#Texto para poner el URL del video
Texto = tkinter.Label(ventana, text="Pon el URL del video", font=("Arial", 16, "normal", "italic",), background="lightblue")
Texto.place(relx=0.17, rely=0.37)



#Botón para descargar el video
Descargar = tkinter.Button(ventana, command=DescargarVideo, text="¡Descarga Ya!")
Descargar.place(relx=0.41, rely=0.68, relheight=0.1, relwidth=0.2)


ventana.mainloop()