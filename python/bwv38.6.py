Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 4, 11, 12, 11, 9, 7, 9, 11, 11, 12, 14, 12, 11, 9],dur=[2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([4, 4, 8, 9, 7, 6, 4, 6, 8, 8, 9, 11, 12, 5],dur=[2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-4, -3, 2, 4, 2, 4, 2, 0, -1, 4, 4, 5, 7, 0],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-10, -12, -13, -15, -13, -12, -13, -15, -8, -8, -3, -5, -7, -8, -7],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([7, 5, 4, 9, 7, 12, 11, 9, 14, 12, 11, 9, 12],dur=[1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([4, 2, 0, -1, 4, 2, 4, 6, 7, 9, 11, 9, 8, 4, 9],dur=[1.0 ,0.5 ,0.5 ,2.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,2.0])
	d2 >> pluck([0, -1, -3, -4, -3, -1, 0, 2, 2, 4, 5, -1, 0, 4],dur=[0.5 ,0.5 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0])
	d3 >> pluck([-12, -10, -8, -12, -13, -15, -17, -5, -7, -8, -10, -8, -15, -3],dur=[1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,2.0])
@structure
def a2():
	d0 >> pluck([11, 12, 14, 7, 11, 9, 7, 7, 12, 11, 9, 4, 7, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 7, 7, 5, 4, 2, 0, -1, 4, 4, 4, 2, 0, 0, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([4, 4, 2, 0, -6, -5, -6, -5, -5, -3, -4, -3, -5, -5, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-8, -10, -12, -13, -12, -10, -22, -17, -12, -15, -8, -7, -12, -14, -15],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
