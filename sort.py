from color import Color

def merge_sort(arr, arr_color, left, right, draw):
	mid = (left + right) // 2

	if left < right: 
		merge_sort(arr, arr_color, left, mid, draw)
		merge_sort(arr, arr_color, mid + 1, right, draw)
		merge_arr(arr, arr_color, draw, left, mid, mid + 1, right)

	return True


def merge_arr(arr, arr_color, draw, left1, right1, left2, right2):
	sorted_array = []
	sorted_index = 0
	i = left1
	j = left2

	while i <= right1 and j <= right2:
		arr_color[i] = Color.RED.value
		arr_color[j] = Color.RED.value
		draw()
		arr_color[i] = Color.BLACK.value
		arr_color[j] = Color.BLACK.value
		if arr[i] < arr[j]:
			sorted_array.append(arr[i])
			i += 1
		else:
			sorted_array.append(arr[j])
			j += 1

	while i <= right1:
		arr_color[i] = Color.RED.value
		draw()
		arr_color[i] = Color.BLACK.value
		sorted_array.append(arr[i])
		i += 1

	while j <= right2:
		arr_color[j] = Color.RED.value
		draw()
		arr_color[j] = Color.BLACK.value
		sorted_array.append(arr[j])
		j += 1

	for x in range(left1, right2 + 1):
		arr[x] = sorted_array[sorted_index]
		sorted_index += 1
		arr_color[x] = Color.BLUE.value
		draw()
		if right2 - left1 == len(arr) - 1:
			arr_color[x] = Color.ORANGE.value
		else:
			arr_color[x] = Color.BLACK.value


def selection_sort(arr, arr_color, draw):
	for i in range(len(arr)):
		arr_color[i] = Color.RED.value
		min_index = i
		for j in range(i+1, len(arr)):
			arr_color[j] = Color.RED.value
			draw()
			if arr[min_index] > arr[j]:
				min_index = j
			arr_color[j] = Color.BLACK.value

		arr_color[i] = Color.BLUE.value
		arr_color[min_index] = Color.BLUE.value
		draw()
		arr[i], arr[min_index] = arr[min_index], arr[i]
		arr_color[i] = Color.BLACK.value
		arr_color[min_index] = Color.BLACK.value

	return True


def insertion_sort(arr, arr_color, draw):
	for i in range(len(arr)):
		arr_color[i] = Color.RED.value
		key = arr[i]
		j = i - 1 
		while j >= 0 and key < arr[j]:
			arr_color[j + 1] = Color.BLUE.value
			arr_color[j] = Color.BLUE.value
			arr[j + 1] = arr[j]
			draw()
			arr_color[j + 1] = Color.BLACK.value
			arr_color[j] = Color.BLACK.value
			j -= 1

		arr_color[i] = Color.BLUE.value
		arr_color[j + 1] = Color.BLUE.value
		draw()
		arr[j + 1] = key
		arr_color[i] = Color.BLACK.value
		arr_color[j + 1] = Color.BLACK.value

	print(arr)

	return True


'''
def merge_sort(arr, arr_color, redraw_array):
	if (len(arr) > 1):
		mid_point = len(arr) // 2
		left_lst = arr[:mid_point]
		right_lst = arr[mid_point:] 
		left_idx = right_idx = index = 0
		merge_sort(left_lst, arr_color, redraw_array)
		merge_sort(right_lst, arr_color, redraw_array)

		# Swap according to which value is the lowest between the right and the left in the original array
		while left_idx < len(left_lst) and right_idx < len(right_lst):
			arr_color[index] = Color.RED.value
			redraw_array()
			arr_color[index] = Color.BLACK.value
			# redraw_array()
			if left_lst[left_idx] < right_lst[right_idx]:
				arr_color[index] = Color.BLUE.value
				redraw_array()
				arr[index] = left_lst[left_idx]
				arr_color[index] = Color.BLACK.value
				left_idx += 1
			else:
				arr_color[index] = Color.BLUE.value
				redraw_array()
				arr[index] = right_lst[right_idx]
				arr_color[index] = Color.BLACK.value
				right_idx += 1
			index += 1

		# if there are more values within the left array, swap the ramaning index from the original according to the left array
		while left_idx < len(left_lst):
			arr_color[index] = Color.BLUE.value
			redraw_array()
			arr[index] = left_lst[left_idx]
			arr_color[index] = Color.BLACK.value
			# redraw_array()
			left_idx += 1
			index += 1

		# if there are more values within the right array, swap the ramaning index from the original according to the right array
		while right_idx < len(right_lst):
			arr_color[index] = Color.BLUE.value
			redraw_array()
			arr[index] = right_lst[right_idx]
			arr_color[index] = Color.BLACK.value
			right_idx += 1
			index += 1
	return True
'''