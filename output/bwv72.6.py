Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 5, 7, 9, 7, 12, 12, 11, 12, 12, 11, 9, 14, 12, 11, 12, 11],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 0, 0, 0, 0, 2, 4, 2, 4, 4, 2, 2, 2, 9, 8, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-3, -5, -7, -8, -7, -5, -3, -5, -5, -5, -5, -5, -7, -5, -3, -1, 0, 2, 4, 4, -1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5])
	d3 >> pluck([-3, -8, -7, -12, -10, -8, -7, -5, -17, -12, -12, -5, -10, -8, -6, -4, -3, -8, -10, -12, -10, -8],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 9, 4, 5, 7, 9, 7, 12, 12, 11, 12, 12, 11, 9, 14],dur=[1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 4, 0, 0, 0, 0, 0, 2, 4, 2, 4, 4, 2, 2, 2],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, 2, 0, -3, -5, -7, -8, -7, -5, -3, -5, -5, -5, -5, -5, -7, -5, -3, -1],dur=[0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-8, -15, -3, -8, -7, -12, -10, -8, -7, -5, -17, -12, -12, -5, -10, -8, -6, -4],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([14, 12, 11, 12, 11, 9, 9, 9, 9, 11, 9, 7, 7, 6, 7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([9, 8, 9, 8, 4, 4, 2, 4, 6, 6, 3, 4, 4, 2, 2],dur=[1.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([0, 2, 4, 4, -1, 4, 2, 0, 0, -1, -3, 2, 0, -1, -1, -3, -3, -1],dur=[0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -8, -10, -12, -10, -8, -15, -3, -5, -6, -8, -10, -5, -6, -8, -10, -11, -10, -17],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([7, 9, 11, 12, 11, 9, 11, 4, 5, 7, 9, 7, 12, 12, 11, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 6, 8, 9, 4, 4, 2, 4, 5, -1, 0, 2, 4, 4, 2, 2, 0, 7, 5, 4, 5, 2, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([0, -1, -3, 2, 4, 5, 7, 0, -1, -3, -4, -3, -1, -3, 4, 4, -3, -5, -5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-12, 0, -1, -3, -5, -7, -8, -3, -5, -7, -8, -10, -12, -10, -5, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)