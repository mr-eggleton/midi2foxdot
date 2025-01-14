Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 10, 9, 7, 14, 14, 12, 10, 9, -60, 12, 10, 9, 7, 9, 10, 12, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0])
	d1 >> pluck([4, 6, 7, 6, 7, 9, 10, 9, 7, 6, -60, 6, 7, 5, 3, 5, 7, 7],dur=[1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([1, 2, 2, 2, 2, 2, 2, 2, -60, 2, 2, 2, 0, -2, 3, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -10, 2, 0, -2, -3, -5, -6, -5, -10, -60, -15, -14, -12, -10, -9, -10, -12, -10],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 7, 7, 9, 5, 4, 2, 4, 5, 7, 9, -60, 9, 7],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0])
	d1 >> pluck([6, 2, 2, 4, 2, 1, 2, 0, 2, 4, 5, -60, 5, 5, 3],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5])
	d2 >> pluck([2, 0, -2, -2, -3, -3, -3, -5, -7, -5, -3, -2, 0, -60, 0, 0],dur=[0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0])
	d3 >> pluck([-10, -17, -5, -11, -10, -15, -14, -15, -17, -19, -60, -19, -12],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([10, 9, 10, 7, 6, 7, 7, 14, 10, 12, 14, 12, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 7, 7, 6, 7, 7, 0, 2, 2, 2, 2, 7, 5, 5, 7, 9, 7, 2],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, 0, 2, 2, 0, -2, -3, -5, -3, -2, -2, -3, 2, 0, -2, 3, 4, 6],dur=[0.75 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-17, -10, -14, -9, -10, -17, -5, -6, -5, -3, -2, 0, 1, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
