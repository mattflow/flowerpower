from core.greeting import get_greeting

def test_get_greeting():
    assert get_greeting("world") == "Hello world"
    assert get_greeting("test") == "Hello test"