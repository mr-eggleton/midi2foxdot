Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 11, 13, 11, 9, 8, 6, 4, 9, 11, 13, 14, 13, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 9, 3, 4, 6, 6, 4, 4, 3, -1, 6, 6, 4, 6, 11, 11, 9, 9, 8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([1, 4, 4, 6, 6, 8, 1, -1, -1, 1, -1, -3, -4, 1, -1, -1, -3, -3, -4, 4, 4, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-15, -16, -15, -13, -11, -9, -8, -15, -13, -20, -18, -16, -15, -13, -11, -10, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 13, 14, 16, 14, 13, 11, 13, 16, 16, 18, 16],dur=[4.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 9, 9, 7, 7, 6, 8, 10, 11, -1, 6, 4, 9, 7, 6, 8],dur=[4.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([1, 4, -1, -1, -2, -1, -6, 6, 4, -2, -3, -1, 1, 1, -1, -1, 1],dur=[4.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-15, -15, -13, -11, -10, -8, -6, -5, -6, -11, -13, -15, -10, -8],dur=[4.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([14, 13, 11, 13, 14, 16, 14, 13, 11, 9, 11, 13, 9, 13, 14, 16],dur=[1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([9, 4, 6, 8, 9, 11, 9, 8, 8, 6, 6, 8, 9, 8, 6, 10, 11, 6],dur=[0.5 ,1.0 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([1, -1, 1, 3, 4, 4, 4, -3, -1, 1, 1, 2, -1, 6, 5, 1, 6, -1, 1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-6, -4, -3, -8, -3, -3, -4, -6, -7, -6, -8, -10, -15, -13, -11, -18, -18, -16, -14],dur=[0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
