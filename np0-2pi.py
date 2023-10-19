import numpy as np
from tabulate import tabulate

def main():

	x = np.linspace(0, 2*np.pi, num=1000)

	x2 = np.sin(x)
	
	x3 = tabulate(np.stack((x,x2),axis=1))
	
	print(x3)


if __name__ == "__main__":
	main()


