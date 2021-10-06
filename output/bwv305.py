Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 7, 7, 9, 11, 12, 11, 9, 7, 12, 11, 12, 9, 7, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-1, 4, 4, 4, 5, 4, 4, 9, 8, 4, 4, 5, 7, 9, 9, 7, 5, 7, 5, 5, 4, 2, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,1.0 ,0.25 ,0.25 ,1.0])
	d2 >> pluck([-5, -1, -1, 0, 2, 0, 4, 5, 4, 2, 0, -1, 4, 5, 4, 2, 0, 0, 0, -2, -3, -1, -3, -4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.75 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0])
	d3 >> pluck([-8, -8, -7, -8, -10, -12, -3, -4, -3, -12, -10, -8, -15, -8, -10, -12, -10, -5, -8, -12, -7, -12, -10, -8],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([4, 9, 9, 7, 12, 11, 9, 7, 7, 12, 7, 9, 4, 9, 7, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([0, 5, 5, 5, 4, 2, 4, 6, 7, 2, 7, 6, 2, 4, 4, 4, 2, 0, -1, 1, 2, 4, 2, 1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,1.0 ,0.5])
	d2 >> pluck([-3, 0, 2, 0, -5, -3, -10, 2, 4, 2, 0, -1, 0, 0, 0, -2, -3, -3, -3, -3, -3],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -5, -7, -8, -10, -12, -13, -12, -13, -15, -17, -13, -12, -10, -17, -12, -13, -15, -13, -12, -20, -19, -17, -15, -13, -11, -15, -10, -15],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([4, 9, 9, 7, 5, 4, 5, 2, 0, 0, 7, 9, 11, 12, 7, 9],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 0, 3, 2, 2, 0, 0, -1, -5, -5, 2, 4, 2, 0, 2, 4, 5, 7, 4, 5],dur=[1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-3, -3, 0, -1, -3, -1, 0, -1, -3, -5, -7, -8, -8, -5, 0, 2, 4, 5, 7, -5, 0, 0],dur=[1.0 ,0.5 ,1.0 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,0.75 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -5, -7, -6, -5, -3, -5, -7, -10, -5, -17, -12, -12, -13, -12, -13, -15, -17, -19, -20, -22, -20, -24, -19, -15],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
