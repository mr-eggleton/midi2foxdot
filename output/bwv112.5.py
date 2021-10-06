Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 9, 11, 12, 14, 12, 11, 9, 11, 11, 11, 9, 11, 12, 11, 9, 7, 9, 9, 7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.75 ,0.25 ,1.0 ,1.0])
	d1 >> pluck([2, 6, 7, 7, 6, 4, 6, 7, 7, 6, 7, 7, 7, 6, 7, 9, 7, 6, 7, 7, 6, 2],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-1, 0, 2, 4, -3, -3, 2, 2, 2, 4, 2, 2, 4, 2, 2, 0, -1, 4, 2, 0, -1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0])
	d3 >> pluck([-17, -5, -6, -8, -10, -15, -13, -12, -10, -17, -8, -13, -12, -10, -15, -13, -12, -10, -8, -10, -12, -10, -17],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([7, 9, 11, 12, 14, 12, 11, 9, 11, 11, 11, 9, 11, 12, 11, 9, 7, 9, 9, 7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.75 ,0.25 ,1.0 ,1.0])
	d1 >> pluck([2, 6, 7, 7, 6, 4, 6, 7, 7, 6, 7, 7, 7, 6, 7, 9, 7, 6, 7, 7, 6, 2],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-1, 0, 2, 4, -3, -3, 2, 2, 2, 4, 2, 2, 4, 2, 2, 0, -1, 4, 2, 0, -1],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0])
	d3 >> pluck([-17, -5, -6, -8, -10, -15, -13, -12, -10, -17, -8, -13, -12, -10, -15, -13, -12, -10, -8, -10, -12, -10, -17],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a2():
	d0 >> pluck([7, 9, 11, 12, 11, 9, 8, 9, 9, 11, 12, 14, 12, 11, 9, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 2, 4, 4, 4, 0, 5, 4, 4, 6, 7, 5, 4, 4, 6, 7, 6, 4, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,1.0])
	d2 >> pluck([-1, -3, -5, -5, -4, -3, 2, 0, -3, 2, 0, -1, 0, 2, 4, -8, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-5, -6, -7, -8, -10, -12, -7, -10, -8, -15, -10, -12, -13, -15, -16, -15, -8, -10, -12, -13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
