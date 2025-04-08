import numpy as np
import matplotlib.pyplot as plt

# Диапазон интенсивностей λ (при фиксированном μ)
mu = 5
lambdas = np.linspace(0.1, 4.9, 100)

rho = lambdas / mu
L = rho / (1 - rho)
W = 1 / (mu - lambdas)
Wq = rho / (mu - lambdas)

plt.figure(figsize=(10, 6))
plt.plot(lambdas, L, label='Среднее число клиентов L')
plt.plot(lambdas, W, label='Время в системе W')
plt.plot(lambdas, Wq, label='Время ожидания Wq')
plt.axvline(mu, color='red', linestyle='--', label='λ = μ (граница устойчивости)')
plt.xlabel('Интенсивность прихода λ')
plt.ylabel('Показатели')
plt.title('Анализ модели M/M/1')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()