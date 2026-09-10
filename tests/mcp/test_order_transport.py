"""Offline contract checks for the pinned official server; never use broker credentials."""
import json
import unittest
import httpx
from fastmcp import Client, FastMCP
from alpaca_mcp_server.overrides import register_order_tools


class OrderTransportTests(unittest.IsolatedAsyncioTestCase):
    async def test_bracket_and_mleg_payloads(self):
        sent = []
        def handler(request):
            sent.append(json.loads(request.content))
            return httpx.Response(200, json={'id': 'mock', 'status': 'new'})
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler), base_url='https://paper-api.alpaca.markets') as http:
            server = FastMCP('offline-test')
            register_order_tools(server, http)
            async with Client(server) as client:
                await client.call_tool('place_stock_order', dict(symbol='TEST', side='buy', qty='1', type='limit', limit_price='10', client_order_id='test-bracket', order_class='bracket', take_profit_limit_price='12', stop_loss_stop_price='9'))
                legs=[dict(symbol='TEST260918C00010000', ratio_qty='1', side='buy', position_intent='buy_to_open'),dict(symbol='TEST260918C00012000', ratio_qty='1', side='sell', position_intent='sell_to_open')]
                await client.call_tool('place_option_order',dict(qty='1',type='limit',limit_price='0.5',client_order_id='test-mleg',order_class='mleg',legs=legs))
        self.assertEqual(sent[0]['client_order_id'], 'test-bracket')
        self.assertEqual(sent[0]['take_profit'], {'limit_price':'12'})
        self.assertEqual(sent[0]['stop_loss'], {'stop_price':'9'})
        self.assertEqual(sent[1]['legs'], legs)
        self.assertEqual(sent[1]['order_class'], 'mleg')

    async def test_timeout_is_not_retried(self):
        calls=[]
        def handler(request):
            calls.append(request)
            raise httpx.ReadTimeout('mock timeout',request=request)
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler),base_url='https://paper-api.alpaca.markets') as http:
            server=FastMCP('offline-test');register_order_tools(server,http)
            async with Client(server) as client:
                result=await client.call_tool('place_stock_order',dict(symbol='TEST',side='buy',qty='1',type='limit',limit_price='10',client_order_id='test-timeout'))
        self.assertEqual(len(calls),1)
        self.assertIn('timeout',str(result.structured_content).lower())
