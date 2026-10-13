import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.wayland.textinput=false"

import sys
import numpy as np
import sounddevice as sd
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout,QHBoxLayout, QPushButton, QListWidget

samp_rate=48000


def playnote(midinote, duration):
    t=np.arange(int(samp_rate*duration))/samp_rate
    sd.play(0.2*np.sin(2*np.pi*(440* 2**((midinote - 69) / 12))*t), samplerate=samp_rate)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("esdaw")

        central = QWidget()
        main_layout=QVBoxLayout(central)

        main_layout.addStretch()

        keys_layout=QHBoxLayout()
        keys_layout.setSpacing(0)
        main_layout.addLayout(keys_layout)

        self.setCentralWidget(central)

        for i in range(60,72):
            key=QPushButton(str(i))
            key.setMinimumHeight(150)
            key.clicked.connect(lambda checked=False,n=i:self.on_click(n))
            keys_layout.addWidget(key)


    def on_click(self,n):
        playnote(n,1)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())
        

