Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([2, 4, 5, 4, 5, 7, 9, 9, 12, 11, 9, 9, 8, 9],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([2, 1, 2, -2, -3, 2, 0, 0, 0, 0, 5, 6, 4, 4, 4],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-3, -5, -3, -5, -7, -7, -8, -7, -7, -5, -4, 0, -1, 0, 2, 0],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d3 >> pluck([-7, -8, -10, -11, -10, -12, -14, -12, -19, -19, -8, -10, -9, -8, -20, -15],dur=[0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([9, 11, 12, 14, 12, 11, 12, 10, 9, 9, 7, 5, 5, 4, 5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([4, 6, 8, 9, 9, 8, 7, 5, 7, 5, 5, 3, 2, 2, 0, 0, 0],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([0, 2, 4, 2, 2, 0, 4, 2, 0, 0, 0, -2, -4, -5, -3, -2, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,3.0])
	d3 >> pluck([-3, -3, -3, -5, -6, -5, -7, -8, -12, -10, -8, -7, -19, -14, -13, -12, -24, -19],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a2():
	d0 >> pluck([9, 7, 5, 7, 9, 7, 5, 4, 5, 7, 5, 4, 2],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,3.0])
	d1 >> pluck([4, 5, 4, 5, 4, 4, 2, 2, 1, 2, 2, 1, 2, 1, -3],dur=[1.0 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,3.0])
	d2 >> pluck([-3, -3, 2, 0, 0, 2, 4, -3, -4, -3, -1, -3, -3, -5, -3, -3, -5, -7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,3.0])
	d3 >> pluck([-11, -10, -12, -14, -12, -17, -15, -13, -11, -10, -14, -15, -16, -15, -10, -8, -7, -5, -3, -15, -10],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)