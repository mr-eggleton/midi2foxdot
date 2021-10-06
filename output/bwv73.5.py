Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 12, 14, 15, 17, 14, 10, 10, 12, 12, 14, 14, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([3, 7, 7, 7, 5, 5, 7, 9, 7, 7, 3, 5, 5, 8, 7, 5, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d2 >> pluck([0, 3, 2, 0, 0, -2, -3, 2, 3, 0, -4, -5, -5, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-12, 0, -1, 0, -3, -2, -6, -5, -9, -4, -7, -13, -13, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([19, 17, 15, 15, 14, 15, 14, 15, 17, 19, 19, 17, 14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([12, 12, 12, 10, 10, 10, 10, 10, 8, 10, 12, 10, 9, 7, 9, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([3, 5, 8, 7, 5, 7, 5, 3, 2, -2, 3, 2, 0, 3, 2, 0, -2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([0, -4, -7, -2, -14, -9, -2, -5, -7, -9, -12, -7, -14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
@structure
def a2():
	d0 >> pluck([14, 15, 14, 12, 12, 14, 12, 10, 8, 7, 12, 12, 11, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([10, 10, 7, 3, 8, 8, 7, 9, 7, 5, 3, 5, 7, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([5, 3, -2, 0, 2, 3, 5, 3, 2, -2, -2, 0, 2, 3, 2, 0, 2, 2, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-2, -5, -9, -4, -5, -7, -6, -5, -10, -9, -4, -5, -17, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)