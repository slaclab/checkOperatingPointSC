import numpy as np
from pydm import Display
from PyQt5 import QtGui, QtCore, QtWidgets 
#from PyQt5.QtGui import QPainter, QColor, QBrush, QPen 
#from PyQt5.QtCore import Qt, QObject
#import epics
#from epics import caget, caput
#from PyQt5.QtWidgets import (QWidgetItem, QCheckBox, QPushButton, QLineEdit,
#                             QGroupBox, QVBoxLayout, QHBoxLayout, QMessageBox, QWidget,
#                             QLabel, QFrame, QComboBox, QRadioButton, QGridLayout,
#                             QColorDialog)
#from pydm.widgets import PyDMDrawingRectangle, PyDMLabel, PyDMTemplateRepeater
#from pydm.widgets.drawing import PyDMDrawingPolygon
#from functools import partial
from epics import PV
#from frontEnd_constants import shapeParameterDict
#from cavityWidget import CavityWidget
from scipy import constants
#from lcls-tools import bc

class checkOperatingPointSC(Display):

    def __init__(self, parent = None, args = None): #, ui_filename='checkOperatingPointSC.ui'):
        super(checkOperatingPointSC, self).__init__(parent=parent,args=args)
        
        # Initialize values (?)
        self.nC              = 0
        self.frequency       = 1.3*np.power(10,9) # cavity frequency in GHz
        self.lambda_chicane  = constants.c / self.frequency
        self.BC1b_R56_target = None
        self.BC1b_E0_target  = None
        self.BC1b_xpos       = None
        #self.
        #self.
        self.nicolesPV = PV('ACCL:L2B:1230:GDES')
        self.nicolesPV.add_callback(self.nicolesCallback)

    def ui_filename(self):
        return 'checkOperatingPointSC.ui'
                        
    def nicolesCallback(self, value, **kw):
        #do math
        # nicolesLabel should match pydm label in ui file (object name)
        self.ui.peakCurrent1.setText(str(value/20.0))


        ''' '''

        gamma = energy / constants.electron_mass


        return BC_dict


    def calcBC1bOffset(self, PV):
        ''' '''
        self.BC1boffset = BC_adjust(self.BC1b_R56_target, self.BC1b_E0_target)
        return

    def calcBC1bActual(self, PV):
        ''' '''
        return

    def getBC1b_E0_Actual(self, PV):
        ''' '''
        #[...] = BC_adjust(self.BC1b_R56_target, self.BC1b_E0_target)
        theta = np.arctan(self.xpos / l) 
        if theta != 0 :
            self.BC1b_E0_actual = BACT / np.sin(theta) * constants.c #np.power(10, -10)
        return

    def calcInjectorPhase_Actual(self, PV):
        ''' '''
        return

    def calcBC_IPK_Actual():
        ''' ''' 
        return

    def getBunchLenght():
        ''' '''
        return

    def getBmagEmittance():
        ''' ''' 
        return

    def test():
        ''' '''
        return
intelclass = checkOperatingPointSC

