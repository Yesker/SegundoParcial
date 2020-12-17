from django.shortcuts import render
from django.http import HttpResponse
from .models import TejidoMama
from django_pandas.io import read_frame
import pandas as pd

# Create your views here.


def home(request):
    
    #return HttpResponse("<hi>Hola mundo soy yo<hi>")
 
   return render(request,'MiAppSintactico/home.html')

def cancer(request):

   return render(request, 'MiAppSintactico/cancer.html')



def sintomas(request):
   partetejido = TejidoMama.objects.all()
   tabla = {'tabla': partetejido}
   return render(request, 'MiAppSintactico/sintomas.html',tabla)  #diccionario de contexto


def VistaTabla(request):
    tejido = TejidoMama.objects.all() #query set
    df = read_frame(tejido) #data frame
    fil,col =df.shape
    protemp = df['temperatura'].mean() 
    procolor = df['color'].mean() 
    proinfla = df['inflamacion'].mean()

      
    destemp = df['temperatura'].std()
    descolor = df['color'].std() 
    desinfla = df['inflamacion'].std() 
    
    maximotem = df ['temperatura'].max()
    maximocol = df ['color'].max()
    maximoinfla = df ['inflamacion'].max()
    
    minitem = df ['temperatura'].min()
    minicol = df ['color'].min()
    miniminfla = df ['inflamacion'].min()
    
    
    
    lista=[]
    
    for i in range (0,fil):
       re = df.iloc[i,1:5].mean()
       lista =[re]

      
    datos = {'promediotemperatura': protemp, 'promediocolor':procolor, 'promedioinflamacion':proinfla, 'stdtemperatura':destemp, 'stdcolor':descolor, 'stdinflamacion':desinfla, 'maxt':maximotem, 'maxc': maximocol,'maxi':maximoinfla , 'minimotem':minitem,'minicolor':minicol,'minimoinfla':miniminfla} 
    datos['modatem']=df['temperatura'].median()
    datos['modacolor']= df['color'].median()
    datos['modainfla']= df['inflamacion'].median()
    
    datos['milista']= lista
    
    
    
    
    ''' datos['ds']=df['temperatura'].std() '''
    

    return render(request, 'MiAppSintactico/tabla.html', datos)

def grafo(request):
   tejido = TejidoMama.objects.all() 
   df = read_frame(tejido)
   
  
   Lista = []
   
   Lista =[{'Registro1':df['id'][j], 'Registro2':df['id'][i], 'Distancia':abs(df.iloc[j,2:5]-df.iloc[i,2:5]).sum()} for j in range (0,4) for i in range (j+1,5)]
   """       Lista2 =[{'D1':df.iloc[j,0:1], 'D2':df.iloc[i,0:1], 'conectado':True if abs(df.iloc[j,2:5]).sum()} for j in range (0,4) for i in range()}]
    """   
   ''' 
   ''' 
   Grafo= []
   i=0
   Umbral = 5
   
   for Informacion in Lista:
      if Informacion['Distancia']< Umbral:
         tupla = (Informacion['Registro1'],Informacion ['Registro2'], Informacion['Distancia'], 'SI')
      else: 
          tupla = (Informacion['Registro1'],Informacion ['Registro2'], Informacion['Distancia'], 'NO')
       
   
      Grafo.append(tupla)
   
   Datos2 = {'datos2': Grafo} 
       
       
       
   return render(request, 'MiAppSintactico/grafo.html', Datos2)


def prevenir(request):
    
   return render(request, 'MiAppSintactico/prevenir.html')


def contacto(request):
    
   return render(request, 'MiAppSintactico/contacto.html')




