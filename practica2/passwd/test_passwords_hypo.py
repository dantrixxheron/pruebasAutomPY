import pytest
import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity
from passwords import validarPwd

@settings(max_examples=100, verbosity=Verbosity.verbose)
@given(st.text(min_size=0, max_size=30))
def test_validar_pwd(pwd):
    # Test for valid passwords
    if len(pwd) >= 8 and len(pwd) <= 16:
        if any(char.isdigit() for char in pwd) and \
           any(char.isupper() for char in pwd) and \
           any(char in "@#$%&*" for char in pwd):
            assert validarPwd(pwd) == True
        else:
            assert validarPwd(pwd) == False
    else:
        assert validarPwd(pwd) == False