def limits(low,high):
	for num in range(low,high+1):
		if num>1:
			for i in range(2,num):
				if(num%i)==0:
					break
			else:
				print(num)
lower_range=int(input("Enter lower limit: "))
upper_range=int(input("Enter upper limit: "))
limits(lower_range,upper_range)