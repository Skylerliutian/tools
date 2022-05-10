CEHCK_IN_URL = 'https://api.juejin.cn/growth_api/v1/check_in'
AID = 2608
UUID = '7092579818038543913'
SIGNATURE = '_02B4Z6wo00f01vY1NIAAAIDDjvvfhA9VvAb2MTAAAOALSN7tdm41yHVCbsvuARUDRal.rnJ50ZceG08BiNpxhxhi91XpV8UzoBIA0cllZ4ccIgiBhBv218GT3mDe3kJ.dJLZi1iGqI7vXwHgd3'

CHECK_DATA = {
    'aid': AID,
    'uuid': UUID,
    '_signature': SIGNATURE,
}


SESSIONID = 'acd673436e16403f7736acac45a2a2ac'
# SESSIONID = '484457e4be932d18f17cfdc79cd47418'
HEADERS = {
    'cookie': f'sessionid={SESSIONID}'
}

PUSH_TOKEN = 'd79adc96b70e42649eb674dc5ac74142'
PUSH_URL = 'http://www.pushplus.plus/send'

DRAW_URL = 'https://api.juejin.cn/growth_api/v1/lottery/draw'

PRIZE_LIST_URL = 'https://api.juejin.cn/growth_api/v1/lottery_history/global_big'

DIP_URL = 'https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky?'