import os
import re
import requests

JUEJIN_COOKIE=''

def init_env():
    env = os.environ.get('JUEJIN_COOKIE') if JUEJIN_COOKIE else 'aid=2608;uuid=7080762933118977575;signature=_02B4Z6wo00f01LFof1wAAIDByaaUWmDjdJixbHvAAE7UuKrnC4Np3gjTiNwhuSmjesjWveCw6zBFSIVFjTMYLD6sSMymm0kmXbTyhyqoV1EHw1ySQMQQdv7tvJqpA.Wy0RuCgxrBrlH4GFMef9;session_id=938812887b7e0d4477e4e72ed8c98dc1;'
    # print(env)
    aid = re.findall(r'aid=(.+?);', env)[0]
    uuid = re.findall(r'uuid=(.+?);', env)[0]
    signature = re.findall(r'signature=(.+?);', env)[0]
    sessionid = re.findall(r'session_id=(.+?);', env)[0]
    return aid, uuid, signature, sessionid

def getPrizeHistoryList():
    body = {
        'page_no': 1,
        'page_size': 5
    }
    params = {
        'aid': AID,
        'uuid': UUID
    }
    idList = []
    try:
        r = requests.post(PRIZE_LIST_URL, json=body, params=params, headers=HEADERS)
        response = r.json()
        lotteries = response['data']['lotteries']
        for l in lotteries:
            idList.append(l['history_id'])
    except Exception as e:
        print(f'error occur in DipLucky {e}')
    return idList

def dipLucky(his_id):
    body = {
        'lottery_history_id': his_id
    }
    params = {
        'aid': AID,
        'uuid': UUID
    }
    r = requests.post(DIP_URL, json=body, params=params, headers=HEADERS)
    response = r.json()
    msg = ''
    if response['err_no'] == 0:
        data = response['data']
        dip_value = data['dip_value']
        total_value = data['total_value']
        msg += f'沾喜气成功，沾到<b>{dip_value}</b>幸运值，共<b>{total_value}</b>幸运值'
    return msg

def drawFunc():
    r = requests.post(DRAW_URL, json=CHECK_DATA, headers=HEADERS)
    response = r.json()
    retval = {}
    if r.status_code == 200:
        data = response['data']
        if response['err_no'] != 0:
            retval['code'] = -1
            retval['msg'] = f'抽奖失败'
        else:
            retval['code'] = 0
            retval['msg'] = f'恭喜您抽中了{data["lottery_name"]}, 获得{data["draw_lucky_value"]}幸运值, 共{data["total_lucky_value"]}幸运值'
    else:
        retval['code'] = -1
        retval['msg'] = '免费抽奖失败'
    return retval

def checkInFunc():
    r = requests.post(CEHCK_IN_URL, json=CHECK_DATA, headers=HEADERS)
    msg = ''
    if r.status_code == 200:
        response = r.json()
        if response['err_no'] != 0:
            msg = f'''签到失败, {response['err_msg']}, 请手动签到或更换session!'''
        else:
            data = response['data']
            msg = f'''签到成功, 今日获得<b>{data['incr_point']}</b>矿石, 总<b>{data['sum_point']}</b>矿石'''
            drawReturn = drawFunc()
            msg += f'''<p>{drawReturn['msg']}</p>'''
            # 签到成功，沾喜气
            # 1. 先获取列表
            historyList = getPrizeHistoryList()
            # 2. 沾喜气
            if len(historyList) > 0:
                dip_msg = dipLucky(historyList[0])
                msg += f'<p>{dip_msg}</p>'
    else:
        msg = f'''
            <p>请求失败,{r.status_code}</p>
            <p>请手动进行签到</p>
        '''
    pushResult('签到结果', msg)
    return

def getBugList():
    params = {
        'aid': AID,
        'uuid': UUID
    }
    r = requests.post(NOT_COLLECT_BUG_URL, json={}, params=params, headers=HEADERS)
    response = r.json()
    bugList = response['data']
    return bugList

def collectBug():
    params = {
        'aid': AID,
        'uuid': UUID
    }
    bugs = getBugList()
    total = 0
    for bug in bugs:
        body = {
            'bug_time': bug['bug_time'],
            'bug_type': bug['bug_type']
        }
        r = requests.post(COLLECT_BUG_URL, json=body, params=params, headers=HEADERS)
        response = r.json()
        if response['err_no'] == 0:
            total += 1
    msg = f'''
        Good Night, skyler, 今日共收取 {total}个bug, 共{len(bugs)}个bug, {len(bugs) - total}个bug收取失败, 可登录掘金查看详情
    '''
    pushResult('bugFix', msg)
    return

if __name__ == '__main__':
    CEHCK_IN_URL = 'https://api.juejin.cn/growth_api/v1/check_in'
    DRAW_URL = 'https://api.juejin.cn/growth_api/v1/lottery/draw'
    PRIZE_LIST_URL = 'https://api.juejin.cn/growth_api/v1/lottery_history/global_big'
    DIP_URL = 'https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky?'
    NOT_COLLECT_BUG_URL = ' https://api.juejin.cn/user_api/v1/bugfix/not_collect?'
    COLLECT_BUG_URL = 'https://api.juejin.cn/user_api/v1/bugfix/collect?'
    
    try:
        AID, UUID, SIGNATURE, SESSIONID = init_env()
        HEADERS = {
            'cookie': f'sessionid={SESSIONID}'
        } 
        CHECK_DATA = {
            'aid': AID,
            'uuid': UUID,
            '_signature': SIGNATURE,
        }
    except:
        print(f'JUEJIN_COOKIE 不存在，请先添加 JUEJIN_COOKIE\nexport JUEJIN_COOKIE="aid=xx;uuid=xx;signature=xx;session_id=xxx;"')
        exit(0)