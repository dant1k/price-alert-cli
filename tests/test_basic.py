from price_alert.__main__ import normalize_symbol

def test_normalize_symbol_map():
    assert normalize_symbol("btc") == "bitcoin"
    assert normalize_symbol("ETH") == "ethereum"
    assert normalize_symbol("SOL") == "solana"
