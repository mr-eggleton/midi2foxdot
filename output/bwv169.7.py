Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 11, 11, 9, 8, 6, 4, 6, 8, 9, 13, 14, 16, 18, 16],dur=[1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 4, 4, 4, 2, 4, 2, 6, 4, 4, 9, 9, 9, 11, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([1, -1, -3, -4, -3, -1, 1, -3, -3, -3, 2, 1, -1, 1, 4, 4, 2, 1, -1],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-3, -4, -6, -8, -10, -11, -13, -15, -10, -11, -13, -8, -15, -3, -1, 1, 2, -4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([16, 14, 13, 11, 9, 8, 6, 8, 9, 13, 13, 13, 11, 13, 9, 9, 11, 13],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([8, 9, 4, 2, 1, -1, 1, 4, 6, 8, 8, 6, 5, 6, 5, 6, 5, 6, 6, 8, 6],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([4, 4, 2, 1, -1, -3, -8, -8, -3, -4, -3, -1, -1, -3, -4, 1, 1, 2, 2, 1],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-8, -3, -11, -10, -8, -15, -3, -7, -6, -10, -11, -6, -10, -11, -13, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([14, 13, 11, 13, 9, 11, 13, 14, 13, 11, 9, 8, 6, 4, 9, 11, 13, 11, 9, 8],dur=[1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d1 >> pluck([4, 4, 2, 11, 9, 8, 9, 4, 2, 1, -1, -3, 4, 4, 6, 6, 4],dur=[1.0 ,2.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5])
	d2 >> pluck([-1, -3, -5, -6, -8, -6, -8, -1, -3, -3, -4, -6, -8, -4, -3, -4, -6, -1, -1],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-16, -15, -10, -4, -6, -8, -3, -11, -10, -10, -11, -9, -13, -11, -9, -8, -16],dur=[1.0 ,2.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
