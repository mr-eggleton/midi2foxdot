Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 12, 11, 9, 16, 16, 14, 12, 11, 14, 12, 11, 9, 11, 12, 14, 12, 11, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 9, 8, 9, 8, 9, 11, 4, 6, 8, 8, 9, 8, 9, 7, 5, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([4, 4, 2, 4, 2, 0, -1, 0, 2, 4, 5, 4, 4, 2, 0, 2, -4, -3, -4, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d3 >> pluck([-8, -3, -1, 0, -1, -3, -4, -3, -8, -13, -12, -10, -8, -7, -8, -10, -8, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 11, 9, 7, 6, 4, 6, 7, 9, 11, 7, 9, 11, 12, 11, 12, 11, 9, 8, 9],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 3, 4, 3, 4, 3, 4, 7, 6, 4, 3, 4, 2, 0, 2, 4, 4, 9, 4, 4, 4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, -5, -3, -1, -1, -1, -3, -1, 0, -6, -1, -3, 9, 8, 4, 2, 0, -1, 0],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-6, -5, -6, -8, -1, -3, -5, -6, -8, -10, -12, -13, -8, -7, -12, -10, -8, -15, -13, -12, -10, -8, -15],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)