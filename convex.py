import numpy as np
import matplotlib.pyplot as plt

# w의 범위를 설정합니다.
w = np.linspace(-5, 5, 4000000)

# 로지스틱 함수 sigma(w) 정의
sigma_w = 1 / (1 + np.exp(-w))

# 첫 번째 함수: (1/(1+e^{-w}) - 1)^2
f1 = (sigma_w - 1)**2

# 두 번째 함수: -log(1/(1+e^{-w}))
# 수학적으로 -log(1/(1+e^{-w})) = log(1+e^{-w})
f2 = np.log(1 + np.exp(-w))

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(w, f1, label=r'$\left(\frac{1}{1+e^{-w}} - 1\right)^2$')
plt.plot(w, f2, label=r'$-\log\left(\frac{1}{1+e^{-w}}\right)$', linestyle='--')

plt.xlabel('w', fontsize=12)
plt.ylabel('Function Value', fontsize=12)
plt.title('Graphs of the Functions', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
