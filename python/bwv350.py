Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 7, 5, 3, 2, 5, 7, 9, 7, 7, 6, 7, 10, 9, 7, 5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 7, 5, 3, 2, 0, -2, 2, 3, 2, 3, 2, 3, 2, 2, 7, 7, 6, 7, 3, 0],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-2, 0, 2, -2, -3, -5, -7, -2, -2, 0, -2, -3, -3, -2, 0, -2, 2, 2, 0, -2, 0, -3],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.25 ,0.25 ,1.0 ,0.5 ,1.0 ,0.75 ,0.25 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-17, -15, -14, -17, -15, -14, -14, -15, -17, -17, -18, -17, -12, -10, -17, -17, -10, -9, -15, -19],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
@structure
def a1():
	d0 >> pluck([2, 5, 7, 9, 7, 7, 6, 7, 14, 14, 14, 7, 12, 12, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, -2, 0, 2, 0, -2, 3, 2, 4, 2, 2, 2, 7, 7, 6, 7, 7, 2, 2, 0],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5])
	d2 >> pluck([-7, -2, -3, -5, 0, -2, -2, -3, -5, -3, -2, 0, -2, -2, 0, 2, 0, -2, -3, -2, 0, -2, -3, -5, -6],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,2.0 ,1.5 ,1.0 ,0.5])
	d3 >> pluck([-14, -14, -9, -10, -12, -11, -10, -17, -17, -15, -14, -12, -10, -9, -8, -6, -5, -10],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([7, 5, 2, 7, 7, 6, 7, 6, 7, 6, 7, 9, 10, 9],dur=[1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([-2, 2, 0, -2, 0, -2, 2, 2, 3, 2, 0, -2, 0, 2, 2, 0, 2, 2, 2, 2],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-5, -2, -3, -5, -3, -7, -2, 0, 2, 0, -2, -3, -5, -3, -5, -3, -2, -3, -3, -5, -6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-9, -15, -19, -14, -17, -15, -14, -12, -10, -9, -10, -12, -14, -12, -14, -15, -17, -15, -17, -18, -17, -15, -14, -17, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a3():
	d0 >> pluck([10, 9, 7, 5, 2, 3, 5, 5, 7, 5, 3, 2, 14, 12, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 2, 0, -2, 0, -2, -3, -2, 0, 2, 3, 5, 3, 2, 2, 0, -1, 0, -1, 7, 7, 6, 7, 6, 4],dur=[1.0 ,0.75 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25])
	d2 >> pluck([-5, -5, -6, -5, -9, -12, -7, -7, -7, -5, -3, -2, -2, -2, -3, -5, -5, -2, 0, 2, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.75 ,0.25 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-17, -10, -9, -15, -14, -12, -10, -10, -9, -14, -12, -10, -9, -12, -5, -17, -15, -14, -12, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
