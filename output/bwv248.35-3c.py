Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 8, 9, 8, 6, 6, 8, 9, 8, 6, 13, 11, 9, 8, 8, 9, 9, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([1, 6, 5, 6, 6, 6, 5, 1, 6, 6, 5, 6, 5, 5, 6, 6, 6, 8, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25])
	d2 >> pluck([-3, -1, 1, 1, -1, -3, -1, 1, 1, -1, -3, -3, -1, 1, 1, 1, 1, 2, 2, 4, 6],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25])
	d3 >> pluck([-6, -6, -4, -3, -1, 1, -11, -10, -10, -11, -13, -11, -18, -6, -4, -3, -1, 1, -11, -6, -8, -10, -11, -10, -13],dur=[1.0 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d4 >> pluck([-6, -6, -4, -3, -1, 1, -11, -10, -10, -11, -13, -11, -18, -6, -4, -3, -1, 1, -11, -6, -8, -10, -11, -10, -13],dur=[1.0 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a1():
	d0 >> pluck([11, 13, 13, 11, 9, 8, 6, 13, 11, 9, 8, 8, 13, 11, 9, 8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 8, 6, 5, 6, 8, 6, 6, 5, 1, 6, 6, 5, 6, 5, 6, 4, 3, 4, 6, 3, 4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([4, 2, 1, -1, -3, 2, 1, 1, 2, 2, -1, -4, 1, -3, -3, -1, 1, 3, 1, 1, -6, -1, -1],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-8, -15, -3, -4, -6, -6, -7, -6, -10, -13, -16, -11, -18, -6, -8, -10, -11, -12, -11, -15, -13, -11, -9, -13, -8],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d4 >> pluck([-8, -20, -15, -3, -4, -6, -6, -7, -6, -10, -13, -16, -11, -18, -6, -8, -10, -11, -12, -11, -15, -13, -11, -9, -13, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
