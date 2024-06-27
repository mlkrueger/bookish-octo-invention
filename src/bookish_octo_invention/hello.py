
def hello(name:str) -> None:
    if name is None or name == '':
        raise IOError('Be friendly, tell me your name!')
    return f"Hello, {name}!"