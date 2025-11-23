import numpy as np
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_abline, ggsave

X = np.loadtxt("X.txt")   
y = np.loadtxt("y.txt")   

X = X.reshape(-1, 1)

ones = np.ones((X.shape[0], 1))
X_design = np.hstack((ones, X))

beta = np.linalg.inv(X_design.T @ X_design) @ (X_design.T @ y)

a = beta[0]  
b = beta[1]  

print("Coeficientes calculados:")
print("Intercepto (a):", a)
print("Inclinação (b):", b)

df = {"x": X.flatten(), "y": y}

plot = (
    ggplot(pd.DataFrame(df), aes("x", "y"))
    + geom_point()
    + geom_abline(intercept=a, slope=b)
)

plot.save("grafico.png")   
