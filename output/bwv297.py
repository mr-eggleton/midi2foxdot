Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([2, 5, 7, 9, 14, 12, 11, 9, 11, 12, 11, 9, 14, 14, 14, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-3, 2, 4, 5, 9, 9, 8, 9, 8, 9, 9, 8, 6, 8, 4, 9, 9, 7, 11, 9],dur=[1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-7, -3, -2, 2, 5, 4, 4, 2, 0, 2, 4, 5, -1, 4, 2, 1, 2, 2, 4, 5, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-10, -10, -17, -22, -10, -3, -8, -7, -12, -10, -8, -20, -15, -7, -2, -3, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([16, 14, 9, 10, 9, 7, 7, 5, 5, 4, 4, 2, 9, 12, 12, 7, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([9, 7, 5, 5, 7, 5, 5, 4, 2, 4, 0, 2, 2, 1, -3, 5, 5, 4, 5, 4],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-3, -3, 2, 2, 0, 0, 2, -2, -5, 0, -2, -3, -2, -2, -3, -5, -7, 2, 0, 0, 0, -3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-11, -10, -8, -7, -7, -8, -7, -14, -12, -19, -14, -17, -15, -22, -10, -15, -17, -15, -14, -12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
