from main import *
import pytest

print(simple_work_calc(10, 2, 2))
print(simple_work_calc(20, 3, 2))
print(simple_work_calc(30, 4, 2))
print(work_calc(10, 2, 2,lambda n: 1))
print(work_calc(20, 1, 2,lambda n: n*n))
print(work_calc(30, 3, 2,lambda n: n))


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n**2)
    
    # Run the comparison
	res = compare_work(work_fn1, work_fn2)

	print("Work Comparison:")
	for n, w1, w2 in res:
		print(f"n={n}: function 1={w1}, function 2={w2}")

	
def test_compare_span():
	
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: n)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n**2)

    # Run the comparison
	res = compare_span(span_fn1, span_fn2)

	print("Span Comparison:")
	for n, s1, s2 in res:
		print(f"n={n}: function 1={s1}, function 2={s2}")
print(test_compare_work())
print(test_compare_span())
