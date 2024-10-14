real = float(input('Quanto você tem na carteira? '))
dolar = real / 5.40
print('Com tantos R${:.2f} você pode comprar tantos U${:.2f}'.format(real,dolar))