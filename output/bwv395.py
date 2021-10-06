Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([13, 9, 11, 13, 14, 16, 14, 13, 13, 14, 16, 16, 11, 13, 11, 9, 8],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([9, 6, 8, 9, 11, 13, 13, 11, 9, 8, 6, 4, 9, 8, 8, 8, 6, 4, 3, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([4, 2, 2, 4, 2, 1, -1, -3, -1, 1, -3, -3, 4, 4, 5, 1, -1, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, 2, 1, -1, -3, -5, -6, -4, -6, -7, -6, -11, -13, -11, -10, -8, -10, -11, -6, -13, -8],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([4, 9, 11, 13, 14, 16, 14, 13, 11, 13, 9, 11, 13, 14, 16, 14, 13],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([-1, 4, 6, 8, 9, 11, 13, 11, 9, 8, 8, 6, 4, 4, 6, 6, 5, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, 2, 4, 6, -1, -4, 1, -1, -3, -1, 1, -1, -4, -2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-10, -11, -13, -15, -10, -8, -7, -6, -4, -3, -2, -1, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
@structure
def a2():
	d0 >> pluck([13, 14, 16, 16, 11, 13, 9, 8, 4, 9, 11, 13, 14, 16, 14, 13, 11, 9],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([6, 4, 9, 8, 6, 4, 3, 1, 6, 4, -1, 4, 6, 8, 9, 9, 8, 4],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, -3, -3, -3, -4, 1, -1, -1, -4, -3, 2, 4, 6, 4, 2, 1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-6, -11, -13, -11, -9, -8, -8, -9, -8, -10, -11, -13, -15, -13, -11, -10, -8, -8, -15],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
