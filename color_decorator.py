import seaborn as sns
import matplotlib.pyplot as plt
from functools import wraps

# Decorator function to set the palette for the plot
def set_palette(style, n=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            palette = get_palette(style, n)
            with sns.color_palette(palette):
                return func(*args, **kwargs)
        return wrapper
    return decorator

# Function to get the palette based on the specified style
def get_palette(style, n):
    palette_setter = PaletteSetter()
    if hasattr(palette_setter, style):
        return getattr(palette_setter, style)(n)
    else:
        raise ValueError(f"Palette style '{style}' is not defined.")

# Class to define different palette styles
class PaletteSetter:
    def darkblue(self, n):
        return sns.dark_palette("#8BF", reverse=True, n_colors=n)
    
    def rainbow(self, n):
        return sns.color_palette("rainbow", n_colors=n)
    
    def Set2(self, n):
        return sns.color_palette("Set2", n_colors=n)

if __name__ == "__main__":
    import numpy as np
    # Example of using the decorator
    @set_palette('darkblue')
    def plot_dist(data1,data2):
        sns.kdeplot(data1, fill=True)
        sns.kdeplot(data2, fill=True)
        plt.show()

    data1 = np.random.normal(0, 1, 1000)
    data2 = np.random.normal(1, 1, 1000)
    plot_dist(data1,data2)