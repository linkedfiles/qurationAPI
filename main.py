from PyKomoran import *
#from docx2pdf import convert
#from tika import parser

from textrank import KeywordSummarizer
from textrank import KeysentenceSummarizer

# WORD -> PDF 변환
#convert("test/sample.docx", "test/sample.pdf")

contents_count = ""

def extract_keyworld(contents):
    result = []

    # PDF 파일에서 텍스트를 추출
    # raw_pdf = parser.from_file('test/sample1.pdf')
    # contents = raw_pdf['content']
    contents_count = contents
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
        cnt = contents_count.count(word)

        result.append({"word": word, "score": rank, "rank": i, "cnt": cnt})
        #print('{} ({:.3})'.format(word, rank))
    return result

#test = '시사회 보고 왔어요 꿈과 사랑에 관한 이야기인데 뭔가 진한 여운이 남는 영화예요 시사회 갔다왔어요 제가 라이언고슬링팬이라서 하는말이아니고 너무 재밌어요 꿈과 현실이 잘 보여지는영화 사랑스런 영화 전 개봉하면 또 볼생각입니당 시사회에서 보고왔는데 여운쩔었다 엠마스톤과 라이언 고슬링의 케미가 도입부의 강렬한음악좋았고 예고편에 나왓던 오디션 노래 감동적이어서 눈물나왔다ㅠ 이영화는 위플래쉬처럼 꼭 영화관에봐야함 색감 노래 배우 환상적인 영화 방금 시사회로 봤는데 인생영화 하나 또 탄생했네 롱테이크 촬영이 예술 영상이 넘나 아름답고 라이언고슬링의 멋진 피아노 연주 엠마스톤과의 춤과 노래 눈과 귀가 호강한다 재미를 기대하면 약간 실망할수도 있지만 충분히 훌륭한 영화 황홀하고 따뜻한 꿈이었어요 imax로 또 보려합니다 좋은 영화 시사해주셔서 감사해요'

#extract_keyworld(test)