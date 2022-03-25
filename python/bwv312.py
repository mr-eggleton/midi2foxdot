Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 12, 11, 9, 11, 12, 14, 16, 14, 12, 11, -60, 14, 12, 11, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([8, 9, 4, 5, 4, 4, 2, 7, 7, 5, 7, 4, 5, 4, 3, 4, -60, 5, 4, 6, 7, 7],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([4, 4, 0, 2, 4, -3, -5, -3, -2, -3, -4, -3, -3, -4, -60, -3, -1, 0, 2, 4, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-8, -3, -5, -7, -8, -10, -11, -10, -15, -8, -60, -10, -3, -5, -7, -8],dur=[1.0 ,1.5 ,0.5 ,1.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 7, 5, 4, 7, 5, 4, 2, 4, 2, 0, 2, 2, 4, 11, 12, 11, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([5, 4, 2, 0, -1, 2, 4, 0, 2, 0, -3, -5, -4, -3, -1, 0, -1, 4, 4, 9, 7, 5, 4],dur=[1.0 ,1.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([0, -2, -3, -1, -4, -1, -3, -5, -3, -7, -8, -8, -3, -3, -4, -5, -3, -1, 0, 2, 4, -8],dur=[1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-7, -8, -10, -11, -10, -8, -8, -15, -13, -12, -12, -13, -12, -13, -15, -17, -19, -20, -8, -15, -13, -12],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
@structure
def a2():
	d0 >> pluck([9, 11, 12, 14, 11, 16, 14, 12, 11, 12, 14, 9, 7, 5, 4, 2, 7, 9, 11, 12],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([2, 0, 4, 9, 9, 8, 7, 6, 7, 7, 7, 5, 4, 2, 2, 1, -3, -1, 0, 0, -1, 4],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-6, -4, -3, 5, 4, -5, -3, -1, 0, 2, 2, 2, 4, -3, -3, -3, -7, -8, -6, -5],dur=[0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-12, -13, -15, -3, -7, -10, -8, -12, -5, -17, -15, -13, -12, -10, -10, -11, -10, -15, -10, -12, -13, -15, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([14, 12, 11, 9, 12, 11, 9, 7, 5, 4, 5, 7, 5, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,3.0])
	d1 >> pluck([2, 4, 4, 9, 8, 9, 7, 9, 11, 7, 4, 5, -1, 2, 7, 5, 5, 4, 4, 2, 2, 4, 2, 0, -1],dur=[0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,3.0])
	d2 >> pluck([-3, -1, 0, 4, 5, 4, 0, 4, 2, 1, 2, 4, -1, 0, 2, -3, -3, -1, -8, -3, -3, -4, -6, -4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-6, -4, -3, -12, -10, -8, -7, -8, -6, -5, -7, -8, -10, -12, -15, -13, -11, -10, -16, -15, -13, -12, -10, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)