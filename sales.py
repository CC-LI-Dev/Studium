sales = [ ('John', 'Miller', 46, 18.67), ('Randy', 'Steiner', 48, 27.99), ('Tina', 'Baker', 53, 27.23), ('Andrea', 'Baker', 40, 31.75), ('Eve', 'Turner', 44, 18.99), ('Henry', 'James', 50, 23.56)]

sales.sort(key=lambda a: a[2]*a[3])
print(sales)

sales.sort(key=lambda a: a[1]+a[0])
print(sales)

