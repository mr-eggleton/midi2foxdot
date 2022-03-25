Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 11, 16, 14, 12, 11, 12, 11, 11, 12, 14, 7, 9, 11, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.25 ,0.25 ,0.5 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([7, 6, 7, 6, 7, 6, 7, 7, 7, 6, 4, 6, 7, 6, 7, 7, 4, 6, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-5, -3, -1, -3, -1, 4, 2, 2, 2, 0, -1, -3, -5, 2, 2, 2, 0, -1],dur=[0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-8, -8, -10, -12, -13, -12, -10, -17, -17, -15, -13, -12, -12, -13, -15, -17, -10, -17],dur=[1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 9, 11, 12, 16, 14, 12, 11, 11, 9, 14, 16, 18, 16, 14, 13, 14],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([4, 2, 6, 7, 9, 7, 7, 6, 4, 2, 1, 2, 7, 11, 9, 7, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d2 >> pluck([1, 2, 2, 0, -1, -3, 2, 2, 2, 1, -3, -5, -6, -1, 7, 6, 4, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-5, -5, -6, -8, -10, -8, -6, -5, -17, -5, -6, -1, -3, -5, -8, -3, -10],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
@structure
def a2():
	d0 >> pluck([14, 14, 11, 12, 14, 16, 9, 11, 12, 14, 12, 11, 11, 9, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([9, 7, 7, 7, 7, 7, 6, 7, 7, 7, 6, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([6, 7, 2, 4, 5, 4, 2, 2, 2, 4, 2, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
	d3 >> pluck([2, 0, -1, -3, -5, -7, -8, -10, -12, -13, -12, -10, -17, -15, -13, -12, -10, -10, -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)