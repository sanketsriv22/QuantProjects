import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


print("hello world")

print("this is the main branch now")

x = np.arange(0,100)
y = np.arange(0,100)

def plotData(x, y):
    df = pd.DataFrame({'x': x, 'y': y})
    sns.scatterplot(data=df, x='x', y='y')
    plt.title('Scatter Plot of x vs y')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.show()

if __name__ == "__main__":
    print("Plotting data...")
    plotData(x,y)
    print("Data plotted successfully!")