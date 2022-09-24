from nlpcda import Randomword

test_str = '''这是个实体：58同城；今天是2020年3月8日11:40，天气晴朗，天气很不错，空气很好，不差；这个nlpcad包，用于方便一键数据增强，可有效增强NLP模型的泛化性能、减少波动、抵抗对抗攻击'''

smw = Randomword(create_num=3, change_rate=0.3)
rs1 = smw.replace(test_str)

print('随机实体替换>>>>>>')
for s in rs1:
    print(s)


from nlpcda import Similarword

test_str = '''这是个实体：58同城；今天是2020年3月8日11:40，天气晴朗，天气很不错，空气很好，不差；这个nlpcad包，用于方便一键数据增强，可有效增强NLP模型的泛化性能、减少波动、抵抗对抗攻击'''

smw = Similarword(create_num=3, change_rate=0.3)
rs1 = smw.replace(test_str)

print('随机同义词替换>>>>>>')
for s in rs1:
    print(s)


from nlpcda import Similarword

test_str = '''这是个实体：58同城；今天是2020年3月8日11:40，天气晴朗，天气很不错，空气很好，不差；这个nlpcad包，用于方便一键数据增强，可有效增强NLP模型的泛化性能、减少波动、抵抗对抗攻击'''

smw = Similarword(create_num=3, change_rate=0.3)
rs1 = smw.replace(test_str)

print('随机同义词替换>>>>>>')
for s in rs1:
    print(s)



from nlpcda import Homophone

test_str = '''这是个实体：58同城；今天是2020年3月8日11:40，天气晴朗，天气很不错，空气很好，不差；这个nlpcad包，用于方便一键数据增强，可有效增强NLP模型的泛化性能、减少波动、抵抗对抗攻击'''

smw = Homophone(create_num=3, change_rate=0.3)
rs1 = smw.replace(test_str)

print('随机近义字替换>>>>>>')
for s in rs1:
    print(s)


from nlpcda import RandomDeleteChar

test_str = '''这是个实体：58同城；今天是2020年3月8日11:40，天气晴朗，天气很不错，空气很好，不差；这个nlpcad包，用于方便一键数据增强，可有效增强NLP模型的泛化性能、减少波动、抵抗对抗攻击'''

smw = RandomDeleteChar(create_num=3, change_rate=0.3)
rs1 = smw.replace(test_str)

print('随机字删除>>>>>>')
for s in rs1:
    print(s)


# from nlpcda import Ner

# ner = Ner(ner_dir_name='ner_data',
#         ignore_tag_list=['O'],
#         data_augument_tag_list=['P', 'LOC','ORG'],
#         augument_size=3, seed=0)
# data_sentence_arrs, data_label_arrs = ner.augment(file_name='0.txt')
# # 3条增强后的句子、标签 数据，len(data_sentence_arrs)==3
# # 你可以写文件输出函数，用于写出，作为后续训练等
# print(data_sentence_arrs, data_label_arrs)


from nlpcda import CharPositionExchange

ts = '''这是个实体：58同城；今天是2020年3月8日11:40，天气晴朗，天气很不错，空气很好，不差；这个nlpcad包，用于方便一键数据增强，可有效增强NLP模型的泛化性能、减少波动、抵抗对抗攻击'''
smw = CharPositionExchange(create_num=3, change_rate=0.3,char_gram=3,seed=1)
rs=smw.replace(ts)
for s in rs:
    print(s)


from nlpcda import EquivalentChar

test_str = '''今天是2020年3月8日11:40，天气晴朗，天气很不错。'''

s = EquivalentChar(create_num=3, change_rate=0.3)
# 添加等价字
s.add_equivalent_list(['看', '瞅'])
res=s.replace(test_str)
print('等价字替换>>>>>>')
for s in res:
    print(s)


from nlpcda import Simbert
config = {
        'model_path': r'D:\NLP\NLP_dataAug\chinese_simbert_L-12_H-768_A-12',
        'CUDA_VISIBLE_DEVICES': '0,1',
        'max_len': 32,
        'seed': 1
}
simbert = Simbert(config=config)
sent = '把我的一个亿存银行安全吗'
synonyms = simbert.replace(sent=sent, k=5)
print(synonyms)





