Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([-60],dur=[rest(16)])
	d1 >> pluck([-60],dur=[rest(16)])
	d2 >> pluck([-60],dur=[rest(16)])
	d3 >> pluck([12, 11, 9, 7, 6, 4, 9, 9, 7, 12, 11, 9, 7, 6, 4, 9, 9, 7],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([4, 2, 4, 5, 4, 2, 0, 0, 5, 4, 6, 7, 3, 4, -1, 4, 3, 4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d5 >> pluck([-5, -3, -1, 0, 2, 0, -1, 0, -1, -3, -1, 0, 0, 0, 2, 4, 6, -1, -3, -5, -5, -6, -8, 0, -1, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
	d6 >> pluck([-12, -5, -10, -8, -3, -5, -7, -5, -3, -1, 0, -3, -5, -6, -8, -10, -12, -15, -18, -13, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d7 >> pluck([-60],dur=[rest(16)])
@structure
def a1():
	d0 >> pluck([-60],dur=[rest(16)])
	d1 >> pluck([-60],dur=[rest(16)])
	d2 >> pluck([-60],dur=[rest(16)])
	d3 >> pluck([7, 9, 11, 12, 14, 16, 14, 12, 12, 11, 9, 7, 6, 4, 9, 9, 7],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([4, 4, 2, 0, -1, -3, 9, 9, 7, 5, 4, 4, 2, 4, 5, 4, 2, 0, 0, 5, 4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d5 >> pluck([0, -1, -3, 4, 4, 2, 0, 0, -1, -5, -5, -3, -1, 0, 2, 0, -1, 0, -1, -3, -1, 0, 0],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d6 >> pluck([-8, -6, -4, -3, -5, -7, -10, -5, -12, -12, -5, -10, -8, -3, -5, -7, -5, -3, -1, 0],dur=[1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d7 >> pluck([-60],dur=[rest(16)])
@structure
def a2():
	d0 >> pluck([-60],dur=[rest(16)])
	d1 >> pluck([-60],dur=[rest(16)])
	d2 >> pluck([-60],dur=[rest(16)])
	d3 >> pluck([12, 11, 9, 7, 6, 4, 9, 9, 7, 7, 9, 11, 12, 14, 16, 14, 12],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d4 >> pluck([6, 7, 3, 4, -1, 4, 3, 4, 4, 4, 2, 0, -1, -3, 9, 9, 7, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d5 >> pluck([0, 2, 4, 6, -1, -3, -5, -5, -6, -8, 0, -1, -1, 0, -1, -3, 4, 4, 2, 0, 0, -1, -5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d6 >> pluck([-3, -5, -6, -8, -10, -12, -15, -18, -13, -8, -8, -6, -4, -3, -5, -7, -10, -5, -12],dur=[1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d7 >> pluck([-60],dur=[rest(16)])
@structure
def a3():
	d0 >> pluck([-60],dur=[rest(16)])
	d1 >> pluck([-60],dur=[rest(16)])
	d2 >> pluck([-60],dur=[rest(16)])
	d3 >> pluck([12, 12, 14, 12, 11, 9, 11, 12, 12, 11, 11, 12, 14, 12, 11, 9, 11, 12, 12, 11],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([4, 5, 5, 4, 2, 0, -1, -3, 6, 7, 7, 7, 5, 4, 2, 4, 5, 7, 9, 2, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d5 >> pluck([-5, -3, -3, -1, 0, 2, 4, 2, 0, 2, 2, 2, -5, -5, -5, 2, 0, -1, -3, -5],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d6 >> pluck([-12, -7, -8, -10, -3, -5, -6, -8, -10, -5, -5, -7, -8, -10, -12, -13, -12, -10, -8, -6, -5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d7 >> pluck([-60],dur=[rest(16)])
@structure
def a4():
	d0 >> pluck([-60],dur=[rest(16)])
	d1 >> pluck([-60],dur=[rest(16)])
	d2 >> pluck([-60],dur=[rest(16)])
	d3 >> pluck([16, 17, 16, 14, 16, 14, 12, 12, 11, 12, 11, 12, 11, 9, 7, 7, 6, 7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([4, 2, 0, 7, 5, 4, 9, 9, 7, 7, 7, 9, 7, 6, 4, 4, 2, 2],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d5 >> pluck([-1, -3, 2, 0, 2, 4, 2, 2, 4, 2, 2, 2, 0, 0, -1, -1, -1, -3, -3, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d6 >> pluck([-4, -3, -1, 0, -1, -3, -5, -7, -10, -5, -12, -5, -5, -6, -6, -8, -8, -9, -8, -10, -10, -11, -10, -17],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d7 >> pluck([-60],dur=[rest(16)])
@structure
def a5():
	d0 >> pluck([-60],dur=[rest(16)])
	d1 >> pluck([-60],dur=[rest(16)])
	d2 >> pluck([-60],dur=[rest(16)])
	d3 >> pluck([16, 14, 12, 11, 16, 17, 16, 14, 16, 14, 12, 12, 11, 12, 12, 12, 12, 14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([4, 6, 7, 6, 4, 6, 8, 9, 7, 5, 7, 5, 4, 5, 7, 7, 7, 7, 4, 6, 7, 5, 4, 5],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d5 >> pluck([-5, -3, -1, 0, 2, 4, 4, -3, -1, 0, 0, 2, 4, 0, 2, 4, 0, 0, -2, -3, -3, -5],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d6 >> pluck([-12, -5, -3, -8, -11, -10, -5, -12, -10, -8, -7, -5, -17, -12, -3, -8, -7, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d7 >> pluck([-60],dur=[rest(16)])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(lambda : Clock.clear(), start + 96)