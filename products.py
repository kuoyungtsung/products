products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == ('q'):
		break
	products.append(name)
print(products)

for p in products:
	print(p)
print(products[0])