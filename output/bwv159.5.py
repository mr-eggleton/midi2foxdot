Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 5, 3, 5, 7, 8, 10, 12, 10, 8, 7, 5, 5, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0])
	d1 >> pluck([3, 2, 0, -2, -2, 3, 1, 3, 3, 8, 7, 5, 3, 3, 2, -2],dur=[1.0 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-2, -2, -4, -5, -7, -9, 3, -4, 1, 0, 2, 3, 2, 3, 0, -2, -4, -5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0])
	d3 >> pluck([-9, -14, -12, -10, -9, -7, -5, -4, -2, 0, -2, -4, -2, -14, -9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([7, 10, 8, 7, 5, 3, 2, 3, 5, 7, 7, 8, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([3, 5, 3, 5, 7, 3, 2, 0, -1, 0, 2, 3, 3, 3, 2, 3, 5, 2, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0])
	d2 >> pluck([-2, -2, 0, 2, 3, 0, -4, -5, -5, -5, -5, -2, -2, -2, 0, -4, -7, -2, -2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-9, -10, -10, -12, -12, -12, -13, -12, -9, -5, -12, 0, -2, -4, -5, -7, -9, -10, -12, -7, -10, -14, -9],dur=[0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
@structure
def a2():
	d0 >> pluck([7, 8, 10, 8, 7, 5, 7, 5, 5, 7, 9, 10, 10, 9, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([3, 3, 4, 5, 1, 0, 0, 2, 4, 0, 0, 2, 3, 1, 3, 5, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0])
	d2 >> pluck([0, 0, -2, 0, -2, -4, -5, -4, -2, 0, -2, -2, 0, 1, 0, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-12, -14, -16, -17, -5, -7, -7, -8, -7, -12, -7, -5, -4, -5, -6, -7, -9, -7, -14],dur=[1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
@structure
def a3():
	d0 >> pluck([10, 7, 12, 10, 8, 7, 5, 7, 8, 10, 8, 7, 5, 5, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0])
	d1 >> pluck([5, 3, 5, 7, 7, 3, 5, -2, 0, 2, 2, -2, 3, 5, 7, 0, 2, 3, 0, 2, -2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0])
	d2 >> pluck([-2, -2, 3, 2, -2, 0, 2, 3, -2, -2, -4, -5, -7, -9, -10, -9, -2, -4, -5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,2.0])
	d3 >> pluck([-10, -14, -9, -9, -12, -5, -5, -7, -5, -4, -2, -9, -10, -12, -14, -16, -14, -21],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
