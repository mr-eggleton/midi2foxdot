Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([-60, 23, 21, 21, 19, 19, 28, 26, 26, 19],dur=[rest(10.5) ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25])
	d1 >> pluck([-60, 11, 9, 9, 7, 7, 16, 14, 14, 7],dur=[rest(10.5) ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25])
	d2 >> pluck([-60, 7, 6, 6, 2, 2, 6, 7],dur=[rest(10.5) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d3 >> pluck([-60, 2, 0, 0, -1, -1, 0, -1],dur=[rest(10.5) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d4 >> pluck([-60, -5, -5],dur=[rest(10.5) ,3.0 ,2.5])
	d5 >> pluck([19, 18, 16, 18, 14, 16, 18, 19, -60],dur=[1.5 ,1.5 ,1.5 ,1.5 ,1.5 ,1.5 ,1.5 ,1.5 ,rest(4.0)])
	d6 >> pluck([11, 9, 11, 9, 9, 7, 7, 12, 11, 9, 11, -60],dur=[1.5 ,1.5 ,1.0 ,0.5 ,1.5 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(4.0)])
	d7 >> pluck([2, 2, 2, 1, 2, 0, 0, -1, -1, -3, 2, 2, -60],dur=[1.5 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,1.5 ,rest(4.0)])
	d8 >> pluck([-5, 2, -5, -3, -10, -5, -12, -10, -17, -60],dur=[1.5 ,1.5 ,1.0 ,0.5 ,1.5 ,1.5 ,1.5 ,1.5 ,1.5 ,rest(4.0)])
	d9 >> pluck([-5, -1, 2, 2, 1, 2, -5, -8, -3, -10, -8, -6, -5, -6, -5, -12, -13, -12, -10, -12, -10, -17, -60],dur=[0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(4.0)])
@structure
def a1():
	d0 >> pluck([18, 19, 28, 26, 26, 19, 18, 19, -60, 19],dur=[0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(10.5) ,0.5])
	d1 >> pluck([6, 7, 16, 14, 14, 7, 6, 7, -60, 11],dur=[0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(10.5) ,0.5])
	d2 >> pluck([0, 2, 6, 7, 0, 2, -60, 4],dur=[0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(10.5) ,0.5])
	d3 >> pluck([-3, -1, 0, -1, -3, -1, -60, 7],dur=[0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(10.5) ,0.5])
	d4 >> pluck([-5, -5, -60, 4],dur=[3.5 ,1.5 ,rest(10.5) ,0.5])
	d5 >> pluck([-60, 19, 19, 14, 14, 12, 11, 12, 14, 12, 11],dur=[rest(5.0) ,1.5 ,1.5 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,1.5 ,0.5])
	d6 >> pluck([-60, 11, 11, 11, 9, 7, 9, 4, 4, 7, 6, 7],dur=[rest(5.0) ,1.5 ,1.5 ,1.5 ,1.5 ,1.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.5])
	d7 >> pluck([-60, 2, 4, 6, 7, 2, 2, 4, -3, -1, 0, 4, 3, 4],dur=[rest(5.0) ,1.5 ,1.5 ,1.0 ,0.5 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.5])
	d8 >> pluck([-60, -5, -6, -8, -1, -6, -5, -8, -6, -4, -3, -8],dur=[rest(5.0) ,1.0 ,0.5 ,1.5 ,1.5 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,0.5])
	d9 >> pluck([-60, -17, -13, -8, -8, -10, -8, -13, -10, -6, -6, -8, -6, -5, -6, -8, -6, -3, -4, -3, -15, -8],dur=[rest(5.0) ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.0 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([19, 18, 18, 16, 16, 24, 23, 23, 16, 15, 16, 24, 23, 23, 16, 15, 16, -60],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(6.0)])
	d1 >> pluck([11, 15, 15, 16, 16, 19, 18, 21, 19, 16, 15, 18, 16, -60],dur=[0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(6.0)])
	d2 >> pluck([4, 6, 6, 7, 7, 16, 15, 18, 11, 7, 6, 9, 7, -60],dur=[0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(6.0)])
	d3 >> pluck([7, 6, 6, 4, 4, 12, 11, 11, 4, 3, 4, 12, 11, 11, 4, 3, 4, -60],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(6.0)])
	d4 >> pluck([4, 4, 4, -60],dur=[5.5 ,3.0 ,1.5 ,rest(6.0)])
	d5 >> pluck([11, -60, 11, 16, 16, 14, 16],dur=[1.0 ,rest(9.0) ,1.5 ,1.5 ,1.5 ,1.0 ,0.5])
	d6 >> pluck([7, -60, 7, 7, 7, 9, 11, 9],dur=[1.0 ,rest(9.0) ,1.5 ,1.5 ,1.0 ,0.5 ,1.0 ,0.5])
	d7 >> pluck([4, -60, 4, 4, 2, 0, -1, 1],dur=[1.0 ,rest(9.0) ,1.5 ,1.0 ,0.5 ,1.5 ,1.0 ,0.5])
	d8 >> pluck([-8, -60, -8, -10, -12, -10, -8, -12, -5],dur=[1.0 ,rest(9.0) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5])
	d9 >> pluck([-8, -60, -8, -10, -8, -12, -8, -5, -5, -6, -5, -17, -13, -10],dur=[1.0 ,rest(9.0) ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5])
@structure
def a3():
	d0 >> pluck([-60, 18, 16, 16, 14, 14, 23, 21, 21, 14, 13, 14, 23, 21, 21, 14, 13, 14, -60],dur=[rest(4.5) ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(1.0)])
	d1 >> pluck([-60, 21, 19, 19, 18, 18, 13, 14, 19, 18, 13, 14, 7, 6, -60],dur=[rest(4.5) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(1.0)])
	d2 >> pluck([-60, 6, 4, 4, 2, 2, 11, 9, 9, 2, 1, 2, 11, 9, 9, 2, 0, 2, -60],dur=[rest(4.5) ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(1.0)])
	d3 >> pluck([-60, 9, 13, 13, 14, 14, 7, 6, 4, 2, 7, 6, 4, 2, -60],dur=[rest(4.5) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(1.0)])
	d4 >> pluck([-60, 2, 2, 2, -60],dur=[rest(4.5) ,3.0 ,6.0 ,1.5 ,rest(1.0)])
	d5 >> pluck([18, 19, 18, 16, 14, -60, 19],dur=[1.5 ,1.0 ,0.5 ,1.5 ,1.5 ,rest(9.0) ,1.0])
	d6 >> pluck([9, 11, 11, 9, 11, 9, 9, -60, 11],dur=[1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(9.0) ,1.0])
	d7 >> pluck([2, -5, 2, 2, 1, 6, -60, 4],dur=[1.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(9.0) ,1.0])
	d8 >> pluck([-6, -1, -8, -6, -5, -3, -10, -60, -8],dur=[1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.5 ,rest(9.0) ,1.0])
	d9 >> pluck([-10, -11, -10, -20, -11, -10, -17, -20, -15, -22, -60, -8, -6],dur=[0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,1.5 ,rest(9.0) ,0.75 ,0.25])
@structure
def a4():
	d0 >> pluck([-60, 23, 21, 21, 19, 19, 28, 26, 26, 19, 18, 19],dur=[rest(9.5) ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.5])
	d1 >> pluck([-60, 11, 9, 9, 7, 7, 16, 14, 14, 7, 6, 7],dur=[rest(9.5) ,1.0 ,0.5 ,1.0 ,0.5 ,0.75 ,0.25 ,0.5 ,0.75 ,0.25 ,0.5 ,0.5])
	d2 >> pluck([-60, 7, 6, 6, 2, 2, 6, 7, 0, 2],dur=[rest(9.5) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-60, 2, 0, 0, -1, -1, 0, -1, -3, -1],dur=[rest(9.5) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5])
	d4 >> pluck([-60, -5, -5],dur=[rest(9.5) ,6.0 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(lambda : Clock.clear(), start + 80)
