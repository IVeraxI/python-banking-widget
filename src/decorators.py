from functools import wraps


def log(filename=None):
    """Декоратор логирует результат вызова функции: успех или ошибку с входными данными."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                return result
            except Exception as exc:
                message = f"{func.__name__} error: {type(exc).__name__}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
        return wrapper
    return decorator
