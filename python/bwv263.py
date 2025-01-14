Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 14, 14, 12, 14, 11, 7, 11, 11, 9, 9, 7, 9, 6, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 2, 9, 7, 9, 9, 6, 7, 2, 7, 7, 7, 6, 6, 4, 2, 4, 1, 2, -3],dur=[1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-1, -1, -3, -1, 4, 2, 2, -1, 2, 2, 2, 2, 2, -1, -3, -3, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-5, -5, -6, -5, -5, -6, -10, -5, -17, -17, -15, -13, -12, -10, -8, -6, -10, -13, -8, -11, -15, -10, -22],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 9, 11, 9, 7, 6, 4, 2, 2, 14, 14, 14, 16, 12, 14, 11, 7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 2, 2, 2, -1, 1, -3, 9, 9, 8, 9, 11, 11, 9, 7, 9, 7, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-6, -5, -3, -6, -5, -3, -3, -5, -6, -6, 6, 6, 5, 4, 4, 2, 2, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-10, -8, -6, -10, -5, -10, -3, -15, -10, -10, 2, 0, -1, -3, -4, -8, -3, -5, -6, -10, -5, -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 11, 9, 9, 7, 9, 6, 2, 7, 9, 11, 12, 14, 12, 11, 9, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([7, 7, 6, 4, 1, 6, 6, 4, 2, 4, 1, 2, -3, 2, -1, 6, 7, 6, 7, 7, 6, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([2, -1, 4, 2, 1, -3, 2, 2, -1, -3, -3, -6, -5, 2, 2, 0, -1, 0, 2, 2, 0, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.75 ,0.25 ,2.0])
	d3 >> pluck([-5, -5, -5, -6, -10, -13, -8, -11, -15, -10, -22, -13, -8, -10, -12, -13, -15, -17, -8, -10, -22, -17],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
