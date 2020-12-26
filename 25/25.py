def main():
	c_public_key = 19241437
	d_public_key = 17346587

	# c_public_key = 5764801
	# d_public_key = 17807724

	for private_key in range(10000000):
		potential = pow(7, private_key, 20201227)
		# potential = apply_transformation(7, private_key)
		if potential == c_public_key:
			public_key = d_public_key
			break
		elif potential == d_public_key:
			private_key = c_public_key
			break

	print(private_key)
	print(public_key)

	encryption_key =  pow(public_key, private_key, 20201227)
	print(encryption_key)


main()
