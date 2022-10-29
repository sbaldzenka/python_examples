
# author : sboldenko
# data   : 29.10.2022
# e-mail : venera.electronica@gmail.com

def search_of_point(R, circle_x, circle_y, point_x, point_y):
	if (point_y >= circle_y):
		result = ((point_x - circle_x) * (point_x - circle_x)) + ((point_y - circle_y) * (point_y - circle_y))

		if ((R * R) >= result):
			return 1
		else:
			return -1
	else:
		return -1

# tests
result = searh_of_point(7.349, 3, 6, 9,10)
print(result)

result = searh_of_point(5, 3, 6, 9,10)
print(result)