Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 9, 7, 5, 2, 5, 7, 9, 10, 14],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([2, 4, 5, 5, 4, 2, -3, -2, 0, 3, 2, 0, -1, 4, 4, 6, 7, 6, 7],dur=[0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
	d2 >> pluck([-2, 0, 0, -2, -3, -7, -5, -3, -5, -7, 0, 0, 2, 0, -2, -3],dur=[1.0 ,2.0 ,0.75 ,0.25 ,1.0 ,1.5 ,0.5 ,2.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-5, -7, -12, -10, -14, -15, -10, -12, -15, -17, -14],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
@structure
def a1():
	d0 >> pluck([12, 10, 9, 7, 12, 12, 12, 14, 12, 10],dur=[2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([7, 6, 7, 7, 6, 2, 7, 7, 5, 5, 4, 5, 5, 4, 5, 7, 9, 7, 5],dur=[1.5 ,0.5 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-5, -6, -5, -3, 2, 3, 2, -3, 2, 0, -2, 0, -2, -3, -2, 0, 0, -2, 0, 2],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-9, -10, -12, -10, -22, -17, -8, -7, -5, -3, -2, -7, -8, -10, -12],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([9, 7, 5, 5, 10, 9, 10, 12, 14, 12, 10, 9],dur=[1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.5 ,0.5])
	d1 >> pluck([5, 5, 4, 0, 2, 7, 9, 9, 2, 7, 9, 10, 9, 7, 6, 7, 2],dur=[1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([2, -5, 0, -3, -2, 0, 2, -2, 3, 2, 2, 3, 5, 3, 2, 3, 0, 2, 3, 5, -7],dur=[1.0 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-14, -12, -19, -14, -15, -17, -5, -6, -5, -7, -9, -10, -12, -14, -2, -3, -5, -7],dur=[1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)