import os
import sys
import time
import multiprocessing as mp

from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit

from file_utils import FileUtils
from parser import Parser
from card_manager import CardManager
from graphic import Graphic


def check_sets(sets: dict) -> None:
    """
    check what sets got all necessary params and files
    :param sets{dict}:
    :return None:
    """
    if not os.path.isfile(sets["save_path"]):
        raise ValueError("Wrong path to initial file")

    if len(sets["last_numbers"]) != 4:
        raise ValueError("not 4 numbers")

    if len(sets["hash"]) < 10:
        raise ValueError("Hash doesn't look correct...")

    if len(sets["bins"])  == 0:
        raise ValueError("Empty bank BINs")


class MainWindow(QMainWindow):
    def __init__(self, sets_path: str):
        """
        app initialization.
        
        :param sets_path: 
        """
        super().__init__()
        self.sets = FileUtils.load_from_json(sets_path)
        check_sets(self.sets)

        self.setWindowTitle("Карточный дешифратор")
        self.setFixedWidth(600)

        # Лейблы (просто надписи)
        self.enc_params_label = QLabel("Данные дешифровки:")
        self.card_num_label = QLabel("Номер карточки:")
        self.result_label = QLabel("Результат:")

        # окна с текстом
        self.enc_params = QTextEdit()
        self.enc_params.setText(FileUtils.load_from_txt(sets_path))
        self.enc_params.setReadOnly(True)

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        self.card_num_edit = QLineEdit()

        # кнопки
        self.decode_button = QPushButton("найти номер карты")
        self.decode_button.clicked.connect(self.decode)
        self.stat_decode_button = QPushButton("статистика декодирования")
        self.stat_decode_button.clicked.connect(self.stat_decode)
        self.check_button = QPushButton("проверить карту на корректность")
        self.check_button.clicked.connect(self.card_num_check)

        # собираем все виджеты в окно приложения
        layout = QVBoxLayout()
        layout.addWidget(self.enc_params_label)
        layout.addWidget(self.enc_params)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result)
        layout.addWidget(self.decode_button)
        layout.addWidget(self.stat_decode_button)
        layout.addWidget(self.card_num_label)
        layout.addWidget(self.card_num_edit)
        layout.addWidget(self.check_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def decode(self) -> None:
        """
        trying find card number using info from settings.json.
        show result and if we find number -> save int into txt file.

        :return None:
        """
        number = CardManager.find_card_from_hash(self.sets['bins'], self.sets['last_numbers'], self.sets['hash'])

        if number:
            self.result.setText(number)
            FileUtils.load_in_txt(number, self.sets['save_path'])
        else:
            self.result.setText("Не удалось найти карту")


    def stat_decode(self)-> None:
        """
        starting decode procedure with different thread number.
        measuring the time and drawing two types of graph.

        :return None:
        """
        statistic = []

        for cores in range(1, int(1.5*mp.cpu_count())):
            start = time.time()
            CardManager.find_card_from_hash(self.sets['bins'], self.sets['last_numbers'], self.sets['hash'], cores)
            work_time = time.time() - start

            statistic.append((cores, work_time))

        Graphic.draw_plot(statistic)
        Graphic.draw_bar(statistic)


    def card_num_check(self)->None:
        """
        take string in field card_num_edit, check what it
        actualy card number and testing it nuber with luhn test

        :return None:
        """
        card_num = self.card_num_edit.text()

        if not card_num.isdigit() : #or len(card_num) != 16
            self.result.setText("Некорректный номер карты")
            return

        if CardManager.alg_luhn(card_num):
            self.result.setText("Карта валидна")
        else:
            self.result.setText("Карта невалидна")


def main() -> None:
    try:
        args = Parser.parse()

        match args.task:
            case 'tests':
                os.system('python unit_tests.py -v')

            case 'gui':
                app = QApplication(sys.argv)
                window = MainWindow(args.settings)
                window.show()
                sys.exit(app.exec())


            case _:
                raise ValueError("incorrect program task")

    except Exception as error:
        print("Error!\n\t", error)


if __name__ == '__main__':
    main()
