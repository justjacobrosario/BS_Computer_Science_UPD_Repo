def main():
	print(pow_digit(3,2))

def pow_digit(a,b):
	return f"{pow(a,b):e}"
	#return f"{pow(a,b,10**11):011d}"
	#return format(pow(a,b,10**11), "011d")

if __name__ == '__main__':
	main()