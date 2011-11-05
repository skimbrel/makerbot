"""menger.py - generate OpenSCAD-compatible descriptions of Menger sponges
Takes a single argument n, an integer number of iterations to run.
Prints OpenSCAD code to stdout.
"""

import argparse

CUBE = "cube(size=1);\n"
SCALE_FACTOR = 3
TRANSLATIONS = (
(0, 0, 0),
(0, 0, 1),
(0, 0, 2),
(0, 1, 0),
(0, 1, 2),
(0, 2, 0),
(0, 2, 1),
(0, 2, 2),
(1, 0, 0),
(1, 0, 2),
(1, 2, 0),
(1, 2, 2),
(2, 0, 0),
(2, 0, 1),
(2, 0, 2),
(2, 1, 0),
(2, 1, 2),
(2, 2, 0),
(2, 2, 1),
(2, 2, 2),
)


def translate(x, y, z, inner):
    return "translate([%(x)s, %(y)s, %(z)s]) {\n%(inner)s}\n" % {
        'x': x,
        'y': y,
        'z': z,
        'inner': inner}


def union(inner):
    return "union() {\n%(inner)s}\n" % {'inner': inner}


def generate(remainingIterations):
    if remainingIterations == 0:
        return CUBE
    else:
        next = generate(remainingIterations - 1)
        children = [translate(
            SCALE_FACTOR ** (remainingIterations - 1) * x,
            SCALE_FACTOR ** (remainingIterations - 1) * y,
            SCALE_FACTOR ** (remainingIterations - 1) * z,
        next) for x, y, z in TRANSLATIONS]
        inner = ''.join(children)
        return union(inner)


def printSponge(iterations):
    output = generate(iterations)
    print output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Make a Menger sponge for OpenSCAD.")
    parser.add_argument('n')
    values = parser.parse_args()
    try:
        iters = int(values.n)
        printSponge(iters)
    except AttributeError, ValueError:
        iters = 1
        printSponge(iters)
