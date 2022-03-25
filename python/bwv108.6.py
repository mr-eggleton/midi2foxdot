Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 11, 11, 18, 16, 18, 16, 14, 13, 11, 13, 14, 13, 14, 16, 18, 16, 14, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([6, 7, 7, 6, 8, 10, 11, 13, 11, 10, 11, 10, 11, 6, 6, 6, 11, 13, 6, 8, 10],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([2, 4, 4, 2, 7, 6, 6, 6, 6, 4, 6, 6, 4, 2, 1, -1, 2, 2, 1, 2, -1, 1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-13, -8, -6, -5, -3, -1, 2, 1, -1, -2, -6, -1, -13, -6, -10, -11, -13, -1, -2, -6, -1, 1, 2, -1, -4, -2, -1, -13, -6],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 13, 11, 11, 16, 14, 13, 14, 16, 14, 13, 11, 9, 9, 14, 13, 14, 16, 18, 16],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([11, 6, 4, 6, 8, 9, 9, 9, 8, 4, 6, 11, 13, 10, 11, 11, 11, 13],dur=[1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([6, 4, 2, 1, -1, -1, 1, 2, 4, -3, 6, 4, 2, 1, 2, 4, 6, 6, 6, 4, 2, 2, 1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-13, -1, -3, -4, -6, -8, -10, -11, -13, -15, -11, -6, -8, -10, -13, -8, -20, -15, -10, -11, -13, -1, -2, -6, -1, 1, 2, -1, -4, -2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([14, 13, 11, 13, 14, 13, 14, 16, 18, 16, 14, 13, 18, 18, 18, 16, 14, 13],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d1 >> pluck([6, 6, 6, 4, 4, 6, 7, 9, 7, 6, 6, 6, 4, 2, 6, 11, 9, 7, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
	d2 >> pluck([1, -1, -2, 2, 1, -1, -5, -3, -3, 2, 2, 1, 1, -1, -2, 1, 1, -1, -1, -3, 7],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5])
	d3 >> pluck([-1, -13, -6, -1, -3, -4, -8, -3, -5, -6, -8, -10, -11, -13, -14, -13, -6, -14, -13, -11, -10, -9, -8, -6, -5, -4, -3, -2],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)