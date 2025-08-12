from lib.counter import *

def test_counter_add():
    counter = Counter()
    counter.add(7)
    assert counter.count == 7

def test_counter_report():
    counter = Counter()
    counter.add(4)
    assert counter.report() == "Counted to 4 so far."

def test_counter_report_multiple_numbers():
    counter = Counter()
    counter.add(4)
    counter.add(1)
    assert counter.report() == "Counted to 5 so far."

# irl I don't think it would be happy about it doing this?
def test_counter_report_negative_number():
    counter = Counter()
    counter.add(4)
    counter.add(-4)
    assert counter.report() == "Counted to 0 so far."