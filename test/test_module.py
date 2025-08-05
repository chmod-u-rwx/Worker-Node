from src.worker_node.module import foo

def test_foo():
    assert foo(1, 2) == 3
    assert foo(2, 2) == 4

