import lab_3_task_1 as gp
import numpy as np
b = 30
ha = 100
a = np.pi / 3
T = 200
z = 300
a = np.sqrt((gp.g * ha * np.tan(b)**2) / 2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a)))
print(a)
sus = (2 / np.sqrt(np.pi)) * (gp.h / (gp.k * T)**(3 / 2)) * gp.e**(-z / (gp.k * T)) * gp.e**(T / 2)
print(sus)
