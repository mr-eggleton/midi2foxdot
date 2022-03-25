Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([3, 10, 10, 12, 14, 15, -60, 14, 15, 14, 12, 12, 10, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0)])
	d1 >> pluck([-2, 3, 3, 3, 5, 7, -60, 5, 12, 10, 3, 7, 5, 3, 2, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0)])
	d2 >> pluck([-5, -4, -2, 0, 1, 0, -2, -4, -2, -60, -2, -2, -3, -2, -3, -7, -60],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,2.0 ,rest(1.0)])
	d3 >> pluck([-9, -7, -5, -5, -4, -5, -7, -9, -60, -14, -12, -5, -9, -7, -14, -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0)])
@structure
def a1():
	d0 >> pluck([10, 12, 10, 8, 7, 5, -60, 7, 3, 5, 7, 8, 10, 8, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([3, 3, 2, 3, -2, -2, -2, -60, 2, 2, 0, -2, -2, 3, 3, 5, 3, 2, 3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0])
	d2 >> pluck([-2, -2, -4, -5, -7, -9, -10, -60, -5, -5, -7, -9, -2, 0, -2, -2],dur=[1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-17, -16, -14, -12, -10, -9, -14, -60, -13, -12, -10, -9, -17, -19, -14, -21],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([14, 15, 14, 12, 12, 10, -60, 15, 14, 12, 10, 12, 10, 8, 7, 8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([5, 7, 5, 5, 7, 5, 3, 2, -60, 7, 7, 3, 3, 3, 5, 7, 5, 3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5])
	d2 >> pluck([2, 0, -2, -2, -3, -7, -60, 0, 0, -2, -4, -5, -5, 2, 0, 0, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-2, -2, -3, -2, -9, -7, -14, -60, -12, -5, -4, -9, -12, -10, -8, -7, -12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)