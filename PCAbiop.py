import numpy as np
import matplotlib.pyplot as plt 
X = np.random.uniform(-20, 80, 20)

V = np.random.normal(0, 2, 20)
f_x = ((3 * X) / 20) + 5

data = [n1 + n2 for n1, n2 in zip(f_x, V)]

covariance_matrix = np.cov(X, data)
print(covariance_matrix)

eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
print(eigen_vectors)
print(eigen_values)
plt.plot(eigen_vectors, eigen_values)
plt.show()