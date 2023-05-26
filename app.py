import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from PyQt5 import uic
import os
from reader import read_from_file


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.out_file = None
        self.directory = None
        uic.loadUi('ui/QVIO.ui', self)
        self.folder_button.clicked.connect(self.browse_folder)
        self.run_button.clicked.connect(self.run)
        self.file_button.clicked.connect(self.select_file)
        self.files = []

    def browse_folder(self):
        self.files.clear()  # На случай, если в списке уже есть элементы
        directory = QFileDialog.getExistingDirectory(self, "Select folder")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.files = os.listdir(directory).copy()
            self.directory = directory
            self.folder_label.setText(directory)

    def select_file(self):
        file = QFileDialog.getOpenFileName(self, 'Select file')
        if file:
            self.out_file = file[0]
            self.file_label.setText(file[0])

    def run(self):
        for file in self.files:
            res = read_from_file(f'{self.directory}/{file}')
            self.listWidget.addItem(f'{file} - {res}')
            if self.out_file:
                with open(self.out_file, 'a') as out_file:
                    out_file.write(f'{file} - {res}\n')


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()


if __name__ == '__main__':
    main()
