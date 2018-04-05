#Ex3_3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input("Number: "))
for i in a:
	if(i < num):
		b.append(i)

print(b)