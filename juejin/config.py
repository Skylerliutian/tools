CEHCK_IN_URL = 'https://api.juejin.cn/growth_api/v1/check_in'
AID = 2608
UUID = '7080762933118977575'
SIGNATURE = '_02B4Z6wo00f01LFof1wAAIDByaaUWmDjdJixbHvAAE7UuKrnC4Np3gjTiNwhuSmjesjWveCw6zBFSIVFjTMYLD6sSMymm0kmXbTyhyqoV1EHw1ySQMQQdv7tvJqpA.Wy0RuCgxrBrlH4GFMef9'

CHECK_DATA = {
    'aid': AID,
    'uuid': UUID,
    '_signature': SIGNATURE,
}


SESSIONID = '938812887b7e0d4477e4e72ed8c98dc1'
# SESSIONID = '484457e4be932d18f17cfdc79cd47418'
HEADERS = {
    'cookie': f'sessionid={SESSIONID}'
}

PUSH_TOKEN = 'd79adc96b70e42649eb674dc5ac74142'
PUSH_URL = 'http://www.pushplus.plus/send'

DRAW_URL = 'https://api.juejin.cn/growth_api/v1/lottery/draw'

PRIZE_LIST_URL = 'https://api.juejin.cn/growth_api/v1/lottery_history/global_big'

DIP_URL = 'https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky?'
