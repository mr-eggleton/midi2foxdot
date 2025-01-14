Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 9, 6, 8, 9, 11, 9, 8, 6, 6, 8, 9, 11, 4, 6, 8, 9, 6, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([1, 2, 4, -3, 2, 1, -1, 4, 3, 3, 4, 6, 6, 3, 4, 4, 6, 3, -1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, -1, 1, 2, 4, -3, -3, -4, -6, -4, -3, -1, -1, -1, 3, -4, -3, -1, 1, -1, -1, -3, -4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-3, -15, -13, -11, -10, -8, -6, -8, -9, -8, -13, -1, -3, -4, -3, -4, -6, -8, -6, -4, -3, -1, -13, -8],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 13, 13, 9, 11, 13, 14, 13, 11, 9, 11, 13, 11, 9, 9, 8, 9],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 9, 1, 6, 8, 10, 11, 4, 6, 8, 6, 4, 2, 1, 3, 4, 2, 1, 6, 4, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, 4, 6, 8, 1, 2, 4, 6, 8, 9, 4, 1, -1, -8, -6, -4, -3, -1, 1, 2, 1],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-8, -3, -4, -6, -7, -6, -8, -10, -11, -13, -11, -10, -8, -6, -4, -3, -8, -6, -8, -9, -8, -15],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
