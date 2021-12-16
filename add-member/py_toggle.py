from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PyToggle(QCheckBox):
    def __init__(
        self,
        parent,
        width = 60,
        # bg_color = "#777",
        bg_color = "#b8b8b9",
        # circle_color = "#DDD",
        circle_color = "#328DBD",
        active_color = "#328DBD",
        animation_curve = QEasingCurve.OutBounce,
        onStateChange = None,
    ):
        QCheckBox.__init__(self,parent=parent)

        # SET DEFAULT PARAMETERS
        self.setFixedSize(width,20)
        self.setCursor(Qt.PointingHandCursor)

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # CREATE ANIMATION
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        # CONNECT STATE CHANGED
        self.stateChanged.connect(self.start_transition)
        self.onStateChanged = onStateChange


    # CREATE NEW SET AND GET CHANGED
    @pyqtProperty(float) #Get
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self,pos):
        self._circle_position = pos
        self.update()

    # SET ANIMTAION TO MOVE
    def start_transition(self, value):
        self.animation.stop() #Stop animation if running
        if value:
            self.animation.setEndValue(self.width() -20)
        else:
            self.animation.setEndValue(3)
        
        # START ANIMATION
        self.animation.start()

        if self.onStateChanged != None:
            self.onStateChanged(self.isChecked())

    # SET NEW HIT AREA
    def hitButton(self, pos: QPoint):
        return  self.contentsRect().contains(pos)

    # DRAW NEW ITEMS
    def paintEvent(self, e):
        # SET PAINTER
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # SET AS NO PEN
        p.setPen(Qt.NoPen)

        # DRAW RECTANGLE
        rect = QRect(0,0,self.width(), self.height())

        # CHECK IF IS CHECKED
        if not self.isChecked():
            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(), self.height(),self.height()/2,self.height() /2) 
            p.setPen(QColor(self._circle_color))
            p.drawText(20,14,"Username")
            
            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,3,14,14)
        else:
            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(), self.height(),self.height()/2,self.height() /2)
            p.setPen(QColor(self._circle_color))
            p.drawText(32,14,"Id")
            
            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,3,14,14)

        p.end()