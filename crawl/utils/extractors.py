from typing import Any


def chain_get(arg: Any, *keys: Any, **defaults: Any) -> Any:
    """
    chain arg.get() with `keys` with default values in `defaults`

    default for key is `defaults[key]`
    if not found, default is None for last key or empty dict for other keys
    """
    if not keys:
        raise ValueError("no keys specified")

    if not arg:
        return None

    *body, tail = keys
    for key in body:
        try:
            arg = arg[key]
        except (IndexError, KeyError):
            arg = ""
        finally:
            arg = arg or defaults.get(key, {})
    try:
        return arg[tail] if arg[tail] else defaults.get(tail)
    except (IndexError, KeyError):
        return defaults.get(tail)


def to_snake_case(string: str) -> str:
    """
    Convert string to snake_case format.
    """
    snake = "".join(["_" + c.lower() if c.isupper() else c for c in string])
    return snake[1:] if snake.startswith("_") else snake
