from tkinter import *
from tkinter.scrolledtext import ScrolledText
import json 
from processor import Processor

def Captura():    
    try:
        proces_list = json.loads(infoData.get("1.0", END))
        processor = Processor(proces_list)
        processor.execute()
    except Exception:        
        vError("ERROR", "Error al ejecutar o con la lista de procesos")
    

def vError(T,MSG):
    Error = Tk()    
    Error.geometry("300x60")
    Error.title(T)
    Error.configure(padx=10,pady=10)
    Label(Error,text=MSG).pack()    
    Error.mainloop() 

window = Tk()

window.title("Simulador de Procesador")
window.geometry('420x380')
    
tPreset = "Simulacion de manejo de procesos en un procesador"
tExample = "Ejemplo de lista de procesos para ingresar : \n \
        [{\"process\" : \"proceso1\",\"weight\" : 50},\n \
        {\"process\" : \"proceso2\",\"weight\" : 50}]"

#LABEL MENSAJE INICIAL 
lblPreset = Label(window,text=tPreset)
lblPreset.place(x=10,y=10,width=360,height=30)

lblExample = Label(window,text=tExample)
lblExample.place(x=5,y=40,width=360,height=60)

infoData = ScrolledText(window,width=45,height=10)
infoData.place(x=10,y=105)

btnCap = Button(window,text="Capturar y Procesar",command=Captura)
btnCap.place(x=120,y=300)

window.mainloop()