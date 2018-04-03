#Ex4

num = int(input("Hit me!\n"))
final_list = [i for i in range(num,0,-1) if (num%i) == 0]
print(final_list)

