Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([14, 14, 13, 11, 9, 14, 16, 18, 18, 18, 18],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([9, 11, 9, 7, 6, 6, 11, 9, 9, 13, 11, 11],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([6, 6, 6, 2, 2, 2, 1, 2, 1, 2, 2],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d3 >> pluck([-10, -13, -10, -6, -5, -1, 2, -1, -5, -3, -10, -2, -1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
@structure
def a1():
	d0 >> pluck([16, 18, 19, 18, 16, 14, 16, 18, 16, 14, 11],dur=[2.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([11, 9, 9, 9, 14, 9, 9, 11, 9, 9, 11, 9, 7, 6, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([2, 1, 2, 4, -3, 2, 1, 6, 4, 2, 2, 1, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-4, -3, -6, -11, -10, -6, -3, -1, 1, 2, -5, -3, -1, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([13, 14, 21, 18, 14, 16, 19, 18, 16, 14],dur=[2.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([11, 10, 11, 9, 9, 11, 9, 9, 9, 7, 6],dur=[1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d2 >> pluck([7, 6, 6, 4, 6, 6, 4, 1, -3, -1, 1, -3],dur=[1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-8, -6, -13, 1, 2, 1, -1, 1, -1, -3, 2, -5, -3, -10],dur=[1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)