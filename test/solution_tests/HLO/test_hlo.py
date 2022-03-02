from solutions.HLO import hello_solution

def test_hello_world():
    assert hello_solution.hello() == "Hello, World!"

def test_hello_requires_no_kwarg():
    assert hello_solution.hello() == 'Hello, World!'

def test_hello_returns_friend_name_if_supplied():
    assert hello_solution.hello() == 'Hello, World!'
    assert hello_solution.hello('John') == 'Hello, John!'