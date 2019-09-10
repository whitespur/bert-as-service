# 文档
https://bert-as-service.readthedocs.io/en/latest/

https://github.com/whitespur/bert-as-service?organization=whitespur&organization=whitespur#1-download-the-pre-trained-bert-model

中文预训练模型地址

https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip

# 安装

>pip install -U bert-serving-server bert-serving-client

# 使用demo

## 作为server 启动:

>bert-serving-start -model_dir /data/cips/result/chinese_L-12_H-768_A-12/ -num_worker=4

## 客户端请求:
详见example/test_client.py

## 问答系统demo
详见example/example8.py,数据在data.md中

