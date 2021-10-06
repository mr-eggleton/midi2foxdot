Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 7, 6, 10, 9, 7, 6, 6, 6, 6, 7, 4, 6, 6, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 2, 1, 2, 7, 5, 3, 2, 4, 2, 2, 0, 2, 2, 0, 0, 3, 2, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-2, -2, -3, -5, -3, 2, 0, -2, -3, -3, -3, -3, -3, -5, -5, -3, 0, 0, -2, -3, -2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0])
	d3 >> pluck([-5, -5, -7, -9, -10, -12, -14, -17, -12, -11, -10, -10, -9, -9, -10, -10, -12, -12, -13, -12, -14, -15, -10, -17],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 9, 12, 9, 5, 7, 9, 10, 10, 9, 7, 6, 6, 6, 6, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([5, 5, 7, 5, 5, 3, 2, 0, 3, 2, 7, 7, 6, 7, 0, 2, 2, 0, 2, 3, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([0, 0, 0, 0, -2, -2, -3, 0, -2, 2, 2, -5, -3, -3, -3, -3, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-7, -7, -5, -7, -8, -7, -9, -9, -10, -9, -8, -7, -6, -5, -17, -10, -9, -10, -10, -15, -14, -12, -14, -13],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)