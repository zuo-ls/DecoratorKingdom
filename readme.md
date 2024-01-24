# DecoratorKingdom
Adding features using decorators.
## 1 Plot decorator
Tools for pretty plots.
### 1.1 Set palette for a plot method via a decorator
```python
from dk.plot import set_palette

@set_palette('darkblue',2) # style is 'darkblue', number of color is 2
def plot_dist(data1,data2):
    sns.kdeplot(data1, fill=True)
    sns.kdeplot(data2, fill=True)
    plt.show()

# plot
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(1, 1, 1000)
plot_dist(data1,data2)
```
## 2 Basic decorator
- classproperty: a decorator for classmethod + property
- superclassmethod: a decorator for class methods with super() behavior.

## 3 Version controller
