from clase1 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
import sys

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5,height=4, dpi=100):
        self.fig=Figure(figsize=(width,height), dpi=dpi)
        self.axes=self.fig.add_subplot(111)
        self.axes.clear()
        

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)


class Functionmain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.playing=False
        self.button=self.ui.pushButton
        self.button.clicked.connect(self.plot_start)
        self.input=self.ui.lineEdit
        self.input.setText("12")
        self.slider=self.ui.horizontalSlider
        self.slider.setValue(int(self.input.text()))
        self.input.returnPressed.connect(self.setvalueslider)
        self.slider.valueChanged.connect(self.setvalueinput)
        self.vbox=QVBoxLayout()
        self.canvas=MplCanvas(self,width=5,height=4,dpi=100)
        self.vbox.addWidget(self.canvas)
        self.widget=self.ui.widget
        self.widget.setLayout(self.vbox)
        self.x=np.linspace(0 ,5*np.pi, 400)
        self.p=0.0
        self.y=np.sin(self.x + self.p)
        self.line,  = self.canvas.axes.plot(self.x, self.y, lw=2, animated=True)
        
        
        
        self.show()

    def update_line(self,i):
        a=self.slider.value()
        self.p += 0.1
        y = a/100*np.sin(self.x + self.p)
        self.line.set_ydata(y)
        return [self.line]
    
    def plot_start(self):
        if self.playing:
            pass
        else:
            self.playing=True
            self.ani=animation.FuncAnimation(self.canvas.figure,
            self.update_line,
            blit=True,
            interval=25 )

        






       

    def setvalueslider(self):
        self.slider.setValue(int(self.input.text()))
    def setvalueinput(self):
        self.input.setText(str(self.slider.value()))





app = QApplication(sys.argv)
mywindows=Functionmain()
mywindows.show()
sys.exit(app.exec_())

