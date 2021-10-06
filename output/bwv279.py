Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 10, 11, 13, 14, 16, 14, 13, 11, 11, 7, 9, 11, 9, 7, 6, 4],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([7, 6, 6, 10, 11, 13, 11, 10, 6, 6, 4, 2, 2, 4, 4, 3, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, 2, 1, 2, 4, 6, 6, 6, 6, 4, 3, -1, -1, -3, -5, -3, -1, 0, -1, -3, -5],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -6, -8, -10, -11, -13, -14, -13, -6, -13, -9, -8, -6, -5, -8, -15, -13, -8],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 10, 11, 13, 14, 16, 14, 13, 11, 11, 7, 9, 11, 9, 7, 6, 4],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([7, 6, 6, 10, 11, 13, 11, 10, 6, 6, 4, 2, 2, 4, 4, 3, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, 2, 1, 2, 4, 6, 6, 6, 6, 4, 3, -1, -1, -3, -5, -3, -1, 0, -1, -3, -5],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -6, -8, -10, -11, -13, -14, -13, -18, -13, -9, -8, -6, -5, -8, -15, -13, -20],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([-60, 4, 7, 9, 4, 7, 9, 11, 11, 16, 15, 16, 18, 14, 13, 11],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-60, -1, 4, 2, 4, 0, -1, -3, -5, 2, 7, 6, 4, 11, 11, 10, 6],dur=[rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-60, -5, -5, 0, -3, -5, 2, 2, -1, -1, -3, -1, -1, 6, 6, 4, 2],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-60, -8, -10, -12, -13, -15, -13, -12, -10, -8, -6, -5, -5, -8, -6, -5, -10, -8, -6, -18, -13],dur=[rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([11, 12, 14, 11, 14, 9, 7, 6, 4, 11, 9, 7, 6, 4],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([7, 9, 2, 2, 0, -1, 4, 2, 2, 0, -1, 1, 3, 4, 12, 3, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([-1, -3, -5, -5, -6, -5, -3, -3, -6, -5, -8, -1, -3, -4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-8, -6, -5, -13, -12, -10, -8, -6, -4, -3, -9, -13, -8, -15, -13, -8],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.75 ,0.25 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
