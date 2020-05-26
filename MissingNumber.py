def getMissingNo(arr):
	length=len(arr)
	sum=0
	idx=-1
	for i in range(0,length):
		sum+=arr[i]
	total=(length+1)*(length+2)/2
	return int(total-sum)
arr=[1,2,4,5,6]
miss=getMissingNo(arr)
print("Missing number is: ",(miss))