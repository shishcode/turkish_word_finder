import pytest
from app.utils import parse_position_constraints

def test_parse_position_constraints_turkish_letters():
    result = parse_position_constraints('1Ç 3Ğ', language='tr')
    assert result == {0: {'ç'}, 2: {'ğ'}}

def test_parse_position_constraints_unicode_letters_other_language():
    result = parse_position_constraints('2É', language='fr')
    assert result == {1: {'é'}}
