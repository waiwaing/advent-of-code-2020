import re

def main():
	input = []
	buffer = ""
	with open("testinput.txt") as f:
		for line in f.readlines():
			line = line.strip()
			
			if line == "":
				input.append(buffer)
				buffer = ""
			else:
				buffer += line + " "
	input.append(buffer)

	input = [x for x in input if x.strip() != ""]
	totValid = 0
	required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

	for row in input:
		valid = True
		for r in required:
			regex = r + ":([^ ]*) "
			match = re.search(regex, row)

			if match == None:
				valid = False
				break

			value = match.group(1)
			try:
				iValue = int(value)
			except:
				iValue = None
				pass

			
			if r == "byr":
				newValid = (iValue >= 1920 and iValue <= 2002)
			elif r == "iyr":
				newValid = (iValue >= 2010 and iValue <= 2020)
			elif r == "eyr":
				newValid = (iValue >= 2020 and iValue <= 2030)
			elif r == "hgt":
				newValid =  (
					(re.match("1(([5-8]\\d)|90|91|92|93)cm", value) != None) or
					(re.match("(59|6\\d|70|71|72|73|74|75|76)in", value) != None)
				)
			elif r == "hcl":
				newValid =  (re.match("^#[0-9a-f]{6}$", value) != None)
			elif r == "ecl":
				newValid =  (value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
			elif r == "pid":
				newValid =  (len(value) == 9)

			if valid and not newValid:
				print(r)
				valid = False

		if valid:
			totValid = totValid + 1 
			print("valid")
		else:
			print("invalid")

	print(totValid)

main()
