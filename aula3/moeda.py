from bcb import currency
import matplotlib.pyplot as plt

moedas = currency.get(['USD'], start='2021-06-07', end='2022-06-08', side='ask')

plt.plot(moedas)
plt.show()
