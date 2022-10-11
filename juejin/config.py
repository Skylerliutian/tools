CEHCK_IN_URL = 'https://api.juejin.cn/growth_api/v1/check_in'
AID = 2608
UUID = ''
SIGNATURE = ''

CHECK_DATA = {
    'aid': AID,
    'uuid': UUID,
    '_signature': SIGNATURE,
}


SESSIONID = ''
# SESSIONID = ''
HEADERS = {
    'cookie': f'sessionid={SESSIONID}'
}

PUSH_TOKEN = ''
PUSH_URL = 'http://www.pushplus.plus/send'

DRAW_URL = 'https://api.juejin.cn/growth_api/v1/lottery/draw'

PRIZE_LIST_URL = 'https://api.juejin.cn/growth_api/v1/lottery_history/global_big'

DIP_URL = 'https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky?'

NOT_COLLECT_BUG_URL = ' https://api.juejin.cn/user_api/v1/bugfix/not_collect?'

COLLECT_BUG_URL = 'https://api.juejin.cn/user_api/v1/bugfix/collect?'
