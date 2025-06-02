FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 先装基础依赖（保持你原来的不变）
RUN apt update && apt install -y \
    openjdk-8-jdk \
    ant \
    maven \
    build-essential \
    git \
    wget \
    unzip \
    && apt clean

# 额外安装python3和pip
RUN apt update && apt install -y python3 python3-pip && apt clean

# 安装 python 包
RUN pip3 install --no-cache-dir networkx matplotlib

# 设置 JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /joana

CMD ["/bin/bash"]
