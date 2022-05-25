# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')


# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def setTitle(self, title):
        self.canvas.ax.set_title(title)

    def clear(self):
        self.canvas.ax.clear()

    def plot(self, x, y, color=None):
        self.canvas.ax.plot(x, y, c=color)

    def pie(self, values, labels=None, legend=None, legend_labels=None, colors=None):
        self.canvas.ax.pie(values, labels=labels, colors=colors)
        if legend or legend_labels:
            self.canvas.ax.legend(loc='best', labels=legend_labels)

    def clear(self):
        self.canvas.ax.clear()
