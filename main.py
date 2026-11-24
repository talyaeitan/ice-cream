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
        self.load_button.clicked.connect(self.load_file_clicked)
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

    def load_file_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Ice Cream CSV", "", "CSV Files (*.csv)")
        if file_path == "":
            return

        self.selected_file = file_path
        self.file_label.setText(os.path.basename(file_path))

        self.temperatures = []
        self.revenues = []

        with open(self.selected_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines[1:]:
            clean_line = line.strip()
            if clean_line != "":
                parts = clean_line.split(",")
                temp = float(parts[0].strip())
                rev = float(parts[1].strip())
                self.temperatures.append(temp)
                self.revenues.append(rev)

        self.plot_graph()

    def plot_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if len(self.temperatures) == 0:
            ax.set_title("Load Ice Cream.csv to view data")
            self.canvas.draw()
            return

        ax.scatter(self.temperatures, self.revenues, s=1)

        ax.set_title("Ice Cream Revenue vs. Outside Temperature")
        ax.set_xlabel("Outside Temperature")
        ax.set_ylabel("Revenue ($)")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

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