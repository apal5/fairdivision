import numpy as np
import matplotlib.pyplot as plt
gfg = np.random.dirichlet((3,4,5,19),size=1000)
count, bins, ignored, = plt.hist(gfg, 30, density=True)
# plt.show()
print(generate_positive_dirichlet_instance(2,3,1000))

def generate_positive_dirichlet_instance(m, n, B=config.B):
    V = list()
    for j in range(n):
        vals = np.random.dirichlet([10 for i in range(m)])
        vals = vals + 0.001
        vals = [np.ceil(B*v) for v in vals]
        while np.sum(vals) > B:
            i = np.random.randint(low=0, high=n)
            if vals[i] > 1:
                vals[i] = vals[i] - 1
        V.append(vals)
    V = np.array(V)
    return V