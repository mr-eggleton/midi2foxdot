Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 9, 7, 9, 5, 4, 2, 9, 11, 12, 14, 9, 11, 12, 11, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 5, 5, 5, 4, 4, 2, 1, 2, 5, 4, 2, 4, 5, 5, 4, 2, 1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, 2, 2, 2, -3, -3, -5, -7, 2, 0, -1, -3, 2, 2, -4, -3, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d3 >> pluck([-11, -10, -8, -7, -13, -11, -10, -15, -10, -10, -3, -5, -7, -8, -10, -12, -13, -15, -8, -15],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
@structure
def a1():
	d0 >> pluck([12, 12, 12, 10, 9, 7, 5, 7, 9, 7, 5, 9, 9, 9, 7, 5, 4, 4, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([9, 7, 5, 4, 2, 0, 2, 4, 5, 4, 5, 0, 2, 4, 2, 2, 2, 2, 1, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, 0, -5, -3, -3, -2, 0, -2, -3, -3, -3, -5, -7, -5, -3, -2, -3, -5, -7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-3, -8, -10, -12, -7, -8, -10, -15, -14, -12, -19, -7, -11, -10, -12, -14, -15, -17, -15, -10],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
@structure
def a2():
	d0 >> pluck([9, 9, 7, 9, 11, 12, 11, 9, 7, 14, 16, 14, 9, 11, 12, 11, 9, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 5, 4, 5, 9, 7, 5, 4, 2, 0, -1, 7, 7, 5, 4, 2, 4, 4, 2, 0, 5],dur=[1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, 2, 0, -2, 0, 2, -5, -6, -5, -1, 0, -1, -3, -4, -3, -3, -4, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-11, -10, -5, -7, -8, -10, -12, -10, -17, -5, -12, -10, -8, -7, -12, -10, -8, -7, -8, -10],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)