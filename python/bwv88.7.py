Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 11, 13, 14, 13, 11, 13, 10, 6, 9, 9, 7, 6, 11, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 4, 6, 6, 6, 7, 9, 7, 7, 6, 1, 1, 2, 4, 4, 6, 4, 2, 1, 2],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-1, 1, 2, 1, -1, 1, 2, 4, 4, 2, 1, -2, -3, -3, -1, 1, 1, -1, -3, -5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-13, -1, -2, -1, -6, -5, -6, -8, -6, -18, -6, -11, -13, -15, -10, -5, -6, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([10, 11, 13, 14, 16, 18, 16, 18, 19, 16, 16, 14, 18, 16, 14, 13],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 2, 6, 6, 11, 9, 7, 6, 11, 11, 9, 7, 6, 9, 10, 11, 4, 3],dur=[1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-6, -6, -2, -1, 7, 6, 4, 2, 2, 2, -1, 1, -3, -3, -1, 1, -6, -5, -3, -6],dur=[1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-6, -13, -6, -1, 1, 2, 1, -1, -3, -5, -3, -10, -10, -11, -13, -15],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
