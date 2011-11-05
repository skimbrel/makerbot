difference() {
	scale([0.333333333333/3, 0.333333333333/3, 0.333333333333/3]) {
		translate([1, 1, 1]) {
			cube(size=10);
		}
		translate([1, 1, 0]) {
			cube(size=10);
		}
		translate([2, 1, 1]) {
			cube(size=10);
		}
		translate([0, 1, 1]) {
			cube(size=10);
		}
		translate([1, 1, 2]) {
			cube(size=10);
		}
		translate([1, 0, 1]) {
			cube(size=10);
		}
		translate([1, 2, 1]) {
			cube(size=10);
		}
	}
}