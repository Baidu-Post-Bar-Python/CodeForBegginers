if ! pip3 --version ; then
    echo 您没有正确安装pip，请参考https://blog.csdn.net/nmjuzi/article/details/79077164
    exit 1
fi
if ! [ -e requirements.txt ] ; then
    echo 请切换工作目录为 pythonchallenge
    exit 1
fi
echo 开始安装依赖
pip3 install -r requirements.txt --index-url https://mirrors.cloud.tencent.com/pypi/simple --trusted-host https://mirrors.cloud.tencent.com
echo 依赖安装完成
exit 0