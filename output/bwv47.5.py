Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 10, 9, 14, 12, 10, 9, 10, 9, 7, 14, 12, 14, 7, 9, 11, 12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([2, 3, 2, 4, 6, 7, 9, 7, 6, 7, 7, 5, 7, 9, 11, 12, 7, 7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-5, 0, -2, 0, 2, 2, 2, 2, 2, 2, 0, -2, 0, 2, 3, 5, 5, 7, 2, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-13, -12, -17, -10, -2, -6, -5, -10, -17, -5, -3, -2, -7, -10, -9, -7, -5, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([10, 9, 14, 12, 10, 9, -60, 7, 9, 10, 10, 12, 12, 14, 14, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 6, 7, 9, 2, 2, -60, 2, 7, 7, 5, 3, 5, 7, 8, 7, 5, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([2, 2, 2, -6, -5, -6, -60, -2, 0, 2, 1, 0, -2, -4, -5, -7, 5, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-5, -10, -12, -14, -15, -17, -10, -60, -17, -5, -7, -9, -4, -5, -7, -14, -14, -9],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
