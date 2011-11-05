"""menger.py - generate OpenSCAD-compatible descriptions of Menger sponges
Takes a single argument n, an integer number of iterations to run.
Prints OpenSCAD code to stdout.

My first attempt at this was to try constructing the sponge exactly the way
the mathematical definition works, i.e. to take the largest cube and
iteratively remove pieces of it. This led to having to track a lot more state
at each step of the recursion and was generally gross.

Instead, this relies on the realization that since we're only ever going
to compute a finite approximation of the fractal, we can build it up from
the smallest piece by constructing each iteration as a union of the next-
smallest iteration. Hurray for approximation.
"""

import argparse
import itertools

CUBE = "cube(size=1);\n"
SCALE_FACTOR = 3
# The list of places we're going to translate our current step to.
# Since an iteration of the sponge is carried out by removing the small cube
# at the very center of the large cube and the six cubes in the center of its
# faces, we want to instead build our sponge by repeating a smaller block
# in all locations *except* those seven points. Luckily, what those points have
# in common (in our vector space) is two or more coordinates equal to 1.
TRANSLATIONS = [vector for vector in itertools.product((0, 1, 2), repeat=3)
    if vector.count(1) < 2]


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
