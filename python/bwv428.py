Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 2, 4, 6, 7, 9, 11, 7, 11, 12, 14, 14, 11, 12, 14, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([2, 2, 0, 0, 2, 2, 2, 4, 2, 2, 4, 6, 7, 5, 4, 6, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-1, -3, -5, -5, -3, -1, 0, -1, 0, -1, -3, -3, -5, -3, -1, -1, -3, -5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-17, -15, -13, -14, -15, -17, -18, -17, -12, -5, -6, -8, -10, -8, -13, -12, -10, -17],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 12, 11, 9, 7, 9, 11, 11, 9, 7, 11, 12, 14, 14, 11, 14, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([2, 2, 4, 6, 7, 6, 4, 3, 4, 4, 2, 9, 7, 11, 11, 9, 7],dur=[1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-1, -3, -1, -1, -1, -1, -1, -1, -5, -3, -1, 0, 2, 2, 4, 5, 4, 6, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-5, -6, -5, -9, -8, -6, -5, -3, -1, -8, -8, -7, -6, -5, -4, -3, -10, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 12, 11, 9, 7, 9, 11, 11, 7, 9, 11, 11, 4, 6, 7, 6, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 7, 6, 4, 2, 2, 2, 4, 4, 6, 6, 4, 6, 7, 6, 4, 2, 2, 2, 1, -3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([2, 0, 2, 2, 2, 0, -1, -3, -5, 0, 0, -1, -1, -3, -3, -1, 0, -1, -3, -5, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-5, -6, -8, -10, -12, -13, -15, -17, -15, -13, -12, -3, -5, -6, -8, -10, -11, -10, -17, -15, -10],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
