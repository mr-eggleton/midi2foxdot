Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([10, 9, 7, 5, 5, 7, 9, 10, 12, 10, 9, 7, 9, 10, 7, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([5, 5, 4, 0, 0, 5, 6, 7, 9, 7, 5, 0, 0, 0, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([2, 0, 0, -2, -3, -3, -2, 3, 2, 2, 2, 2, 4, 5, 5, 4, 2, 4, -3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0])
	d3 >> pluck([-14, -7, -12, -19, -9, -11, -12, -5, -6, -5, 2, 0, -2, -3, -5, -7, 0, -12, -7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([-60, 10, 9, 10, 12, 12, 14, 12, 10, 12, 5, 7, 9, 10, 12, 14, 12, 10],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-60, 2, 3, 5, 5, 5, 5, 3, 1, 0, 5, 5, 4, 2, 7, 9, 10],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-60, -7, 0, 2, -3, -3, -4, -5, 3, 3, 2, 7, 5, 5, 3, 2],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-60, -10, -12, -14, -7, -7, -14, -9, -16, -15, -13, -11, -10, -8, -6, -5, -7],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)