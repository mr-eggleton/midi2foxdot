Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 6, 7, 9, 10, 9, 7, 7, 9, 9, 14, 12, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([2, 3, 2, 0, -2, 3, 2, 2, 2, 2, 3, 2, 2, 7, 6, 7, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d2 >> pluck([-2, -3, -3, -5, 0, -6, -5, -6, -2, -2, 0, 0, -1, 0, 2, 4, -5, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-5, -12, -10, -9, -10, -12, -10, -10, -17, -5, -5, -6, -7, -9, -10, -11, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 12, 10, 9, 10, 12, 10, 9, 7, 10, 9, 7, 5, 4, 2, 4, 5, 7, 9],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 5, 5, 3, 3, 2, 0, 9, 6, 7, 6, 2, 7, 5, 4, 2, 2, 1, 2, 4, 5, 1, 2, 5, 4, 5],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0])
	d2 >> pluck([2, 3, 5, 7, -2, 0, 2, -5, 0, 2, 3, -3, 2, -2, 2, 1, 2, 4, -3, -5, -3, 0, 2, 0, 0],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-2, -2, -3, -5, -5, -7, -9, -10, -12, -10, -17, -5, -5, -7, -8, -10, -10, -15, -14, -12, -19],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
