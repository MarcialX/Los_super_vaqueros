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
      self.VIEW_5 = "src/img/ArtesPowerRangers/Pantalla 5/Back5.jpg"

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
      self.ui.name_v3.move(int(self.size_x/2 - name_x/2),int(self.size_y/2 + 2*name_y))

      #--------------Keyboard-----------
      self.promptTex = ""
      self.ui.keyboard.move(int(self.size_x/2 - self.ui.keyboard.width()/2),int(self.size_y/2))
      self.ui.key_a.mouseReleaseEvent = self.key_a
      self.ui.key_b.mouseReleaseEvent = self.key_b
      self.ui.key_c.mouseReleaseEvent = self.key_c
      self.ui.key_d.mouseReleaseEvent = self.key_d
      self.ui.key_e.mouseReleaseEvent = self.key_e
      self.ui.key_f.mouseReleaseEvent = self.key_f
      self.ui.key_g.mouseReleaseEvent = self.key_g
      self.ui.key_h.mouseReleaseEvent = self.key_h
      self.ui.key_i.mouseReleaseEvent = self.key_i
      self.ui.key_j.mouseReleaseEvent = self.key_j
      self.ui.key_k.mouseReleaseEvent = self.key_k
      self.ui.key_l.mouseReleaseEvent = self.key_l
      self.ui.key_m.mouseReleaseEvent = self.key_m
      self.ui.key_n.mouseReleaseEvent = self.key_n
      self.ui.key_o.mouseReleaseEvent = self.key_o
      self.ui.key_p.mouseReleaseEvent = self.key_p
      self.ui.key_q.mouseReleaseEvent = self.key_q
      self.ui.key_r.mouseReleaseEvent = self.key_r
      self.ui.key_s.mouseReleaseEvent = self.key_s
      self.ui.key_t.mouseReleaseEvent = self.key_t
      self.ui.key_u.mouseReleaseEvent = self.key_u
      self.ui.key_v.mouseReleaseEvent = self.key_v
      self.ui.key_w.mouseReleaseEvent = self.key_w
      self.ui.key_x.mouseReleaseEvent = self.key_x
      self.ui.key_y.mouseReleaseEvent = self.key_y
      self.ui.key_z.mouseReleaseEvent = self.key_z

      self.ui.key_1.mouseReleaseEvent = self.key_1
      self.ui.key_2.mouseReleaseEvent = self.key_2
      self.ui.key_3.mouseReleaseEvent = self.key_3
      self.ui.key_4.mouseReleaseEvent = self.key_4
      self.ui.key_5.mouseReleaseEvent = self.key_5
      self.ui.key_6.mouseReleaseEvent = self.key_6
      self.ui.key_7.mouseReleaseEvent = self.key_7
      self.ui.key_8.mouseReleaseEvent = self.key_8
      self.ui.key_9.mouseReleaseEvent = self.key_9
      self.ui.key_0.mouseReleaseEvent = self.key_0

      self.ui.key_punto.mouseReleaseEvent = self.key_punto
      self.ui.key_puntocoma.mouseReleaseEvent = self.key_puntocoma
      self.ui.key_coma.mouseReleaseEvent = self.key_coma
      self.ui.key_space.mouseReleaseEvent = self.key_space
      self.ui.key_money.mouseReleaseEvent = self.key_money
      self.ui.key_cs.mouseReleaseEvent = self.key_cs
      self.ui.key_cc.mouseReleaseEvent = self.key_cc
      self.ui.key_guionbajo.mouseReleaseEvent = self.key_guion_bajo
      self.ui.key_guion.mouseReleaseEvent = self.key_guion_alto
      self.ui.key_admirar.mouseReleaseEvent = self.key_admiracion
      self.ui.key_porcentage.mouseReleaseEvent = self.key_porcentaje
      self.ui.key_arroba.mouseReleaseEvent = self.key_arroba
      self.ui.key_number.mouseReleaseEvent = self.key_number

      self.ui.key_delete.mouseReleaseEvent = self.key_delete

      #-------------Continuar----------- 
      c3x = self.ui.continue_btn_V3.width()*rel_x
      c3y = self.ui.continue_btn_V3.height()*rel_y

      self.ui.continue_btn_V3.resize(int(c3x),int(c3y))
      self.ui.continue_btn_V3.move(int(self.size_x/2 - c3x/2),int(y_init_btn))
      self.ui.continue_btn_V3.mousePressEvent = self.pressContinueV3
      self.ui.continue_btn_V3.mouseReleaseEvent = self.releaseContinueV3

      self.firstTime = False

      #--------------Vista 5---------------
      #------------Muestra GIF-------------
      altura_gif = 350*rel_y
      gif_x = self.ui.the_gif.width()*rel_x
      gif_y = self.ui.the_gif.height()*rel_y

      self.ui.the_gif.resize(int(gif_x),int(gif_y))
      self.ui.the_gif.move(int(self.size_x/2 - gif_x/2),int(altura_gif))
      #--------------Marco-----------------
      altura_mark = 1250*rel_y
      mark_x = self.ui.cuadro.width()*rel_x
      mark_y = self.ui.cuadro.height()*rel_y

      self.ui.cuadro.resize(int(mark_x),int(mark_y))
      self.ui.cuadro.move(int(self.size_x/2 - mark_x/2),int(altura_mark))
      #-----------Atrás botón--------------
      altura_atras = 1350*rel_y
      base_atras = 130*rel_x

      atras_x = self.ui.atras.width()*rel_x
      atras_y = self.ui.atras.height()*rel_y

      self.ui.atras.resize(int(atras_x),int(atras_y))
      self.ui.atras.move(int(base_atras),int(altura_atras))
      self.ui.atras.mousePressEvent = self.pressAtrasV5
      self.ui.atras.mouseReleaseEvent = self.releaseAtrasV5
      #-----------Continuar botón--------------
      base_con = 575*rel_x

      con_x = self.ui.continuar_V5.width()*rel_x
      con_y = self.ui.continuar_V5.height()*rel_y

      self.ui.continuar_V5.resize(int(con_x),int(con_y))
      self.ui.continuar_V5.move(int(base_con),int(altura_atras))
      self.ui.continuar_V5.mousePressEvent = self.pressContinueV5
      self.ui.continuar_V5.mouseReleaseEvent = self.releaseContinueV5

      #Posiciones de los botones continuar
      self.positionV2 = self.ui.continue_btn.pos()
      self.positionV3 = self.ui.continue_btn_V3.pos()
      self.positionV5 = self.ui.continuar_V5.pos()
      self.positionAtras = self.ui.atras.pos()

      self.ui.show()

   #-----------KEYBOARD-------------
   def writePrompt(self):
      self.ui.prompt.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
      self.ui.prompt.setText(self.promptTex)

   def key_delete(self,event):
      self.promptTex = self.promptTex[:-1]
      self.writePrompt()

   def key_a(self,event):
      self.promptTex = self.promptTex + "A"
      self.writePrompt()

   def key_b(self,event):
      self.promptTex = self.promptTex + "B"
      self.writePrompt()

   def key_c(self,event):
      self.promptTex = self.promptTex + "C"
      self.writePrompt()

   def key_d(self,event):
      self.promptTex = self.promptTex + "D"
      self.writePrompt()

   def key_e(self,event):
      self.promptTex = self.promptTex + "E"
      self.writePrompt()

   def key_f(self,event):
      self.promptTex = self.promptTex + "F"
      self.writePrompt()

   def key_g(self,event):
      self.promptTex = self.promptTex + "G"
      self.writePrompt()

   def key_h(self,event):
      self.promptTex = self.promptTex + "H"
      self.writePrompt()

   def key_i(self,event):
      self.promptTex = self.promptTex + "I"
      self.writePrompt()

   def key_j(self,event):
      self.promptTex = self.promptTex + "J"
      self.writePrompt()

   def key_k(self,event):
      self.promptTex = self.promptTex + "K"
      self.writePrompt()

   def key_l(self,event):
      self.promptTex = self.promptTex + "L"
      self.writePrompt()

   def key_m(self,event):
      self.promptTex = self.promptTex + "M"
      self.writePrompt()

   def key_n(self,event):
      self.promptTex = self.promptTex + "N"
      self.writePrompt()

   def key_o(self,event):
      self.promptTex = self.promptTex + "O"
      self.writePrompt()

   def key_p(self,event):
      self.promptTex = self.promptTex + "P"
      self.writePrompt()

   def key_q(self,event):
      self.promptTex = self.promptTex + "Q"
      self.writePrompt()

   def key_r(self,event):
      self.promptTex = self.promptTex + "R"
      self.writePrompt()

   def key_s(self,event):
      self.promptTex = self.promptTex + "S"
      self.writePrompt()

   def key_t(self,event):
      self.promptTex = self.promptTex + "T"
      self.writePrompt()

   def key_u(self,event):
      self.promptTex = self.promptTex + "U"
      self.writePrompt()

   def key_v(self,event):
      self.promptTex = self.promptTex + "V"
      self.writePrompt()

   def key_w(self,event):
      self.promptTex = self.promptTex + "W"
      self.writePrompt()

   def key_x(self,event):
      self.promptTex = self.promptTex + "X"
      self.writePrompt()

   def key_y(self,event):
      self.promptTex = self.promptTex + "Y"
      self.writePrompt()

   def key_z(self,event):
      self.promptTex = self.promptTex + "Z"
      self.writePrompt()

   def key_1(self,event):
      self.promptTex = self.promptTex + "1"
      self.writePrompt()

   def key_2(self,event):
      self.promptTex = self.promptTex + "2"
      self.writePrompt()

   def key_3(self,event):
      self.promptTex = self.promptTex + "3"
      self.writePrompt()

   def key_4(self,event):
      self.promptTex = self.promptTex + "4"
      self.writePrompt()

   def key_5(self,event):
      self.promptTex = self.promptTex + "5"
      self.writePrompt()

   def key_6(self,event):
      self.promptTex = self.promptTex + "6"
      self.writePrompt()

   def key_7(self,event):
      self.promptTex = self.promptTex + "7"
      self.writePrompt()

   def key_8(self,event):
      self.promptTex = self.promptTex + "8"
      self.writePrompt()

   def key_9(self,event):
      self.promptTex = self.promptTex + "9"
      self.writePrompt()

   def key_0(self,event):
      self.promptTex = self.promptTex + "0"
      self.writePrompt()

   def key_punto(self,event):
      self.promptTex = self.promptTex + "."
      self.writePrompt()

   def key_arroba(self,event):
      self.promptTex = self.promptTex + "@"
      self.writePrompt()

   def key_puntocoma(self,event):
      self.promptTex = self.promptTex + ";"
      self.writePrompt()

   def key_coma(self,event):
      self.promptTex = self.promptTex + ","
      self.writePrompt()

   def key_guion_bajo(self,event):
      self.promptTex = self.promptTex + "_"
      self.writePrompt()

   def key_guion_alto(self,event):
      self.promptTex = self.promptTex + "-"
      self.writePrompt()

   def key_porcentaje(self,event):
      self.promptTex = self.promptTex + "%"
      self.writePrompt()

   def key_money(self,event):
      self.promptTex = self.promptTex + "$"
      self.writePrompt()

   def key_admiracion(self,event):
      self.promptTex = self.promptTex + "!"
      self.writePrompt()

   def key_cs(self,event):
      self.promptTex = self.promptTex + "["
      self.writePrompt()

   def key_cc(self,event):
      self.promptTex = self.promptTex + "]"
      self.writePrompt()

   def key_space(self,event):
      self.promptTex = self.promptTex + " "
      self.writePrompt()

   def key_number(self,event):
      self.promptTex = self.promptTex + "#"
      self.writePrompt()

   #--------------------------------- 

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
      if self.promptTex != "":
         self.View4()

   def pressContinueV5(self,event):
      #Se guarda el tamaño original del botón
      self.x_cV5 = self.ui.continuar_V5.width()
      self.y_cV5 = self.ui.continuar_V5.height()

      self.ui.continuar_V5.resize(int(self.x_cV5*self.b),int(self.y_cV5*self.b))

      position = self.ui.continuar_V5.pos()

      x = position.x()
      y = position.y()
      self.ui.continuar_V5.move(x + ((1-self.b)*self.x_cV5)/2,y + ((1-self.b)*self.y_cV5)/2)
      #self.ui.continue_btn.setPixmap(startPress)

   def releaseContinueV5(self,event):
      self.ui.continuar_V5.resize(self.x_cV5,self.y_cV5)

      x = self.positionV5.x()
      y = self.positionV5.y()
      self.ui.continuar_V5.move(x,y)
      self.ui.setCurrentWidget(self.ui.View6)
      #self.ui.continue_btn.setPixmap(startRel)

   def pressAtrasV5(self,event):
      #Se guarda el tamaño original del botón
      self.x_aV5 = self.ui.atras.width()
      self.y_aV5 = self.ui.atras.height()

      self.ui.atras.resize(int(self.x_aV5*self.b),int(self.y_aV5*self.b))

      position = self.ui.atras.pos()

      x = position.x()
      y = position.y()
      self.ui.atras.move(x + ((1-self.b)*self.x_aV5)/2,y + ((1-self.b)*self.y_aV5)/2)
      #self.ui.continue_btn.setPixmap(startPress)

   def releaseAtrasV5(self,event):
      self.ui.atras.resize(self.x_aV5,self.y_aV5)

      x = self.positionAtras.x()
      y = self.positionAtras.y()
      self.ui.atras.move(x,y)
      self.ui.setCurrentWidget(self.ui.View4)
      #self.ui.continue_btn.setPixmap(startRel)

   def View3(self):
      #Nueva vista 3
      palette  = QPalette()
      palette.setBrush(QPalette.Background,QBrush(QPixmap(self.VIEW_3).scaled(self.size_x,self.size_y)))
      self.ui.setPalette(palette)

      #Acción Envía Vista 3
      self.ui.setCurrentWidget(self.ui.View3)

      for i in range(len(self.IsChecked)):
         if self.IsChecked[i][1] == True:
            face_ranger = QPixmap(self.URL_FACES[i])
            self.ui.photo_ranger.setPixmap(face_ranger)
            break

   def View4(self):
      #Pasamos a vista 4
      #Aquí va lo del GIF
      self.ui.setCurrentWidget(self.ui.View4)
      print "Tomamos la fotito... y pasamos a la otra vista"
      self.View5()

   def View5(self):
      #Pasamos vista 5
      #----------------------
      #Aqui se pone el gif :)
      #----------------------

      #Te gusta la foto?
      self.ui.setCurrentWidget(self.ui.View5)

#Ejecución del programa
app = QtGui.QApplication(sys.argv)
MyWindow = MainWindow()
sys.exit(app.exec_())