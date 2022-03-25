Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 14, 12, 10, 9, 7, 9, 16, 17, 17, 16, 14, 16, 14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d1 >> pluck([5, 5, 7, 9, 2, 4, 5, 5, 4, 5, 9, 9, 9, 9, 9, 7, 5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0])
	d2 >> pluck([2, 2, 4, 5, 7, 0, 2, 0, 0, 4, 4, 2, 2, 1, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([2, 0, -2, -3, -5, -7, -14, -12, -7, -11, -10, -8, -7, -5, -3, -15, -10],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([17, 16, 14, 12, 14, 16, 17, 17, 12, 14, 12, 10, 9, 10, 9],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d1 >> pluck([9, 7, 7, 5, 5, 10, 10, 9, 7, 9, 9, 9, 7, 9, 7, 6, 7, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([2, 0, -2, 0, 0, -2, 0, 2, 0, -2, 0, 5, 3, 2, 2, 2, 2, 2],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([-10, -5, -3, -2, -3, -5, -7, -7, -7, -2, -6, -5, -17, -10],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a2():
	d0 >> pluck([17, 16, 17, 19, 17, 16, 14, 16, 9, 10, 9, 7, 12, 9],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([7, 7, 12, 12, 12, 12, 11, 12, 5, 4, 2, 4, 5, 5, 4, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([2, 0, 2, 4, 5, 7, 9, 7, 7, 0, -2, 0, 0, -2, -3, -5, 0, 0],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-13, -12, 0, -1, -3, -5, -7, -5, -12, -7, -5, -3, -2, 0, -12, -7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)