# Base image
FROM tiangolo/uwsgi-nginx-flask:python3.8

# Environment File
ENV STATIC_URL /static
ENV STATIC_PATH '/app/static'
ENV LISTEN_PORT 5000

# Set web server root as working directory
WORKDIR /app

# Copy all files
COPY . .

# Install required packages
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install wheel
RUN pip install -r requirements.txt
RUN pip cache purge