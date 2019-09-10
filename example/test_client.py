from bert_serving.client import BertClient
bc = BertClient(ip='119.3.63.9', port=5555)  # ip address of the GPU machine
print ("result is {}".format(bc.encode(['杭州明天什么天气', '上海明天下雨吗', '这款衣服有货吗'])))
