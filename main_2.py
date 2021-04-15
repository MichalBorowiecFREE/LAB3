import numpy as np
import matplotlib.pyplot as plt

c=0
f=0
x_0 = 1
x_p = 2

l_wezlow = 4;

wezly = np.array([[1,0],
                 [2,1],
                 [2,0.5],
                 [4,0.75]])
elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

twb_L = 'D'
twb_P = 'D'
wwb_L = 0
wwb_P = 1

n = 100

def generujTabliceGeometrii(p,k,n):
    tmp = (k-p) / (n-1)
    m_wezly = np.array([1,p])
    m_elementy = np.array([1,1,2])


    for i in range(1, n, 1):
        m_wezly = np.block([
            [m_wezly],
            [i+1, i * tmp + p],
        ])
    for i in range (1,n,1):
        m_elementy = np.block([
            [m_elementy],
            [i,i,i+1]
        ])


    return m_wezly,m_elementy


WEZLY,ELEMENTY = generujTabliceGeometrii(x_0,x_p,n)
print(WEZLY)
print(ELEMENTY)




