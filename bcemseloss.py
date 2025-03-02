import numpy as np
import matplotlib.pyplot as plt

# g의 범위를 설정 (0보다 커야 log(g)가 정의됨)
g = np.linspace(-4, 6, 100000)

# 각 함수 정의
y_log = -np.log(g)         # log(g)
y_sq  = (g - 1)**2        # (g-1)^2

# 그래프 그리기
plt.figure(figsize=(8, 5))
plt.plot(g, y_log, label=r'$\log(g)$')
plt.plot(g, y_sq, label=r'$(g-1)^2$')

# 그래프 설정
plt.xlabel('g', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('log(g) and (g-1)^2', fontsize=14)
plt.legend()
plt.grid(True)

plt.show()
