import numpy as np
from tabulate import tabulate
from astropy.table import Table

x = np.linspace(0, 2 * (np.pi), 1000)

y = np.sin(x)

tableData = [(a,b) for a, b in zip(x,y)]

tableHeaders = ["x", "y"]
pythonTable = tabulate(tableData, tablefmt="grid", headers=tableHeaders,
	floatfmt=".3f")

def main():
	print(pythonTable)

if __name__ == '__main__':
	main()