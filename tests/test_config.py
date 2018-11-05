from airswap_exercise import config

def test_base_url():
	assert config.BASE_URL == "https://api.binance.com"

def test_base_symbol():
	assert config.BASE_SYMBOL == "ETHBTC"

