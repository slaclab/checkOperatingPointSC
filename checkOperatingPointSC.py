from pydm import Display
from PyQt5 import QtGui, QtCore, QtWidgets 
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen 
from PyQt5.QtCore import Qt, QObject
import epics
from epics import caget, caput
from PyQt5.QtWidgets import (QWidgetItem, QCheckBox, QPushButton, QLineEdit,
                             QGroupBox, QVBoxLayout, QHBoxLayout, QMessageBox, QWidget,
                             QLabel, QFrame, QComboBox, QRadioButton, QGridLayout,
                             QColorDialog)
from pydm.widgets import PyDMDrawingRectangle, PyDMLabel, PyDMTemplateRepeater
from pydm.widgets.drawing import PyDMDrawingPolygon
from functools import partial
from epics import PV
from frontEnd_constants import shapeParameterDict
from cavityWidget import CavityWidget
#from lcls_tools import constants

class checkOperatingPointSC(Display):

    def ui_filename(self):
        return 'checkOperatingPointSC.ui'
        
    def __init__(self, parent = None, args = None):
        super(checkOperatingPointSC, self).__init__(parent=parent,args=args)
        
        # Initialize values (?)
        self.nC              = 0
        self.BC1b_R56_target = None
        self.BC1b_E0_target  = None
        self.BC1b_xpos       = None
        self.
        self.

    def conv2nC(self, PV):
        '''Convert ICT voltage to nC'''
        self.nC = voltage * constants.echarge * np.power(10, -9)  
        return

    def calcBC1bOffset(self, PV):
        ''' '''
        self.BC1boffset = BC_adjust(self.BC1b_R56_target, self.BC1b_E0_target)
        return

    def calcBC1bActual(self, PV):
        ''' '''
        return

    def getBC1b_E0_Actual(self, PV):
        ''' '''
        [...] = BC_adjust(self.BC1b_R56_target, self.BC1b_E0_target)
        theta = np.arctan(self.xpos / l) 
        if theta != 0 :
            self.BC1b_E0_actual = BACT / np.sin(theta) * constants.c #np.power(10, -10)
        return
