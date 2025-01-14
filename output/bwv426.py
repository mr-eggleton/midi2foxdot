Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([12, 11, 9, 9, 9, 11, 12, 11, 9, 7, -60, 11, 12, 11, 12, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 5, 7, 5, 4, 5, 5, 9, 7, 7, 5, 5, 4, -60, 7, 7, 7, 7, 5],dur=[0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-5, -5, 0, 0, 0, 2, 5, 4, 2, 0, 0, 0, -60, 2, 4, 2, 0, 0],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-12, -10, -8, -7, -5, -7, -8, -10, -5, -7, -8, -7, -12, -60, -5, -12, -8, -5, -7, -8, -12, -7, -8],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a1():
	d0 >> pluck([11, 7, 9, 11, -60, 11, 11, 11, 9, 11, 12, 7, 7],dur=[1.0 ,1.0 ,2.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([5, 4, 4, 4, -60, 4, 6, 9, 7, 6, 4, 4, 2, 5, 4],dur=[1.0 ,1.0 ,2.0 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,2.0 ,0.5 ,1.0 ,0.5])
	d2 >> pluck([2, -1, -3, -1, 0, -3, -4, -60, -5, -1, 6, 6, 4, 4, 2, 0, -1, -3, 2, 0, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.5 ,0.25 ,0.25])
	d3 >> pluck([-10, -13, -8, -10, -12, -13, -15, -12, -8, -60, -8, -9, -8, -6, -4, -3, -1, 0],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([9, 11, 12, 9, 11, 11, 12, 14, 14, 12, 9, 11, 14, 14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([4, 2, 2, 0, 7, 6, 7, 7, 6, 7, 9, 11, 9, 7, 6, 7, 9, 7, 9],dur=[0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([0, -1, -3, -5, 4, 2, 2, 2, 0, -1, 4, 4, 2, 2, 6, 4, 2, 0],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-6, -5, -6, -8, -12, -10, -17, -17, -15, -13, -16, -15, -13, -12, -10, -17, 2, 0, -1, -3],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a3():
	d0 >> pluck([14, 14, 16, 14, 12, 11, 11, 7, 9, 11, 12, 14, 12, 11, 9, 11, 12],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([11, 9, 7, 5, 4, 6, 7, 7, 5, 4, 4, 6, 7, 9, 7, 7, 5, 4, 5, 4, 2, 4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,2.0])
	d2 >> pluck([-1, -1, 0, -1, -3, 4, 2, 0, 0, 2, 2, 2, 2, 2, -1, -5],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-5, -7, -8, -10, -12, -10, -8, -17, -12, -13, -15, -17, -18, -17, -10, -17, -12],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
