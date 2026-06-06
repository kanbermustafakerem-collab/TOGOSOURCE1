def greet(name: str) -> str:
    """Greets the user with a standard message."""
    if not name:
        return "Hello World!"
    return f"Hello {name}, welcome to the project!"


def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b