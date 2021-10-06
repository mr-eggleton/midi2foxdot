Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 9, 10, 9, 7, 6, 7, 9, 10, 9, 7, 10, 12, 12, 14, 10, 12, 12, 14],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 7, 5, 3, 2, 2, 6, 7, 6, 2, 7, 5, 7, 9, 10, 2, 7, 10, 9, 7, 6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-2, 0, 2, 0, -2, -3, -2, 0, 2, 3, -3, 2, -2, 2, 0, 5, 5, 7, 7, 0, 2, 3, -3],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.25 ,0.25 ,0.5 ,1.0])
	d3 >> pluck([-17, -5, -12, -10, 0, -2, -3, -5, -12, -10, -17, -5, -3, -7, -2, -3, -5, -7, -9, -10, -9, -10],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 15, 14, 15, 17, 15, 14, 12, 10, 12, 10, 14, 10, 12, 10, 9, 7, 6, 7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 9, 10, 12, 10, 9, 10, 9, 5, 9, 7, 7, 6, 7, 6, 7, 3, 2, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-2, 0, -7, -7, 5, 3, 2, 3, 0, 2, 2, 2, 0, 2, 2, 0, -2, -3, -1, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0])
	d3 >> pluck([-5, -12, -14, -15, -14, -7, -7, -14, -6, -5, -17, -15, -14, -12, -22, -21, -24, -22, -17],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
