import requests
from config import *

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
    else:
        msg = f'''
            <p>请求失败,{r.status_code}</p>
            <p>请手动进行签到</p>
        '''
    pushResult(msg)
    return

def pushResult(msg):
    data = {
        'token': PUSH_TOKEN,
        'title': '签到结果',
        'content': msg,
    }
    r = requests.post(PUSH_URL, json=data)
    print('执行结果:',msg)

    
if __name__ == '__main__':
    checkInFunc()
    # drawFunc()

