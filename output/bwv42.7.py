Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 6, 6, 5, 6, 8, 9, 8, 6, 9, 11, 11, 13, 11, 9, 11, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([1, 2, 2, 1, 1, 6, 6, 5, 1, 6, 4, 6, 8, 9, 9, 8, 6, 8, 9],dur=[1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0])
	d2 >> pluck([-3, -3, -3, -4, -1, -3, -4, -6, 1, -1, -3, 1, -1, 4, 4, 2, 1, -1, 4, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-6, -8, -10, -11, -13, -11, -9, -7, -6, -13, -11, -18, -6, -4, -6, -8, -3, -4, -6, -8, -10, -8, -15],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([13, 13, 11, 13, 11, 9, 11, 9, 8, 6, 6, 8, 9, 9, 11, 9, 8, 6, 6],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([9, 9, 5, 6, 8, 6, 6, 4, 3, 3, 5, 6, 6, 8, 6, 5, 6, 4, 2, 1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([4, 4, 2, 2, 1, 1, -1, -1, -1, -1, 1, 2, 2, 1, -1, -3, -2, -1, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-3, -4, -6, -4, -6, -7, -6, -8, -9, -8, -13, -1, -6, -8, -10, -11, -13, -11, -10, -11, -13, -6],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 13, 11, 6, 8, 9, 8, 6, 8, 6, 6, 6, 4, 9, 11, 13, 11, 9, 11],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 4, 2, 4, 6, 6, 5, 1, 1, 1, 4, 2, 2, 1, 1, 6],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, -1, 1, 2, 1, 1, -1, -3, -3, -3, -4, -6, -4, -3, -4, -3, -3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-8, -3, -4, -3, -1, -3, -1, 1, -11, -6, -18, -16, -15, -13, -11, -11, -10, -11, -13, -15, -7, -6, -11, -10, -13],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a3():
	d0 >> pluck([11, 13, 14, 13, 11, 13, 14, 11, 9, 9, 13, 13, 11, 9, 11, 13],dur=[1.0 ,2.0 ,2.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([4, 4, 11, 4, 6, 4, 4, 4, 8, 9, 8, 6, 6],dur=[1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, -4, -3, -3, -3, -6, -4, 2, 1, 1, 6, 4, 2, 1],dur=[1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-8, -15, -13, -11, -10, -8, -20, -15, -7, -6, -6, -4, -2],dur=[1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5])
@structure
def a4():
	d0 >> pluck([14, 13, 16, 13, 14, 13, 11, 13, 13, 14, 13, 14, 16, 14, 13, 11, 9],dur=[1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([6, 5, 6, 8, 11, 11, 9, 9, 8, 9, 8, 9, 11, 13, 13, 11, 9, 4, 4, 6, 4, 2, 1],dur=[0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-1, -4, -3, -1, 4, 4, 4, 2, 1, -1, -3, -4, -6, -4, -3, -1, -3, -3, -4, -8],dur=[0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-1, -6, -8, -8, -8, -8, -8, -6, -4, -3, -10, -8, -15],dur=[1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a5():
	d0 >> pluck([9, 13, 13, 9, 11, 9, 8, 6, 4, 6, 8, 9, 6, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([1, 4, 4, 6, 6, 6, 4, 4, 2, 1, 2, 4, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-8, -3, -3, -3, 2, 1, -1, -1, -4, -3, -1, 1, -1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-15, -15, -13, -11, -15, -10, -11, -10, -8, -6, -4, -3, -1, -11, -13, -15, -13, -11, -10],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(lambda : Clock.clear(), start + 96)
