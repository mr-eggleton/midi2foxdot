Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([14, 15, 14, 12, 14, 7, 12, 12, 10, 9, 10, 12, 9, 7, 14, 15, 17, 19, 9],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 5, 5, 4, 6, 7, 9, 7, 6, 7, 9, 6, 2, 7, 10, 10, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, -2, -3, -2, 0, 2, 3, 2, 0, 2, 3, 2, 0, -2, -2, 0, 2, 3, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-5, -12, -7, -14, -2, -3, -5, -6, -5, -12, -10, -17, -5, -5, -7, -9, -7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([7, 5, 17, 17, 19, 15, 14, 14, 14, 15, 14, 12, 10, 12, 5, 10, 10, 9, 14],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([5, 9, 10, 7, 9, 10, 10, 5, 5, 7, 7, 5, 4, 2, 0, 4],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5])
	d2 >> pluck([2, 0, 2, 0, 5, 5, -2, 0, 4, 2, 0, 2, 0, -2, -3, -5, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-7, -9, -9, -10, -10, -9, -7, -14, -2, -3, -5, -3, -2, -3, -5, -7, -8, -7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([12, 10, 9, 7, 5, 17, 16, 14, 19, 9, 17, 17, 16, 13, 14, 14],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,3.0])
	d1 >> pluck([5, 5, 4, 0, 2, 10, 9, 7, 4, 5, 7, 9, 10, 9, 9, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([2, 0, -2, -3, 9, 7, 5, 4, 2, 4, 2, 2, 7, 4, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,3.0])
	d3 >> pluck([-14, -12, -19, -10, -5, -3, -2, -11, -10, -5, -3, -15, -10],dur=[1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a3():
	d0 >> pluck([17, 14, 12, 11, 12, 17, 19, 20, 19, 17, 15, 14, 12, 15, 17, 15, 14, 12, 18],dur=[1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([9, 5, 5, 7, 0, 8, 7, 5, 12, 8, 7, 5, 3, 7, 7, 10, 9, 7, 9],dur=[1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([2, -3, -1, 0, 2, 3, 5, 3, 2, 3, 5, 3, 0, 0, -1, -5, 0, -1, 0, 2, 3, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-10, -9, -7, -5, -4, -5, -3, -1, 0, -7, -5, -12, -12, 0, 0],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,1.0])
@structure
def a4():
	d0 >> pluck([19, 7, 12, 12, 15, 14, 12, 10, 9, 10, 7, 9, 10, 12, 14, 15, 12, 18, 19, 21, 14, 14, 15, 9],dur=[1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([2, 7, 9, 10, 9, 7, 6, 7, 9, 11, 12, 10, 9, 7, 6, 7, 7],dur=[2.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, -2, 3, 3, -6, -3, 2, 2, 3, 5, 7, 5, 3, 2, 9, 2, 2, -2],dur=[1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-2, -3, -5, -7, -9, -10, -7, -9, -10, -12, -6, -10, -5, -7, -9, -10, -12, -14, -12, -15, -14, -12, -10],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(lambda : Clock.clear(), start + 80)
