Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([5, 9, 11, 12, 12, 10, 12, 14, 12, 14, 16, 14, 16, 17],dur=[1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 5, 5, 7, 5, 7, 5, 5, 5, 7, 9, 10, 9],dur=[1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d2 >> pluck([-3, 0, 2, 4, 0, 2, 0, -2, -7, -2, -2, 0, 2, 0, 0],dur=[1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-19, -7, -10, -12, 0, -2, -3, -5, -3, -2, -3, -2, -5, -12, -7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([17, 9, 10, 12, 10, 9, 7, 9, 10, 9, 7, 5],dur=[2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([9, 5, 5, 5, 2, 4, 5, 4, 6, 7, 5, 4, 5, 4, 2],dur=[2.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, -2, -3],dur=[2.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-7, -19, -10, -12, -14, -15, -17, -19, -12, -14, -15, -17, -15, -14, -15, -14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([7, 9, 7, 9, 11, 12, 16, 17, 14, 17],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([4, 5, 7, 5, 5, 7, 12, 12, 10, 5, 10],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, 0, 0, 0, 2, 4, 7, 5, 5, 4, 2, 1, 2],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-17, -19, -7, -8, -7, -8, -10, -12, 0, -2, -3, -2, -14, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([16, 14, 13, 9, 14, 9, 10, 9, 7, 5, 4, 5, 2],dur=[2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([10, 10, 9, 4, 9, 7, 5, 4, 2, 1, 2, 2, 1, -3],dur=[2.0 ,1.0 ,2.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0])
	d2 >> pluck([7, 5, 4, 1, 2, 0, -2, 5, 4, 2, 4, 5, 2, -3, -7],dur=[2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-5, -7, -5, -3, -15, -5, -7, -8, -10, -5, -3, -2, -3, -5, -3, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a4():
	d0 >> pluck([2, 6, 6, 7, 6, 7, 9, 10, 12, 10, 9, 10, 7, 12],dur=[2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
	d1 >> pluck([-3, 0, -3, 2, 2, 0, -2, 2, 2, 2, 0, -2, 7, 4],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-7, -3, -3, -2, 0, 2, -3, -5, -6, -5, -6, -5, -5],dur=[2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-10, -15, -10, -12, -14, -15, -17, -6, -8, -10, -5, -10, -17, -8, -12],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a5():
	d0 >> pluck([12, 12, 14, 16, 17, 16, 14, 16, 12, 17, 12, 9, 14, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([5, 7, 5, 4, 2, 4, 5, 7, 7, 4, 5, 5, 5, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-3, 0, -1, 0, 0, -1, 0, -5, 0, 0, -2, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d3 >> pluck([-7, -8, -10, -12, -10, -5, -17, -12, -12, -15, -19, -14, -2, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a6():
	d0 >> pluck([10, 12, 9, 7, 12, 9, 5, 14, 16, 17, 9, 7, 5, 5],dur=[1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([7, 5, 5, 4, 5, 5, 5, 7, 9, 5, 4, 0],dur=[2.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d2 >> pluck([2, 0, 0, 0, 0, 0, -2, -2, 0, 0, 2, 0, -2, 0, -3],dur=[1.0 ,1.0 ,1.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-5, -8, -7, -12, 0, -2, -3, -7, -3, -2, -5, -7, -7, -15, -14, -12, -19],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(a6, start + 96)
Clock.schedule(lambda : Clock.clear(), start + 112)
