import json
from urllib.request import urlopen
import os


from requests import NullHandler

class LeerPreg:
    def __init__(self, url):        
        self.url = url
        data_base = urlopen(url)
        self.data = json.loads( data_base.read() )
        

    def leerNumMat(self):         
        return len(self.data['materias'])

    def leerMaterias(self):         
        newlist = list()
        for i in self.data['materias'].keys():
            newlist.append(i)             
        return newlist

    def leerQuestMat(self, mater):
        lista = self.data.get('materias').get(mater).get('questions')    
        return lista

    
            
        
    
       