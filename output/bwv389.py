Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([12, 12, 11, 9, 7, 12, 14, 16, 16, 16, 14, 16, 16, 14, 12, 14, 14, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([7, 9, 7, 7, 5, 4, 5, 7, 9, 7, 7, 7, 7, 9, 11, 9, 7, 7, 9, 7, 5, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([4, 4, 4, 2, 0, 0, 0, -1, 0, 0, 2, 4, 5, 4, 2, 0, -1, 0, -1, -5],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([0, -1, -3, -8, -7, -12, -10, -8, -7, -5, -12, -12, 0, -4, -3, -5, -7, -5, -8, -7, -5, -12],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([12, 12, 14, 16, 14, 16, 12, 11, 9, 9, 14, 12, 11, 12, 11, 9, 7, 7, 12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 5, 12, 7, 5, 4, 4, 4, 4, 2, 2, 7, 4, 6, 2, 2, 7, 5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-5, -3, -5, -3, -1, -1, -1, -3, -4, 0, 0, -1, -3, -5, -5, 2, 0, -1, -1, -3, -5],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-12, -7, -8, -7, -5, -4, -3, -8, -15, -3, -5, -6, -5, -6, -8, -12, -10, -17, -5, -7, -8],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a2():
	d0 >> pluck([12, 14, 14, 16, 14, 16, 12, 12, 17, 17, 16, 14, 16, 14, 14, 16, 16, 17],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 9, 5, 7, 7, 5, 7, 5, 7, 5, 7, 9, 10, 4, 5, 7, 7, 9, 9],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([0, 0, -1, 0, -2, -3, 0, 2, 4, 5, 7, 1, -3, -1, 0, 0, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -5, -7, -10, -5, -12, -10, -8, -7, -8, -10, 2, -5, -2, -3, -10, -5, 0, -1, -3, -5, -7, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a3():
	d0 >> pluck([17, 19, 17, 16, 17, 19, 12, 16, 14, 12, 11, 12, 11, 9, 7, 7, 12, 11, 9, 7, 14],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([10, 10, 9, 7, 5, 7, 9, 7, 7, 4, 6, 2, 2, 9, 2, 4, 5, 7, 9],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 4, 2, 0, -2, -3, 0, -1, -3, 2, -5, 2, 0, -1, -1, -8, -6, -5, 2, 2, 0, 0, -1],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-10, -12, -10, -8, -7, 0, -6, -5, -8, -12, -10, -17, -17, -15, -13, -12, -10, -8, -7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
