import time
import numpy as np
from petinsert_main_ui import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui

from system import System
from sync import Sync
from backend import Backend
from os.path import expanduser
import logging

# create logger handler to route log data to the text browser on the gui
class QHandler(logging.Handler):

    def __init__(self, parent):
        logging.Handler.__init__(self)
        self.parent = parent
    def emit(self, record):
        # write to text browser in GUI
        self.parent.textBrowser.append(self.format(record))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('system.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class main(qtw.QMainWindow,Ui_MainWindow):
    

    def __init__(self,system_instance,*args, **kwargs):
        super().__init__(*args, **kwargs)


        # self.ui = Ui_MainWindow()
        self.setupUi(self)
        
        # create variables
        self.sys = system_instance
        self.backend = self.sys.backend
        self.sync = self.sys.sync
        print(f"self.sync:{self.sync}.")

        self.pushButton_ResetBackend.clicked.connect(self.get_status)
        self.pushButton_directory.clicked.connect(self.choose_directory)
        # self.pushButton_powerUp.clicked.connect(self.power_toggle_cb)
        # self.pushButton_startAquisition.clicked.connect(self.startAcquire)
        
        # self.pushButton_bias.clicked.connect(self.bias_toggle_cb)
        # self.pushButton_powerStatus.clicked.connect(self.get_set_power)
        # self.pushButton_current.clicked.connect(self.get_current)
        # self.pushButton_temperature.clicked.connect(self.get_current)
        
        
        # self.enum = tk.Button(self.root, text = "Enumerate", command = self.enumerate)
        # self.power_toggle = ToggleButton(self.root, "Power ON", "Power OFF", self.power_toggle_cb)
        # self.bias_toggle = ToggleButton(self.root, "Bias ON", "Bias OFF", self.bias_toggle_cb)
        # self.power_rd = tk.Button(self.root, text = "Read power state", command = self.get_set_power)
        # self.power_wr = tk.Button(self.root, text = "Set power state", command = lambda: self.get_set_power(True))
        # self.current = tk.Button(self.root, text = "Read current", command = self.get_current)

        # pack_args = {'fill': tk.X, 'expand': True, 'padx': 10, 'pady': 10}
        # self.refresh.pack(**pack_args)
        # self.enum.pack(**pack_args)
        # self.power_toggle.pack(**pack_args)
        # self.bias_toggle.pack(**pack_args)

        # Separator(self.root).pack(fill = tk.X, padx = 10, pady = 20)
        
        # self.power_rd.pack(**pack_args)
        # self.power_wr.pack(**pack_args)
        # self.current.pack(**pack_args)

    def choose_directory(self):
        
        input_dir = qtw.QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.lineEdit_directory.setText(input_dir)
        directory = self.lineEdit_directory.text()
        logger.debug(f"Acquisition data archive: {directory}.")
    
    # def startAcquire(self):
    #     print('acquisition started')

    def set_led(self,stateIn):
    	# this method is used to change the color of an indicator LED
    	ICON_RED_LED = ":/red/red-light-icon-8.png"
    	ICON_GREEN_LED = ":/green/green-led-on-md.png"
    	if stateIn:
           logger.debug('device on')
           self.label_statusLed.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
           logger.debug('device off')
           self.label_statusLed.setPixmap(QtGui.QPixmap(ICON_RED_LED))
    	

    def get_status(self):
        #ICON_RED_LED = ":/red/red-light-icon-8.png"
        #ICON_GREEN_LED = ":/green/green-led-on-md.png"

         # check system status
        sync_status = self.sync.get_status()
        self.set_led(sync_status)
        #if sync_status:
         #   self.label_statusLed.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        #else:
         #   self.label_statusLed.setPixmap(QtGui.QPixmap(ICON_RED_LED))

        
        # Directly check the status of each backend
        be_status = self.sys.get_status()
        be_status = zip(self.backend, be_status)
        #[b.status.config(bg = 'green' if s else 'red') for b,s in be_status]
        [print(f'{s}{b}') for b,s in be_status]
        [set_led(s) for b,s in be_status]
         # self.label_statusLed.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))

         # # Check the RX status for each port on each backend to infer the frontend state
         # sys_rx = self.sys.get_rx_status()
         # for be, be_rx in zip(self.backend, sys_rx):
         #     for fe, err in zip(be.frontend, be_rx):
         #         fe.status.config(bg = 'red' if err else 'green')

    # def power_toggle_cb(self, turn_on = False):
    #     if turn_on:
    #         for i in range(1,5):
    #             pwr = [True]*i + [False]*(4-i)
    #             self.sys.get_set_power(True, [pwr]*4)
    #             #popup_status.config(text = f'Module: {i}')
    #             popup_status.config(text = 'f')
    #             time.sleep(1)
    #             self.update_pwr_states()
    #     else:
    #         self.sys.get_set_power(True, [[False]*4]*4)

    #     self.update_pwr_states()
    #     self.get_status()


    # def get_set_power(self, update = False):
    #     states = []
    #     for b in self.backend:
    #         states.append([v.get() for v in b.m_pow_var])
    #     states = self.sys.get_set_power(update, states)
    #     print(states)
    #     return states

    # def update_pwr_states(self):
    #     pwr_states = self.get_set_power()
    #     for b,s_all in zip(self.backend, pwr_states):
    #         [v.set(s) for v,s in zip(b.m_pow_var, s_all)]

    # def enumerate(self):
    #     sys_idx = self.sys.get_physical_idx()
    #     for be, be_idx in zip(self.backend, sys_idx):
    #         for indicator, phys_idx in zip(be.m_pow, be_idx):
    #             indicator.config(text = phys_idx)

    # def get_current(self):
    #     print(self.sys.get_current())

    

    # def bias_toggle_cb(self, turn_on = False):
    #     if turn_on:
    #         vals = np.linspace(0.0, 29.5, 5)
    #         for v in vals:
    #             self.sys.set_bias(v)
    #             time.sleep(1)


    #     else:
    #         self.sys.set_bias(0.0)



if __name__=='__main__':
    


    sys = System()
    app = qtw.QApplication([])
    mainWindow = main(sys)

    Qhandler = QHandler(mainWindow)
    Qhandler.setFormatter(formatter)
    logger.addHandler(Qhandler)
    mainWindow.show()

    app.exec_()


