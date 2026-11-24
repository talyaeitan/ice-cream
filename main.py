import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QVBoxLayout, QHBoxLayout
)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from about import AboutWindow


class IceCreamWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.revenues = []
        self.selected_file = ""

        self.about_window = AboutWindow()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ice Cream Revenue Analysis")
        self.setGeometry(150, 150, 700, 550)

        self.title_label = QLabel("Ice Cream Truck Revenue")
        self.title_label.setObjectName("title")

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.about_clicked)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.about_button)

        self.load_button = QPushButton("Load Data File")
        self.file_label = QLabel("No file selected")

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.load_button)
        file_layout.addWidget(self.file_label)
        file_layout.addStretch()

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        main_layout = QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addLayout(file_layout)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

        self.plot_graph()

    def plot_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([1, 2, 3], [10, 20, 30])
        ax.set_title("Temporary Graph")
        self.canvas.draw()

    def about_clicked(self):
        self.about_window.show()

    def closeEvent(self, event):
        self.about_window.close()


if __name__ == "__main__":
    app = QApplication()
    with open("style.qss") as f:
            app.setStyleSheet(f.read())
    window = IceCreamWindow()
    window.show()
    app.exec()