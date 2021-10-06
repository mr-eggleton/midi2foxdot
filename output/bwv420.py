Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 11, 12, 11, 16, 14, 12, 11, 12, 11, 9, 16, 14, 16, 9, 11, 13, 14],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 4, 4, 6, 8, 9, 8, 9, 8, 9, 9, 9, 7, 7, 5, 4, 5],dur=[1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([0, 0, -1, -3, -4, -3, -1, 0, 2, 4, 4, 2, 0, -1, 1, 2, 0, -2, -3, -3, -3, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-15, -3, -4, -3, -8, -10, -12, -13, -15, -8, -15, -3, -3, -5, -7, -8, -10, -11, -10, -15, -22],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([12, 11, 16, 16, 14, 12, 11, 9, 11, 12, 12, 14, 14, 16, 16, 14, 12],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([4, 4, 4, 11, 12, 11, 9, 8, 4, 4, 5, 7, 9, 5, 7, 7, 7, 9],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, -4, -3, -4, -3, -1, 0, 2, 4, 0, -1, -3, -3, -3, -1, 0, -1, 0, 0, 0],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-15, -8, -10, -12, -8, -6, -4, -3, -8, -15, -3, -5, -7, -8, -7, -8, -5, -7, -8, -10, -12, -7],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)