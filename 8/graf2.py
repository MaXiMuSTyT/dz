
import numpy as np
import pylab
from matplotlib.widgets import Slider,RadioButtons, CheckButtons
import numpy

def df(x):
    dy = 4*np.sin(x**2 +2) * (2*x -3) +2*x * (4*x**2-12*x +9)* np.cos(x**2 +2)
    return dy
def f(x):
    y = (2*x-3)**2 * np.sin(x**2 +2)
    return y
def kf(x,x0):
    yk = f(x0) + df(x0) *(x-x0)
    return yk






def gauss(sigma, mu, x):

    return (1.0 / (sigma * numpy.sqrt(2.0 * numpy.pi)) *
            numpy.exp(-((x - mu) ** 2) / (2 * sigma * sigma)))


if __name__ == '__main__':
    def updateGraph():

        global pointf
        global slider_point
        global graph_axes
        global radiobuttons_color
        global kas_visible

        colors = {'Красный': 'r', 'Синий': 'b', 'Черный': '#000','Пунктир':'--','Штрих-пунктир':'-.'}


        x = numpy.arange(1, 5.0, 0.01)

        style = colors[radiobuttons_color.value_selected]
        point = slider_point.val
        graph_axes.clear()
        graph_axes.plot(x, f(x), style)




        graph_axes.plot([point], [f(point)], 'o')


        if kas_visible:
            graph_axes.plot(x,kf(x,point))
        pylab.draw()

    def onChangeGraph(value):
        updateGraph()

    def onRadioButtonsClicked(label):
        updateGraph()

    def onCheckClicked(label):
        global kas_visible
        if label == 'Касательная':
            kas_visible = not kas_visible

        updateGraph()

    fig, graph_axes = pylab.subplots()
    graph_axes.grid()

    kas_visible = True
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.55)

    axes_slider_point = pylab.axes([0.05, 0.35, 0.85, 0.04])
    slider_point = Slider(axes_slider_point,
                          label='Перемещение точки',
                          valmin=1.0,
                          valmax=5.0,
                          valinit=0.5,
                          valfmt='%1.2f')


    slider_point.on_changed(onChangeGraph)

    axes_radiobuttons = pylab.axes([0.05, 0.05, 0.2, 0.2])

    radiobuttons_color = RadioButtons(axes_radiobuttons,
                                      ['Красный', 'Синий', 'Черный','Пунктир','Штрих-пунктир'])
    radiobuttons_color.on_clicked(onRadioButtonsClicked)

    axes_checkbuttons = pylab.axes([0.35, 0.15, 0.2, 0.1])

    checkbutton_grid = CheckButtons(axes_checkbuttons,
                                    ['Касательная'],
                                    [True])
    checkbutton_grid.on_clicked(onCheckClicked)

    updateGraph()
    pylab.show()




