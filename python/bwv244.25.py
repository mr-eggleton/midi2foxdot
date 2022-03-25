Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 7, 9, 11, 9, 14, 14, 13, 14, 14, 13, 11, 16, 14, 13, 13, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([2, 2, 2, 2, 2, 4, 6, 7, 9, 9, 8, 9, 7, 9, 11, 11, 11, 10, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-1, -3, -5, -6, -5, -3, -1, -3, 4, 6, 4, 2, 4, 6, 7, 7, 6, 7, 6, 4, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-1, -6, -5, -10, -8, -6, -5, -3, -15, -10, -13, -15, -8, -6, -5, -3, -1, -8, -6, -13],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 11, 11, 13, 11, 9, 9, 8, 9, 9, 11, 13, 14, 13, 11, 13],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([6, 4, 6, 8, 8, 6, 6, 4, 4, 6, 6, 4, 4, 2, 2, 4, 6, 8, 5, 6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([2, 1, -1, 4, 2, 1, 1, -1, 1, 2, 1, 2, 2, 1, 1, -1, -1, -2, -2, -4, -6, -1, 2, -4, -2],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-1, -3, -4, -6, -8, -7, -6, -8, -9, -8, -15, -10, -16, -14, -13, -11, -10, -13, -6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([6, 7, 9, 11, 9, 14, 14, 13, 14, 14, 13, 11, 16, 14, 13, 13, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([6, 6, 6, 5, 6, 6, 4, 6, 7, 6, 6, 4, 6, 8, 10, 11, 11, 11, 10, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 1, 2, -1, 1, 2, 1, -1, -3, -3, -3, -1, 1, 3, 4, -1, 1, 2, -4, 1, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-1, -3, -4, -6, -1, -3, -4, -3, -10, -6, -4, -3, -4, -5, -6, -7, -6, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)