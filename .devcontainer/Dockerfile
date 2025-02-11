# Python 3.12 ベースのイメージを使用
FROM python:3.13 as backend

WORKDIR /workspace

# uv をインストール
RUN pip install uv && uv python pin 3.13

# Final image
FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm

# Copy 'uv' executable from builder
COPY --from=backend /usr/local/bin/uv /usr/local/bin/uv

# 必要なパッケージをインストール
RUN apt update && apt install -y zsh curl git
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q -O /usr/local/bin/hadolint https://github.com/hadolint/hadolint/releases/download/v2.4.1/hadolint-Linux-x86_64 \
    && chmod 755 /usr/local/bin/hadolint

RUN usermod --shell /bin/zsh vscode

# Switch to 'vscode' user
USER vscode

# oh-my-zsh をインストール
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true

# Voltaをインストール
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl https://get.volta.sh | bash

# Volta が PATH に含まれることを保証

ENV VOLTA_HOME=/vscode/.volta
ENV PATH=$VOLTA_HOME/bin:$PATH

