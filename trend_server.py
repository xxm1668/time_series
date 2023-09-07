from neuralprophet import NeuralProphet
from datetime import datetime

m = NeuralProphet(batch_size=8, epochs=2200, learning_rate=1)


def trend_predict(df, pred_len):
    df_train, df_val = m.split_df(df, valid_p=0.2, local_split=True)
    train_metrics = m.fit(df_train)
    print(train_metrics)
    future = m.make_future_dataframe(df, periods=pred_len, n_historic_predictions=True)
    forecast = m.predict(future)
    trend = forecast['yhat1'].values.tolist()[-2:]
    date = forecast['ds'].values.tolist()[-2:]
    result = []

    for i in range(len(date)):
        tmp = {}
        # 将纳秒转换为秒
        seconds_timestamp = date[i] / 1e9
        # 将秒时间戳转换为日期时间对象
        datetime_obj = datetime.fromtimestamp(seconds_timestamp)
        # 格式化日期为字符串
        formatted_date = datetime_obj.strftime('%Y-%m-%d')
        tmp['day'] = formatted_date
        tmp['trend'] = trend[i]
        result.append(tmp)
    return result
