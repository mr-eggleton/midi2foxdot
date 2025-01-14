Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([5, 5, 7, 5, 4, 5, 0, -60, 5, 5, 7, 5, 4, 5, 2, -60, 17, 17, 19, 17, 16, 17, 19],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([5, 5, 7, 5, 4, 5, 0, -60, 5, 5, 7, 5, 4, 5, 2, -60, 10, 10],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,3.0 ,1.0])
	d10 >> pluck([-7, -7, -5, -7, -8, -7, -12, -60, -7, -7, -5, -7, -8, -7, -10, -60, 2, 0],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,3.0 ,1.0])
	d11 >> pluck([-7, -7, -5, -7, -8, -7, -12, -60, -7, -7, -5, -7, -8, -7, -10, -60, -10, -8],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,3.0 ,1.0])
@structure
def a1():
	d0 >> pluck([19, 10, 9, 14, 10, 9, 7, 5, 5, 7, 5, 4, 5, 0, -60, 5, 5, 7, 5],dur=[1.0 ,1.0 ,2.0 ,0.75 ,0.25 ,2.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25])
	d1 >> pluck([10, 7, 5, 10, 7, 5, 4, 5, 5, 7, 5, 4, 5, 0, -60, 5, 5, 7, 5],dur=[1.0 ,1.0 ,2.0 ,0.75 ,0.25 ,2.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25])
	d10 >> pluck([0, 0, 2, -5, 0, -1, 0, -1, 0, -7, -7, -5, -7, -8, -7, -12, -60, -7, -7, -5, -7],dur=[2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25])
	d11 >> pluck([-8, -7, -10, -14, -12, -7, -7, -5, -7, -8, -7, -12, -60, -7, -7, -5, -7],dur=[2.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25])
@structure
def a2():
	d0 >> pluck([4, 5, 2, -60, 17, 17, 19, 17, 16, 17, 21, 19, 19, 19, 21, 19, 18, 19, 22, 21],dur=[0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([4, 5, 2, -60, 16, -60, 12],dur=[0.5 ,0.5 ,1.0 ,rest(5.0) ,3.0 ,rest(3.0) ,3.0])
	d10 >> pluck([-8, -7, -10, -60, 10, -60, 15],dur=[0.5 ,0.5 ,1.0 ,rest(5.0) ,3.0 ,rest(3.0) ,3.0])
	d11 >> pluck([-8, -7, -10, -60, 1, -60, 6],dur=[0.5 ,0.5 ,1.0 ,rest(5.0) ,3.0 ,rest(3.0) ,3.0])
@structure
def a3():
	d0 >> pluck([21, 21, 22, 21, 19, 21, 24, 22, 21, 19, 17, 19, 10, 17, 9, 16, 7, 17, 9, 21, 19, 17, -60, 0, 0, 2, 0, -1, 0, 17],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([-60, 15, 14, 12, 10, 9, 12, 10, 9, -60, 3],dur=[rest(3.0) ,1.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,rest(5.0) ,1.0])
	d10 >> pluck([-60, 6, 7, 9, 10, 12, 4, 5, -60, 8],dur=[rest(3.0) ,1.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,rest(5.0) ,1.0])
	d11 >> pluck([-60, -2, -2, -2, -2, 0, -12, -7, -60, -1],dur=[rest(3.0) ,1.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,rest(5.0) ,1.0])
@structure
def a4():
	d0 >> pluck([17, 19, 17, 16, 17, 2, 2, 3, 2, 1, 2, 19, 21, 19, 18, 19, 7, 7, 9, 7, 6, 7, 24, 26, 24, 23, 24, 26, 27, 26],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25])
	d1 >> pluck([3, 2, -60, 5, 4, -60, 10, 9, 12],dur=[1.0 ,1.0 ,rest(3.0) ,2.0 ,1.0 ,rest(3.0) ,2.0 ,1.0 ,2.0])
	d10 >> pluck([8, -60, -2, -60, 3, 3, 6],dur=[2.0 ,rest(3.0) ,3.0 ,rest(3.0) ,2.0 ,1.0 ,2.0])
	d11 >> pluck([-1, -60, -12, -60, -7, -19, -2],dur=[2.0 ,rest(3.0) ,3.0 ,rest(3.0) ,2.0 ,1.0 ,2.0])
@structure
def a5():
	d0 >> pluck([25, 26, 28, 28, 28, 29, (-3, 5), (-3, 5), (-3, 5), (-3, 5), (-3, 5), 7, 9, 12, 10, 7, 5, 4, -60, 10, 10],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,0.0 ,0.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,1.0])
	d1 >> pluck([10, 9, 7, 9, 7, 9, 7, 5, (-3, 5), -60, 9, 9, (-5, 4), (-5, 4)],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(3.5) ,0.5 ,1.0 ,3.0 ,3.0])
	d10 >> pluck([7, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,3.0])
	d11 >> pluck([-14, -12, -12, -12, -19, -60, -12, -10, -12, -13, -12, -24, -60, -12, -10, -12, -13, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5])
