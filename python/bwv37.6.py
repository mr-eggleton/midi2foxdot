Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 9, 9, 11, 7, 6, 4, 11, 13, 11, 9, 8, 6, 8, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([1, 2, 4, 4, 6, 6, 4, 3, -1, 8, 9, 8, 1, 3, 4, 4, 3, -1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, -3, -1, 1, 2, 1, -1, -1, -3, -4, -3, -4, 4, 4, 4, 3, 1, -1, -3, -1, 1, -1, -3, -4, -3, -4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.25 ,0.25 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.25 ,0.25 ,0.5 ,1.0])
	d3 >> pluck([-6, -11, -15, -10, -9, -8, -13, -8, -8, -15, -8, -6, -4, -3, -1, -13, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([4, 9, 9, 9, 11, 8, 6, 4, 11, 13, 11, 9, 8, 6, 8, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-1, 1, 2, 4, 3, 4, 6, -1, 4, 3, 4, 4, 4, 4, 4, 3, 1, 3, -1],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, -5, -6, -8, -6, -6, -4, -3, -1, -3, -4, -1, -3, -1, 1, -1, 3, 4, -1, -4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.75 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-10, -11, -12, -13, -11, -9, -8, -13, -8, -4, -3, -4, -11, -9, -8, -15, -13, -8],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([16, 14, 13, 11, 9, 9, 11, 13, 11, 13, 14, 13, 11, 10, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([8, 6, 4, 6, 8, 9, 7, 6, 8, 9, 8, 10, 11, 10, 11, 6, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([1, -3, -1, 1, 2, 4, 4, 2, 1, 2, 4, 4, 6, 4, 6, 4, 2, 1, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,3.0])
	d3 >> pluck([-11, -6, -4, -3, -8, -10, -11, -10, -15, -8, -11, -13, -11, -10, -8, -6, -13],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
@structure
def a3():
	d0 >> pluck([4, 9, 11, 13, 14, 16, 14, 13, 11, 14, 13, 11, 16, 14, 13, 11, 9, 11, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([4, 1, 4, 4, 6, 4, 6, 8, 6, 4, 4, 6, 8, 9, 4, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5])
	d2 >> pluck([-4, -6, -4, -3, -3, -1, 1, -1, -3, 4, -3, -1, 1, 2, 4, -1, -3, -3, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-11, -6, -8, -3, -6, -11, -10, -8, -6, -4, -3, -4, -6, -8, -10, -11, -13, -15, -13, -11, -10, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
