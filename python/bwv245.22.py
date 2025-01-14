Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 6, 8, 9, 11, 11, 9, 8, 6, 11, 13, 15, 16, 15, 13, 13, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([-1, 4, 4, 4, 4, 4, 3, 4, 3, 6, 6, 10, 11, 6, 6, 8, 8, 10, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, -1, 1, 2, 1, -1, 1, -1, -1, 3, 1, 6, -1, 1, 3, 4, 4, 3, 1, 3],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-20, -8, -11, -16, -11, -18, -16, -15, -13, -1, -2, -4, -6, -4, -2, -1, -8, -6, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 16, 15, 13, 11, 9, 8, 6, 6, 11, 9, 8, 6, 8, 9, 8, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 13, 11, 9, 8, 8, 6, 4, 3, 2, 0, -1, -3, -1, 0, -1, 4, 3, -1],dur=[1.0 ,1.0 ,1.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d2 >> pluck([4, 8, 8, 8, 6, 6, 3, 4, -1, -1, -1, -4, -6, -8, -7, -6, -6, -4, -3, -1, -6, -4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -9, -11, -16, -15, -13, -11, -9, -8, -13, -13, -12, -11, -10, -9, -8, -13, -20],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
