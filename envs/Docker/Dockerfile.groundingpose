ARG PYTORCH="2.4.0"
ARG CUDA="12.1"
ARG CUDNN="9"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel
# FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0 7.5 8.0 8.6+PTX" \
    TORCH_NVCC_FLAGS="-Xfatbin -compress-all" \
    CMAKE_PREFIX_PATH="$(dirname $(which conda))/../" \
    FORCE_CUDA="1"

# Install the required packages
RUN apt-get update \
&& apt-get install -y ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 wget vim ncurses-bin \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Install MMDetection
RUN conda clean --all \
    && conda create -y -n groundingpose python=3.10 \
    && git clone --recursive https://github.com/yang-yang-o-o/GroundingPose.git /GroundingPose \
    && cd /GroundingPose
    
RUN git clone https://github.com/yang-yang-o-o/tools.git ~/tools \
    && conda run -n groundingpose pip install -r ~/tools/envs/Docker/requirements.txt \
    && bash ~/tools/envs/zsh/install.sh \
    && mv ~/tools/envs/zsh/.zshrc ~/ \
    && source ~/.zshrc
    
# 设置默认环境为 groundingpose
ENV PATH=/opt/conda/envs/groundingpose/bin:$PATH
ENV CONDA_DEFAULT_ENV=groundingpose

# 默认进入 GroundingPose 目录
WORKDIR /GroundingPose

# 默认命令（可以改为你需要运行的脚本）
# CMD ["python"]

# docker build -t test .
# docker run --gpus all -it --name my-container test