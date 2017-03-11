#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui,uic
from PyQt4.QtGui import QPalette,QBrush,QPixmap
import time

class MainWindow(QtGui.QMainWindow):

   def __init__(self):

      QtGui.QMainWindow.__init__(self)
      
      #Dimensiones originales
      size_x_Original = 1080
      size_y_Original = 1920

      #Direcciones de Imágenes de fondo
      self.MAIN_VIEW = "src/img/ArtesPowerRangers/Pantalla 1/1.jpg"
      self.VIEW_2 = "src/img/ArtesPowerRangers/Pantalla 2/1 Back.jpg"

      # Se monta la interfaz de usuario para la pantalla principal
      self.ui = uic.loadUi("views/a.ui")

      #Se bloquea el marco superior 
      self.ui.setWindowFlags(self.ui.windowFlags() | QtCore.Qt.CustomizeWindowHint)
      self.ui.setWindowFlags(self.ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

      #Full Screen
      self.ui.showFullScreen()
      screen = QtGui.QDesktopWidget().screenGeometry()  

      #Dimensiones de la pantalla
      self.size_x = screen.width()
      self.size_y = screen.height()

      #Relación imagen/pantalla
      rel_x = float(self.size_x)/float(size_x_Original)
      rel_y = float(self.size_y)/float(size_y_Original)

      #----------Vista 1---------------
      #Se carga la imagen principal
      palette  = QPalette()
      palette.setBrush(QPalette.Background,QBrush(QPixmap(self.MAIN_VIEW).scaled(self.size_x,self.size_y)))
      self.ui.setPalette(palette)
      #Vista de inicio
      self.ui.setCurrentWidget(self.ui.View1)

      #----------Bóton Inicio-----------
      nx = self.ui.inicio_btn.width()*rel_x
      ny = self.ui.inicio_btn.height()*rel_y

      self.ui.inicio_btn.resize(int(nx),int(ny))
      self.ui.inicio_btn.move(int(self.size_x/2 - nx/2),int(7*self.size_y/8))
      self.ui.inicio_btn.mousePressEvent = self.pressStartV1
      self.ui.inicio_btn.mouseReleaseEvent = self.releaseStartV1
      #----------------------------------
      #----------------------------------

      #-----------Vista 2----------------
      #-----------Título-----------------
      tx = self.ui.title_v2.width()*rel_x
      ty = self.ui.title_v2.height()*rel_y

      self.ui.title_v2.resize(int(tx),int(ty))
      self.ui.title_v2.move(int(self.size_x/2 - tx/2),int(self.size_y/10))

      #----------Bóton Ranger Azul-----------
      y_init = 403*rel_y

      brx = self.ui.blue_ranger.width()*rel_x
      bry = self.ui.blue_ranger.height()*rel_y

      self.ui.blue_ranger.resize(int(brx),int(bry))
      self.ui.blue_ranger.move(int(self.size_x/2 - brx/2),int(y_init))
      self.ui.blue_ranger.mousePressEvent = self.pressBlue 

      #----------Bóton Ranger Rosa-----------
      self.ui.pink_ranger.resize(int(brx),int(bry))
      self.ui.pink_ranger.move(int(self.size_x/2 - brx/2),int(y_init + bry))
      self.ui.pink_ranger.mousePressEvent = self.pressPink 

      #----------Bóton Ranger Rojo-----------
      self.ui.red_ranger.resize(int(brx),int(bry))
      self.ui.red_ranger.move(int(self.size_x/2 - brx/2),int(y_init + 2*bry))
      self.ui.red_ranger.mousePressEvent = self.pressRed   

      #----------Bóton Ranger Amarillo-----------
      self.ui.yellow_ranger.resize(int(brx),int(bry))
      self.ui.yellow_ranger.move(int(self.size_x/2 - brx/2),int(y_init + 3*bry))
      self.ui.yellow_ranger.mousePressEvent = self.pressYellow  

      #----------Bóton Ranger Negro-----------
      self.ui.black_ranger.resize(int(brx),int(bry))
      self.ui.black_ranger.move(int(self.size_x/2 - brx/2),int(y_init + 4*bry))
      self.ui.black_ranger.mousePressEvent = self.pressBlack   

      #----------Botón Continuar-------------
      y_init_btn = 1700*rel_y

      c2x = self.ui.continue_btn.width()*rel_x
      c2y = self.ui.continue_btn.height()*rel_y

      self.ui.continue_btn.resize(int(c2x),int(c2y))
      self.ui.continue_btn.move(int(self.size_x/2 - c2x/2),int(y_init_btn))
      self.ui.continue_btn.mousePressEvent = self.pressContinueV2
      self.ui.continue_btn.mouseReleaseEvent = self.releaseContinueV2

      self.ui.show()

   def pressStartV1(self,event):

      START_BTN_PRESS = "src/img/ArtesPowerRangers/Pantalla 1/inicio_btn.png"

      #Imagen de press button
      startPress = QtGui.QPixmap(START_BTN_PRESS)

      #Se guarda el tamaño original del botón
      self.x_v1b1 = self.ui.inicio_btn.width()
      self.y_v1b1 = self.ui.inicio_btn.height()

      self.ui.inicio_btn.resize(int(self.x_v1b1*0.9),int(self.y_v1b1*0.9))

      position = self.ui.inicio_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.inicio_btn.move(x + (0.1*self.x_v1b1)/2,y + (0.1*self.y_v1b1)/2)
      self.ui.inicio_btn.setPixmap(startPress)

   def releaseStartV1(self,event):
      START_BTN_REL = "src/img/ArtesPowerRangers/Pantalla 1/inicio_btn.png"

      #Imagen de press button
      startRel = QtGui.QPixmap(START_BTN_REL)

      self.ui.inicio_btn.resize(self.x_v1b1,self.y_v1b1)

      position = self.ui.inicio_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.inicio_btn.move(x - (0.1*self.x_v1b1)/2,y - (0.1*self.y_v1b1)/2)
      self.ui.inicio_btn.setPixmap(startRel)

      #Acción Envía Vista 2
      #Cambio de fondo vista 2
      palette  = QPalette()
      palette.setBrush(QPalette.Background,QBrush(QPixmap(self.VIEW_2).scaled(self.size_x,self.size_y)))
      self.ui.setPalette(palette)
      
      self.ui.setCurrentWidget(self.ui.View2)

   def pressRed(self, event):
      #Se guarda el tamaño original del botón
      self.x_red = self.ui.red_ranger.width()
      self.y_red = self.ui.red_ranger.height()

      self.ui.red_ranger.resize(int(self.x_red*0.9),int(self.y_red*0.9))

      position = self.ui.red_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.red_ranger.move(x + (0.1*self.x_red)/2,y + (0.1*self.y_red)/2)

   def pressBlack(self, event):
      #Se guarda el tamaño original del botón
      self.x_black = self.ui.black_ranger.width()
      self.y_black = self.ui.black_ranger.height()

      self.ui.black_ranger.resize(int(self.x_black*0.9),int(self.y_black*0.9))

      position = self.ui.black_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.black_ranger.move(x + (0.1*self.x_black)/2,y + (0.1*self.y_black)/2)

   def pressPink(self, event):
      #Se guarda el tamaño original del botón
      self.x_pink = self.ui.pink_ranger.width()
      self.y_pink = self.ui.pink_ranger.height()

      self.ui.pink_ranger.resize(int(self.x_pink*0.9),int(self.y_pink*0.9))

      position = self.ui.pink_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.pink_ranger.move(x + (0.1*self.x_pink)/2,y + (0.1*self.y_pink)/2)

   def pressBlue(self, event):
      #Se guarda el tamaño original del botón
      self.x_blue = self.ui.blue_ranger.width()
      self.y_blue = self.ui.blue_ranger.height()

      self.ui.blue_ranger.resize(int(self.x_blue*0.9),int(self.y_blue*0.9))

      position = self.ui.blue_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.blue_ranger.move(x + (0.1*self.x_blue)/2,y + (0.1*self.y_blue)/2)

   def pressYellow(self, event):
      #Se guarda el tamaño original del botón
      self.x_yellow = self.ui.yellow_ranger.width()
      self.y_yellow = self.ui.yellow_ranger.height()

      self.ui.yellow_ranger.resize(int(self.x_yellow*0.9),int(self.y_yellow*0.9))

      position = self.ui.yellow_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.yellow_ranger.move(x + (0.1*self.x_yellow)/2,y + (0.1*self.y_yellow)/2)

   def pressContinueV2(self,event):
      #Se guarda el tamaño original del botón
      self.x_cV2 = self.ui.continue_btn.width()
      self.y_cV2 = self.ui.continue_btn.height()

      self.ui.continue_btn.resize(int(self.x_cV2*0.9),int(self.y_cV2*0.9))

      position = self.ui.inicio_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.inicio_btn.move(x + (0.1*self.x_v1b1)/2,y + (0.1*self.y_v1b1)/2)
      self.ui.inicio_btn.setPixmap(startPress)

   def releaseContinueV2(self,event):
      START_BTN_REL = "src/img/ArtesPowerRangers/Pantalla 1/inicio_btn.png"

      #Imagen de press button
      startRel = QtGui.QPixmap(START_BTN_REL)

      self.ui.inicio_btn.resize(self.x_v1b1,self.y_v1b1)

      position = self.ui.inicio_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.inicio_btn.move(x - (0.1*self.x_v1b1)/2,y - (0.1*self.y_v1b1)/2)
      self.ui.inicio_btn.setPixmap(startRel)

      #Acción Envía Vista 2
      #Cambio de fondo vista 2
      palette  = QPalette()
      palette.setBrush(QPalette.Background,QBrush(QPixmap(self.VIEW_2).scaled(self.size_x,self.size_y)))
      self.ui.setPalette(palette)
      
      self.ui.setCurrentWidget(self.ui.View2)

#Ejecución del programa
app = QtGui.QApplication(sys.argv)
MyWindow = MainWindow()
sys.exit(app.exec_())