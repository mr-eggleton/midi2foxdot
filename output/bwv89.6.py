Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 10, 12, 14, 14, 14, 12, 10, 12, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([2, 2, 2, 2, 7, 6, 6, 7, 7, 6, 7, 9, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-2, -2, -3, -5, -2, 3, -3, -3, -2, 0, 2, 3, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-17, -5, -6, -5, -9, -10, -12, -14, -15, -17, -12, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([9, 10, 12, 14, 14, 12, 14, 14, 10, 12, 14, 14, 12, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([6, 7, 9, 10, 10, 10, 9, 10, 9, 7, 9, 7, 5, 5, 7, 5, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 2, 5, 5, 7, 7, 5, 5, 2, 2, 5, -2, -2, -2, -3, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-10, -5, -7, -2, -3, -5, -7, -9, -7, -14, -18, -17, -5, -7, -9, -10, -12, -14, -7, -9, -12, -7, -14],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([14, 17, 14, 14, 14, 12, 12, 12, 14, 12, 10, 12, 10, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([10, 12, 10, 9, 7, 7, 5, 4, 5, 7, 6, 6, 7, 7, 7, 6, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([5, 5, 5, 7, 9, -3, -2, -2, -3, -5, -3, -5, -3, 2, 2, 0, 2, 3, 2, 0, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-2, -3, -2, -6, -5, -8, -12, -7, -9, -10, -12, -14, -15, -17, -7, -9, -10, -12, -10, -17],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)