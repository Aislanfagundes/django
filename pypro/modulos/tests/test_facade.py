import pytest

from pypro.modulos.models import Modulo
from model_bakery import baker
from pypro.modulos import facade


@pytest.fixture
def modulos(db):
    return [baker.make(Modulo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()
