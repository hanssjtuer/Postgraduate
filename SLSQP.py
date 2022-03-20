# Jinhao Cao, NAOCE, SJTU, 20200501
# SLSQP

import math, scipy.optimize

def RandomAxisRandomBeta(Axis, Beta):
	# rotate beta at origin around axis and return matrix
	Beta = math.pi / 180 * Beta;
	u, v, w = Axis[0], Axis[1], Axis[2]
	d = u * u + v * v + w * w
	h = d ** 0.5
	m11 = (u * u + (v * v + w * w) * math.cos(Beta)) / d
	m21 = (u * v * (1 - math.cos(Beta)) + w * h * math.sin(Beta)) / d
	m31 = (u * w * (1 - math.cos(Beta)) - v * h * math.sin(Beta)) / d
	m12 = (u * v * (1 - math.cos(Beta)) - w * h * math.sin(Beta)) / d
	m22 = (v * v + (u * u + w * w) * math.cos(Beta)) / d
	m32 = (v * w * (1 - math.cos(Beta)) + u * h * math.sin(Beta)) / d
	m13 = (u * w * (1 - math.cos(Beta)) + v * h * math.sin(Beta)) / d
	m23 = (v * w * (1 - math.cos(Beta)) - u * h * math.sin(Beta)) / d
	m33 = (w * w + (u * u + v * v) * math.cos(Beta)) / d
	return [m11, m21, m31, 0, m12, m22, m32, 0, m13, m23, m33, 0, 0, 0, 0, 1]

def MatrixMultiply(Axis, TR):
	# axis times matrix and return axis
	Newer = [0, 0, 0]
	Newer[0] = Axis[0] * TR[0] +  Axis[1] * TR[1] +  Axis[2] * TR[2] + 1 * TR[3];
	Newer[1] = Axis[0] * TR[4] +  Axis[1] * TR[5] +  Axis[2] * TR[6] + 1 * TR[7];
	Newer[2] = Axis[0] * TR[8] +  Axis[1] * TR[9] +  Axis[2] * TR[10] + 1 * TR[11];
	return Newer

# example for PlanePlaneParallel
def SequentialLeastSquaresProgramming(Part1_Plane=[0, 1, 0],
									  Part2_Plane=[-1, 0, 0],
									  Part3_Plane1=[math.sqrt(2)/2, -math.sqrt(2)/2, 0],
									  Part3_Plane2=[math.sqrt(2)/2, math.sqrt(2)/2, 0]):
	def Objective(Rotate):
		return Rotate[3]

	def Constraint1(Rotate):
		Newer = MatrixMultiply(Part3_Plane1, RandomAxisRandomBeta([Rotate[0], Rotate[1], Rotate[2]], Rotate[3]))
		return abs((Newer[0] * Part1_Plane[0] + Newer[1] * Part1_Plane[1] + Newer[2] * Part1_Plane[2]) / (Newer[0] ** 2 + Newer[1] ** 2 + Newer[2] ** 2) ** 0.5) - 1

	def Constraint2(Rotate):
	 	Newer = MatrixMultiply(Part3_Plane2, RandomAxisRandomBeta([Rotate[0], Rotate[1], Rotate[2]], Rotate[3]))
	 	return abs((Newer[0] * Part2_Plane[0] + Newer[1] * Part2_Plane[1] + Newer[2] * Part2_Plane[2]) / (Newer[0] ** 2 + Newer[1] ** 2 + Newer[2] ** 2) ** 0.5) - 1

	def Constraint3(Rotate):
		return (math.pow(Rotate[0], 2) + math.pow(Rotate[1], 2) + math.pow(Rotate[2], 2))**0.5 - 1

	Bound = ((-1.0, 1.0), (-1.0, 1.0), (-1.0, 1.0), (-180, 180))

	Con1 = {'type':'eq', 'fun':Constraint1}
	Con2 = {'type':'eq', 'fun':Constraint2}
	Con3 = {'type':'eq', 'fun':Constraint3}
	Cons = ([Con1, Con2, Con3])

	InitialSolution = [1.0, 1.0, 1.0, 90.0]

	OptimalSolution = scipy.optimize.minimize(Objective, InitialSolution, method='SLSQP', bounds=Bound, constraints=Cons, tol=1e-2, options={'maxiter':100})
	return OptimalSolution

print(SequentialLeastSquaresProgramming())