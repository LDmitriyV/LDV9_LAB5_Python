#!/usr/bin/env python3
# coding=utf-8


#Если во втором столбце стоят две единицы, то уменьшить максимальный элемент первой строки в два раза, а
#все единицы в таблице заменить нулями

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')



            data = file.readlines()
            # выводим считанные данные на экран
            # for lines in data:
            #     self.plainTextEdit.appendPlainText(lines.strip('\n'))


            global list_of_numbers
            list_of_numbers = []

            # \b -- ищет границы слов
            # [0-9] -- описывает что ищем
            # + -- говорит, что искать нужно минимум от 1 символа
            for lines in data:
                lineSplit = lines.split()
                list_of_numbers.append(lineSplit)
            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:5}".format(str(i))
                    self.plainTextEdit.insertPlainText(new_str)
                self.plainTextEdit.appendPlainText("")

    def process_data(self):
        if validation_of_data():
            max_num = find_max()
            find_one = find_one_of_second_column()

            # -*- выполнение задания -*-
            if find_one == 2:

                reducing_max_num_of_double(max_num)
                num_change()

                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n')

                # выводим список на экран
                for lists in list_of_numbers:
                    for i in lists:
                        new_str = "{:5}".format(str(i))
                        self.plainTextEdit.insertPlainText(new_str)
                    self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    "Во втором столбце отсутсвуют две единицы")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:5}".format(str(i))
                    file.write(new_str)
                file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_max():
    """
    находим максимальное число в списке
    :return: максимальное число
    """
    max_num = float('-inf')
    for lists in list_of_numbers:
        for i in lists:
            if max_num < int(i):
                max_num = int(i)
    return max_num


def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """

    lenth_list = 0
    for lists in list_of_numbers:
        lenth_list += len(lists)
    if lenth_list == 30:
        for lists in list_of_numbers:
            for i in lists:
                try:
                    int(i)
                except Exception:
                    return False
        return True
    else:
        return False


def reducing_max_num_of_double(max_num):
    """
    уменьшение максимального числа в два раза
    :param max_num: максимальное число
    :return: pass
    """

    for j in range(len(list_of_numbers[0])):
        if int(list_of_numbers[0][j]) == max_num:
            list_of_numbers[0][j] = str(max_num / 2)
            break
    pass


def find_one_of_second_column():
    """
    находим единицу во втором столбце
    :return: число едениц
    """
    one_count =0
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers[i])):
        # перебираем каждую строку
            if j == 1:
                if int(list_of_numbers[i][j]) == 1:  # если второй элемент строки равен 1
                    one_count += 1
    return one_count

def num_change():

    """
    замена 1 на 0
    """

    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers[i])):
            if float(list_of_numbers[i][j]) == 1:
                list_of_numbers[i][j] = str(0)



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
