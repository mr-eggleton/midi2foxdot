Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 14, 12, 10, 9, 10, 9, 7, 9, 10, 7, 5, 9, 10, 12, 11, 13],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5])
	d1 >> pluck([5, 7, 7, 5, 5, 4, 5, 4, 5, 5, 4, 0, 5, 7, 9, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([2, 2, 4, 2, 2, -2, 0, 0, 0, 2, -2, -5, 0, -3, 0, 2, 4, 2, 2, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-10, -12, -14, -15, -10, -17, -15, -14, -12, -7, -14, -12, -19, -7, -8, -6, -5, -7, -8],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 12, 14, 16, 14, 12, 11, 9, -60, 9, 7, 4, 5, 4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([9, 11, 9, 9, 9, 9, 8, 4, -60, 1, 2, 4, 4, 2, 1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([2, -1, 4, 4, 5, -1, 4, 2, 1, -60, -8, -10, -3, -3, -3],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d3 >> pluck([-6, -4, -3, -12, -10, -8, -20, -15, -60, -15, -13, -11, -10, -22, -15],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
