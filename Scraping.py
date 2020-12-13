# -*- coding:utf-8 -*- #
import requests
from bs4 import BeautifulSoup

class PageScraping:
    def __init__(self,url):
        self.url = url
    def obtenerHTML(self):
        url = self.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content ,'html.parser')
        self.html = soup
    def getPropertyOfElementsOfType(self,element,propiedad):
        htmlText = self.html
        for data in htmlText.find_all(element):
            print(data.get(propiedad))

    def getPropertyOfElement(self,element,clase,propiedad):
        htmlText = self.html
        data = htmlText.find(element,class_=clase)
        print(data.get(propiedad))
        
    def getElementByClass(self,element,clase):
        htmlText = self.html
        datos = htmlText.find(element,class_=clase)
        print(datos)
    def getAllElemenstOfType(self,element):
        htmlText = self.html
        datos = htmlText.find_all(element)
        print(datos)
    def getTextElementByClass(self,element,clase):
        htmlText = self.html
        datos = htmlText.find(element,class_=clase)
        datos = datos.text
        print(datos)
    def getAllTextElementOfTypeByClass(self,element,clase):
        htmlText = self.html
        datos = htmlText.find_all(element,class_=clase)
        for data in datos:
            print(data.get_text())
        

        
        
