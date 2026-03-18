def calcular_valor_total(quantidade: int, preco_unitario: float) -> float:
    """
    Calcula o valor total de uma venda.

    Args:
        quantidade (int): A quantidade de itens vendidos.
        preco_unitario (float): O preço unitário de cada item.

    Returns:
        float: O valor total da venda.
    """
    if quantidade < 0 or preco_unitario < 0:
        raise ValueError("Quantidade e preço unitário devem ser valores positivos.")
    return round(quantidade * preco_unitario,2)

def aplicar_desconto_fidelidade(valor_total: float, e_cliente_vip: bool) -> float:
    """
    Aplica 10% de desconto se o cliente for VIP.
    """
    if e_cliente_vip:
        return round(valor_total * 0.90,2)
    return valor_total

def extrair_status_perdido(codigo_status: int) -> str:
    """
    Traduz código de status do banco de dados.
    """
    stauts_map = {
        1: "Pendente",
        2: "Pago",
        3: "Enviado",
        4: "Entregue"
    }
    return stauts_map.get(codigo_status, "Desconhecido")