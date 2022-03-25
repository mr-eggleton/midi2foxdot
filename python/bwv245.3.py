Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 7, 6, 2, 7, 9, 10, 10, 12, 10, 9, 9, 10, 12, 14, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([2, 3, 2, 0, 2, -3, 2, 4, 6, 7, 7, 9, 7, 6, 6, 7, 9, 10],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, -2, -3, -5, -3, -6, -5, 0, 2, 2, 3, 2, 2, 2, 2, 3, 5, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-5, -12, -10, -9, -10, -12, -14, -15, -17, -5, -6, -5, -10, -10, -5, 0, -2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([10, 15, 15, 14, 13, 12, 12, 10, 10, 9, 7, 5, 2, 3, 5, 5, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([5, 7, 9, 10, 10, 10, 10, 9, 5, 7, 5, 3, 2, 4, 2, -3, 2, 3, 5, 5, 3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([2, 0, -2, -2, 0, 2, -2, 7, 5, 3, 2, 2, 0, -2, -3, -7, -2, -2, -2],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-4, -5, -6, -7, -8, -7, -14, -17, -12, -11, -10, -12, -14, -12, -10, -14, -9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)