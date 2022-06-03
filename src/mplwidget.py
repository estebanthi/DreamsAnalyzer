# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
import numpy as np

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

    def draw(self):
        self.canvas.draw()

    def plot(self, x, y, color=None):
        self.canvas.ax.plot(x, y, c=color)
        self.canvas.draw()

    def pie(self, values, labels=None, legend=None, legend_labels=None, colors=None):
        if values != [0 for value in range(len(values))]:
            self.canvas.ax.pie(values, labels=labels, colors=colors, autopct=lambda p: '{:.0f}%'.format(p))
            if legend or legend_labels:
                self.canvas.ax.legend(loc='best', labels=legend_labels)

        self.canvas.draw()

    def bar(self, x, y, color=None, space=0, width=0.3, label=None, ylabel=None, xlabel=None, legend=None):

        x_axis = np.arange(len(x))
        self.canvas.ax.bar(x_axis + space, y, color=color, width=width, label=label)

        self.canvas.ax.set_xticks(x_axis, x)

        self.canvas.ax.set_ylabel(ylabel)
        self.canvas.ax.set_xlabel(xlabel)

        if legend:
            self.canvas.ax.legend()

        self.canvas.draw()

    def format(self, title, x, y, xticks_nb):
        xticks = self.canvas.ax.get_xticks()
        self.canvas.ax.set_xticks(xticks[::len(xticks) // xticks_nb])
        if len(xticks) <= 8:
            self.canvas.ax.set_xticks(xticks[::2])
        self.canvas.ax.margins(x=0)
        self.canvas.ax.set_title(title)
        self.draw()
