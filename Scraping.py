# -*- coding:utf-8 -*- #

#Importando las librerias
import requests
from bs4 import BeautifulSoup

#Inicializando la clase Scraping
class Scraping:
    
    #Creando el constructor
    def __init__(self,url):
        self.url = url
        
    #Funcion para obtener el html
    def getHTML(self):
        url = self.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content ,'html.parser')
        self.html = soup
        return self.html
    
    #Funcion para obtener una propiedad de un elemento segun el tipo
    def getPropertyOfElementsOfType(self,element,propiedad):
        htmlText = self.html
        for data in htmlText.find_all(element):
            return data.get(propiedad)

    #Funcion para obtener la propiedad de un elemento
    def getPropertyOfElement(self,element,clase,propiedad):
        htmlText = self.html
        data = htmlText.find(element,class_=clase)
        return data.get(propiedad)

    #Funcion para obtener un elemento por clase
    def getElementByClass(self,element,clase):
        htmlText = self.html
        datos = htmlText.find(element,class_=clase)
        return datos

    #Funcion para obtener los elementos de un tipo
    def getAllElemenstOfType(self,element):
        htmlText = self.html
        datos = htmlText.find_all(element)
        return datos

    #Funcion para obtener el texto de un elemento por clase
    def getTextElementByClass(self,element,clase):
        htmlText = self.html
        datos = htmlText.find(element,class_=clase)
        datos = datos.text
        return datos

    #Funcion para obtener todos los textos de los elementos de un tipo segun su clase
    def getAllTextElementOfTypeByClass(self,element,clase):
        htmlText = self.html
        datos = htmlText.find_all(element,class_=clase)
        for data in datos:
            return data.get_text()
        

        
        
