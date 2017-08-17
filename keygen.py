import sys

firstArray = bytearray.fromhex("AA 89 C4 FE 46")
secondArray = bytearray.fromhex("78 F0 D0 03 E7")
thirdArray = bytearray.fromhex("F7 FD F4 E7 B9")
fourthArray = bytearray.fromhex("B5 1B C9 50 73")

def normal(string, keys):	
	eax = 0
	for i in range(len(string)):
		a = string[i]
		b = keys[eax]
		xorResult = a ^ b
		keys[eax] = a
		string[i] = xorResult
		
		eax += 1
		
		if eax is 5:
			eax = 0
			
def reverse(string, keys):
	edi = 0
	for i in range(len(string)):
		a = keys[edi]
		b = len(string) - i - 1
		c = string[b]
		result = a ^ c
		string[b] = result
		keys[edi] = c
		
		edi+=1
		
		if edi is 5:
			edi = 0
			
def justBeforeEnd(string):
	byteArray = bytearray(4)
	for i in range(len(string)):
		a = i & 0x3
		b = byteArray[a]
		c = string[i]
		result = b + c
		byteArray[a] = result & 0xff
		
	return byteArray
	
def dividing(byteArray):
	toDivide = int.from_bytes(byteArray, byteorder="little")
	divider = 0xA
	result = bytearray()
	
	while toDivide is not 0:
		modulo = toDivide % divider
		toDivide = int(toDivide / divider)
		result.append(0x30 + int(modulo))
	
	result.reverse()
	return result
	
if (len(sys.argv)) < 2:
	print("You have to specify a username")
	sys.exit()

		
string = bytearray(sys.argv[1].encode("ascii"))
string.append(0)
del string[0]

normal(string, firstArray)
reverse(string, secondArray)
normal(string, thirdArray)
reverse(string, fourthArray)
bytes = justBeforeEnd(string)
print("Your key is:", dividing(bytes).decode("ascii"))
