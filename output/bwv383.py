Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 11, 12, 12, 11, 9, 11, 12, 14, 9, 7, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 4, 4, 4, 4, 6, 8, 9, 9, 8, 4, 7, 7, 9, 7, 5, 4, 2, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,1.0 ,0.25 ,0.25])
	d2 >> pluck([-1, -1, 0, -1, -3, 4, 5, 2, -1, 4, 2, 0, 2, 4, 5, 4, 2, 0, -2, -3, -1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25])
	d3 >> pluck([-8, -8, -10, -12, -13, -15, -16, -15, -12, -10, -13, -8, -15, -5, -7, -8, -10, -8, -7, -13, -12, -10],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([4, -60, 2, 4, 5, 7, 5, 4, 2, 0, -60, 0],dur=[4.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0])
	d1 >> pluck([-1, -60, -1, 0, -1, 0, 2, 4, 4, 2, 2, 0, 0, -1, -5, -60, -5],dur=[4.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0])
	d2 >> pluck([-4, -60, -5, -5, 0, -3, -1, 0, -5, -5, -5, -7, -8, -60, -5],dur=[4.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.75 ,0.25 ,2.0 ,rest(1.0) ,1.0])
	d3 >> pluck([-8, -60, -5, -7, -8, -3, -5, -17, -15, -13, -12, -17, -24, -60, -8, -7],dur=[4.0 ,rest(1.0) ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,0.5 ,0.5])
@structure
def a2():
	d0 >> pluck([7, 7, 9, 11, 12, 12, 11, 9, 11, 12, 14, 9, 7, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 0, 4, 5, 5, 4, 4, 9, 8, 9, 9, 8, 6, 8, 4, 8, 9, 9, 7, 5, 4, 4, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-5, 0, 0, 2, 2, 0, 2, 4, 4, -1, 4, 2, 0, 4, 4, 2, 2, 0, -2, -3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-8, -10, -8, -12, -7, -16, -15, -13, -12, -10, -8, -15, -8, -3, -5, -7, -8, -10, -10, -11, -10, -7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a3():
	d0 >> pluck([4, -60, 9, 7, 4, 5, 7, 5, 4, -60, 9, 7, 4, 5, 7],dur=[2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([1, -60, 5, 4, 2, 2, 0, 2, 2, 0, -60, 4, 2, 2, 0, -1, -3, 2, -1],dur=[2.0 ,rest(1.0) ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-3, -60, 0, 0, -1, -3, -3, -5, -1, 0, -60, 0, -1, -5, -7, -8, -10, -5],dur=[2.0 ,rest(1.0) ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-3, -60, -19, -17, -15, -10, -12, -13, -17, -15, -60, -15, -13, -12, -10, -13, -17],dur=[2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
@structure
def a4():
	d0 >> pluck([4, 9, 7, 9, 11, 12, 11, 9, 7, 5, 4, 2, 9, 7, 5],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([0, 4, 4, 4, 4, 4, 5, 7, 5, 5, 4, 4, 2, 0, -1, -2, 0, 5, 5, 4, 4, 2],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-5, 0, -1, 0, -1, -3, 2, -5, 0, -1, -3, -1, -3, -4, -5, -3, 2, 2, -1, 0, -5],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-12, -15, -12, -8, -10, -12, -13, -15, -16, -15, -13, -12, -10, -8, -5, -7, -8, -10, -12, -13, -17, -15, -13],dur=[2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a5():
	d0 >> pluck([4, 9, 7, 9, 11, 12, 11, 9, 7, 12, 11, 14, 9, 7, 5],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([0, 4, 4, 2, 0, 2, 4, 7, 6, 7, 7, 7, 9, 7, 5, 4, 2, 4, -3, 2],dur=[2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-5, 0, 0, -2, -3, -5, -7, -5, 4, -3, 2, 0, -1, 4, 2, 4, 5, 4, 2, 0, -1, 1, 2, -3],dur=[2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-12, -12, -10, -8, -7, -8, -10, -12, -10, -8, -8, -7, -5, -10, -8, -7, -7, -8, -10, -7],dur=[2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(lambda : Clock.clear(), start + 96)
