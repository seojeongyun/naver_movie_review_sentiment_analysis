 1. 자연어처리 개요

   - 텍스트 전처리: https://wikidocs.net/21694  (토큰화, 정제/정규화, 어간추출, 불용여, 정규표현식, 정수인코딩, 패딩, 원-핫인코딩, 데이터분리, 한국어전처리) 

   - 언어모델: https://wikidocs.net/21695 (언어모델, 통계적언어모델, n-gram 언어모델, etc) 



   - 카운트기반 단어표현: https://wikidocs.net/24557 (Bag-of-word, 문서단어행렬, TF-IDF)



 2. 워드임베딩 

   - 워드임베딩: https://wikidocs.net/33520

   - 워드투벡터(Word2Vec): https://wikidocs.net/22660



 3. RNN 개념: https://wikidocs.net/48558



 4. 자연어처리 Task

   - 이름분류 : https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html

   - 자동번역 (using Seq-to-Seq): https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html



   - 네이버영화리뷰 감성분류 

     + https://wikidocs.net/44249

     + https://wikidocs.net/94600


Session II: 

1. 크롤링 사례
  
  - 논문수집: https://wikidocs.net/211405
  
  - BTS가수 크롤링: https://wikidocs.net/214309


2. 데이터 전처리
  
  - 정규화, 토큰화, 어근화, 어근추출: https://team-platform.tistory.com/38
  
  - konlpy 형태소 분석기: https://konlpy.org/en/latest/
  
  - 키위형태소 분석기: https://github.com/bab2min/kiwipiepy


3. 텍스트 빈도분석과 워드 클라우드 
   https://wikidocs.net/214313

# Word2Vec과 같이 자연어 처리를 위해 위 예제를 공부함.

# 한국어 전처리를 위해 사용되는 konlpy의 okt라는 형태소 분석기를 사용하는데 이 형태소 분석기를 사용하기 위해 버전 맞추느라 엄청 고생했던 기억이 있음.

# 위키독스에서는 tensorflow 문법을 사용하는데 이를 Torch 문법으로 바꾸어 적용하였음.
