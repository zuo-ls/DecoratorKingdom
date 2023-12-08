# PlotPark

Tools for pretty plots.

## Set palette for a plot method via a decorator
```
from color_decorator import set_palette

@set_palette('darkblue',2) # 
def plot_dist(data1,data2):
    sns.kdeplot(data1, fill=True)
    sns.kdeplot(data2, fill=True)
    plt.show()

# plot
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(1, 1, 1000)
plot_dist(data1,data2)
```