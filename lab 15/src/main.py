import matplotlib.pyplot as plt
import numpy as np
import plotly as ply
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from matplotlib import pyplot as plt
import argparse

def task_2():
    N = 100
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


def task_1():
    x = np.linspace(-2, 2, 100)
    y1 = np.sin(x)*(1/x)*np.cos(x**2+1/x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.set_xlabel("x")  # подпись оси х
    ax.set_ylabel("y")  # подпись оси y
    ax.legend()  # показывать условные обозначения

    plt.show()  # показать рисунок
    fig.savefig('1.png')  # сохранить в png


if __name__ == '__main__':
    task_1()
    #task_2()


