Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 9, 9, 11, 9, 7, 6, 4, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,4.0])
	d1 >> pluck([6, 7, 6, 7, 9, 9, 7, 6, 7, 6, 4, 2, 1, -1, 1, -3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.5 ,1.0 ,0.25 ,0.25 ,1.0 ,4.0])
	d2 >> pluck([2, 4, 4, 2, 2, 2, 2, 1, -1, -3, -1, -3, -5, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,4.0])
	d3 >> pluck([-10, -11, -10, -8, -6, -10, -5, -17, -10, -8, -6, -5, -3, -15, -10],dur=[1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,4.0])
@structure
def a1():
	d0 >> pluck([9, 9, 9, 9, 11, 7, 11, 11, 12, 11, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,4.0])
	d1 >> pluck([2, 1, 2, 4, 1, 2, 4, 6, 7, 6, 4, 7, 8, 9, 8, 4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.5 ,0.5 ,4.0])
	d2 >> pluck([-6, -8, -3, -5, -6, -6, -8, -1, -1, 4, 4, 4, -3, 5, 4, 1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,4.0])
	d3 >> pluck([-10, -15, -13, -11, -15, -10, -11, -9, -8, -9, -8, -8, -10, -12, -13, -15, -19, -22, -20, -15],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,4.0])
@structure
def a2():
	d0 >> pluck([9, 9, 9, 9, 14, 9, 9, 11, 11, 9, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,4.0])
	d1 >> pluck([6, 6, 4, 6, 7, 9, 9, 7, 6, 6, 4, 3, 4, 4, 2, 0, -1],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,4.0])
	d2 >> pluck([2, 2, 1, 2, 4, 6, 4, 2, 0, 2, 2, 2, 0, -1, -3, -5, -6, -8, -6, -5],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,1.0 ,4.0])
	d3 >> pluck([-10, -8, -6, -5, -6, -8, -10, -12, -13, -15, -13, -11, -10, -10, -5, -6, -8, -10, -12, -11, -10, -9, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,4.0])
@structure
def a3():
	d0 >> pluck([9, 9, 9, 9, 9, 6, 7, 6, 4, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.5 ,0.5 ,4.0])
	d1 >> pluck([4, 1, 2, 4, 6, 6, 4, 7, 6, 4, 4, 3, 1, 3, 4, 2, 2, 1, -1, 1, -3],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,4.0])
	d2 >> pluck([-8, -5, -6, -8, -10, -3, 2, 2, 1, 0, -1, -1, -1, -1, -5, -8, -3, -6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,4.0])
	d3 >> pluck([-11, -15, -13, -11, -10, -8, -6, -5, -3, -15, -13, -20, -17, -13, -15, -17, -20, -15, -22],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,4.0])
@structure
def a4():
	d0 >> pluck([9, 11, 12, 9, 8, 9],dur=[2.0 ,2.0 ,4.0 ,2.0 ,2.0 ,4.0])
	d1 >> pluck([6, 5, 4, 4, 5, 7, 9, 7, 7, 5, 4, 4],dur=[2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,4.0])
	d2 >> pluck([-3, 2, 0, -1, -3, -5, -7, -8, -10, 2, 0, -1, 1],dur=[1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,4.0])
	d3 >> pluck([-10, -16, -15, -13, -12, -10, -13, -8, -15],dur=[2.0 ,2.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,4.0])
@structure
def a5():
	d0 >> pluck([14, 16, 9, 11, 13, 9, 8],dur=[3.0 ,1.0 ,2.0 ,2.0 ,4.0 ,3.0 ,1.0])
	d1 >> pluck([11, 9, 7, 6, 6, 8, 9, 8, 1, 1, 2, 4, 6, 4, 2],dur=[3.0 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-6, -8, -6, -5, -8, -6, -4, -3, -6, 1, -1, -3, -4, -6, -4, -3, -1, 1, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-13, -11, -10, -9, -8, -7, -6, -13],dur=[3.0 ,1.0 ,2.0 ,2.0 ,2.0 ,2.0 ,2.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(lambda : Clock.clear(), start + 96)
