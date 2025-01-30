import pandas as pd
import matplotlib.pyplot as plt
def iris_operations():
    df = pd.read_csv("iris.csv")
    
    print("First 5 rows:")
    print(df.head())
    
    print("Last 5 rows:")
    print(df.tail())
    
    print("Dataset Info:")
    print(df.info())
    
    print("Overview of columns:")
    print(df.describe())
    
    df.plot()
    plt.show()

iris_operations()
