Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([-60, 21, 20, 21, -60],dur=[rest(6.0) ,2.0 ,1.0 ,2.0 ,rest(5.0)])
	d1 >> pluck([-60, 18, 16, 14, 16, -60],dur=[rest(6.0) ,1.0 ,1.0 ,1.0 ,2.0 ,rest(5.0)])
	d2 >> pluck([-60, 14, 9, 2, 9, -60],dur=[rest(6.0) ,1.0 ,1.0 ,1.0 ,2.0 ,rest(5.0)])
	d3 >> pluck([-60, -10, -15, -10, -15, -60],dur=[rest(6.0) ,1.0 ,1.0 ,1.0 ,2.0 ,rest(5.0)])
	d4 >> pluck([13, 14, 13, 11, 13, 14, 16, 18, 16, 14, 13, -60, 16, 14, 13, 14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
	d5 >> pluck([6, 6, 6, 4, 2, 9, 7, 6, 8, 9, 11, 4, -60, 6, 6, 4, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
	d6 >> pluck([-2, -1, -2, -1, -3, -1, 1, 2, 4, 6, 8, 1, -60, 1, -1, -3, -5, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d7 >> pluck([-6, -13, -6, -5, -6, -8, -10, -11, -13, -15, -60, -14, -13, -8, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([-60, 26, 25, 26, -60, 21],dur=[rest(2.0) ,2.0 ,1.0 ,3.0 ,rest(6.0) ,2.0])
	d1 >> pluck([-60, 14, 16, 18, 19, 21, 21, -60, 18, 16],dur=[rest(2.0) ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0 ,rest(6.0) ,1.0 ,1.0])
	d2 >> pluck([-60, 6, 9, 16, 18, -60, 14, 9],dur=[rest(2.0) ,1.0 ,1.0 ,1.0 ,3.0 ,rest(6.0) ,1.0 ,1.0])
	d3 >> pluck([-60, -10, -15, -15, -10, -60, -10, -15],dur=[rest(2.0) ,1.0 ,1.0 ,1.0 ,3.0 ,rest(6.0) ,1.0 ,1.0])
	d4 >> pluck([11, 9, 6, 7, 9, 7, 6, 13, 14, 13, 11, 13, 14, 16, 18, 16],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d5 >> pluck([2, 4, 6, 4, 2, 4, 6, 6, 4, 2, 9, 7, 6, 8, 9],dur=[0.5 ,0.5 ,3.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d6 >> pluck([-1, 1, 2, -3, -3, -2, -1, -2, -1, -3, -1, 1, 2, 4, 6],dur=[0.5 ,0.5 ,3.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d7 >> pluck([-5, -6, -1, -3, -15, -10, -11, -13, -6, -5, -6, -8, -10, -11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([20, 21, -60, 26, 25, 26],dur=[1.0 ,2.0 ,rest(7.0) ,2.0 ,1.0 ,3.0])
	d1 >> pluck([14, 16, -60, 14, 16, 18, 19, 21, 21],dur=[1.0 ,2.0 ,rest(7.0) ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([2, 9, -60, 6, 9, 16, 18],dur=[1.0 ,2.0 ,rest(7.0) ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-10, -15, -60, -10, -15, -15, -10],dur=[1.0 ,2.0 ,rest(7.0) ,1.0 ,1.0 ,1.0 ,3.0])
	d4 >> pluck([14, 13, -60, 16, 14, 13, 14, 11, 9, 6, 7, 9, 7, 6],dur=[1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d5 >> pluck([11, 4, -60, 6, 6, 4, 6, 2, 4, 6, 4, 2],dur=[1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0 ,1.0 ,3.0])
	d6 >> pluck([8, 1, -60, 1, -1, -3, -5, -3, -1, 1, 2, -3, -3],dur=[1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0 ,1.0 ,3.0])
	d7 >> pluck([-13, -15, -60, -14, -13, -8, -10, -5, -6, -1, -3, -15, -10],dur=[1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a3():
	d0 >> pluck([21, 21, 21, 26, 25, 26, 25, 23, 21, 21, 19, 18, 16, 18, 20, 21, 20, 21],dur=[1.0 ,4.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,1.0])
	d1 >> pluck([14, 16, 18, 19, 18, 19, 21, 19, 18, 21, 19, 18, 16, 14, 9, 14, 16, 18, 16, 16],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,0.25 ,0.25 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([6, 9, 14, 16, 14, 9, 2, 9, 9, 16, 18, 14, 19, 16, 21, 9, -60, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(3.0) ,1.0])
	d3 >> pluck([-10, -15, -10, -15, -10, -10, -15, -10, -15, -10, -15, -10, -60, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(3.0) ,1.0])
	d4 >> pluck([9, 7, 6, 4, 6, 2, 4, 6, 13, 14, 13, 11, 9, 11, 13, 14, 16, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d5 >> pluck([6, 4, 2, 2, 1, 2, 2, -5, -3, 9, 9, 7, 6, 6, 6, 11, 11, 9],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d6 >> pluck([-3, -3, -3, -3, -3, -3, -1, 1, -6, 4, 2, -5, 2, 4, 6, 6, 2, -1, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d7 >> pluck([-10, -10, -11, -10, -15, -10, -8, -6, -8, -10, -14, -10, -8, -6, -8, -10, -11, -13, -8, -15],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a4():
	d0 >> pluck([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, -60, 25, 26, -60, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,rest(4.0) ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0])
	d1 >> pluck([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, -60, 16, 18, -60, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,rest(4.0) ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0])
	d2 >> pluck([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, -60, 9, 9, -60, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,rest(4.0) ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0])
	d3 >> pluck([-10, -10, -10, -15, -15, -15, -15, -15, -15, -15, -60, -15, -10, -60],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,rest(8.0)])
	d4 >> pluck([18, 16, 13, 14, 16, 11, 9, 7, 6, 4, 9, 11, 13, 14, 16, 14, 13, 11],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d5 >> pluck([9, 9, 9, 4, 6, 7, 6, 4, 2, 4, 2, 1, 1, 9, 8, 6, 4, 6, 7, 6, 11, 10, 6],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d6 >> pluck([2, 1, 6, 4, 2, 1, -1, -8, -3, -3, -3, -3, 4, 2, 4, 2, 1, 1, -1, 1, 4, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d7 >> pluck([-10, -3, -15, -13, -11, -10, -8, -10, -11, -13, -11, -15, -10, -3, -4, -6, -8, -6, -5, -14, -13, -18, -13],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(lambda : Clock.clear(), start + 80)