@structure
def a6():
	d0 >> pluck([9, 10, 14, 12, 9, 7, 5, -60, 17, 17, 16, 17, 21, 19, 19, 17, 17, 16, 16, 14, 12, 10, 9, 9, 11, 13],dur=[0.0 ,0.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,1.0 ,0.0 ,0.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,0.5 ,0.25 ,0.25])
	d1 >> pluck([(-3, 5), (-3, 5), (-2, 7), (-2, 7), (-3, 7), (-3, 5)],dur=[3.0 ,3.0 ,3.0 ,3.0 ,3.0 ,1.0])
	d10 >> pluck([0, 0, 4, 4, 4, 4, 1, 1, 4, 4, 2, 2],dur=[3.0 ,3.0 ,3.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d11 >> pluck([-24, -60, -12, -10, -12, -13, -12, -24, -60, -12, -10, -12, -13, -12, -11, -15, -11, -10],dur=[1.0 ,rest(2.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a7():
	d0 >> pluck([14, 16, 17, 16, 14, 12, 11, 9, 7, 7, 9, 11, 12, 11, 12, 11, 12, 11, 12, 11, 12, 12, 13, 12, 10, 12, 15, 13],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,3.0 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,3.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.5])
	d1 >> pluck([(-3, 5), (-5, 5), (-5, 3), (0, 3), (0, 4), 0, 0, 1],dur=[2.0 ,3.0 ,3.0 ,3.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d10 >> pluck([2, 2, 2, 2, 2, 2, -1, -1, 2, 2, 0, 0, 0, 0, 0, 0, -9, -7, -9, -10, -9, -9, -9, -7, -9],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.5 ,0.25 ,0.25])
	d11 >> pluck([-60, -13, -17, -13, -12, -60, -16, -15, -14],dur=[rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,3.0 ,3.0 ,2.0])
@structure
def a8():
	d0 >> pluck([10, 8, 7, 1, 12, 13, 17, 15, 12, 10, 9, 6, 14, 15, 17, 15, 14, 12],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([1, 2, -60, 15, 13, 1, 3, 4, -60, 17, 15, 6, 8, 7, 8, 9],dur=[1.0 ,1.0 ,rest(0.5) ,0.25 ,0.25 ,1.0 ,3.0 ,1.0 ,rest(0.5) ,0.25 ,0.25 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0])
	d10 >> pluck([-10, -9, -9, -9, -7, -9, -10, -9, -9, 9, 9, -1, 0, 5, 3],dur=[0.5 ,0.5 ,3.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0])
	d11 >> pluck([-14, -14, -12, -12, -12, -12, -10, -9, -7, -6],dur=[1.0 ,3.0 ,3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0])
@structure
def a9():
	d0 >> pluck([11, 7, 9, 11, 12, 14, 16, 18, 19, 18, 19, 18, 19, -60, 23, 23, 24, 23, 7, 9, 11, 12, 14, 16, 18, 19, 18, 19, 18, 19, -60, 23, 23, 24, 23, -5, -3, -1, 0, 2, 4, 6, 7, 6, 7, 7, 7, 9, 11],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
	d1 >> pluck([7, -60, 2, 2, 3, 2, -60, 14, 14, 15, 14, -60, 2, 2, 3, 2, -60, 14, 14, 15, 14, -60, 14, 14, 15, 14, -5, -3, -1],dur=[1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25])
	d10 >> pluck([2, -60, -1, -1, 0, -2, -60, 7, 7, 7, 7, -60, -1, -1, 0, -1, -60, 7, 7, 7, 7, -60, -1, -1, 0, -1, -5, -3, -1],dur=[1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25])
	d11 >> pluck([-5, -60, -5, -17, -15, -14, -12, -10, -8, -6, -5, -6, -5, -6, -5, -60, -5, -17, -15, -13, -12, -10, -8, -6, -5, -6, -5, -6, -5, -60, -5, -5, -12, -5, -17, -15, -13],dur=[1.0 ,rest(2.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25])
@structure
def a10():
	d0 >> pluck([12, 14, 16, 18, 19, 18, 19, 18, 19, 19, 19, 19, 20, 20, 20, 20, 21, 21, 17, 17, 14, 14, 11, 11, 7, 7, 11, 11, 12, 12, 14, 14],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([0, 2, 4, 6, 7, 6, 7, 6, 7, -60, 7, 7, 7, 7, 11, 11],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(10.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d10 >> pluck([0, 2, 4, 6, 7, 6, 7, 6, 7, -60, 5, 5, 4, 4, 2, 2],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(10.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d11 >> pluck([-12, -10, -8, -6, -5, -6, -5, -6, -5, -60],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(13.0)])
@structure
def a11():
	d0 >> pluck([16, 16, 19, 17, -60, 20, 21, 24, 18, 21, 19, -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,rest(6.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,rest(1.5)])
	d1 >> pluck([12, 12, 16, 14, -60, 11, 16, 4, 12, 12, 10, -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,rest(6.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,rest(1.5)])
	d10 >> pluck([0, 0, -1, 4, 4, 5, 5, 2, 2, -1, -1, -4, -4, 4, 4, 2, 2, 0, 0, -3, -3, 2, 2, -5, -5, 7, -60],dur=[0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(1.5)])
	d11 >> pluck([-60, -6, -5, -4],dur=[rest(14.5) ,0.5 ,0.5 ,0.5])
@structure
def a12():
	d0 >> pluck([-60, 17, 17, 16, 16, 14, 14, 12, 12, 12, 11, -60, 7, 7, 8, 8, 5, 5, 20, 20],dur=[rest(5.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([-60, 2, 2, 4, 12, 10, 10, 7, 7, 8, -60, 2, 2, -1, -1],dur=[rest(5.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,rest(3.5) ,0.5 ,0.5 ,0.5 ,0.5])
	d10 >> pluck([-60, -5, -5, -5, 7, 5, 5, 4, 4, 2, -60, 8, 8, 5, 5, 2, 2],dur=[rest(5.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,rest(2.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d11 >> pluck([-3, -3, -7, -7, -10, -10, -13, -13, -17, -17, -13, -13, -12, -12, -10, -10, -8, -8, -7, -60],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,rest(5.5)])
@structure
def a13():
	d0 >> pluck([19, 24, 24, 26, 23, 24, (-5, 4), (-5, 4), (-5, 4), (-5, 4), 16, 17, 16, 14, 12, 11, -60, 17, 19, 17],dur=[1.0 ,1.0 ,2.0 ,0.75 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.5 ,0.25 ,0.25])
	d1 >> pluck([0, 16, 15, 15, 17, 14, 12, (-5, 4), -60, (-5, 4), (-5, 4), (-5, 4), (-5, 4), (-5, 4), (-5, 4), (-5, 5), -1],dur=[0.5 ,1.0 ,0.5 ,2.0 ,0.75 ,0.25 ,0.5 ,0.5 ,rest(2.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,2.0])
	d10 >> pluck([3, 0, -6, -6, -5, -5, 7, 7, -5, -5, 0, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -10, (-10, -5)],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,2.0])
	d11 >> pluck([-60, 7, 9, 7, 6, 7, 7, 7, 9, 7, 6, 7, 7],dur=[rest(5.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0])
@structure
def a14():
	d0 >> pluck([16, 14, 13, -60, 22, 22, 21, 19, 17, 16, 14, 13, 14, 9, 10, 13, 14, 16, 17, 16, 14, 9, 10, 13, 14, 16, 17, 16, 14, 9, 11, 13, 14, 16, 17, 16, 14, 9, 10, 13, 14, 16, 17, 16, 14, 9, 10, 13],dur=[0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
	d1 >> pluck([-1, -2, (-5, 7), -3, (5, 9), -60, -3, -1, 1],dur=[1.0 ,3.0 ,3.0 ,1.0 ,1.0 ,rest(6.25) ,0.25 ,0.25 ,0.25])
	d10 >> pluck([(-10, -5), (-8, -5), -8, -7, 2, -60, -3, -1, 1],dur=[1.0 ,3.0 ,3.0 ,1.0 ,1.0 ,rest(6.25) ,0.25 ,0.25 ,0.25])
	d11 >> pluck([7, 7, 9, 7, 6, 7, 10, 9, -7, -60, -15, -13, -11],dur=[1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,rest(6.25) ,0.25 ,0.25 ,0.25])
@structure
def a15():
	d0 >> pluck([14, 16, 17, 19, 21, 19, 17, 16, 14, 12, 11, 9, 7, 14, 12, 14, 12, 0, -1, -1, 5, 5, 4, 4, 9, 9, 7],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,3.0 ,3.0 ,0.0 ,0.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([2, 4, 5, 7, 9, 7, 5, 4, 2, 0, -3, -1, -5, -3, -1, 0, 2, 4, 6, 7, 11, 11, 11, 11, 11, 12, -5, -5, -5, 2, 2, 0, 0, 0, 0, 0],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d10 >> pluck([2, 4, 5, 7, 9, 7, 5, 4, 2, 0, -1, -3, -5, -3, -1, 0, 2, 4, 6, 7, 5, 5, 5, 5, 5, 4, -8, -10, -10, -1, -1, 0, 0, -7, -7, -8],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d11 >> pluck([-10, -8, -7, -5, -3, -5, -7, -8, -10, -12, -13, -15, -17, -15, -13, -12, -10, -8, -6, -5, -5, -5, -5, -5, -5, -12, -60],dur=[0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(6.0)])
@structure
def a16():
	d0 >> pluck([7, 12, 12, 11, 11, 17, 17, -60, 16, 17, 16, 14, 16, 21, 21, 19],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(4.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0])
	d1 >> pluck([0, 7, 7, 5, 5, 2, 2, -60, 12, 12, 12, 12],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(4.0) ,3.0 ,3.0 ,1.0 ,1.0])
	d10 >> pluck([-8, 4, 4, 2, 2, -1, -1, -60, 7, 2, 2, 4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(4.0) ,3.0 ,3.0 ,1.0 ,1.0])
	d11 >> pluck([-60, 0, -6, -6, -5],dur=[rest(8.0) ,3.0 ,3.0 ,1.0 ,1.0])
@structure
def a17():
	d0 >> pluck([11, 12, 12, 11, 11, 17, 17, 16, 16, 21, 21, 19, 19, 24, 24, 23, 23, 29, 29, -60],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(4.0)])
	d1 >> pluck([5, 4, 7, 5, 5, 2, 2, 4, 4, 12, 12, 12, 12, 19, 19, 17, 17, 14, 14, -60],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(4.0)])
	d10 >> pluck([2, 0, 4, 2, 2, -1, -1, 0, 0, 5, 5, 4, 4, 16, 16, 14, 14, 11, 11, -60],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(4.0)])
	d11 >> pluck([-17, -12, -60],dur=[1.0 ,1.0 ,rest(14.0)])
@structure
def a18():
	d0 >> pluck([(0, 3), (0, 3), (0, 3), (0, 3), (0, 4), 5, 2, 0, (-5, 4), (-5, 4), (-5, 4), (-5, 4), (-5, 4)],dur=[3.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([-5, -4, -3, -3, -3, 2, -1, 0, (-5, 4), -60],dur=[3.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,rest(3.0)])
	d10 >> pluck([0, -4, -6, -7, -8, -3, -7, -8, 0, 0, 0, 0, 0, 0],dur=[3.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d11 >> pluck([-12, -16, -18, -19, -20, -22, -17, -12, -10, -12, -13, -12, -24],dur=[3.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
@structure
def a19():
	d0 >> pluck([(-5, 4), 14, 16, 19, 17, -60, (-5, 5), 21, 23, 24, 28, 19, -60, 17, 16, 14, 16, 17, 16, 14, 16, 17, 16, 14, 16, 19, 17],dur=[2.0 ,0.0 ,0.0 ,1.0 ,1.0 ,rest(1.0) ,3.0 ,0.0 ,0.0 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,1.0])
	d1 >> pluck([16, 16, (-5, 5), -60, 23, 23, (-5, 4), (-5, 4), (-5, 5)],dur=[1.0 ,1.0 ,3.0 ,rest(1.0) ,1.0 ,1.0 ,3.0 ,3.0 ,2.0])
	d10 >> pluck([0, 2, 2, 0, 0, 2],dur=[2.0 ,3.0 ,3.0 ,3.0 ,3.0 ,2.0])
	d11 >> pluck([-60, -12, -10, -12, -13, -12, -24, -60, -10, -12, -13, -12, -10, -12, -13, -12, -10, -12, -13, -12, -24, -60, -10, -12, -13, -12, -10, -12, -13, -12],dur=[rest(2.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
@structure
def a20():
	d0 >> pluck([-60, 24, 23, 21, 23, 24, 23, 21, 23, 24, 23, 21, 23, 24, 28, 26, 24, 22, 21, 19, 17, 16, 24, 22, 21, 19, 17, 16, 14, 12, 19, 17, 16, 14, 12, 11, 9, 7, 16, 14, 12, 11, 9, 7, 5, 4, 12, 11, 9, 7, 5, 4, 2, 0, -1, 0, -1, 0, -1, 0, -1],dur=[rest(1.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
	d1 >> pluck([(-5, 5), (-5, 5), (-5, 4), (-5, 4, 12), -60, 4, 12, 11, 9, 7, 5, 4, 2, 0, -1, 0, -1, 0, -1, 0, -1],dur=[1.0 ,3.0 ,1.0 ,1.0 ,rest(6.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
	d10 >> pluck([2, 2, 0, (-5, 4), -60, -8, 0, -1, -3, -5, -7, -8, -10, -12, -1, 0, -1, 0, -1, 0, -1],dur=[1.0 ,3.0 ,1.0 ,1.0 ,rest(6.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
	d11 >> pluck([-10, -12, -13, -12, -24, -60, -12, -12, -60, -8, 0, -1, -3, -5, -7, -8, -10, -12, -13, -12, -13, -12, -13, -12, -13],dur=[0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,rest(6.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
@structure
def a21():
	d0 >> pluck([0, 0, 0, 0, -60, 21, 28, 26, 25, 23, 21, 20, 18, 16, 21, 20, 18, 16, 14, 13, 11, 9, 16, 14, 13, 11, 9, 8, 6, 4, 9, 8, 6, 4, 2, 1, -1, -3, -4, -3, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0])
	d1 >> pluck([0, -5, -5, -5, -60, (-3, 9), -60, 9, 8, 6, 4, 2, 1, -1, -3, -4, -3, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,rest(5.25) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0])
	d10 >> pluck([0, -8, -8, -8, -60, -3, -60, 9, 8, 6, 4, 2, 1, -1, -3, -4, -3, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,rest(5.25) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0])
	d11 >> pluck([-12, -24, -24, -24, -60, -15, -60, -8, -3, -4, -6, -8, -10, -11, -13, -15, -16, -15, -16, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,rest(5.0) ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0])
@structure
def a22():
	d0 >> pluck([-3, -3, -2, -2, 14, 17, 22, 26, 22, 26, 22, 26, 22, 26, 22, 27, -60, -2, 27, 22, 27, 22, 27, 22, 27, 22, 27, -60, 12, 10],dur=[1.0 ,1.0 ,3.0 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(2.0) ,1.0 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,rest(0.5) ,0.25 ,0.25])
	d1 >> pluck([-3, -3, -2, -2, -2, -2, -2, -60, 15, 19, 22, -2, -2, 10, -60],dur=[1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,rest(0.25) ,0.25 ,0.25 ,0.25 ,1.0 ,1.0 ,1.5 ,rest(0.5)])
	d10 >> pluck([-3, -3, -2, 0, -2, -3, -2, -7, -2, 0, -2, -3, -2, -5, 3],dur=[1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,2.0])
	d11 >> pluck([-15, -15, -14, -12, -14, -15, -14, -19, -14, -12, -14, -15, -14, -17, -5],dur=[1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0 ,2.0])
@structure
def a23():
	d0 >> pluck([9, 10, 12, 3, 24, 15, 14, 16, 14, 13, 14, 16, 7, 28, 19],dur=[0.5 ,0.5 ,2.0 ,1.0 ,2.0 ,1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,2.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([-60],dur=[rest(16)])
	d10 >> pluck([3, 3, 0, -60, 7, 7, 4, -60],dur=[1.0 ,2.0 ,1.0 ,rest(3.0) ,3.0 ,2.0 ,1.0 ,rest(3.0)])
	d11 >> pluck([-5, -3, -60, -2, 1, -60],dur=[1.0 ,3.0 ,rest(3.0) ,3.0 ,3.0 ,rest(3.0)])
@structure
def a24():
	d0 >> pluck([-60, 22, 24, 22, 21, 22, 13, 28, 26, 25, 28, 26, 25, 26, 25, 28, 26],dur=[rest(6.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25])
	d1 >> pluck([-60, 10, 12, 10, 9, 10, 19, 17, 16, 16, 19, 17, 16, 14, 16],dur=[rest(7.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
	d10 >> pluck([-60, 10, 12, 10, 9, 10, 1, 4, 5, 7, 7, 9, 10, 10, 9, 10],dur=[rest(3.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d11 >> pluck([-2, 0, -2, -3, -2, -11, -10, -9, -8, 1, 2, 4, 4, 5, 7, 7, 5, 7],dur=[1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
@structure
def a25():
	d0 >> pluck([25, 26, 15, 15, 17, 15, 14, 15, 6, 7, 8, 27, 29, 27, 26, 27, 18, 24, 22, 21, 24, 22, 21],dur=[1.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0])
	d1 >> pluck([16, 19, 17, 16, 14, -60, 9, 10, 11, 12, 21, 19, 18, 21, 19, 18],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,rest(6.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0])
	d10 >> pluck([10, 9, -60, 3, 5, 3, 2, 3, 0, 2, 3, 3, 0, 2],dur=[1.5 ,0.5 ,rest(7.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25])
	d11 >> pluck([7, 5, -60, 3, 6, 3, 2, 3, -6, -5, -6, -3, -3, -2, 0, 0, -3, -2],dur=[1.5 ,0.5 ,rest(3.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25])
@structure
def a26():
	d0 >> pluck([21, 22, 21, 24, 22, 21, 22, -60, 20, 22, 20, 19, 20, 11, 20, 20],dur=[0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,rest(6.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([18, 19, 18, 21, 19, 18, 19, -60, 8, 10, 8, 7, 8, 14, 12],dur=[0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,rest(7.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0])
	d10 >> pluck([3, 2, 3, 3, 0, 2, 3, 2, 8, 10, 8, 7, 8, -1, 0, 1, 2, 3, 4, 5, 8, 7],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d11 >> pluck([0, -2, 0, 0, -3, -2, 0, -2, -60, -4, -2, -4, -5, -4, -13, -12, -11, -10, 5, 3],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,rest(3.0) ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a27():
	d0 >> pluck([20, 20, 17, 19, 20, 19, 20, 20, 17, 19, 20, 19, 13, 10, 12, 28, 31, 29, 28, 29, 13, 10, 12, 28, 31, 29, 28, 29, 21, 21, 24, 22, 21, 22, 21],dur=[1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([11, 14, 12, 11, 12, 11, 14, 12, 11, 12, -60, 13, 12, -60, 13, 12, 12, 15, 13, 12, 10, 12, 15, 13],dur=[0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,rest(1.0) ,1.5 ,0.5 ,rest(1.0) ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25])
	d10 >> pluck([5, 8, 7, 5, 7, 5, 8, 7, 5, 7, 10, 7, 8, 10, 8, 10, 7, 8, 10, 8, 6, 3, 5, 6, 5, 6, 3, 5],dur=[0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25])
	d11 >> pluck([2, 5, 3, 2, 3, 2, 5, 3, 2, 3, -60, 3, 0, 1, 3, 1, 3, 0, 1],dur=[0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,rest(6.0) ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25])
@structure
def a28():
	d0 >> pluck([21, 24, 22, 21, 22, 25, 25, 27, 25, 24, 25, 22, 22, 24, 22, 21, 22, 17, 17, 18, 17, 16, 17, 13, 13, 15, 13, 12, 13, 1, 1, 1, 1],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([12, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 18, 18, 20, 18],dur=[1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,3.0 ,3.0 ,1.0 ,0.5 ,0.25 ,0.25])
	d10 >> pluck([6, 5, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],dur=[1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,3.0 ,3.0 ,2.0])
	d11 >> pluck([3, 1, -14, -60, -6],dur=[1.5 ,0.5 ,1.0 ,rest(11.0) ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(a6, start + 96)
Clock.schedule(a7, start + 112)
Clock.schedule(a8, start + 128)
Clock.schedule(a9, start + 144)
Clock.schedule(a10, start + 160)
Clock.schedule(a11, start + 176)
Clock.schedule(a12, start + 192)
Clock.schedule(a13, start + 208)
Clock.schedule(a14, start + 224)
Clock.schedule(a15, start + 240)
Clock.schedule(a16, start + 256)
Clock.schedule(a17, start + 272)
Clock.schedule(a18, start + 288)
Clock.schedule(a19, start + 304)
Clock.schedule(a20, start + 320)
Clock.schedule(a21, start + 336)
Clock.schedule(a22, start + 352)
Clock.schedule(a23, start + 368)
Clock.schedule(a24, start + 384)
Clock.schedule(a25, start + 400)
Clock.schedule(a26, start + 416)
Clock.schedule(a27, start + 432)
Clock.schedule(a28, start + 448)
Clock.schedule(lambda : Clock.clear(), start + 464)
