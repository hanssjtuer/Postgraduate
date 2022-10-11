pos = [(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9)]
cen = [(2, 10), (5, 8), (1, 2)]
fir = 1
ele = []
while True:
	gro = [[], [], []]
	are = [[], [], []]
	for i in range(0, 3, 1):
		for j in pos:
			gro[i].append(((cen[i][0]-j[0])**2 + (cen[i][1]-j[1])**2) ** 0.5)
	for j in range(0, 8, 1):
		if gro[0][j]<gro[1][j] and gro[0][j]<gro[2][j]:
			are[0].append(pos[j])
		elif gro[1][j]<gro[0][j] and gro[1][j]<gro[2][j]:
			are[1].append(pos[j])
		elif gro[2][j]<gro[0][j] and gro[2][j]<gro[1][j]:
			are[2].append(pos[j])
	ele.append(are)
	if len(ele)>2:
		if ele[-1] == ele[-2]:
			print('the final three groups:')
			for i in ele[-1]:
				print(i)
			break
	for i in range(0, len(are), 1):
		grl = len(are[i])
		xal=yal = 0
		for j in range(0, grl, 1):
			xal += are[i][j][0]
			yal += are[i][j][1]
		cen[i] = (xal/grl, yal/grl)
	if fir == 1:
		print('three centers after the first loop:')
		for i in cen:
			print(i)
		fir += 1





