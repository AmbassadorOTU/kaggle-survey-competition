import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns


def bar_plot(data, title):
    style.use('ggplot')
    plt.figure(figsize=(12,7))
    plots = data.plot(kind='barh', color='blue')
    plt.title(title)
    for bar in plots.containers:
        # set the bar label
        plots.bar_label(bar, fmt='%.0f', label_type='edge', size=8)
    plt.show()
    

def bar2_plot(data, title):
    style.use('ggplot')
    plt.figure(figsize=(12,7))
    plt.title(title)
    plots = data.plot(kind='bar', color='blue')
    for bar in plots.patches:
      # Using Matplotlib's annotate function and
      # passing the coordinates where the annotation shall be done
      # x-coordinate: bar.get_x() + bar.get_width() / 2
      # y-coordinate: bar.get_height()
      # free space to be left to make graph pleasing: (0, 8)
      # ha and va stand for the horizontal and vertical alignment
        plots.annotate(format(bar.get_height(), '.0f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=8, xytext=(0, 8),
                       textcoords='offset points')
    plt.show()
        
        
def bar3_plot(data, title):
    style.use('ggplot')
    plt.figure(figsize=(12,7))
    plt.title(title)
    plots = data.plot(kind='barh', color='blue')
    for bar in plots.containers:
    # set the bar label
        plots.bar_label(bar, fmt='%.0f', label_type='edge', size=8)
    plt.show()