import matplotlib.pyplot as plt
import numpy as np
import plotly as ply
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from matplotlib import pyplot as plt
import argparse
import sys
import logging


def word_count():
    logging.basicConfig(level=logging.DEBUG, filename='myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
    try:
        logging.debug("Okay")
    except OSError as e:
        logging.error("Error!")

def help():
    print("----ПРОГРАМА ПОСТРОЕНИЯ ГРАФИКА ФУНКЦИИ!----\n")
    print("Usage:\n"
          "pars.py [integer] <options>\n")
    print("positional arguments:\n"
          "integer            количество точек на графике(натуральное число)\n")
    print("optional arguments:\n"
          "\n-h, --help       показать это справочное сообщение и выйти"
          "\n--task_2         построение веб-графика функции"
          "\n--task_1         построение графика функции в PyCharm")
    return 0

def task_1(points):
    x = np.linspace(-2, 2, points)
    y1 = np.sin(x)*(1/x)*np.cos(x**2+1/x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.set_xlabel("x")  # подпись оси х
    ax.set_ylabel("y")  # подпись оси y
    ax.legend()  # показывать условные обозначения

    plt.show()  # показать рисунок
    fig.savefig('1.png')  # сохранить в png

def task_2(N):
    random_x = np.linspace(-2, 5, N)
    random_y0 = np.random.randn(N) + 5

    trace0 = go.Scatter(
        x=random_x,
        y=random_x*np.sin(5*random_x),
        mode='lines',
        name='lines'
    )
    data = [trace0]
    y = random_x * np.sin(5 * random_x)
    ply.offline.plot(data, filename='line-mode.html')
    plt.plot(random_x, y)
    plt.savefig("out.pdf")



lenArg=len(sys.argv)
if lenArg<1:
    print('Вы не ввели ни одного аргумента!!')
    print("Введите аргумент -h или --help чтобы посмотреть доступные аргументы.")

else:
    try:
        if sys.argv[1]=="-h" or sys.argv[1]=="--help":
            help()
        else:
            word_count()
            graph_points=int(sys.argv[1])
            if sys.argv[2] == "--task_1":
                task_1(graph_points)
            elif sys.argv[2] == "--task_2":
                task_2(graph_points)
            else:
                print('Вы ввели не допустимый второй аргумент!')
                print("Введите аргумент -h или --help чтобы посмотреть доступные аргументы.")
            word_count()
    except ValueError :
        print('Вы ввели недопустимое значение!')
        print("Введите аргумент -h или --help чтобы посмотреть доступные аргументы.")
    except Exception:
        print('Вы вели слишком мало аргументов,'
              'либо ввели не допустимый аргумент!')
        print("Введите аргумент -h или --help чтобы посмотреть доступные аргументы.")
