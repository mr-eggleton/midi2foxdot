Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([14, 14, 9, 10, 12, 10, 9, 9, 7, 10, 10, 9, 7, 6, 7, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([7, 7, 9, 7, 7, 7, 6, 2, 2, 3, 3, 2, 2, 0, 0, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-2, 0, 2, 2, 2, 0, 2, 3, 2, 0, -2, -5, -5, -5, -6, -5, -3, -2, -6],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-5, -3, -2, -6, -5, -9, -12, -10, -17, -5, -7, -9, -10, -12, -10, -9, -15, -17, -10],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([14, 14, 9, 10, 12, 10, 9, 9, 7, 10, 10, 9, 7, 6, 7, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([2, 7, 6, 7, 7, 7, 6, 2, 2, 3, 3, 2, 2, 0, 0, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-2, 0, 2, 2, 2, 0, 2, 3, 2, 0, -2, -5, -5, -5, -6, -5, -3, -2, -6],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-17, -15, -14, -12, -10, -5, -9, -12, -10, -17, -5, -7, -9, -10, -12, -10, -9, -15, -17, -10],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
@structure
def a2():
	d0 >> pluck([9, 10, 12, 9, 10, 9, 7, 7, 5, 10, 12, 14, 14, 15, 14, 12, 12, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([6, 7, 7, 5, 5, 5, 4, 0, 5, 7, 9, 10, 10, 10, 10, 9, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 2, 0, 0, -2, 0, 2, 0, -2, -3, -2, 3, 5, 5, 3, 5, 7, 5, 3, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-10, -5, -7, -8, -7, -9, -10, -14, -12, -7, -10, -12, -14, -2, -3, -5, -9, -7, -14],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([14, 14, 12, 14, 10, 12, 14, 14, 14, 12, 10, 9, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([5, 5, 5, 3, 2, 2, 7, 6, 7, 7, 9, 7, 7, 6, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-2, -2, -3, -3, -5, -2, -3, -5, -3, -2, 0, 2, 3, 2, 3, 2, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-14, -12, -10, -9, -7, -6, -5, -7, -9, -10, -5, -3, -2, -6, -5, -12, -10, -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
