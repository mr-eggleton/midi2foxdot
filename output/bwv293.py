Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 7, 2, 5, 7, 9, 9, 7, 9, 7, 2, 5, 7, 9, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 0, -1, 1, 2, 0, -1, 4, 2, 0, -1, 2, 2, 0, -1, 1, 2, 0, -1, 4, 2, 2],dur=[1.0 ,0.5 ,1.0 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-7, -5, -5, -3, -5, -5, -6, -10, -7, -5, -5, -3, -5, -5, -6, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-10, -8, -5, -10, -8, -10, -12, -10, -17, -10, -8, -5, -10, -8, -10, -12, -10, -17],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 11, 12, 9, 7, 7, 5, 4, 5, 7, 2, 5, 7, 9, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([5, 5, 4, 2, 2, 4, 2, 1, 2, 0, -1, 0, -1, 1, 2, 0, -1, 4, 2, 0, -1],dur=[1.0 ,1.5 ,1.0 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([0, 2, -5, -3, -1, 0, -1, 0, -2, -3, -3, -3, -5, -5, -3, -5, -5, -6, -10],dur=[1.0 ,1.0 ,1.0 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-7, -8, -10, -12, -7, -6, -5, -12, -11, -10, -15, -10, -8, -5, -10, -8, -10, -12, -10, -17],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
