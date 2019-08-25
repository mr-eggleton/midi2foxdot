Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([(-60,), (11,), (13,), (14,), (-60,), (16,), (18,), (18,), (14,)],dur=[Fraction(2, 3), Fraction(2, 3), Fraction(2, 3), Fraction(2, 3), 0.0, Fraction(2, 3), Fraction(2, 3), 3.0, 1.0],amp=[0, 1, 1, 1, 0, 1, 1, 1, 1])
	d1 >> pluck([(-60,), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[4.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5],amp=[0, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a1():
	d0 >> pluck([(21,), (21,), (18,), (21,), (18,)],dur=[4.0, 2.0, 1.0, 0.5, 0.5],amp=[1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -3), (-10, -3), (-10, -3), (-10, -3)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a2():
	d0 >> pluck([(14,), (11,), (14,), (16,), (18,), (18,), (23,)],dur=[2.5, 0.5, 0.5, 0.5, 3.0, 0.75, 0.25],amp=[1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a3():
	d0 >> pluck([(21,), (18,), (21,), (18,), (21,), (18,)],dur=[2.0, 2.0, 2.0, 1.0, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -3), (-10, -3), (-10, -3), (-10, -3)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a4():
	d0 >> pluck([(14,), (18,), (-60,), (14,), (18,), (-60,), (14,), (18,), (14,), (18,)],dur=[4.0, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 1.25],amp=[1, 1, 0, 1, 1, 0, 1, 1, 1, 1])
	d1 >> pluck([(-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-15, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-11,)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a5():
	d0 >> pluck([(18,), (-60,), (14,), (18,), (-60,), (14,), (18,), (14,), (18,), (18,), (-60,), (18,), (18,), (18,), (18,), (-60,), (18,), (18,), (18,)],dur=[0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 1.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.75],amp=[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1])
	d1 >> pluck([(-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -3), (-10, -3), (-10, -3), (-10, -3)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a6():
	d0 >> pluck([(14,), (11,), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-1, 2), (-1, 2), (-1, 2), (-1, 2), (-1, 2), (-1, 2), (-1, 2), (1,)],dur=[1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-17, -10), (-17, -10), (-17, -10), (-17, -10), (-60,), (6,), (-60,), (2,), (6,), (-60,), (2,), (6,), (2,), (6,)],dur=[0.5, 0.5, 0.5, 0.5, 2.0, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 1.25],amp=[1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1])
@structure
def a7():
	d0 >> pluck([(2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 9), (2, 9), (2, 9), (2, 9)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(6,), (-60,), (2,), (6,), (-60,), (2,), (6,), (2,), (6,), (6,), (-60,), (6,), (6,), (6,), (9,), (-60,), (9,), (9,), (6,)],dur=[0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 1.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.75],amp=[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1])
@structure
def a8():
	d0 >> pluck([(-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-60,), (2,), (-1,), (2,), (-13, -10), (-1,), (2,), (6,)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2.0, 0.5, 0.5, 0.25, 0.75],amp=[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(2,), (-1,), (-60,), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-60,), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[1.0, 2.0, 1.0, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
@structure
def a9():
	d0 >> pluck([(9,), (9,), (9,), (9,), (9,), (9,), (9,), (6,)],dur=[4.0, 0.5, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-15, -10)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a10():
	d0 >> pluck([(2,), (-1,), (2,), (-1,), (2,), (-13, -10), (-1,), (2,), (6,)],dur=[1.0, 2.0, 0.5, 0.5, 2.0, 0.5, 0.5, 0.25, 0.75],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-15, -10), (-15, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-60,), (-13, -10), (-13, -10), (-13, -10), (-11,), (-11,)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
@structure
def a11():
	d0 >> pluck([(9,), (6,), (2,), (9,), (9,), (9,), (9,), (9,), (9,), (2,)],dur=[1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-15, -10)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a12():
	d0 >> pluck([(-1,), (-15, -10), (-15, -10), (-15, -10), (4,), (4,), (4,), (4,), (4,), (4,), (4,), (4,), (4,), (4,), (4,), (4,)],dur=[3.0, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-60,), (7,), (7,), (-60,), (6,), (-60,), (4,), (-60,), (-1,), (2,)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 1.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 1.0, 1.0],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1])
@structure
def a13():
	d0 >> pluck([(2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4, 13, 16), (-60,), (4,), (4,), (4,), (4,), (4,), (4,)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(2,), (2,), (1,), (7,), (7,), (-60,), (6,), (-60,), (4,), (-60,)],dur=[1.0, 1.0, 4.0, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 0, 1, 0, 1, 0])
@structure
def a14():
	d0 >> pluck([(4,), (4,), (4,), (4,), (4,), (4,), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (4,), (4,), (4,), (4,), (4,), (4,)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-1,), (2,), (2,), (4,), (-3,), (-5,)],dur=[1.0, 1.0, 1.0, 1.0, 2.0, 2.0],amp=[1, 1, 1, 1, 1, 1])
@structure
def a15():
	d0 >> pluck([(4,), (4,), (4,), (4,), (4,), (4,), (2,), (2,), (2,), (2,), (2,), (2,), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-5,), (2,), (2,), (4,), (1,), (2,)],dur=[1.0, 1.0, 1.0, 1.0, 1.0, 3.0],amp=[1, 1, 1, 1, 1, 1])
@structure
def a16():
	d0 >> pluck([(-1, 2), (-1, 2), (-1, 2), (-1, 2), (-1, 2), (-1, 2), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (-3, 4), (2,), (2,), (2,), (2,), (2,), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(6,), (2,), (1,), (-3,), (-1,), (-3,), (-60,), (-6,), (-5,)],dur=[1.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.25, 1.0, 1.5],amp=[1, 1, 1, 1, 1, 1, 0, 1, 1])
@structure
def a17():
	d0 >> pluck([(-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-60,), (-5, 2), (-5, 2), (-60,), (-5, 2), (-60,), (-5, 2)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 1.0, 0.25, 0.25, 1.0, 0.25, 0.25, 0.25, 0.25, 2.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1])
	d1 >> pluck([(-5,), (7,), (6,), (-60,), (2,), (7,), (-60,), (6,), (-60,), (2,)],dur=[2.0, 1.0, 0.25, 0.25, 1.0, 0.25, 0.25, 0.25, 0.25, 2.5],amp=[1, 1, 1, 0, 1, 1, 0, 1, 0, 1])
@structure
def a18():
	d0 >> pluck([(-5, 2), (-60,), (-15,), (-60,), (-13,), (-60,), (-11,), (-60,), (18,)],dur=[2.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2.0],amp=[1, 0, 1, 0, 1, 0, 1, 0, 1])
	d1 >> pluck([(2,), (-60,), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[2.0, 4.0, 0.5, 0.5, 0.5, 0.5],amp=[1, 0, 1, 1, 1, 1])
@structure
def a19():
	d0 >> pluck([(18,), (14,), (21,), (21,)],dur=[1.0, 1.0, 4.0, 2.0],amp=[1, 1, 1, 1])
	d1 >> pluck([(-13, -10), (-13, -10), (-13, -10), (-13, -10), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6)],dur=[0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a20():
	d0 >> pluck([(18,), (21,), (18,), (14,), (11,), (14,), (16,), (18,)],dur=[1.0, 0.5, 0.5, 2.5, 0.5, 0.5, 0.5, 2.0],amp=[1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -3), (-10, -3), (-10, -3), (-10, -3), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a21():
	d0 >> pluck([(18,), (18,), (23,), (21,), (18,), (21,)],dur=[1.0, 0.75, 0.25, 2.0, 2.0, 2.0],amp=[1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-13, -10), (-13, -10), (-13, -10), (-13, -10), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -3), (-10, -6), (-10, -6), (-10, -6), (-10, -6)],dur=[0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a22():
	d0 >> pluck([(18,), (21,), (18,), (14,), (14,), (18,), (-60,), (14,), (18,), (-60,), (14,)],dur=[1.0, 0.5, 0.5, 3.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5],amp=[1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1])
	d1 >> pluck([(-10, -3), (-10, -3), (-10, -3), (-10, -3), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-15, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a23():
	d0 >> pluck([(18,), (14,), (18,), (18,), (-60,), (14,), (18,), (-60,), (14,), (18,), (14,), (18,), (18,), (-60,), (18,), (18,), (18,)],dur=[0.25, 0.5, 1.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 1.25, 0.25, 0.25, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])
	d1 >> pluck([(-13, -10), (-13, -10), (-13, -10), (-11,), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a24():
	d0 >> pluck([(18,), (-60,), (18,), (18,), (18,), (14,), (11,), (-17, -10), (-17, -10), (-17, -10), (-15, -10), (-1, 2), (-1, 2), (-1, 2), (-1, 2)],dur=[0.25, 0.25, 0.5, 0.25, 0.75, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -3), (-10, -3), (-10, -3), (-10, -3), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-60,), (6,), (-60,), (2,), (6,), (-60,), (2,)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2.0, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1])
@structure
def a25():
	d0 >> pluck([(-1, 2), (-1, 2), (-1, 2), (1,), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6), (2, 6)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(6,), (2,), (6,), (6,), (-60,), (2,), (6,), (-60,), (2,), (6,), (2,), (6,), (6,), (-60,), (6,), (6,), (6,)],dur=[0.25, 0.5, 1.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.5, 1.25, 0.25, 0.25, 0.5, 0.5, 0.5],amp=[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])
@structure
def a26():
	d0 >> pluck([(2, 9), (2, 9), (2, 9), (2, 9), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-5, 2), (-60,), (2,), (-1,), (2,)],dur=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2.0],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1])
	d1 >> pluck([(9,), (-60,), (9,), (9,), (6,), (2,), (-1,), (-60,), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[0.25, 0.25, 0.5, 0.25, 0.75, 1.0, 2.0, 1.0, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
@structure
def a27():
	d0 >> pluck([(-13, -10), (-1,), (2,), (6,), (9,), (9,), (9,), (9,)],dur=[0.5, 0.5, 0.25, 0.75, 4.0, 0.5, 1.0, 0.5],amp=[1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-60,), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6), (-10, -6)],dur=[0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
@structure
def a28():
	d0 >> pluck([(9,), (9,), (9,), (6,), (2,), (-1,), (2,), (-1,), (2,)],dur=[0.5, 0.5, 0.5, 0.5, 1.0, 2.0, 0.5, 0.5, 2.0],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1])
	d1 >> pluck([(-10, -3), (-10, -3), (-10, -3), (-10, -3), (-15, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-17, -10), (-15, -10), (-15, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10), (-13, -10)],dur=[0.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25],amp=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
Clock.clear()

start = Clock.mod(4)
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 8)
Clock.schedule(a2, start + 16)
Clock.schedule(a3, start + 24)
Clock.schedule(a4, start + 32)
Clock.schedule(a5, start + 40)
Clock.schedule(a6, start + 48)
Clock.schedule(a7, start + 56)
Clock.schedule(a8, start + 64)
Clock.schedule(a9, start + 72)
Clock.schedule(a10, start + 80)
Clock.schedule(a11, start + 88)
Clock.schedule(a12, start + 96)
Clock.schedule(a13, start + 104)
Clock.schedule(a14, start + 112)
Clock.schedule(a15, start + 120)
Clock.schedule(a16, start + 128)
Clock.schedule(a17, start + 136)
Clock.schedule(a18, start + 144)
Clock.schedule(a19, start + 152)
Clock.schedule(a20, start + 160)
Clock.schedule(a21, start + 168)
Clock.schedule(a22, start + 176)
Clock.schedule(a23, start + 184)
Clock.schedule(a24, start + 192)
Clock.schedule(a25, start + 200)
Clock.schedule(a26, start + 208)
Clock.schedule(a27, start + 216)
Clock.schedule(a28, start + 224)
Clock.schedule(lambda : Clock.clear(), start + 232)