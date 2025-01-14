Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 6, 2, 9, 9, 11, 11, 4, 4, 9, 7, 6, 2, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0)])
	d1 >> pluck([4, 2, 6, 4, 2, 9, 6, 7, 2, 1, 2, 1, -1, -3, 4, 2, -3, -60],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0)])
	d2 >> pluck([-3, -3, -3, -3, 2, 2, -5, -5, -6, -8, -3, -3, -6, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0)])
	d3 >> pluck([-11, -10, -11, -10, -8, -6, -8, -6, -10, -5, -17, -15, -17, -15, -13, -11, -13, -11, -15, -10, -10, -60],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,rest(1.0)])
@structure
def a1():
	d0 >> pluck([9, 11, 11, 9, 7, 6, 4, 6, 8, 9, 11, 8, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([2, 2, 7, 6, 4, -3, 1, 2, 4, 4, 6, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0 ,1.0])
	d2 >> pluck([-3, -5, -3, -1, 1, 2, 2, 1, 2, 1, -3, -1, -3, 2, -1, 1],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0 ,1.0])
	d3 >> pluck([-6, -5, -8, -3, -15, -10, -15, -10, -11, -10, -13, -11, -13, -11, -10, -8, -20, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([9, 9, 9, 14, 12, 11, 11, 11, 11, 16, 14, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([4, 6, 4, 6, 7, 9, 7, 9, 6, 7, 6, 4, 4, 4, 4, 4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([1, 2, 2, 2, 2, 2, -1, -3, -4, -6, -4, -3, -1, -3, -1, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-15, -10, -11, -10, -8, -6, -8, -6, -10, -5, -9, -8, -9, -8, -6, -4, -6, -4, -8, -3],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
@structure
def a3():
	d0 >> pluck([9, 11, 9, 11, 13, 14, 9, 9, 7, 6, 4, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([2, 7, 9, 7, 11, 10, 11, 9, 7, 6, 4, 2, 2, 1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([2, 2, 2, 2, 4, 6, 4, 2, -3, -3, -1, -3, -5, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-6, -5, -3, -5, -6, -5, -6, -5, -8, -1, -11, -10, -8, -6, -5, -3, -15, -10],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
