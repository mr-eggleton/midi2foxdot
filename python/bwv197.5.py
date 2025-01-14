Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 11, 11, 9, 8, 6, 4, 6, 8, 9, 11, 9, 13, 14, 16, 18, 16],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 4, 4, 2, 1, -1, 1, -3, 2, 1, 6, 4, 4, 9, 11, 13, 14, 13, 11, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([1, -1, -3, -4, -3, -1, -3, -4, -1, -6, -1, -8, -3, -4, 1, 4, 4, -3, -1, 1],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-3, -4, -6, -8, -10, -11, -15, -10, -10, -11, -10, -13, -11, -6, -10, -8, -15, -3, -3, -4, -6, -4, -3],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
@structure
def a1():
	d0 >> pluck([16, 14, 13, 11, 9, 8, 6, 8, 9, 13, 13, 13, 11, 13, 9, 9, 11, 13],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([8, 6, 8, 5, 1, 2, 2, 1, 4, 4, 4, 6, 8, 6, 5, 6, 5, 6, 6, 8, 9],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([2, -4, -3, -3, -1, -8, -3, -3, -4, -3, -1, -1, -3, -4, 1, 1, 1, -1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-1, -7, -11, -6, -8, -10, -11, -13, -15, -15, -13, -11, -10, -8, -10, -11, -6, -6, -8, -10, -11],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([14, 13, 11, 9, 11, 13, 14, 13, 11, 9, 8, 6, 8, 9, 11, 9, 8, 6, 4],dur=[1.0 ,1.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([11, 11, 9, 7, 6, 6, 8, 9, 11, 9, 8, 6, 4, 3, 4, 6, 8, 6, 6, 4, 3, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0])
	d2 >> pluck([-3, -4, -6, -8, -3, -3, 2, 1, -1, 1, 3, 4, -1, -1, -1, 1, 3, 4, -1, -1, -3, -4],dur=[0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,2.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-13, -8, -15, -13, -11, -10, -10, -8, -6, -4, -3, -1, 1, -3, -1, -3, -4, -6, -8, -9, -11, -9, -8, -4, -1, -13, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
