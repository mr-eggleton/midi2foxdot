Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([16, 16, 16, 16, 14, 12, 11, 12, 14, 16, 16, 14, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([8, 8, 9, 11, 9, 9, 8, 4, 6, 7, 7, 5, 4, 5, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-1, -1, 0, -1, 0, 2, 4, 5, -1, -3, -2, -2, -3, -3, -4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d3 >> pluck([-8, -8, -3, -5, -7, -8, -10, -8, -3, -5, -11, -11, -10, -15, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([9, 11, 12, 9, 9, 7, 5, 4, 5, 7, 9, 9, 7, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([4, 4, 4, 5, 4, 2, 1, 2, 4, 3, 2, 2, 1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d2 >> pluck([0, -1, -3, -1, 0, 2, 4, -3, -3, -3, 0, 0, 0, -2, 0, 2, -3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
	d3 >> pluck([-3, -4, -3, -7, -11, -10, -15, -10, -12, -19, -18, -17, -16, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
@structure
def a2():
	d0 >> pluck([9, 8, 9, 11, 12, 11, 9, 12, 14, 16, 16, 14, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([2, 4, 4, 6, 8, 9, 7, 6, 7, 7, 7, 5, 5, 4, 6, 7],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d2 >> pluck([-3, -1, 0, 2, 4, 2, 2, 0, -2, -3, -3, -3, -1, 0, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
	d3 >> pluck([-7, -8, -10, -12, -13, -15, -13, -12, -10, -9, -10, -11, -10, -8, -7, -5, -3, -5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
@structure
def a3():
	d0 >> pluck([9, 11, 12, 9, 9, 7, 5, 4, 5, 7, 9, 9, 7, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([9, 4, 4, 4, -3, 2, 1, 2, 4, 5, 5, 4, 2, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([2, 0, -1, -3, -1, 0, 2, 4, -3, -3, -3, 0, 0, 0, 0, -1, -3, -4, -3],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-6, -4, -3, -15, -13, -11, -10, -15, -10, -12, -19, -17, -15, -13, -12, -10, -8],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)