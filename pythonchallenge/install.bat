@echo off
where /q pip3 || echo ��û����ȷ��װpip����ο�https://blog.csdn.net/nmjuzi/article/details/79077164 && exit 1
where /q requirements.txt || echo ���л�����Ŀ¼Ϊ pythonchallenge && exit 1
echo ��ʼ��װ����
pip3 install -r requirements.txt --index-url https://mirrors.cloud.tencent.com/pypi/simple --trusted-host https://mirrors.cloud.tencent.com
echo ������װ���