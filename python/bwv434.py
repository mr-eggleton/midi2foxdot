Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 9, 11, 12, 11, 9, 11, 8, 6, 4, 7, 7, 5, 4, 9, 9, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([0, 2, 4, 4, 4, 6, 8, 9, 7, 5, 4, -1, 4, 4, 2, 2, 1, 2, 3, 4, 6],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-3, -1, 0, -1, -3, -4, -3, -10, -8, 4, 2, 0, -1, -3, -4, -1, 0, 2, 0, -1, -3, -3, -1, 0, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-3, -12, -8, -15, -13, -12, -10, -8, -8, -8, -3, -1, -3, -4, -5, -6, -7, -8, -9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a1():
	d0 >> pluck([8, 9, 11, 12, 14, 16, 16, 14, 16, 17, 14, 12, 16, 14, 12, 11],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 8, 9, 7, 7, 9, 9, 7, 5, 4, 4, 6, 8, 9, 7, 5],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-1, 0, 2, 0, 4, 4, 2, 0, 0, 0, -1, -5, -3, -3, 4, 4, 3, 2],dur=[0.5 ,0.25 ,0.25 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -15, -8, -3, -1, 0, -1, -3, -5, -7, -10, -5, -12, -11, -10, -8, -7, -6, -5, -4],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
