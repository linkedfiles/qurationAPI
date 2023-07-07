from PyKomoran import *
#from docx2pdf import convert
#from tika import parser

from textrank import KeywordSummarizer
from textrank import KeysentenceSummarizer

# WORD -> PDF 변환
#convert("test/sample.docx", "test/sample.pdf")

def extract_keyworld(contents):
    result = []

    # PDF 파일에서 텍스트를 추출
    # raw_pdf = parser.from_file('test/sample1.pdf')
    # contents = raw_pdf['content']
    contents = contents.strip()
    contents = contents.replace("\n", "")

    # 사용자사전 주소
    user_dic_path = 'dic.user'

    # 형태소 분석기 객체생성
    komoran = Komoran("EXP")


    # 텍스트 토큰화
    extract_text_arr = [contents]

    # 사용자 사전 적용전
    #print("# 사용자 사전 적용 전" + komoran.get_plain_text(contents))

    # 사용자 사전 등록
    komoran.set_user_dic(user_dic_path)
    komoran.set_fw_dic(user_dic_path)
    #print("# 사용자 사전 적용 후" + komoran.get_plain_text(contents))
    extract_text = [komoran.get_plain_text(contents).strip()]

    #print(extract_text_arr)
    #print(extract_text)


    # textRank (pageRank)
    def komoran_tokenize(sent):
        words = sent.split()
        words = [w for w in words if ('/NNP' in w or '/NNG' in w)]
        return words

    keyword_extractor = KeywordSummarizer(
        tokenize = komoran_tokenize,
        window = 2,
        verbose = False
    )

    # 10문장 추출
    keywords = keyword_extractor.summarize(extract_text, topk=10)
    i = 0
    for word, rank in keywords:
        i += 1
        word = word.replace(" ", "")
        word = word.strip("/NNP""NNG")
        rank = round(rank, 3)
        cnt = extract_text.count(word)

        result.append({"word": word, "score": rank, "rank": i, "cnt": cnt})
        print('{} ({:.3})'.format(word, rank))
    return result
