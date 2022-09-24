

def google_backtrans():
    import os
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"

    #!pip install googletrans==4.0.0-rc1 -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.douban.com
    from googletrans import Translator
    translator = Translator(service_urls=['translate.google.cn'])
    # translator = Translator()
    texts=["预估金额与实际金额不一致","我刚刚关锁成功了但是车上的锁没有关上"]
    for text in texts:
        print(text)
        res_1 = translator.translate(text,dest="French")# 先翻译成法语
        res_2 = translator.translate(res_1.text,dest="zh-cn")
        print(res_2.text)
    
        res_3 = translator.translate(text,dest="english")# 先翻译成英语
        res_4 = translator.translate(res_3.text,dest="zh-cn")
        print(res_4.text)
        print("--------------------------------------")


def baidu_backtrans():
    from backtrans import BackTranslation_Baidu
    trans = BackTranslation_Baidu(appid='20220923001352148', secretKey='otTvG7M7b7AArM08GqKt')
    result = trans.translate('我今天真的是非常开心', src='auto', tmp='en')
    print(result.source_text)
    print(result.tran_text)
    print(result.result_text)
    # 'hello'
    trans.closeHTTP()


if __name__=='__main__':
    baidu_backtrans()
    google_backtrans()