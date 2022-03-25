Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 7, 9, 11, 12, 11, 9, 7, 6, 7, 9, 7, 6, 4, 12, 11, 16, 14, 6, 12],dur=[1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([4, 4, 6, 7, 9, 7, 3, 4, 6, 6, 4, 4, 3, 4, 3, 4, 7, 6, 4, 6, 6, 7, 6],dur=[1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-5, -1, 0, -3, -5, -3, -1, 0, -1, -1, -1, -5, -3, -5, -5, -3, -1, -1, -3, -3, -1, 0],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -8, -9, -8, -9, -8, -6, -5, -3, -1, -13, -8, -8, -8, -10, -12, 0, -1, -3],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0 ,1.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 9, 9, 7, 11, 9, 11, 7, 9, 11, 12, 14, 12, 11, 12, 11, 9, -60, 12, 6],dur=[0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,1.0])
	d1 >> pluck([7, 7, 6, 2, 7, 9, 6, 7, 4, 6, 4, 2, 4, 4, 2, 4, -60, 4, 3, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,0.5 ,0.5])
	d2 >> pluck([2, 4, 2, 0, -1, 2, 2, 2, 1, 2, -4, -3, -3, -1, -4, -3, -1, 0, -60, 0, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,1.0])
	d3 >> pluck([-5, -12, -10, -17, -5, -6, -10, -5, -10, -8, -10, -12, -13, -8, -3, -15, -60, -3, -1, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([16, 15, 16, 14, 12, 11, 9, 19, 18, 16, 15, 13, 11, -60, 16, 14, 12, 11, 9, 11, 3, 4, 9, 7, 6, 4, 4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,0.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([6, 4, 6, 7, 5, 4, 9, 11, 12, 6, 4, 3, -60, 4, 4, 6, 3, 6, 4, 4, 4, 3, -1],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-1, 0, -1, -3, -5, -4, -3, -1, 0, -1, -6, -60, -1, -3, -1, 0, -6, -3, -1, -3, -1, -3, -5, -5],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-1, -3, -5, -6, -8, -10, -12, -13, -15, -13, -13, -60, -4, -3, -15, -3, -3, -6, -5, -12, -13, -15, -13, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)