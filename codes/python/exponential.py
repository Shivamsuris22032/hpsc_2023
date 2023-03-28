"""Python module to calculate exponential using series expansion"""
import numpy as np
import matplotlib.pyplot as plt
import math
import timeit
def expo(x,debug=False):
	
	n=100
	series=1
	term_adder=1
	for i in range(1,n+1):
		term_adder=term_adder * x/i
		series_init=series
		series+=term_adder
	if debug:
		if abs(series-series_init)<1e-5:
			print("Converging")
	return series

x=np.linspace(0,1,100)

#Default Exponential function
begin_time1 = timeit.default_timer()
y1=np.exp(x)
end_time1 = timeit.default_timer() - begin_time1
print('Execution time for default exponential function: ',end_time1)

#User Defined Exponential function
begin_time2 = timeit.default_timer()
y2=expo(x)
end_time2 = timeit.default_timer() - begin_time2
print('Execution time for User Defined exponential function: ',end_time2)
diff_time=abs(end_time2 - end_time1)
print('Difference of time taken: ',diff_time)
plt.plot(x,y1,label='Python defined exp(x)')
plt.plot(x,y2,'+',label='User defined exp(x)')
plt.xlabel('x')
plt.ylabel('Exp(x)')
plt.title('Comparison of exponential functions')
plt.legend()
plt.show()
