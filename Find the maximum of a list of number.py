list = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
	ele = int(input("Enter elements: "))
	list.append(ele)
print("Largest element is:", max( list))
