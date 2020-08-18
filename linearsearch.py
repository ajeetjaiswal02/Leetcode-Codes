listdata = [2,5,6,72,125]
values = 5
def LinearSearch(listdata,values):
	index = 0
	while (index < len(listdata) and listdata[index]<values):
		index+=1
	if (index >= len(listdata) or listdata[index] != values):
		return -1
	return index	

result = LinearSearch(listdata,values)
print(result)
		


