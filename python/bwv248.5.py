Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 9, 7, 5, 4, 2, 4, 11, 12, 12, 11, 12, 14, 11, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,3.0])
	d1 >> pluck([4, 2, 0, 2, 2, 4, 4, 2, 2, 0, 0, -1, -3, -1, 4, 4, 9, 9, 8, 4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-4, -3, -1, 0, 2, -5, -3, -4, -3, -4, -4, -3, -1, 0, 5, 4, 2, 0],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-8, -7, -5, -15, -13, -12, -19, -20, -8, -3, -5, -7, -8, -10, -13, -8, -20, -15],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
@structure
def a1():
	d0 >> pluck([12, 11, 9, 7, 9, 11, 12, 12, 7, 9, 7, 5, 4, 5, 4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d1 >> pluck([9, 7, 5, 4, 2, 0, 5, 5, 4, 2, 4, 4, 5, -2, -3, -3, -5, -3, 2, 1],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d2 >> pluck([4, 2, 0, -1, -3, -5, -7, -5, -3, -5, -7, -5, 0, 0, 2, 4, 2, 1, 2, -4, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-3, -10, -8, -7, -8, -10, -15, -13, -12, -24, -12, -7, -8, -10, -11, -10, -10, -15],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
@structure
def a2():
	d0 >> pluck([12, 11, 12, 14, 12, 11, 9, 11, 4, 5, 4, 2, 7, 5, 4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([2, 2, 7, 7, 6, 7, 7, 6, 7, 7, 0, 2, 0, -7, 2, 2, 0, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, -5, -3, -1, 0, 2, 4, 4, 2, 2, 0, 0, -1, -1, -3, -3, -5, -3, -1, -3, -4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-18, -17, -5, -6, -8, -10, -12, -15, -10, -17, -12, -13, -15, -13, -12, -12, -13, -13, -15, -16, -15, -20],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)