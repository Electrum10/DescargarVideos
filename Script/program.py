import tkinter
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog

#Configuración básica de la ventana
ventana = tkinter.Tk()
ventana.title("Descargador de Videos de YouTube")
ventana.geometry("700x500")
ventana.configure(background="#B3B3B3")

directorio = ""


#Función para descargar el video
def DescargarVideo():
        URL = Url.get()
        Selección = Combo.get()
        ytObject = YouTube(URL)
        if Selección == "MP3":
            video = ytObject.streams.filter(only_audio=True).first()
            directorio = filedialog.askdirectory(title = "Selecciona en donde quieres que se descargue el video")
            video.download(directorio)
        elif Selección == "MP4":
            video = ytObject.streams.get_highest_resolution()
            directorio = filedialog.askdirectory(title = "Selecciona en donde quieres que se descargue el video")
            video.download(directorio)

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
Descargar.place(relx=0.41, rely=0.75, relheight=0.1, relwidth=0.2)


Elegir = tkinter.Label(ventana, text = "¿En que formato quieres el video?", font=("Arial", 12, "normal", "italic",), background="lightblue")
Elegir.place(relx =0.35, rely=0.48 )


Combo = ttk.Combobox(ventana, state="readonly" ,values=("MP3", "MP4"))
Combo.place(relx=0.41, rely=0.55)


ventana.mainloop()