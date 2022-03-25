Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 9, 9, 10, 12, 10, 7, 14, 14, 12, 10, 9, 7, 6, 9, 10, 12, 14, 15, 14, 10, 17, 17, 16, 14, 12, 10, 9],dur=[1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([2, 3, 2, 2, 2, 7, 6, 7, 2, 6, 7, 5, 5, 5, 10, 12, 4, 5],dur=[1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-2, 0, -2, -3, -5, -3, -2, 0, -2, -3, 2, 2, 0, -2, 0, 2, -5, 0, 0],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-5, -5, -6, -5, -7, -9, -10, -9, -12, -10, -10, -5, -3, -2, -3, -5, -7, -8, -12, -7],dur=[1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 13, 14, 16, 17, 19, 17, 16, 16, 14, 14, 10, 9, 11, 14, 19, 15, 12, 14, 17, 15, 14, 15],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([5, 7, 5, 4, 2, 4, 5, 7, 6, 9, 7, 7, 7, 3, 8, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, -2, -3, -3, -3, 2, 2, 1, -1, 1, -3, 2, 2, 2, 0, 0, 0, -1, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-2, -8, -7, -11, -10, -3, -15, -10, -6, -5, -7, -9, -4, -7, -10, -5, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)