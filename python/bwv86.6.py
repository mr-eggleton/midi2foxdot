Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 11, 11, 11, 14, 13, 11, 9, 11, 8, 4, 6, 8, 10, 11, 13, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 6, 8, 9, 8, 6, 4, 9, 8, 4, 6, 4, 4, 3, 4, 1, 6, 4, 3, 4, 3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0])
	d2 >> pluck([4, 6, 4, 3, 4, -3, -1, 1, 2, 4, 2, 1, -1, -1, -3, -4, -6, -6, -1, -2, -6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d3 >> pluck([-8, -9, -13, -8, -6, -4, -3, -8, -15, -9, -8, -6, -4, -11, -6, -8, -9, -11, -13, -6, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 16, 15, 13, 15, 16, 15, 13, 11, 11, 16, 11, 13, 8, 9, 11, 9, 8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 6, 8, 10, 11, 10, 11, 11, 6, 6, 8, 4, 6, 8, 9, 4, 6, 8, 6, 5],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, 1, -6, 6, 6, -1, -2, 3, 4, -1, 4, 4, 1, 2, 1, 1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-8, -11, -9, -8, -6, -1, -4, -8, -6, -13, -8, -4, -8, -3, -1, 1, -7, -6, -11],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)