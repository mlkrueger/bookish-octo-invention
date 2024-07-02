
def hello(name:str) -> str:
    if name is None or name == '':
        raise IOError('Be friendly, tell me your name!')
    return f"Hello, {name}!"