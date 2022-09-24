import json
import random
import copy
from nlpcda import Simbert
from tqdm import tqdm


def get_data(file='train.json'):
    ori = []
    with open(file=file, mode='r', encoding='utf8') as fp:
        while True:
            line = fp.readline()
            if len(line) == 0:
                break
            else:
                res = json.loads(line)
                ori.append(res)
                print(res['id'])
    return ori

class BaiduAPI:    
    def __init__(self, appid='20220923001352148', secretKey='otTvG7M7b7AArM08GqKt', aug_nums=3):
        from backtrans import BackTranslationBaidu
        self.trans = BackTranslationBaidu(appid=appid, secretKey=secretKey)
    
    def replace(self, sent, create_num):
        tmps = ['jp', 'en', 'kor', 'de', 'fra']
        random.shuffle(tmps)
        ress = []
        for i in range(create_num):
            result = self.trans.translate(sent, src='zh', tmp=tmps[i])
            try:
                print(result.source_text)
                print(result.tran_text)
                print(result.result_text)
                ress.append((result.result_text, 1))
            except Exception as e:
                print(e)
        return ress
    
    def close(self):
        self.trans.closeHTTP()

class SentGenerator:
    def __init__(self, api, aug_nums=3):
        self.aug_nums = aug_nums
        if api=='simbert':
            config = {
                    'model_path': r'D:\NLP\NLP_dataAug\chinese_simbert_L-12_H-768_A-12',
                    'CUDA_VISIBLE_DEVICES': '0',
                    'max_len': 32,
                    'seed': 42
            }
            self.model = Simbert(config=config)
        elif api=='baidu':
            self.model = BaiduAPI()
        elif api=='eda':
            from edazh.eda import EdaZh
            self.model = EdaZh()
        self.api = api

    def run(self, sent):
        return self.model.replace(sent=sent, create_num=self.aug_nums)
    
    def close(self):
        if self.api == 'baidu':
            self.model.close()
    

def aug(file='train.json', api='eda', aug_nums=5, aug_ratio=0.5):
    ori = get_data(file=file)
    random.shuffle(ori)
    new = []
    delimiters = ['。','，','：']
    sent_generator = SentGenerator(api=api, aug_nums=aug_nums)

    # i=0
    for i in tqdm(range(len(ori))):
        sents = [ori[i]['abstract']]
        # print(sents)
        # split abstract into sentences
        for delim in delimiters:
            sents = [x.split(delim) for x in sents]
            sents = [item for sublist in sents for item in sublist]
        sents = [x for x in sents if len(x)>0]
        # add title at head
        sents = [ori[i]['title']] + sents
        # get replace sentence number
        replacesize = max(int(len(sents) * aug_ratio), 1)
        # sample indices
        idxx = random.sample([*range(len(sents))], replacesize)
        # simbert inference to get aug_sentences, shape: [idxx][aug_nums]
        aug_sents = []
        for j in idxx:
            try:
                aug_sents.append(sent_generator.run(sent=sents[j]))
            except Exception as e:
                # pass
                print(e)
        # for each aug_num, replace all indices sentences and add to new list
        for k in range(aug_nums):
            sents_ = copy.copy(sents)
            for aug_s, idx in zip(aug_sents, idxx):
                try:
                    sents_[idx] = aug_s[k][0]
                except Exception as e:
                    # pass
                    print(e)
            new.append({
                'id': ori[i]['id'],
                'title': sents_[0],
                'assignee': ori[i]['assignee'],
                'abstract': '，'.join(sents_[1:]),
                'label_id': ori[i]['label_id'],
            })

        if (i+1)%4==0:
            print("********************************* save {} samples".format((i+1)*aug_nums))
            with open('train_aug.json', mode='w', encoding='utf8') as fp:
                for n in new:
                    fp.writelines(json.dumps(n, ensure_ascii=False)+'\n')
    
    sent_generator.close()
    
    with open('train_aug.json', mode='w', encoding='utf8') as fp:
        for n in new:
            fp.writelines(json.dumps(n, ensure_ascii=False)+'\n')

def sum_data(file='train.json', seg_num=7, repeat_ori=2):
    ori = get_data(file=file)
    dat = ori*repeat_ori
    for i in range(1,seg_num+1):
        fn = file.split('.')[0]+'_aug_p'+str(i)+'.json'
        dat += get_data(file=fn)
    with open('train_aug.json', mode='w', encoding='utf8') as fp:
        for n in dat:
            fp.writelines(json.dumps(n, ensure_ascii=False)+'\n')
    


if __name__=='__main__':
    # aug()
    sum_data()