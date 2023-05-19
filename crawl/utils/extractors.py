from typing import Any


def chain_get(arg: Any, *keys: Any, **defaults: Any) -> Any:
    """
    chain arg.get() with `keys` with default values in `defaults`

    default for key is `defaults[key]`
    if not found, default is None for last key or empty dict for other keys

    >>> arg = {'a': {'b': {'c': 1}}}
    >>> chain_get(arg, 'a', 'b', 'c')
    ... 1
    >>> chain_get(arg, 'a', 'b', 'd')
    ...
    >>> chain_get(arg, 'a', 'b', 'd', d=2)
    ... 2
    >>> chain_get(arg, 'd', 'f', 'e', f={'e': 'hello'})
    ... 'hello'
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
