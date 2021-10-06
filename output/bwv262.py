Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 14, 9, 11, 9, 7, 6, 6, 9, 9, 7, 6, 4, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0])
	d1 >> pluck([2, 2, 2, 2, 2, 1, 6, 6, 2, 2, 1, -1, 1, 2, 2, 1, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-6, -6, -5, -3, -5, -6, -8, -10, -8, -10, -10, -6, -6, -5, -3, -1, -3, -5, -6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,2.0])
	d3 >> pluck([-10, -13, -18, -17, -15, -15, -22, -22, -10, -10, -8, -6, -5, -8, -3, -15, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
@structure
def a1():
	d0 >> pluck([4, 4, 6, 8, 9, 9, 8, 9, 9, 11, 13, 14, 14, 13, 13, 11, 11],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([1, 1, 2, 1, 6, 4, 2, 1, 1, 4, 6, 7, 6, 6, 6, 4, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, -3, -3, -3, -1, -1, -3, -3, -5, -3, -1, -1, -2, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-15, -15, -10, -6, -8, -10, -8, -15, -8, -13, -11, -10, -8, -6, -13],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,2.0])
@structure
def a2():
	d0 >> pluck([6, 6, 11, 9, 9, 8, 9, 11, 9, 7, 6, 4, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0])
	d1 >> pluck([2, 2, 2, 1, 2, 2, 1, 2, 2, 1, -1, 1, 2, 2, 1, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-3, -3, -5, -6, -8, -10, -6, -8, -10, -8, -5, -6, -5, -3, -1, -3, -5, -6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,2.0])
	d3 >> pluck([-10, -10, -17, -15, -13, -15, -17, -10, -8, -6, -5, -8, -3, -15, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
