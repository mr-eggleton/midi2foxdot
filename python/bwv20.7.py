Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([5, 7, 9, 10, 12, 12, 14, 16, 17, 5, 7, 9, 10, 12, 12, 10, 9, 7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 5, 4, 5, 9, 10, 9, 7, 9, 0, 5, 7, 7, 5, 5, 4, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, -2, 0, -2, -3, 0, 5, 5, 0, 0, -3, 2, 2, 0, -2, -3, -2, 0, 0],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-7, -7, -5, -3, -7, -2, 0, -7, -7, -8, -10, -12, -14, -15, -10, -17, -15, -14, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 5, 5, 10, 9, 7, 5, 5, 7, 9, 10, 12, 12, 14, 16, 17],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 2, 2, 4, 5, 5, 4, 0, 0, 5, 4, 5, 9, 10, 9, 7, 9],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, -3, -3, -5, -3, 2, 0, -2, -3, -3, -2, 0, -2, -3, 0, 5, 5, 0, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-11, -10, -8, -7, -10, -5, -10, -12, -14, -12, -19, -7, -7, -5, -3, -7, -2, 0, -7],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([5, 7, 9, 10, 12, 12, 10, 9, 7, 9, 5, 5, 10, 9, 7, 5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([0, 5, 7, 7, 5, 5, 4, 5, 4, 4, 4, 2, 2, 4, 5, 5, 4, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, 2, 2, 0, -2, -3, -2, 0, 0, -3, -3, -3, -5, -3, 2, 0, -2, -3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-7, -8, -10, -12, -14, -15, -10, -17, -15, -14, -12, -11, -10, -8, -7, -10, -5, -10, -12, -14, -12, -19],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([12, 7, 9, 10, 10, 9, 9, 7, 12, 14, 16, 17, 9, 7, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([5, 7, 7, 6, 7, 7, 6, 2, 5, 5, 12, 10, 9, 7, 5, 5, 4, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-3, -2, 0, 2, 4, -3, -2, 0, -2, 0, -2, -3, -5, -7, -5, -3, -2, 0, -5, 0, -2, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-7, -8, -9, -10, -11, -10, -10, -17, -15, -14, -12, -10, -8, -7, -12, -12, -19],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
