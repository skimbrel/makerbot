import argparse

CUBE = "cube(size=10);\n"
SCALE_FACTOR = 1.0 / 3.0
TRANSLATIONS = (
	(1,1,1),
	(1,1,0),
	(2,1,1),
	(0,1,1),
	(1,1,2),
	(1,0,1),
	(1,2,1),
	)

def scale(factor, inner):
	return "scale([%(factor)s/3, %(factor)s/3, %(factor)s/3]) {\n%(inner)s}\n" % {'factor': factor, 'inner': inner}

def translate(x, y, z, inner):
	return "translate([%(x)s, %(y)s, %(z)s]) {\n%(inner)s}\n" % {
		'x': x,
		'y': y,
		'z': z,
		'inner': inner
	}
	
def union(inner):
	return "union() {\n%(inner)s}\n" % { 'inner': inner }

def diff(inner):
	return "difference() {\n%(inner)s}\n" % { 'inner': inner }
	
def generate(remainingIterations, op):
	if remainingIterations == 0:
		return CUBE
	else:
		if op == 'UNION':
			nextOp = diff
			op = union
		else:
			nextOp = union
			op = diff
		next = generate(remainingIterations - 1, nextOp)
		children = [ scale(SCALE_FACTOR, translate(x, y, z, next)) for x, y, z in TRANSLATIONS ]
		inner = ''.join(children)
		return op(scale(SCALE_FACTOR, inner))

def printSponge(iterations):
	output = generate(iterations, 'union')
	print output

def main():
	parser = argparse.ArgumentParser(description="Make a Menger sponge for OpenSCAD.")
	parser.add_argument('n')
	args = parser.parse_args()
	try:
		iters = int(args.n)
	except AttributeError, ValueError:
		iters = 1
	printSponge(iters)
	
if __name__ == '__main__':
	main()

	
	
		
	