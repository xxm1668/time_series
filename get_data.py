import requests
import json
import pandas as pd
from trend_server import trend_predict

metric_dic = {'cv': '点击渠道链接按钮', 'pv': '进入渠道链接页面'}


def get_data(event_id, metric):
    # 定义请求的 URL
    url = 'https://cdp.365sydc.com/v2/stat/101993?'

    headers = {
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Basic aW5uZXI6ZDA4ZGQ3OGYzMjM5NDUwYjgzNDM1MzIwMzJhZGQ4NTU='  # 如果需要授权，请替换为有效的访问令牌
    }
    # 循环遍历日期范围

    # 定义请求参数
    params = {
        'metrics': 'users',
        'dimensions': '$day,event.渠道链接ID',
        'conditions': {
            "$day": ["between", '2023-08-01', '2023-08-30'],
            "$event_name": ["==", metric_dic[metric]],
            "event.渠道链接ID": ["==", str(event_id)]
        }
    }
    url = url + 'metrics=' + params['metrics'] + '&dimensions=' + params['dimensions'] + '&conditions=' + json.dumps(
        params['conditions'], ensure_ascii=False)
    print(url)
    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    # 检查响应状态码
    result = []
    if response.status_code == 200:
        # 处理响应数据，可以使用 response.json() 来解析 JSON 数据
        result2 = response.json()
        data = result2['data']['results']
        if len(data) > 0:
            result = result2['data']['results']
    else:
        print(f"Request failed with status code {response.status_code}")
    pd_data = {'ds': [], 'y': []}
    if len(result) != 0:
        for res in result:
            users = res['users']
            date = res['day']
            date = str(date)[:4] + '-' + str(date)[4:6] + '-' + str(date)[6:]
            pd_data['ds'].append(date)
            pd_data['y'].append(users)
            print(date)
    df = pd.DataFrame(pd_data)
    return df


def predict(event_id, pred_len, metric):
    try:
        result = get_data(event_id, metric)
        if len(result) < 10:
            return {'code': 428, 'msg': '数据量不足！'}
        result = result.loc[result.index[::-1]]
        result = result.tail(10)
        try:
            trend = trend_predict(result, pred_len)
        except:
            return {'code': 428, 'msg': '检测时间不连贯！'}
    except:
        return {'code': 500, 'msg': '服务请求异常！'}
    return {'code': 200, 'data': trend}


if __name__ == '__main__':
    result = predict(40)
    print(result)
