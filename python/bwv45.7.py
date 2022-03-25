Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 8, 6, 4, 11, 11, 13, -60, 13, 6, 6, 11, 9, 8, 6, 4],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 3, 4, 6, 8, 9, -60, 6, 4, 3, 1, 3, 4, 6, 4, 3, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, -1, -3, -1, 4, 4, -60, 1, -1, -1, -1, -1, -1, -3, -4],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-20, -8, -6, -4, -6, -8, -3, -60, -2, -1, -3, -4, -9, -8, -13, -20],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 13, 13, 11, 9, 8, -60, 6, 8, 10, 11, 13, 15, 13, 11, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([4, 4, 9, 9, 8, 6, 4, -60, 6, 6, 4, 6, 8, 6, 3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-1, -3, 1, 6, 4, 3, 4, 4, 3, -1, -60, -1, -1, 1, -6, -1, -1, -1, -2, -6],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-4, -3, -6, -1, -13, -8, -60, -9, -8, -11, -9, -8, -6, -18, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 11, 11, 16, 14, 13, -60, 13, 13, 13, 18, 16, 15, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0)])
	d1 >> pluck([6, 4, 4, 4, 6, 8, 9, -60, 9, 9, 10, 11, 11, 10, 11, -60],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0)])
	d2 >> pluck([-1, -3, -4, -6, -4, -3, -1, 4, 4, -60, 4, 6, 1, 3, 4, 6, -60],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0)])
	d3 >> pluck([-9, -8, -9, -8, -6, -4, -6, -8, -3, -60, -3, -4, -6, -8, -9, -11, -13, -60],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0)])
@structure
def a3():
	d0 >> pluck([11, 13, 11, 13, 15, 16, -60, 11, 11, 9, 8, 6, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([11, 9, 11, 11, 9, 8, 6, 4, -60, 6, 4, 4, 4, 3, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([4, 4, 4, -3, -1, -3, -4, -60, -6, -4, -3, -4, -3, -1, 1, -1, -3, -4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-4, -3, -4, -6, -13, -11, -60, -9, -8, -9, -11, -13, -15, -13, -20],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)