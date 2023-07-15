from tumtumtree.simulation.metrics import FakeFunction
def test_fake_function():
    expected = 1
    output = FakeFunction()
    assert output == expected
