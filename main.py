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

      #Clicked button
      self.p = 1.15
      self.b = 0.95

      #Flags Vista 2
      self.IsChecked = [['Red',False],['Pink',False],['Blue',False],['Black',False],['Yellow',False]]

      #Direcciones de Imágenes de fondo
      self.MAIN_VIEW = "src/img/ArtesPowerRangers/Pantalla 1/1.jpg"
      self.VIEW_2 = "src/img/ArtesPowerRangers/Pantalla 2/1 Back.jpg"
      self.VIEW_3 = "src/img/ArtesPowerRangers/Pantalla 3/1 Back.jpg"

      #Direcciones Caras Vista 3
      self.URL_FACES = ["src/img/ArtesPowerRangers/Pantalla 3/3 Rengers/Red.jpg",
                        "src/img/ArtesPowerRangers/Pantalla 3/3 Rengers/Pink.jpg",
                        "src/img/ArtesPowerRangers/Pantalla 3/3 Rengers/Blue.jpg",
                        "src/img/ArtesPowerRangers/Pantalla 3/3 Rengers/Black.jpg",
                        "src/img/ArtesPowerRangers/Pantalla 3/3 Rengers/Yellow.jpg"]

      self.RED = "src/img/ArtesPowerRangers/Pantalla 2/Red.jpg"
      self.RED_BLOCK = "src/img/ArtesPowerRangers/Pantalla 2/red_blocked.png"
      self.BLUE = "src/img/ArtesPowerRangers/Pantalla 2/Blue.jpg"
      self.BLUE_BLOCK = "src/img/ArtesPowerRangers/Pantalla 2/azul_blocked.png"
      self.BLACK = "src/img/ArtesPowerRangers/Pantalla 2/black.jpg"
      self.BLACK_BLOCK = "src/img/ArtesPowerRangers/Pantalla 2/black_blocked.png"
      self.PINK = "src/img/ArtesPowerRangers/Pantalla 2/pink.jpg"
      self.PINK_BLOCK = "src/img/ArtesPowerRangers/Pantalla 2/pink_blocked.png"
      self.YELLOW = "src/img/ArtesPowerRangers/Pantalla 2/yellow.jpg"
      self.YELLOW_BLOCK = "src/img/ArtesPowerRangers/Pantalla 2/yellow_blocked.png"

      # Se monta la interfaz de usuario para la pantalla principal
      self.ui = uic.loadUi("views/main.ui")

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

      #-----------Vista 2----------------
      #-----------Título-----------------
      tx = self.ui.title_v2.width()*rel_x
      ty = self.ui.title_v2.height()*rel_y

      self.ui.title_v2.resize(int(tx),int(ty))
      self.ui.title_v2.move(int(self.size_x/2 - tx/2),int(self.size_y/10))

      #----------Bóton Ranger Azul-------
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
      
      #--------------------------------------
      #Se guarda el tamaño original del botón
      self.x_red = self.ui.red_ranger.width()
      self.y_red = self.ui.red_ranger.height()

      #Se guarda el tamaño original del botón
      self.x_black = self.ui.black_ranger.width()
      self.y_black = self.ui.black_ranger.height()

      #Se guarda el tamaño original del botón
      self.x_pink = self.ui.pink_ranger.width()
      self.y_pink = self.ui.pink_ranger.height()

      #Se guarda el tamaño original del botón
      self.x_blue = self.ui.blue_ranger.width()
      self.y_blue = self.ui.blue_ranger.height()

      #Se guarda el tamaño original del botón
      self.x_yellow = self.ui.yellow_ranger.width()
      self.y_yellow = self.ui.yellow_ranger.height()

      self.positionV2 = self.ui.continue_btn.pos()
      self.positionV3 = self.ui.continue_btn_V3.pos()

      #------------Vista 3--------------
      #-----------Título-----------------
      t3x = self.ui.title_v3.width()*rel_x
      t3y = self.ui.title_v3.height()*rel_y

      self.ui.title_v3.resize(int(t3x),int(t3y))
      self.ui.title_v3.move(int(self.size_x/2 - t3x/2),int(self.size_y/9))

      fx = self.ui.photo_ranger.width()*rel_x
      fy = self.ui.photo_ranger.height()*rel_y

      self.ui.photo_ranger.resize(int(fx),int(fy))
      self.ui.photo_ranger.move(int(self.size_x/2 - fx/2),int(self.size_y/6))

      name_x = self.ui.name_v3.width()*rel_x
      name_y = self.ui.name_v3.height()*rel_y

      self.ui.name_v3.resize(int(name_x),int(name_y))
      self.ui.name_v3.move(int(self.size_x/2 - name_x/2),int(self.size_y/2 + name_y))

      #--------------Keyboard-----------
      self.ui.keyboard.move(int(self.size_x/2 - self.ui.keyboard.width()/2),int(self.size_y/2))

      #-------------Continuar----------- 
      c3x = self.ui.continue_btn_V3.width()*rel_x
      c3y = self.ui.continue_btn_V3.height()*rel_y

      self.ui.continue_btn_V3.resize(int(c3x),int(c3y))
      self.ui.continue_btn_V3.move(int(self.size_x/2 - c3x/2),int(y_init_btn))
      self.ui.continue_btn_V3.mousePressEvent = self.pressContinueV3
      self.ui.continue_btn_V3.mouseReleaseEvent = self.releaseContinueV3

      self.firstTime = False

      self.ui.show()

   def checking(self, color):
      for i in range(len(self.IsChecked)):
         if self.IsChecked[i][0] == color:
            self.IsChecked[i][1] = True
         else:
            self.IsChecked[i][1] = False

   def unlock(self):
      for i in range(len(self.IsChecked)):
         if self.IsChecked[i][1] == True:
            if self.IsChecked[i][0] == 'Red':
               self.releaseRed()
            elif self.IsChecked[i][0] == 'Blue':
               self.releaseBlue()
            elif self.IsChecked[i][0] == 'Pink':
               self.releasePink()
            elif self.IsChecked[i][0] == 'Black':
               self.releaseBlack()
            elif self.IsChecked[i][0] == 'Yellow':
               self.releaseYellow()

   def isSelected(self):
      k = False
      for i in range(len(self.IsChecked)):
         if self.IsChecked[i][1] == True:
            k = True
      return k

   def pressStartV1(self,event):
      START_BTN_PRESS = "src/img/ArtesPowerRangers/Pantalla 1/inicio_btn.png"

      #Imagen de press button
      startPress = QtGui.QPixmap(START_BTN_PRESS)

      #Se guarda el tamaño original del botón
      self.x_v1b1 = self.ui.inicio_btn.width()
      self.y_v1b1 = self.ui.inicio_btn.height()

      self.ui.inicio_btn.resize(int(self.x_v1b1*self.b),int(self.y_v1b1*self.b))

      position = self.ui.inicio_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.inicio_btn.move(x + ((1-self.b)*self.x_v1b1)/2,y + ((1-self.b)*self.y_v1b1)/2)
      self.ui.inicio_btn.setPixmap(startPress)

   def releaseStartV1(self,event):
      START_BTN_REL = "src/img/ArtesPowerRangers/Pantalla 1/inicio_btn.png"

      #Imagen de press button
      startRel = QtGui.QPixmap(START_BTN_REL)

      self.ui.inicio_btn.resize(self.x_v1b1,self.y_v1b1)

      position = self.ui.inicio_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.inicio_btn.move(x - ((1-self.b)*self.x_v1b1)/2,y - ((1-self.b)*self.y_v1b1)/2)
      self.ui.inicio_btn.setPixmap(startRel)

      #Acción Envía Vista 2
      self.View2()

   def View2(self):
      #Cambio de fondo vista 2
      palette  = QPalette()
      palette.setBrush(QPalette.Background,QBrush(QPixmap(self.VIEW_2).scaled(self.size_x,self.size_y)))
      self.ui.setPalette(palette)
      
      self.ui.setCurrentWidget(self.ui.View2)

   def pressRed(self, event):
      if self.firstTime == False:
         blue_btn = QPixmap(self.BLUE_BLOCK)
         self.ui.blue_ranger.setPixmap(blue_btn)
         black_btn = QPixmap(self.BLACK_BLOCK)
         self.ui.black_ranger.setPixmap(black_btn)
         pink_btn = QPixmap(self.PINK_BLOCK)
         self.ui.pink_ranger.setPixmap(pink_btn)
         yellow_btn = QPixmap(self.YELLOW_BLOCK)
         self.ui.yellow_ranger.setPixmap(yellow_btn)
         self.firstTime = True

      #Red esta activo
      if (self.IsChecked[0][1] == False):
         self.unlock()
         self.checking('Red')

         self.ui.red_ranger.resize(int(self.x_red*self.p),int(self.y_red*self.p))
         position = self.ui.red_ranger.pos()

         x = position.x()
         y = position.y()
         self.ui.red_ranger.move(x + ((1-self.p)*self.x_red)/2,y + ((1-self.p)*self.y_red)/2)
         red_btn = QPixmap(self.RED)
         self.ui.red_ranger.setPixmap(red_btn)
         self.ui.red_ranger.raise_()

   def pressBlack(self, event):
      if self.firstTime == False:
         blue_btn = QPixmap(self.BLUE_BLOCK)
         self.ui.blue_ranger.setPixmap(blue_btn)
         red_btn = QPixmap(self.RED_BLOCK)
         self.ui.red_ranger.setPixmap(red_btn)
         pink_btn = QPixmap(self.PINK_BLOCK)
         self.ui.pink_ranger.setPixmap(pink_btn)
         yellow_btn = QPixmap(self.YELLOW_BLOCK)
         self.ui.yellow_ranger.setPixmap(yellow_btn)
         self.firstTime = True

      #Black esta activo
      if (self.IsChecked[3][1] == False):
         self.unlock()
         self.checking('Black')

         self.ui.black_ranger.resize(int(self.x_black*self.p),int(self.y_black*self.p))
         position = self.ui.black_ranger.pos()

         x = position.x()
         y = position.y()
         self.ui.black_ranger.move(x + ((1-self.p)*self.x_black)/2,y + ((1-self.p)*self.y_black)/2)
         black_btn = QPixmap(self.BLACK)
         self.ui.black_ranger.setPixmap(black_btn)
         self.ui.black_ranger.raise_()

   def pressPink(self, event):
      if self.firstTime == False:
         blue_btn = QPixmap(self.BLUE_BLOCK)
         self.ui.blue_ranger.setPixmap(blue_btn)
         black_btn = QPixmap(self.BLACK_BLOCK)
         self.ui.black_ranger.setPixmap(black_btn)
         red_btn = QPixmap(self.RED_BLOCK)
         self.ui.red_ranger.setPixmap(red_btn)
         yellow_btn = QPixmap(self.YELLOW_BLOCK)
         self.ui.yellow_ranger.setPixmap(yellow_btn)
         self.firstTime = True

      #Pink esta activo
      if (self.IsChecked[1][1] == False):
         self.unlock()
         self.checking('Pink')

         self.ui.pink_ranger.resize(int(self.x_pink*self.p),int(self.y_pink*self.p))
         position = self.ui.pink_ranger.pos()

         x = position.x()
         y = position.y()
         self.ui.pink_ranger.move(x + ((1-self.p)*self.x_pink)/2,y + ((1-self.p)*self.y_pink)/2)
         pink_btn = QPixmap(self.PINK)
         self.ui.pink_ranger.setPixmap(pink_btn)
         self.ui.pink_ranger.raise_()

   def pressBlue(self, event):
      if self.firstTime == False:
         red_btn = QPixmap(self.RED_BLOCK)
         self.ui.red_ranger.setPixmap(red_btn)
         black_btn = QPixmap(self.BLACK_BLOCK)
         self.ui.black_ranger.setPixmap(black_btn)
         pink_btn = QPixmap(self.PINK_BLOCK)
         self.ui.pink_ranger.setPixmap(pink_btn)
         yellow_btn = QPixmap(self.YELLOW_BLOCK)
         self.ui.yellow_ranger.setPixmap(yellow_btn)
         self.firstTime = True

      #Blue esta activo
      if (self.IsChecked[2][1] == False):
         self.unlock()
         self.checking('Blue')

         self.ui.blue_ranger.resize(int(self.x_blue*self.p),int(self.y_blue*self.p))
         position = self.ui.blue_ranger.pos()

         x = position.x()
         y = position.y()
         self.ui.blue_ranger.move(x + ((1-self.p)*self.x_blue)/2,y + ((1-self.p)*self.y_blue)/2)
         blue_btn = QPixmap(self.BLUE)
         self.ui.blue_ranger.setPixmap(blue_btn)
         self.ui.blue_ranger.raise_()

   def pressYellow(self, event):
      if self.firstTime == False:
         blue_btn = QPixmap(self.BLUE_BLOCK)
         self.ui.blue_ranger.setPixmap(blue_btn)
         black_btn = QPixmap(self.BLACK_BLOCK)
         self.ui.black_ranger.setPixmap(black_btn)
         pink_btn = QPixmap(self.PINK_BLOCK)
         self.ui.pink_ranger.setPixmap(pink_btn)
         red_btn = QPixmap(self.RED_BLOCK)
         self.ui.red_ranger.setPixmap(red_btn)
         self.firstTime = True

      #Yellow esta activo
      if (self.IsChecked[4][1] == False):
         self.unlock()
         self.checking('Yellow')

         self.ui.yellow_ranger.resize(int(self.x_yellow*self.p),int(self.y_yellow*self.p))
         position = self.ui.yellow_ranger.pos()

         x = position.x()
         y = position.y()
         self.ui.yellow_ranger.move(x + ((1-self.p)*self.x_yellow)/2,y + ((1-self.p)*self.y_yellow)/2)
         yellow_btn = QPixmap(self.YELLOW)
         self.ui.yellow_ranger.setPixmap(yellow_btn)
         self.ui.yellow_ranger.raise_()

   def pressContinueV2(self,event):
      #Se guarda el tamaño original del botón
      self.x_cV2 = self.ui.continue_btn.width()
      self.y_cV2 = self.ui.continue_btn.height()

      self.ui.continue_btn.resize(int(self.x_cV2*self.b),int(self.y_cV2*self.b))

      position = self.ui.continue_btn.pos()

      x = position.x()
      y = position.y()
      self.ui.continue_btn.move(x + ((1-self.b)*self.x_cV2)/2,y + ((1-self.b)*self.y_cV2)/2)
      #self.ui.continue_btn.setPixmap(startPress)

   def pressContinueV3(self,event):
      #Se guarda el tamaño original del botón
      self.x_cV3 = self.ui.continue_btn_V3.width()
      self.y_cV3 = self.ui.continue_btn_V3.height()

      self.ui.continue_btn_V3.resize(int(self.x_cV3*self.b),int(self.y_cV3*self.b))

      position = self.ui.continue_btn_V3.pos()

      x = position.x()
      y = position.y()
      self.ui.continue_btn_V3.move(x + ((1-self.b)*self.x_cV3)/2,y + ((1-self.b)*self.y_cV3)/2)
      #self.ui.continue_btn.setPixmap(startPress)

   def releaseRed(self):
      self.ui.red_ranger.resize(self.x_red,self.y_red)
      position = self.ui.red_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.red_ranger.move(x - ((1-self.p)*self.x_red)/2,y - ((1-self.p)*self.y_red)/2)
      red_block = QPixmap(self.RED_BLOCK)
      self.ui.red_ranger.setPixmap(red_block)

   def releaseBlue(self):
      self.ui.blue_ranger.resize(self.x_blue,self.y_blue)
      position = self.ui.blue_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.blue_ranger.move(x - ((1-self.p)*self.x_blue)/2,y - ((1-self.p)*self.y_blue)/2)
      blue_block = QPixmap(self.BLUE_BLOCK)
      self.ui.blue_ranger.setPixmap(blue_block)

   def releasePink(self):
      self.ui.pink_ranger.resize(self.x_pink,self.y_pink)
      position = self.ui.pink_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.pink_ranger.move(x - ((1-self.p)*self.x_pink)/2,y - ((1-self.p)*self.y_pink)/2)
      pink_block = QPixmap(self.PINK_BLOCK)
      self.ui.pink_ranger.setPixmap(pink_block)

   def releaseYellow(self):
      self.ui.yellow_ranger.resize(self.x_yellow,self.y_yellow)
      position = self.ui.yellow_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.yellow_ranger.move(x - ((1-self.p)*self.x_yellow)/2,y - ((1-self.p)*self.y_yellow)/2)
      yellow_block = QPixmap(self.YELLOW_BLOCK)
      self.ui.yellow_ranger.setPixmap(yellow_block)   

   def releaseBlack(self):
      self.ui.black_ranger.resize(self.x_black,self.y_black)
      position = self.ui.black_ranger.pos()

      x = position.x()
      y = position.y()
      self.ui.black_ranger.move(x - ((1-self.p)*self.x_black)/2,y - ((1-self.p)*self.y_black)/2)
      black_block = QPixmap(self.BLACK_BLOCK)
      self.ui.black_ranger.setPixmap(black_block)

   def releaseContinueV2(self,event):
      self.ui.continue_btn.resize(self.x_cV2,self.y_cV2)

      x = self.positionV2.x()
      y = self.positionV2.y()
      self.ui.continue_btn.move(x,y)
      #self.ui.continue_btn.setPixmap(startRel)
      if self.isSelected() == True:
         self.View3()

   def releaseContinueV3(self,event):
      self.ui.continue_btn_V3.resize(self.x_cV3,self.y_cV3)

      x = self.positionV3.x()
      y = self.positionV3.y()
      self.ui.continue_btn_V3.move(x,y)
      #self.ui.continue_btn.setPixmap(startRel)
      if self.isSelected() == True:
         self.View4()

   def View3(self):
      #Acción Envía Vista 3
      #Cambio de fondo vista 4
      palette  = QPalette()
      palette.setBrush(QPalette.Background,QBrush(QPixmap(self.VIEW_3).scaled(self.size_x,self.size_y)))
      self.ui.setPalette(palette)
      
      self.ui.setCurrentWidget(self.ui.View3)

      for i in range(len(self.IsChecked)):
         if self.IsChecked[i][1] == True:
            face_ranger = QPixmap(self.URL_FACES[i])
            self.ui.photo_ranger.setPixmap(face_ranger)
            break

   def View4(self):
      self.ui.setCurrentWidget(self.ui.View4)
      print "Hola"

#Ejecución del programa
app = QtGui.QApplication(sys.argv)
MyWindow = MainWindow()
sys.exit(app.exec_())