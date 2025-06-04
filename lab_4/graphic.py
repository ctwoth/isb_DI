from matplotlib import pyplot as plt
import numpy as np


class Graphic:
    @staticmethod
    def draw_plot(data: list[(int, float)]):
        """
        drawing plot-graph with pyplot lib.

        :param data of x and y axes:
        :return:
        """
        fig = plt.figure(figsize=(30, 5))
        x = [x[0] for x in data]
        y = [x[1] for x in data]

        plt.ylabel('время')
        plt.xlabel('кол-во процессов')
        plt.title('зависимость времени от числа процессов')

        plt.plot(x,y, color='navy', linestyle='--', marker='x', linewidth=1, markersize=4)
        plt.show()

    @staticmethod
    def draw_bar(data: list[(int, float)]):
        """
        drawing bar-graph with pyplot lib.

        :param data of x and y axes:
        :return:
        """
        fig = plt.figure(figsize=(30, 5))
        x = [x[0] for x in data]
        y = [x[1] for x in data]

        plt.ylabel('время')
        plt.xlabel('кол-во процессов')
        plt.title('зависимость времени от числа процессов')

        plt.bar(x, y, color='blue', width=0.5)
        plt.show()
