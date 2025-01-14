Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 11, 9, 7, 6, 4, 6, 13, 14, 14, 13, 11, 13, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d1 >> pluck([2, 2, 2, 2, 4, 4, 2, 2, 1, 2, 4, 2, 4, 6, 6, 4, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,3.0])
	d2 >> pluck([-3, -5, -3, -1, -3, -3, -1, -3, -3, -2, -1, -1, -1, -2, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-10, -5, -6, -13, -11, -10, -17, -15, -10, -11, -13, -11, -10, -8, -6, -18, -13],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([14, 13, 11, 9, 11, 13, 14, 14, 9, 11, 9, 7, 7, 6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([6, 4, 7, 6, 4, 2, 7, 7, 6, 4, 6, 6, 7, 6, 6, 4, 3],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-1, -3, -5, -1, 2, 1, -1, -3, -5, -3, -1, -3, -5, -3, 2, 2, 0, -1, -1, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-13, -8, -6, -5, -6, -8, -10, -10, -10, -5, -6, -8, -9, -8, -6, -5, -3, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
@structure
def a2():
	d0 >> pluck([14, 13, 14, 16, 14, 13, 11, 13, 6, 7, 6, 4, 9, 6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([4, 4, 4, 6, 8, 9, 9, 8, 9, 2, 1, -1, 1, 2, 2, -1, 1, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([-1, -3, -1, -3, -1, 1, -3, 6, 4, 4, -3, -5, -3, -3, -3, -3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-4, -3, -4, -6, -8, -9, -8, -15, -10, -8, -6, -5, -3, -15, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
