Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 11, 9, 7, 6, 4, 6, 13, 14, 14, 13, 14, 16, 13, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.125 ,0.125 ,1.0 ,3.0])
	d1 >> pluck([2, 2, 4, 6, -1, 1, 2, 2, 1, 2, 10, 11, 11, 11, 10, 6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-3, -1, 1, 2, -5, -3, -1, -5, -8, -3, -3, 6, 6, 2, 6, 7, 4, 6, 1, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-10, -5, -6, -1, -3, -5, -3, -10, -6, -1, -6, -5, -10, -8, -11, -6, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([6, 11, 9, 7, 6, 4, 6, 13, 14, 14, 13, 14, 16, 13, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.125 ,0.125 ,1.0 ,3.0])
	d1 >> pluck([2, 2, 4, 6, -1, 1, 2, 2, 1, 2, 10, 11, 11, 11, 10, 6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-3, -1, 1, 2, -5, -3, -1, -5, -8, -3, -3, 6, 6, 2, 6, 7, 4, 6, 1, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-10, -5, -6, -1, -3, -5, -3, -10, -6, -1, -6, -5, -10, -8, -11, -6, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
@structure
def a2():
	d0 >> pluck([14, 13, 9, 11, 13, 14, 14, 9, 11, 9, 7, 7, 6, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([11, 9, 9, 7, 6, 7, 7, 4, 2, 11, 9, 9, 6, 7, 6, 6, 4, 4, 1],dur=[1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([4, 4, 2, 2, 4, 1, 6, -1, 6, 2, 2, 2, -1, -1, -2, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-3, -4, -3, -5, -6, -10, -5, -6, -8, -3, -1, -3, -1, -5, -10, -6, -10, -5, -10, -13, -8, -8, -6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
@structure
def a3():
	d0 >> pluck([14, 13, 16, 14, 13, 11, 13, 6, 7, 6, 4, 9, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([11, 9, 4, 6, 4, 6, 2, 4, 4, 6, -1, 4, 2, 2, 1, -1, 1, 2],dur=[1.0 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,3.0])
	d2 >> pluck([4, 4, -1, -3, -3, -3, -1, -4, -3, 2, 2, 1, -1, -3, -3, -3, -3],dur=[1.0 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-4, -8, -3, -4, -6, -11, -10, -13, -8, -15, -10, -8, -6, -5, -3, -5, -3, -15, -10],dur=[0.5 ,0.5 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)