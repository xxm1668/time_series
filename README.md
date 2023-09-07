# Advertising Predictor

广告投放指标（PV，CV）预测

### 1. 环境安装
> git clone https://github.com/ourownstory/neural_prophet  
> pip install .  
> pip install -r requirements.txt

### 2. 服务端开启
> python3 server.py

### 3. 客户端调用
* 详见client.py

### 4. docker容器启动
> * 1 配置docker容器环境：docker build -t times-series:latest .
> * 2 docker容器部署 docker run -p 80:6080 times-series:latest
> * 3 停止docker服务 docker stop 服务ID/docker rm 服务ID

### 4. 接口详解
>1、url：http://192.168.204.99:8000/trend/event_id/predict_length/cv|pv
> * 注：event_id，即广告的id；predict_length，即预测长度；cv|pv表示cv和pv二选一；  
>如http://192.168.204.99:8000/trend/44/2/pv；44为广告id，2表示可以预测后两天的  
>2、返回的格式  
> * (1)正确返回：{'code': 200, 'data': [{'day': 'yyyy-mm-dd', 'trend': xxx}, {'day': 'yyyy-mm-dd', 'trend': xxx}]}  
> * (2)错误返回：  
>   * ①{'code': 428, 'msg': '数据量不足！'}  
>   * ②{'code': 428, 'msg': '检测时间不连贯！'}  
>   * ③{'code': 500, 'msg': '服务请求异常！'}  