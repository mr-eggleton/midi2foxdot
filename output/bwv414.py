Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 11, 12, 14, 11, 7, 9, 11, 12, 11, 9, 7, 7, 9, 11, 11, 9, 7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([7, 7, 9, 7, 7, 5, 4, 2, 4, 2, 2, 0, -1, 4, 2, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 2, 2, 2, 2, 0, 0, -5, -5, -5, -6, -5, 0, -1, -3, -5, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-17, -5, -6, -5, -8, -7, -5, -12, -17, -10, -8, -10, -12, -10, -8, -6, -5, -13, -12, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 7, 11, 9, 11, 7, 4, 6, 7, 9, 11, 7, 7, 7],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 0, -1, 7, 6, 6, 4, 2, 1, 2, 1, 2, 3, -1, 4, 2],dur=[0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-6, -10, 2, 2, 0, -1, -1, -3, -3, -5, -6, -6, -5, 0, -1, 0],dur=[1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-10, -17, -17, -10, -9, -8, -3, -5, -6, -8, -10, -13, -8, -10, -8, -6, -5, -3],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)