Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 9, 16, 14, 16, 12, 11, 9, 11, 12, 11, 12, 14, 16, 14, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 5, 4, 4, 2, 4, 5, 4, 4, 4, 4, 9, 8, 9, 7, 9, 11, 9, 8],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([0, 2, 0, -1, -3, -3, 0, -1, -3, -1, -3, -4, -3, 4, 4, 4, 4, 5, 4, 4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-15, -3, -7, -12, -10, -16, -15, -8, -12, -13, -15, -8, -3, -1, 0, -4, -3, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([12, 11, 9, 9, 14, 12, 11, 12, 9, 7, 7, 12, 11, 12, 14, 16, 14, 12, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([9, 2, 4, 6, 6, 7, 7, 6, 2, 4, 5, 7, 2, 4, 5, 7, 8, 9, 8],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, -3, 2, 2, 4, 2, 0, -1, 0, -1, 0, -5, -3, -1, -3, -5, 0, 2, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -5, -6, -8, -10, -12, -13, -8, -12, -10, -17, -12, -10, -8, -7, -5, -7, -8, -10, -12, -13, -15, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([9, 11, 12, 11, 12, 14, 16, 14, 12, 11, 16, 16, 16, 14, 12, 11, 12, 11, 8, 9, 11, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([4, 2, 2, 4, 5, 7, 5, 4, 4, 4, 8, 9, 7, 5, 4, 5, 4, 5, 4, 5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([0, -1, -3, -1, -3, -5, 0, 0, -1, -1, -3, -4, -1, 0, 1, 2, 4, 2, 0, -3, -4, -3],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-3, -5, -6, -10, -5, -7, -8, -10, -12, -13, -15, -16, -15, -8, -8, -3, -5, -7, -8, -7, -8, -10, -12, -10, -13, -12, -10, -8, -10],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)