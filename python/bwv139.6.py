Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 6, 8, 9, 11, 11, 9, 8, 6, 11, 13, 15, 16, 15, 13, 13, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([-1, 4, 4, 3, 4, 4, -1, -1, 1, 3, 6, 6, 6, 4, 6, 8, 6, 4, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d2 >> pluck([-4, -3, -1, -3, -4, -4, -6, -4, -3, -1, 3, 1, -2, -1, -1, -1, -2, -1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-20, -8, -6, -4, -11, -9, -8, -13, -1, -2, -4, -6, -4, -6, -8, -6, -18, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([4, 6, 8, 9, 11, 11, 9, 8, 6, 11, 13, 15, 16, 15, 13, 13, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([-1, 4, 4, 3, 4, 4, -1, -1, 1, 3, 6, 6, 6, 4, 6, 8, 6, 4, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d2 >> pluck([-4, -3, -1, -3, -4, -4, -6, -4, -3, -1, 3, 1, -2, -1, -1, -1, -2, -1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-20, -8, -6, -4, -11, -9, -8, -13, -1, -2, -4, -6, -4, -6, -8, -6, -18, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 16, 15, 13, 11, 9, 8, 6, 11, 9, 8, 6, 8, 9, 8, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 6, 8, 9, 11, 4, 6, 8, 1, 3, 4, 3, 8, 6, 4, 4, 4, 3, 4, 4, 3, -1],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, 1, 1, -1, -3, -3, -4, -3, -1, 1, 3, 3, 1, -1, 1, -1, -3, -1, -3, -4],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -9, -11, -6, -4, -3, -9, -7, -6, -4, -2, -1, -4, -11, -9, -8, -15, -13, -11, -13, -15, -13, -20],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
