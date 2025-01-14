Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 11, 9, 7, 9, 9, 11, 7, 9, 11, 12, 14, 12, 11, 9, 7, 9, 7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([2, 4, 6, 7, 7, 6, 7, 7, 6, 7, 4, 6, 7, 11, 9, 7, 6, 7, 7, 6, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-1, -1, 4, 4, 2, 2, 4, 0, -3, 2, 2, 4, 2, -5, -3, -1, 0, 2, 2, 0, -1, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-5, -6, -8, -10, -12, -13, -12, -15, -10, -17, -12, -5, -6, -8, -1, -3, -5, 2, -10, -5],dur=[0.5 ,0.5 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([-5, -6, -8, -20, -8, -10, -12, -24, -12, -13, -12, -15, -10, -22, -17, -12, -5, -6, -8, -20, -13, -15, -17, -13, -10, -22, -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 11, 9, 7, 6, 7, 9, 11, 9, 9, 7, 6, 7, 2, 7, 9, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 6, 6, 4, 4, 3, 4, 2, 2, 2, 2, 0, 2, 2, 0, -1, -1, 4, 3],dur=[1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 2, 2, 0, -1, 0, -6, -1, -1, -3, -3, -5, -6, -6, -5, -3, -1, 0, -1, -3, -5, -5, -6, -8, -6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-5, -3, -1, 0, 2, -5, -3, -1, -8, -6, -5, -10, 2, 0, -1, -3, -5, -6, -8, -10, -12, -13],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d4 >> pluck([-17, -15, -13, -12, -10, -22, -17, -15, -13, -1, -8, -6, -5, -17, -10, -10, -12, -13, -1, -13, -15, -17, -5, -17, -18, -20, -22, -24, -12, -13],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
