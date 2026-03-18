import pytest
from notebooks.proccessamento_vendas import (
    calcular_valor_total,
    aplicar_desconto_fidelidade,
    extrair_status_perdido
)

def test_calcular_valor_total():
    assert calcular_valor_total(10, 5.0) == 50.0
    assert calcular_valor_total(3, 19.99) == 59.97

def test_calcular_valor_total_negativo():
    with pytest.raises(ValueError):
        calcular_valor_total(-1, 5.0)
    with pytest.raises(ValueError):
        calcular_valor_total(10, -5.0)

def test_aplicar_desconto_fidelidade():
    assert aplicar_desconto_fidelidade(100.0, True) == 90.0
    assert aplicar_desconto_fidelidade(100.0, False) == 100.0

def test_extrair_status_perdido():
    assert extrair_status_perdido(1) == "Pendente"
    assert extrair_status_perdido(2) == "Pago"
    assert extrair_status_perdido(3) == "Enviado"
    assert extrair_status_perdido(4) == "Entregue"
    assert extrair_status_perdido(5) == "Desconhecido"