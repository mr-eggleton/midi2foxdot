Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([14, 9, 11, 13, 14, 16, 18, 16, 14, 13, 14, -60, 18, 16, 14, 13, 11],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([6, 7, 9, 7, 9, 10, 11, 13, 6, 4, 4, 6, -60, 9, 9, 7, 6, 7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, 2, 2, 2, 2, 1, 2, 1, -1, -3, -3, -60, 2, 1, 2, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-10, -8, -6, -5, -6, -4, -2, -1, -3, -4, -3, -10, -60, 2, -3, -1, -8],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 11, 13, 14, 16, 16, 14, 13, 11, -60, 18, 19, 16, 18],dur=[1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([6, 7, 6, 8, 10, 11, 9, 7, 6, 4, 2, -60, 11, 11, 9, 9],dur=[1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([1, 2, 4, -2, -1, 1, 1, -1, -2, -1, -60, 2, 2, -1, 1, 1, -3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-6, -6, -8, -10, -11, -13, -14, -11, -6, -5, -6, -8, -6, -13, -60, -1, -8, -3, -10],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([14, 16, 18, 11, 18, 19, 16, 18, 14, 16, 18, 11, -60, 14, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0])
	d1 >> pluck([7, 7, 6, 6, 11, 11, 9, 9, 7, 6, 4, 9, 7, -60, 6, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0])
	d2 >> pluck([-1, -1, 1, 2, 6, 4, 4, 2, 2, 1, -1, -1, -1, -60, -1, -1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-5, -6, -8, -14, -13, 2, 2, 1, 1, -1, -3, -5, -6, -8, -9, -8, -60, -13, -11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([11, 9, 11, 7, 7, 6, -60, 11, 9, 14, 14, 13, 14, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0)])
	d1 >> pluck([6, 8, 1, 6, 6, 4, 3, -60, 2, 9, 9, 7, 6, -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0)])
	d2 >> pluck([-3, -4, -6, -6, -5, -3, -1, 1, 3, -60, -1, 1, 2, 1, 2, 4, 6, 4, 2, -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(2.0)])
	d3 >> pluck([-9, -7, -6, -9, -8, -6, -5, -3, -1, -60, -5, -6, -5, -3, -15, -10, -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(2.0)])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
