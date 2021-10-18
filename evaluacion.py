
from tkinter import * 
from requests import *
from leerFileAPI import *

class Interfaz:
    
    def __init__(self, ventana):
        self.selec = IntVar()
        self.cuentaPreguntas = 0
        self.correctas = 0
        self.objLeer = NullHandler        
        self.listQues =[]
        self.listMat =[]
        self.b2 =  NullHandler 
        self.b1 =  NullHandler 
        self.bSalir = NullHandler
        self.cuentaLisMat = 0
        
        self.ventana=ventana
        self.ventana.geometry('700x530+0+0');
        self.ventana.title("Sistema de Evaluacion ")  
        self.loadScreenStart("Para iniciar tu examen presiona el boton empezar","")                     

        return

    def ponLabels(self, tx1, tx2):
        tf = "                                                                                                 "
        
        lab = Label (self.ventana,text=tf,font=("Helvetica",18)).place(x=70, y=10)
        lab = Label (self.ventana,text=tx1,font=("Helvetica",18)).place(x=70, y=10)
        lab2 = Label (self.ventana,text=tf,font=("Helvetica",14)).place(x=70, y=50)
        lab2 = Label (self.ventana,text=tx2,font=("Helvetica",14)).place(x=70, y=50)
        return

    def ponPregunta(self, pregunta):
        
        textoFake = "                                                                                                 " 
        self.lab = Label (self.ventana,text=textoFake,font=("Helvetica",14)).place(x=100, y=100)
        self.lab = Label (self.ventana,text=pregunta,font=("Helvetica",14)).place(x=100, y=100)
        return

    def actualizaRadios(self, i):     

        pregunta = self.listQues[i]  
        self.ponPregunta(pregunta['pregunta'])
        uno = pregunta['answers'][0]        
        dos = pregunta['answers'][1]        
        tres = pregunta['answers'][2]        
        cuat = pregunta['answers'][3]        
        self.ponRadios(uno, dos, tres, cuat)


    def ponRadios(self, texto1, texto2, texto3, texto4 ):        
        txtoFake = "                                                                                                      "
        self.rb1 = Radiobutton(self.ventana, text=txtoFake, variable=self.selec, command=self.estado, value=1).place(x=100, y=150)
        self.rb1 = Radiobutton(self.ventana, text=texto1, variable=self.selec, command=self.estado, value=1).place(x=100, y=150)

        self.rb2 = Radiobutton(self.ventana, text=txtoFake, variable=self.selec, command=self.estado, value=2).place(x=100, y=200)
        self.rb2 = Radiobutton(self.ventana, text=texto2, variable=self.selec, command=self.estado, value=2).place(x=100, y=200)

        self.rb3 = Radiobutton(self.ventana, text=txtoFake, variable=self.selec, command=self.estado, value=3).place(x=100, y=250)
        self.rb3 = Radiobutton(self.ventana, text=texto3, variable=self.selec, command=self.estado, value=3).place(x=100, y=250)

        self.rb4 = Radiobutton(self.ventana, text=txtoFake, variable=self.selec, command=self.estado, value=4).place(x=100, y=300)
        self.rb4 = Radiobutton(self.ventana, text=texto4, variable=self.selec, command=self.estado, value=4).place(x=100, y=300)
        
        return

    def unableBotonSig(self):         
         self.b2['state']=DISABLED         
         

    def ponLabelAciertos(self, total, resp, corr): 
        tf = "                                         "
        lab1 = Label (self.ventana,text=tf, font=("Helvetica",12)).place(x=80, y=400)
        lab1 = Label (self.ventana,text='Total  de  Preguntas  : '+str(total), font=("Helvetica",12)).place(x=80, y=400)

        lab2 = Label (self.ventana,text=tf, font=("Helvetica",12)).place(x=80, y=430)
        lab2 = Label (self.ventana,text='Preguntas contestadas : '+str(resp), font=("Helvetica",12)).place(x=80, y=430)

        lab3 = Label (self.ventana,text=tf,font=("Helvetica",12)).place(x=80, y=460)
        lab3 = Label (self.ventana,text="Respuestas Correctas  : "+str(corr),font=("Helvetica",12)).place(x=80, y=460)
        
    def estado(self):
        if self.cuentaPreguntas < len( self.listQues ):
            self.b2['state']=NORMAL    

       

    def empieza(self):
        
        if self.cuentaLisMat == 0:
            self.loadBase("https://onalonso.github.io/test_questions/")

        self.loadScreenExam( self.listMat[self.cuentaLisMat] )
        
        return

    def loadBase(self, fileName):
        self.objLeer =  LeerPreg(fileName)        
        self.listMat = self.objLeer.leerMaterias()        
        

    def loadScreenStart(self,txt,txt1):        
        
        self.ponLabels(txt,txt1)
        
        self.b1 =   Button(self.ventana, text="Empezar", width=9, height=1, font=("Helvetica",15), command=self.empieza )               
        self.b1.place(x=500, y=430)
        
    
    def loadScreenExam(self, mate):
         
        self.listQues = self.objLeer.leerQuestMat( mate )       
        self.b2 =   Button(self.ventana, text="Sig", width=9, height=1, font=("Helvetica",15), command=self.avanza ) 
        self.b2.place(x=350, y=430)

        tex = "  Selecciona la respuesta Correcta "
        tex1 = "                      Examen de " + self.listMat[ self.cuentaLisMat ]
        self.ponLabels( tex, tex1 )        
        self.actualizaRadios(0)
        self.ponLabelAciertos(len(self.listQues),0,0)
        self.b1['state']=DISABLED
        self.unableBotonSig()

    def loadScreenInt(self,txt,txt1):
        self.loadScreenStart(txt,txt1)        
        self.ponPregunta("Para seguir con otra materia presiona Empieza")
        self.cuentaPreguntas = 0
        self.cuentaLisMat += 1
        self.correctas = 0
        self.unableBotonSig()

        self.disBut()

    def disBut(self): 
        tf = "                                                                                                        "
        self.rb1 = Radiobutton(self.ventana, text=tf, variable=self.selec, command=self.estado, value=1, state='disabled').place(x=100, y=150)
        self.rb2 = Radiobutton(self.ventana, text=tf, variable=self.selec, command=self.estado, value=2,state='disabled').place(x=100, y=200)
        self.rb3 = Radiobutton(self.ventana, text=tf, variable=self.selec, command=self.estado, value=3,state='disabled').place(x=100, y=250)
        self.rb4 = Radiobutton(self.ventana, text=tf, variable=self.selec, command=self.estado, value=4,state='disabled').place(x=100, y=300)
                
 
    def loadScreenFinal(self,txt,txt1):
        self.loadScreenStart(txt,txt1)        
        self.b1['state'] = DISABLED
        self.bSalir = Button(self.ventana, text="Salir", width=9, height=1, font=("Helvetica",15), command=self.salir )       
        self.bSalir.place(x=500, y=430)
        self.ponPregunta("Terminaste tus examenes presiona Salir")
        self.cuentaPreguntas = 0
        self.cuentaLisMat += 1
        self.unableBotonSig()
        self.disBut()
        
    def salir(self):
        self.ventana.destroy()
        return

    def avanza(self):

        pregunta = self.listQues[self.cuentaPreguntas]    
        if self.selec.get() == pregunta['responses']:
            self.correctas += 1         
        self.cuentaPreguntas += 1 
        self.ponLabelAciertos(len(self.listQues), self.cuentaPreguntas, self.correctas)            
              
        self.selec = IntVar() 
        if self.cuentaPreguntas < len( self.listQues):                       
           
            self.actualizaRadios(self.cuentaPreguntas)  
        else:                
            if self.cuentaLisMat == (len(self.listMat) - 1):
                txt = " Terminaste tu examen de " + self.listMat[ self.cuentaLisMat]
                self.loadScreenFinal(txt, "En la parte de abajo puedes ver tus resultados")
            else:
                tf="                                                                     "                
                self.ponRadios(tf, tf, tf, tf) 
                txt = " Terminaste tu examen de " + self.listMat[ self.cuentaLisMat]
                self.loadScreenInt(txt,"En la parte de abajo puedes ver tus resultados")

        self.unableBotonSig()  
           
        return

    def loop(self):
        self.ventana.mainloop()    

    

if __name__=='__main__':            
   
    ventana_principal=Tk()
    test = Interfaz(ventana_principal)
    test.loop()

        
    