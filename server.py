from fastapi import FastAPI
from get_data import predict

# 创建 FastAPI 应用
app = FastAPI()


# 定义一个路由
@app.get("/trend/{event_id}/{pred_len}/{metric}")
def trend_pred(event_id: int, pred_len: int, metric: str):
    return predict(event_id, pred_len, metric)


# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
