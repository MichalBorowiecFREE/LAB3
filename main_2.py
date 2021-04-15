import numpy as np
import matplotlib.pyplot as plt

c=0
f=0
x_0 = 1
x_p = 2

l_wezlow = 5;

twb_L = 'D'
twb_P = 'D'
wwb_L = 0
wwb_P = 1

wezly = np.array([[1,0],
                 [2,1],
                 [2,0.5],
                 [4,0.75]])
elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

def generujTabliceGeometrii(p,k,n):
    tmp = (k-p) / (n-1)
    m_wezly = np.array([1,p])
    m_elementy = np.array([1,1,2])

    for i in range(1, n, 1):
        m_wezly = np.block([
            [m_wezly],
            [i+1, i * tmp + p],
        ])
    for i in range (2,n,1):
        m_elementy = np.block([
            [m_elementy],
            [i,i,i+1]
        ])

    return m_wezly,m_elementy

wezly,elementy = generujTabliceGeometrii(x_0,x_p,l_wezlow)
print(wezly)
print(elementy)

def rysowanie(matrix):
    y = np.zeros(matrix.shape[0])
    plt.plot(matrix[:, 1], y, marker='o')

    for i in range(0, np.size(y), 1):
        plt.text(x=matrix[i, 1], y=y[i]-0.005, s=int(matrix[i, 0]))

    for i in range(0, np.size(y) - 1, 1):
        plt.text(x=(matrix[i, 1] + matrix[i + 1, 1]) / 2, y=y[i] + 0.003, s=int(i + 1), color='red')
    plt.show()

rysowanie(wezly)


