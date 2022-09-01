import pytest
from matematica.Calculadora import *

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)

@pytest.mark.op_simples
def test_subtracao_dois_valores_positivos():
    v1 = 3.0
    v2 = 50.0
    assert -47 == sub(v1, v2)

@pytest.mark.op_simples
def test_multiplicacao_dois_valores_positivos():
    v1 = 3.0
    v2 = 5.0
    assert 15 == multiplicacao(v1, v2)

@pytest.mark.op_simples
def test_divisao_dois_valores_positivos():
    v1 = 20
    v2 = 10
    assert 2 == divisao(v1,v2)

@pytest.mark.op_simples
@pytest.mark.exercicio_1
def divisao_por_zero():
    v1 = 20
    v2 = 0
    assert np.inf == divisao(v1, v2)


@pytest.mark.op_complexas
def test_media_dois_valores_positivos():
    lista = [300, 100, 200]
    assert 200 == media_lista_valores(lista)

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_media_dois_valores_positivos_com_str():
    lista = [10, 30, 's']
    assert  20== media_lista_valores(lista)

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_media_lista_vazia():
    lista = []
    assert 0 == media_lista_valores(lista)
