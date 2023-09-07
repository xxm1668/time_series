# 使用一个基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 拷贝应用程序代码到容器
COPY . /app

# 安装依赖项
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 克隆 GitHub 仓库
RUN git clone https://github.com/ourownstory/neural_prophet neural_prophet

# 切换到项目目录
WORKDIR /app/neural_prophet

# 安装依赖项
RUN pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple
# 设置环境变量
ENV APP_ENV production

# 启动应用程序
CMD ["python3", "server.py"]
