import pytest
from bookish_octo_invention import hello
import asyncio

@pytest.mark.parametrize(
    'name', ['Matthew','Octo-Cat','World','', None]
)
def test_hello(name:str) -> None:
    if name not in [None, '']:
        greeting = hello.hello(name)
        assert greeting == f"Hello, {name}!"
    else:
        with pytest.raises(IOError):
            greeting = hello.hello(name)