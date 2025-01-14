Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 11, 7, 9, 9, 11, 12, 11, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0])
	d1 >> pluck([2, 4, 6, 7, 5, 4, 5, 5, 7, 7, 7, 7],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0])
	d2 >> pluck([-1, -1, 2, 2, 0, 0, 2, 4, 2, 5, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,2.0 ,0.5 ,0.5 ,3.0 ,1.0])
	d3 >> pluck([-5, -6, -8, -10, -17, -12, -7, -8, -10, -12, -8, -5, -12, -5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 13, 14, 9, 11, 13, 14, 14, 13, 14, 9, 9],dur=[1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 6, 6, 7, 7, 6, 7, 9, 7, 6, 7, 4, 6, 6, 6],dur=[1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0])
	d2 >> pluck([2, 4, -3, 2, 2, -3, 2, 2, 0, -1, -3, -3, 2, 2],dur=[1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0])
	d3 >> pluck([-5, -6, -8, -10, -10, -5, -3, -1, -6, -5, -3, -10, -10, -12],dur=[0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 12, 14, 16, 14, 12, 11, 9, 16, 14, 12, 14, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d1 >> pluck([8, 9, 8, 9, 7, 6, 8, 9, 9, 8, 4, 4, 6, 7, 9, 9, 7, 6, 7],dur=[1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([2, 4, 2, 0, -1, -3, -1, 0, 4, 5, 4, 2, 0, 7, 0, 2, 4, 2, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
	d3 >> pluck([-13, -15, -13, -12, -12, -13, -15, -10, -8, -15, 0, -1, -3, -5, -6, -8, -10, -5, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
