#Ex6
frase = input("HEY B0SS, Give me a palindrome, PLEASE \n")
#frase = "THIS IS A frase"
frase = frase.replace(" ","").lower()
print(frase[::-1])
print(frase)
if(frase == frase[::-1]):
    print("IT'S A PALINDROME B0SS")
else:
    print("SORRY B0SS")