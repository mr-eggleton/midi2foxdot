Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([14, 14, 14, 14, 12, 10, 9, 14, 14, 15, 17, 15, 14, 12, 14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([7, 6, 7, 6, 7, 9, 7, 6, 7, 6, 7, 6, 5, 7, 5, 12, 10, 10, 9, 10],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, 0, 2, 0, -2, -3, -2, 0, 2, 2, 2, 2, 2, 0, -2, -2, -3, -5, -7, 5, 7, 5, 5],dur=[0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-17, -15, -14, -12, -10, -8, -6, -5, -3, -10, -5, -3, -2, 0, 2, -2, -3, -5, -7, -9, -10, -12, -7, -14, -10, -9, -12, -7, -14],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 12, 10, 9, 7, 9, 10, 9, 14, 10, 10, 12, 14, 15, 14, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([10, 9, 7, 7, 6, 7, 0, 9, 2, 4, 6, 9, 9, 7, 5, 3, 8, 7, 7, 7, 9],dur=[0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([5, 3, 2, 4, -3, 2, 0, -2, 0, -2, -3, 2, 0, -2, -3, -5, 2, 2, 2, 3, 5, 7, 5, 2, 2, 0, 2, 4, 6, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-14, -12, -11, -10, -9, -8, -7, -6, -5, -11, -10, -6, -5, -7, -9, -10, -12, -14, -12, 0, -2, -3, -5],dur=[1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)