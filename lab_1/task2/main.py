import sys
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from constants import *


def load_from_txt(path: str)  -> str:
    """
    загрузка текста из файла

    :param path:
    :return text_from_txt:
    """
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()

    return text


def decode_text(text:str, alphabet: str, key: str) -> str:
    """
    Проходимся по тексту.
    Встречая очередной символ, ищем его позицию(pos) в alphabet,
    Если находим - меняем его на символ стоящей на той же позиции в key.

    :param text:
    :param alphabet:
    :param key:
    :return decoded_text:
    """
    rez = list(text)

    for i in range(len(rez)):
        pos = alphabet.find(rez[i])

        if pos != -1:
            rez[i] = key[pos]

    return ''.join(rez)


def text_stat(text: str) -> list[list[str | float]]:
    """
    Находим все уникальные символы в тексте.
    Проходясь по ним, считаем их частоту и добавляем в stat пары вида: [{символ}, {частота встречаемости}].
    Сортируем массив по частоте в порядке убывания.

    :param text:
    :return text_stat:
    """
    txt_len = len(text.replace('\n', ''))
    alphabet = set(list(text.replace('\n', '')))
    stat = []

    for simv in alphabet:
        stat.append([simv, text.count(simv)/txt_len])

    stat.sort(key= lambda x: x[1])
    stat.reverse()

    return stat

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Декодирование частотным анализом")
        self.setFixedWidth(600)

        # Лейблы (просто надписи)
        self.enc_label = QLabel("Кодированный текст:")
        self.alph_label = QLabel("Алфавит")
        self.key_label = QLabel("Ключ")
        self.result_label = QLabel("Результат:")

        # окна с текстом
        self.enc_txt = QTextEdit()
        self.enc_txt.setText(load_from_txt(TEXT_PATH))

        self.alphabet = QTextEdit()
        self.alphabet.setFixedHeight(35)

        self.key = QTextEdit()
        self.key.setFixedHeight(35)

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        # кнопка
        self.stat_button = QPushButton("Статистика текста")
        self.stat_button.clicked.connect(self.stat)
        self.decode_button = QPushButton("Декодировать по алфавиту и ключу")
        self.decode_button.clicked.connect(self.decode)

        # собираем все виджеты в окно приложения
        layout = QVBoxLayout()
        layout.addWidget(self.enc_label)
        layout.addWidget(self.enc_txt)
        layout.addWidget(self.alph_label)
        layout.addWidget(self.alphabet)
        layout.addWidget(self.key_label)
        layout.addWidget(self.key)

        layout.addWidget(self.stat_button)
        layout.addWidget(self.decode_button)

        layout.addWidget(self.result_label)
        layout.addWidget(self.result)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def stat(self) -> None:
        """
        Получаем статистику по данному тексту.
        Достаём алфавит частоты встречаемости данного текста (строка из всех уникальных символов в тексте в порадке убывания встречаемости)
        и глобальный алфавит частоты встречаемости

        выводим оба алфавита, а после выводим построчно символы и их частоты их обоих алфавитов

        :param self:
        :return None:
        """
        stat = text_stat(self.enc_txt.toPlainText())

        alphabet_txt = ''.join([x[0] for x in stat])
        global_alphabet = ''.join([x[0] for x in GLOBAL_STAT])

        txt = f'алфавит по встречаемости в тексте: {alphabet_txt}\nглобальный алфавит по встречаемость: {global_alphabet}'

        txt += '\n\nстатистика текста:\t\tглобальная статистика:\n'
        for i in range(len(stat)):
            txt += f'\'{stat[i][0]}\' -- {str(stat[i][1])}\t\t'
            txt += f'\'{GLOBAL_STAT[i][0]}\' -- {str(GLOBAL_STAT[i][1])}\n'

        self.result.setText(txt)

    def decode(self) -> None:
        """
        Проверяем, что длина алфавита (символы которые хотим поменять) совпадает с длиной ключа (на какие символы меняем).
        Если совпали - вызываем функцию декодирования (замены) и выводим результат, иначе сообщаем о неверных длинах

        :param self:
        :return None:
        """
        alphabet = self.alphabet.toPlainText()
        key = self.key.toPlainText()
        text = self.enc_txt.toPlainText()

        if len(alphabet) != len(key):
            self.result.setText('длины ключа и алфавита не совпадают!')
            return

        decoded_text = decode_text(text, alphabet, key)
        self.result.setText(decoded_text)


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()