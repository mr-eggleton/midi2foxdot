Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([2, 5, 5, 7, 7, 9, 9, 10, 9, 7, 5, -3, 5, 5, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-3, 2, 4, 5, 5, 4, 2, 0, 2, 2, 7, 5, 5, 4, 2, 4, 0, -3, -5, -7, 2, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-7, -3, 0, 2, 0, -2, -3, -5, -7, -8, 0, 2, -5, 0, -2, -3, -7, -5, -3, -2, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5])
	d3 >> pluck([-10, -10, -15, -14, -12, -7, -8, -10, -17, -15, -14, -12, -19, -7, -8, -10, -12, -14, -15, -17, -19],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a1():
	d0 >> pluck([7, 9, 9, 7, 5, 4, 2, 9, 5, 7, 4, 9, 5, 7, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 0, 5, 5, 4, 2, 2, 1, -3, 4, 4, 2, 2, 4, 1, 4, 2, 0, 2, 0],dur=[1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-5, -7, 0, 0, -2, -3, -2, -3, -5, -7, -3, -3, -2, -3, -3, -3, -5, -5],dur=[1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-20, -19, -17, -15, -14, -12, -10, -17, -15, -22, -11, -10, -17, -15, -12, -12, -13, -12],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)