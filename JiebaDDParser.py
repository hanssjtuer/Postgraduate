import jieba
from ddparser import DDParser

jieba.initialize()

stop_words = ["，", "的"]
word_replace={"为": "是", "建筑信息模型":"BIM"}

test_contents = [
    "清华大学是985高校"
    ]

jieba.add_word('建筑信息模型', freq=None, tag='n')
jieba.add_word('全生命周期', freq=None, tag='n')
jieba.add_word('建筑环境产业', freq=None, tag='n')
jieba.add_word('985', freq=None, tag='n')

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        for k in range(1, 10, 1):
            jieba.add_word(str(i)+"."+str(j)+"."+str(k), freq=None, tag='n')

for content in test_contents:
    result = jieba.cut(content,cut_all=False,HMM=True)
    result = list(result)
    temp = []
    for i in result:
        if i in word_replace.keys():
            i = word_replace[i]
        if i.strip() not in stop_words:
            temp.append(i)
    print(temp)
    
    ddp = DDParser(prob=True)
    result=ddp.parse_seg([temp])
    print(result)
