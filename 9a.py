import pandas as pd
import matplotlib.pyplot as plt

def pandas_operations():
    df = pd.read_csv("iris.csv")
    
    # Scatter Plot
    df.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm')
    plt.show()
    
    # Histogram
    df['SepalLengthCm'].plot(kind='hist')
    plt.show()

pandas_operations()
