testc = int(input())
for i in range(0,testc):
	l_i = input()
	l_i.split()
	shy_max = int(l_i[0])
	str_ = l_i[1]
	var_i = 0
	out_i = 0
	for j in range(0,shy_max+1):
		add_j = 0
		if (var_i < j):
			add_j += j - var_i
			out_i += add_j
		var_i += int(str_[j]) + add_j
	print(out_i)

