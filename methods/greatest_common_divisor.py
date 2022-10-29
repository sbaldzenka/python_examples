# author : sboldenko
# data   : 29.10.2022
# e-mail : venera.electronica@gmail.com

def greatest_common_divisor(a, b):
	a_divisors = []
	b_divisors = []

	i = 0

	while (i < a):
		div = (a - i)
		result = a % div

		if (result == 0):
			a_divisors.append(div)

		i = i + 1

	i = 0

	while (i < b):
		div = (b - i)
		result = b % div

		if (result == 0):
			b_divisors.append(div)

		i = i + 1

	if (a > b):
		max_value = 0

		for a_div in a_divisors:
			for b_div in b_divisors:
				if ((a_div == b_div) and (b_div > max_value)):
					max_value = b_div

		return max_value
	else:
		max_value = 0

		for b_div in b_divisors:
			for a_div in a_divisors:
				if ((b_div == a_div) and (a_div > max_value)):
					max_value = a_div

		return max_value

# tests

a = 6
b = 16
result = greatest_common_divisor(a, b)
print(a / result, "/", b / result)

a = 9
b = 3
result = greatest_common_divisor(a, b)
print(a / result, "/", b / result)

a = 100
b = 200
result = greatest_common_divisor(a, b)
print(a / result, "/", b / result)