from binance import Client
from logger import setup_logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = setup_logger()
        base_url = 'https://testnet.binancefuture.com' if testnet else 'https://fapi.binance.com'
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = base_url

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            self.logger.info(f"Order Request: symbol={symbol}, side={side}, type={order_type}, qty={quantity}, price={price}")
            params = {'symbol': symbol, 'side': side, 'type': order_type, 'quantity': quantity}
            if order_type == 'LIMIT':
                params.update({'price': price, 'timeInForce': 'GTC'})
            order = self.client.futures_create_order(**params)
            self.logger.info(f"Order Success: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Order Error: {str(e)}")
            return {'error': str(e)}
