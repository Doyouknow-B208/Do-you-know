<template>
  <div class="APIscene" style="overflow:auto;">
    <div style="display: flex; justify-content: space-around; border-width: 2px; margin-bottom:3px;">
      <div v-if="name=='손흥민'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >대회 기록</h1>
        <h3 class="title">토트넘 훗스퍼 FC (2015 ~) : UEFA 챔피언스 리그 준우승: 2018-19</h3>
        <h3 class="title">대한민국 축구 국가대표팀 : AFC 아시안컵 준우승: 2015</h3>
        <h3 class="title">대한민국 U-23 축구 국가대표팀 : UEFA 챔피언스 리그 준우승</h3>
        <h3 class="title">아시안 게임 금메달: 2018</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >개인 수상</h1>
        <h3 class="title">프리미어 리그 득점왕: 2021-22</h3>
        <h3 class="title">프리미어 리그 이달의 선수: 2016년 09월, 2017년 04월, 2020년 10월</h3>
        <h3 class="title">프리미어 리그 올해의 골: 2019-20</h3>
        <h3 class="title">프리미어 리그 이달의 골: 2018년 11월, 2019년 12월</h3>
        <h3 class="title">PFA 올해의 팀: 2020-21</h3>
        <h3 class="title">PFA 팬 선정 이달의 선수: 2018년 01월</h3>
        <h3 class="title">런던 풋볼 어워즈 올해의 선수: 2018-19</h3>
        <h3 class="title">런던 풋볼 어워즈 올해의 골: 2019-20</h3>
        <h3 class="title">토트넘 홋스퍼 원 홋스퍼 올해의 선수: 2018-19, 2019-20, 2021-22</h3>
        <h3 class="title">토트넘 홋스퍼 원 홋스퍼 주니어 올해의 선수: 2018-19, 2019-20, 2021-22</h3>
        <h3 class="title">토트넘 홋스퍼 오피셜 서포터즈 클럽 올해의 선수: 2018-19, 2019-20, 2021-22</h3>
        <h3 class="title">토트넘 홋스퍼 오피셜 서포터즈 클럽 올해의 골: 2018-19, 2019-20</h3>
        <h3 class="title">FA컵 득점왕: 2016-17</h3>
        <h3 class="title">발롱도르 후보: 2019 (22위), 2022</h3>
        <h3 class="title">FIFA FIFPro 월드 XI 후보: 2019 (FW 14위), 2020 (FW 15위)</h3>
        <h3 class="title">FIFA 푸스카스상: 2020[81]</h3>
        <h3 class="title">AFC 아시아 베스트 XI: 2012</h3>
        <h3 class="title">AFC 올해의 아시아 국제 선수: 2015, 2017, 2019, 2020</h3>
        <h3 class="title">IFFHS 올해의 아시아 축구 선수: 2020, 2021</h3>
        <h3 class="title">IFFHS 올해의 AFC팀: 2020, 2021</h3>
        <h3 class="title">IFFHS 10년의 AFC 최고 선수 (2011–2020)</h3>
        <h3 class="title">IFFHS 10년의 AFC팀 (2011–2020)</h3>
        <h3 class="title">HS 올타임 아시아 드림팀: 2021</h3>
        <h3 class="title">아시아 베스트 풋볼러: 2014, 2015, 2017, 2018, 2019, 2020, 2021</h3>
        <h3 class="title">KFA 올해의 선수: 2013, 2014, 2017, 2019, 2020, 2021</h3>
        <h3 class="title">KFA 올해의 골: 2015, 2016, 2018, 2021</h3>
      </div>
       <div v-else-if="name=='김연아'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2006년</h1>
        <h3 class="title">경기도 교육청 제1호 글로벌 인재상</h3>
        <h3 class="title">대한민국 국회대상 스포츠 부문상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2009년</h1>
        <h3 class="title">Mnet 20's Choice 'Hot 스포츠스타상</h3>
        <h3 class="title">제6회 TVCF 어워즈 2008 모델부문 최우수상 '올해의 모델상'</h3>
        <h3 class="title">제55회 대한체육회 체육대상 우수상</h3>
        <h3 class="title">포브스코리아 선정 대한민국 '파워 셀리브리티 40인' 1위 선정</h3>
        <h3 class="title">유니버설 뮤직 '파이브 플래티넘 디스크상'</h3>
        <h3 class="title">제1회 대한민국 브랜드 이미지 어워드 문화예술부문</h3>
        <h3 class="title">제40회 경기도체육상 스포츠 스타상</h3>
        <h3 class="title">제4회 앙드레김 베스트 스타 어워드 스타상</h3>
        <h3 class="title">대한민국광고대상 모델상</h3>
        <h3 class="title">제47회 대한민국체육상 경기부문 최우수상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2010년</h1>
        <h3 class="title">미국 '올해의 스포츠 우먼상 수상'</h3>
        <h3 class="title">미국 시사주간지 타임 선정 '세계에서 가장 영향력 있는 100인' - 영웅부문 2위</h3>
        <h3 class="title">미주동포후원재단 선정 '자랑스런 한국인상'</h3>
        <h3 class="title">미국 '로스앤젤레스 명예시민'으로 위촉</h3>
        <h3 class="title">스포츠 일러스트레이티드 가장 인상적인 스포츠 선수 10인</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2011년</h1>
        <h3 class="title">2011 외신홍보상 스포츠 부문수상</h3>
        <h3 class="title">문화체육관광부 • 한국관광공사 선정 제2회 한국관광의 별 특별 공로자</h3>
        <h3 class="title">2011 SBS 연예대상 특별상 수상</h3>
        <h3 class="title">제12회 대한민국 국회대상 올해의 공로상</h3>
        <h3 class="title">제9회 올해의 브랜드 대상 특별상 스포츠인부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2012년</h1>
        <h3 class="title">국민훈장 모란장</h3>
        <h3 class="title">2012 자랑스런 대한민국 시민 대상 - 스포츠발전 공로대상(국위선양공로부문)</h3>
        <h3 class="title">제17회 코카콜라 체육대상 공로상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2013년</h1>
        <h3 class="title">미국스포츠아카데미 올해의 여자선수상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2014년</h1>
        <h3 class="title">제19회 코카콜라 체육대상 최우수선수상 공동수상</h3>
        <h3 class="title">자랑스러운 고대인상 수상</h3>
        <h3 class="title">제8회 포니정 혁신상 수상</h3>
        <h3 class="title">미 포브스 선정, 아시아 자선가</h3>
        <h3 class="title">고대체육인상 수상</h3>
        <h3 class="title">대한민국 광고모델상</h3>
        <h3 class="title">스포츠마케팅대상 모델상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2015년</h1>
        <h3 class="title">제 1회 국가브랜드 대상 스포츠부문 대상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016년</h1>
        <h3 class="title">대한체육회 '스포츠영웅' 선정 및 명예의전당 헌액</h3>
        <h3 class="title">한국에서 가장 영향력이 있는 스포츠 스타 1위</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2018년</h1>
        <h3 class="title">제23회 국가올림픽연합회 어워즈 아웃스탠딩 퍼포먼스상</h3>
        <h3 class="title">시사저널 선정 차세대 리더 문화/예술/스포츠 부문 2위, 종합 공동 9위</h3>
      </div>
      <div v-else-if="name=='김연경'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >대회수상</h1>
        <h3 class="title">2005-06 KT&G V-리그 신인선수상</h3>
        <h3 class="title">2005-06 KT&G V-리그 정규리그 + 챔피언결정전 MVP</h3>
        <h3 class="title">2006-07 HILLSTATE V-리그 정규리그 + 챔피언결정전 MVP</h3>
        <h3 class="title">2007-08 KOVO V-리그 정규리그 MVP</h3>
        <h3 class="title">2008-09 NH농협 V-리그 챔피언결정전 MVP</h3>
        <h3 class="title">2009 흥국생명배 한·일 V리그 TOP매치 MVP</h3>
        <h3 class="title">2009 동아스포츠대상 여자프로배구부문 대상</h3>
        <h3 class="title">2009-10 V.프리미어리그 감투상(敢闘賞)</h3>
        <h3 class="title">2010 수원 · IBK 기업은행 KOVO컵 MVP</h3>
        <h3 class="title">2010-11 V.프리미어리그 MVP</h3>
        <h3 class="title">2011-12 CEV 챔피언스 리그 MVP</h3>
        <h3 class="title">2012 런던 올림픽 MVP</h3>
        <h3 class="title">2012 MBN 여성스포츠대상 5월 MVP</h3>
        <h3 class="title">2014 V-리그 10주년 올스타 베스트7 공격형 레프트</h3>
        <h3 class="title">2014-15 터키 리그 MVP</h3>
        <h3 class="title">2015 터키 컵 MVP</h3>
        <h3 class="title">2015-16 CEV 챔피언스 리그 베스트 아웃사이드 스파이커</h3>
        <h3 class="title">2015-16 터키 리그 베스트 아웃사이드 스파이커</h3>
        <h3 class="title">2017 한국여성단체협의회 올해의 여성상</h3>
        <h3 class="title">2017-18 중국 슈퍼 리그 최고 외인상</h3>
        <h3 class="title">2019 FIVB 월드클럽챔피언십 베스트 아웃사이드 스파이커</h3>
        <h3 class="title">2020년 제58회 대한민국 체육상 경기상</h3>
        <h3 class="title">2020년 K-스포노믹스 포럼 시상식 대한체육회장상</h3>
        <h3 class="title">2020년 MBN 여성스포츠대상</h3>
        <h3 class="title">2020-21 KOVO V-리그 정규리그 MVP</h3>
        <h3 class="title">2021년 국가브랜드 스포츠 부문 대상</h3>
        <h3 class="title">2021년 국제배구연맹 올해의 선수 1위</h3>
      </div>
      <div v-else-if="name=='이상한 변호사 우영우'" style="width:60%; border-color:black; border-style: solid;">
        <h3 class="title" style="color:yellow; margin:1rem;">본 작품은 종영한지 얼마 지나지 않아 평가 및 흥행 요소로 대체합니다.</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >평가 및 흥행 요소</h1>
        <h3 class="title">배우들의 준수한 연기력</h3>
        <h3 class="title">빠른 전개 속도</h3>
        <h3 class="title">준수한 각본</h3>
        <h3 class="title">일부 자폐 당사자들의 호평</h3>
        <h3 class="title">입체적인 등장인물</h3>
        <h3 class="title">주제의식과 연출 방식의 일치</h3>
        <h3 class="title">단정짓지 않는 '열려 있음'을 표방함</h3>
      </div>
      <div v-else-if="name=='태양의 후예'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2017 방송통신위원회 방송대상</h1>
        <h3 class="title">대상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >드라마 피버 어워즈</h1>
        <h3 class="title">여우주연상</h3>
        <h3 class="title">베스트 악역</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >	제29회 한국PD대상</h1>
        <h3 class="title">작품상-TV드라마</h3>
        <h3 class="title">출연자상 (탤런트)</h3>
        <h3 class="title">제작부문상 (TV작가)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >Soompi Awards</h1>
        <h3 class="title">여우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >서울가요대상, 골든디스크</h1>
        <h3 class="title">OST 상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >KoreanUpdates Awards</h1>
        <h3 class="title">Best Actress</h3>
        <h3 class="title">Couple of the year</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016 KBS 연기대상</h1>
        <h3 class="title">대상</h3>
        <h3 class="title">우수상</h3>
        <h3 class="title">베스트 커플</h3>
        <h3 class="title">신인상</h3>
        <h3 class="title">작가상</h3>
        <h3 class="title">아시아 최고 커플상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제29회 그리메상</h1>
        <h3 class="title">대상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016 육군홍보대상</h1>
        <h3 class="title">육군홍보대상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제21회 아시안 텔레비전 어워즈</h1>
        <h3 class="title">최우수 드라마상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제6회 대한민국한류대상</h1>
        <h3 class="title">대중문화대상 - 드라마부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제8회 멜론 뮤직 어워드</h1>
        <h3 class="title">뮤직스타일상 - OST부분</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제1회 아시아 아티스트 어워즈</h1>
        <h3 class="title">베스트 셀러브리티 남자 부분</h3>
        <h3 class="title">베스트 셀러브리티 여자 부분</h3>
        <h3 class="title">베스트 OST 상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제7회 대한민국 대중문화예술상</h1>
        <h3 class="title">대통령 표창</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016 한국광고주대회</h1>
        <h3 class="title">광고주가 뽑은 좋은 프로그램상 - 드라마 부분</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제9회 코리아드라마페스티벌</h1>
        <h3 class="title">작품상, 남자 우수연기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제5회 아시아태평양 스타 어워즈</h1>
        <h3 class="title">대상</h3>
        <h3 class="title">남자 연기상</h3>
        <h3 class="title">여자 연기상</h3>
        <h3 class="title">베스트커플상</h3>
        <h3 class="title">올해의 드라마상</h3>
        <h3 class="title">베스트 아시아 태평양 스타상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제11회 서울 드라마 어워즈</h1>
        <h3 class="title">한류 드라마 - 최우수 작품상</h3>
        <h3 class="title">한류 드라마 - 남자 연기자상</h3>
        <h3 class="title">한류 드라마 - 주제가상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제43회 한국방송대상</h1>
        <h3 class="title">중단편드라마부문 - 작품상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016 신스틸러 페스티벌</h1>
        <h3 class="title">올해의 신스틸러상, 신인 신스틸러상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016 이달의 좋은 프로그램상</h1>
        <h3 class="title">4월의 좋은 프로그램상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제52회 백상예술대상</h1>
        <h3 class="title">TV부분 - 대상</h3>
        <h3 class="title">TV부분 - 남자 인기상</h3>
        <h3 class="title">TV부분 - 여자 인기상</h3>
        <h3 class="title">아이치이 스타상</h3>
      </div>
      <div v-else-if="name=='오징어 게임'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제11회 아름다운 예술인상</h1>
        <h3 class="title">영화예술인상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제12회 할리우드 뮤직 인 미디어 어워즈</h1>
        <h3 class="title">TV쇼/리미티드시리즈 음악상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제31회 고섬 어워즈</h1>
        <h3 class="title">장편 시리즈상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2021 비저너리 어워즈</h1>
        <h3 class="title">2021 비저너리</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제47회 피플스 초이스 어워즈</h1>
        <h3 class="title">올해의 정주행 쇼</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2021 미국영화연구소상</h1>
        <h3 class="title">특별상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제18회 한국이미지상</h1>
        <h3 class="title">디딤돌상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제79회 골든 글로브 시상식</h1>
        <h3 class="title">남우조연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제20회 자랑스런한국인대상</h1>
        <h3 class="title">문화예술부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제20회 디렉터스컷 어워즈</h1>
        <h3 class="title">올해의 감독상</h3>
        <h3 class="title">올해의 각본상상</h3>
        <h3 class="title">올해의 여자배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제28회 미국 배우조합상</h1>
        <h3 class="title">드라마 여자배우상</h3>
        <h3 class="title">드라마 남자배우상</h3>
        <h3 class="title">스턴트 앙상블상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제26회 미국 미술감독조합상</h1>
        <h3 class="title">1시간 현대 싱글카메라 시리즈상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제37회 인디펜던트 스피릿 시상식</h1>
        <h3 class="title">남자배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제27회 크리틱스 초이스 시상식</h1>
        <h3 class="title">드라마 남우주연상</h3>
        <h3 class="title">외국어 시리즈상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제2회 크리틱스 초이스 슈퍼 어워즈</h1>
        <h3 class="title">액션 시리즈 작품상</h3>
        <h3 class="title">액션 시리즈 남자배우상상</h3>
        <h3 class="title">액션 시리즈 여자배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제26회 새틀라이트 어워즈</h1>
        <h3 class="title">드라마 작품상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제58회 백상예술대상</h1>
        <h3 class="title">대상</h3>
        <h3 class="title">연출상</h3>
        <h3 class="title">예술상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제16회 포니정 혁신상</h1>
        <h3 class="title">혁신상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제26회 부천국제판타스틱영화제</h1>
        <h3 class="title">시리즈 영화상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제1회 청룡시리즈어워즈</h1>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">신인여우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2022 골드 더비 TV 어워즈</h1>
        <h3 class="title">드라마 여우게스트상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2022 할리우드 비평가 협회 TV 어워즈</h1>
        <h3 class="title">드라마 남우주연상</h3>
        <h3 class="title">국제 시리즈상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제14회 도리안 TV 어워즈</h1>
        <h3 class="title">비영어 TV 쇼상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제74회 프라임타임 에미상</h1>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">연출상</h3>
        <h3 class="title">여우게스트상</h3>
        <h3 class="title">현대극 미술상</h3>
        <h3 class="title">싱글에피소드 특수시각효과상</h3>
        <h3 class="title">스턴트 퍼포먼스상</h3>
      </div>
      <div v-else-if="name=='기생충'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제72회 칸 영화제</h1>
        <h3 class="title">황금종려상 수상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제40회 청룡영화상</h1>
        <h3 class="title">최우수작품상</h3>
        <h3 class="title">감독상</h3>
        <h3 class="title">미술상</h3>
        <h3 class="title">여우주연상</h3>
        <h3 class="title">여우조연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제77회 골든글로브상</h1>
        <h3 class="title">외국어영화상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제73회 영국 아카데미 시상식</h1>
        <h3 class="title">각본상</h3>
        <h3 class="title">비영어영화상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제92회 미국 아카데미 시상식</h1>
        <h3 class="title">작품상</h3>
        <h3 class="title">감독상</h3>
        <h3 class="title">각본상</h3>
        <h3 class="title">국제장편영화상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제45회 세자르상</h1>
        <h3 class="title">외국어영화상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제56회 대종상</h1>
        <h3 class="title">최우수작품상</h3>
        <h3 class="title">감독상</h3>
        <h3 class="title">시나리오상</h3>
        <h3 class="title">여우조연상</h3>
        <h3 class="title">음악상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제56회 백상예술대상</h1>
        <h3 class="title">대상</h3>
        <h3 class="title">작품상</h3>
        <h3 class="title">남자신인연기상</h3>
      </div>
      <div v-else-if="name=='올드보이'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2018년 BBC 선정 100대 비영어권 영화</h1>
        <h3 class="title">29위</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2016년 BBC 선정 100대 21세기 영화</h1>
        <h3 class="title">30위</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제 57회 칸 영화제</h1>
        <h3 class="title">감독상</h3>
        <h3 class="title">최우수작품상</h3>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">여우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제24회 청룡영화상</h1>
        <h3 class="title">감독상</h3>
        <h3 class="title">최우수작품상</h3>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">여우조연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제3회 대한민국 영화대상</h1>
        <h3 class="title">감독상</h3>
        <h3 class="title">최우수작품</h3>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">음악상</h3>
        <h3 class="title">조명상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제40회 백상예술대상</h1>
        <h3 class="title">감독상</h3>
        <h3 class="title">남자최우수연기상</h3>
        <h3 class="title">여자신인연기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제41회 대종상</h1>
        <h3 class="title">감독상</h3>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">음악상</h3>
        <h3 class="title">조명상</h3>
        <h3 class="title">편집상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제12회 이천 춘사영화상</h1>
        <h3 class="title">남우주연상</h3>
        <h3 class="title">촬영상</h3>
        <h3 class="title">편집상</h3>
        <h3 class="title">심사위원특별상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제 4회 부산영화평론가협회상</h1>
        <h3 class="title">감독상</h3>
        <h3 class="title">최우수작품상</h3>
        <h3 class="title">여우주연상</h3>
        <h3 class="title">촬영상</h3>
      </div>
      <div v-else-if="name=='부산행'" style="width:60%; border-color:black; border-style: solid;">
        <h3 class="title" style="color:yellow; margin:1rem;">본 작품은 수상 기록이 없으므로 흥행 기록으로 대체합니다.</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >글로벌 흥행 1억 달러 이상 한국 영화</h1>
        <h3 class="title">2위</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >연도별 대한민국 박스오피스 1위</h1>
        <h3 class="title">2016년도</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >대한민국 박스오피스 1위 영화</h1>
        <h3 class="title">2016년도 29주차</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >관객 및 매출 통계</h1>
        <h3 class="title">최종 누적매출액 93,182,579,048원</h3>
        <h3 class="title">누적관객수 11,566,862명</h3>
      </div>
      <div v-else-if="name=='BTS'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >한국대중음악상</h1>
        <h3 class="title">FAKE LOVE</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >올해의 음악인</h1>
        <h3 class="title">2018년 ~ 2019년</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >올해의 아티스트상</h1>
        <h3 class="title">2018년~2020년</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >올해의 앨범상</h1>
        <h3 class="title">화양연화 Young Forever</h3>
        <h3 class="title">LOVE YOURSELF 轉 'Tear'</h3>
        <h3 class="title">MAP OF THE SOUL : PERSONA</h3>
        <h3 class="title">MAP OF THE SOUL : 7</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >올해의 노래상</h1>
        <h3 class="title">작은 것들을 위한 시 (Boy With Luv)</h3>
        <h3 class="title">Dynamite</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >WORLDWIDE ICON OF THE YEAR</h1>
        <h3 class="title">LOVE YOURSELF 承 Her(2018년)</h3>
        <h3 class="title">LOVE YOURSELF 結 Answer(2019년)</h3>
        <h3 class="title">MAP OF THE SOUL : PERSONA(2020년)</h3>
        <h3 class="title">MAP OF THE SOUL : 7(2021년)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >디지털 음원대상</h1>
        <h3 class="title">작은 것들을 위한 시 (Boy With Luv)(2020년)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >서울가요대상 대상</h1>
        <h3 class="title">DNA</h3>
        <h3 class="title">FAKE LOVE</h3>
        <h3 class="title">작은 것들을 위한 시</h3>
        <h3 class="title">ON</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >역대 빌보드 뮤직 어워드</h1>
        <h3 class="title">톱 듀오/그룹상(2019년)</h3>
        <h3 class="title">톱 듀오/그룹상(2021년)</h3>
        <h3 class="title">톱 소셜 아티스트상(2017년)</h3>
        <h3 class="title">톱 소셜 아티스트상(2021년)</h3>
        <h3 class="title">톱 송 세일즈 아티스트상(2021년)</h3>
        <h3 class="title">톱 셀링 송(2021년)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >역대 아메리칸 뮤직 어워드</h1>
        <h3 class="title">Artist of the Year(2021년)</h3>
        <h3 class="title">Favorite Duo or Group Pop/Rock(2019년~2021년)</h3>
        <h3 class="title">Favorite Social Artist(2018년~2020년)</h3>
        <h3 class="title">Tour of the Year(2019년)</h3>
        <h3 class="title">Favorite Pop Song(2021년)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >역대 MTV 비디오 뮤직 어워드</h1>
        <h3 class="title">Best Group(2019년)</h3>
        <h3 class="title">Best Group(2020년)</h3>
        <h3 class="title">Best Pop(2020년)</h3>
        <h3 class="title">Best K-Pop(2019년)</h3>
        <h3 class="title">Best K-Pop(2020년)</h3>
        <h3 class="title">Best Cheography(2020년)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제9회 멜론 뮤직 어워드</h1>
        <h3 class="title">신인상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제28회 골든디스크 시상식</h1>
        <h3 class="title">신인상 음반부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제23회 서울가요대상</h1>
        <h3 class="title">신인상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제3회 가온차트 뮤직 어워즈</h1>
        <h3 class="title">올해의 신인상 그룹부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제2회 YinYueTai VChart Awards</h1>
        <h3 class="title">Top New Artist</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제29회 골든디스크 시상식</h1>
        <h3 class="title">본상 음반부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제24회 서울가요대상</h1>
        <h3 class="title">본상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제4회 가온차트 뮤직 어워즈</h1>
        <h3 class="title">올해의 발견상 월드루키부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제29회 The Japan Gold Disk Award</h1>
        <h3 class="title">New Artist of The Year (Asia)</h3>
        <h3 class="title">Best 3 New Artists (Asia)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제9회 케이블TV 방송대상</h1>
        <h3 class="title">케이블스타상 인기상 한류부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제11회 멜론 뮤직 어워드</h1>
        <h3 class="title">댄스 남자부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제17회 엠넷 아시안 뮤직 어워즈</h1>
        <h3 class="title">월드 퍼포먼스</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제25회 서울가요대상</h1>
        <h3 class="title">본상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제30회 골든디스크 시상식</h1>
        <h3 class="title">본상 음반부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제5회 가온차트 뮤직 어워즈</h1>
        <h3 class="title">특별상 월드한류스타상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제7회 대한민국대중문화예술상</h1>
        <h3 class="title">문화체육관광부장관표창</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제1회 아시아 아티스트 어워즈</h1>
        <h3 class="title">베스트 아이콘상 가수부문</h3>
        <h3 class="title">베스트 아티스트상 가수부문</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제12회 멜론 뮤직 어워드</h1>
        <h3 class="title">TOP 10</h3>
        <h3 class="title">올해의 앨범상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제31회 골든디스크 시상식</h1>
        <h3 class="title">본상 음반부문</h3>
        <h3 class="title">글로벌 케이팝 아티스트상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제26회 서울가요대상</h1>
        <h3 class="title">뮤직비디오상</h3>
        <h3 class="title">댄스 퍼포먼스상</h3>
        <h3 class="title">본상</h3>
        <h3 class="title">최고 앨범상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제6회 가온차트 뮤직 어워즈</h1>
        <h3 class="title">V LIVE 글로벌 인기상</h3>
        <h3 class="title">올해의 가수상 음반부문 4분기</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제31회 The Japan Gold Disk Award</h1>
        <h3 class="title">Best 3 Albums (Asia)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제5회 YinYueTai VChart Awards</h1>
        <h3 class="title">Best Stage Performance</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제24회 Billboard Music Awards</h1>
        <h3 class="title">Top Social Artist</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제1회 소리바다 베스트 케이뮤직 어워즈</h1>
        <h3 class="title">신한류 아티스트상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제44회 한국방송대상</h1>
        <h3 class="title">가수상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제19회 엠넷 아시안 뮤직 어워즈</h1>
        <h3 class="title">베스트 뮤직비디오</h3>
        <h3 class="title">베스트 아시안 스타일</h3>
        <h3 class="title">올해의 가수상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제13회 멜론 뮤직 어워즈</h1>
        <h3 class="title">TOP 10</h3>
        <h3 class="title">핫트렌드상(슈가)</h3>
        <h3 class="title">뮤직비디오상</h3>
        <h3 class="title">글로벌 아티스트</h3>
        <h3 class="title">올해의 베스트송</h3>
      </div>
      <div v-else-if="name=='싸이'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2012: American Music Awards</h1>
        <h3 class="title">New Media Award상 (강남스타일)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2012: MTV Europe Music Awards</h1>
        <h3 class="title">Best Video상 (강남스타일)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2013: NRJ Music Awards(프랑스)</h1>
        <h3 class="title">NRJ Award of Honor상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2013: NRJ Music Awards(프랑스)</h1>
        <h3 class="title">Chanson Internationale de l'année (International Song of the Year)상 - (강남스타일)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2013: NRJ Music Awards(프랑스)</h1>
        <h3 class="title">Clip de l'année (Video of the Year)상 (강남스타일)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2013: Billboard Music Awards</h1>
        <h3 class="title">Streaming Song (Video)상 (강남스타일)</h3>
      </div>
      <div v-else-if="name=='이정재'" style="width:60%; border-color:black; border-style: solid;">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제31회 백상예술대상</h1>
        <h3 class="title">TV부문 남자 신인연기상</h3>
        <h3 class="title">영화부문 남자 신인연기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제33회 대종상영화제</h1>
        <h3 class="title">신인남자배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제15회 한국영화평론가협회상</h1>
        <h3 class="title">신인남우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제16회 청룡영화상</h1>
        <h3 class="title">신인남우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >SBS 연기대상</h1>
        <h3 class="title">남자 신인상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제33회 백상예술대상</h1>
        <h3 class="title">영화부문 인기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제35회 백상예술대상</h1>
        <h3 class="title">영화부문 인기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제19회 한국영화평론가협회상</h1>
        <h3 class="title">남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제20회 청룡영화상</h1>
        <h3 class="title">남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제38회 저축의 날</h1>
        <h3 class="title">국무총리 표창</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제29회 황금촬영상</h1>
        <h3 class="title">연기대상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제1회 스타일 아이콘 어워즈</h1>
        <h3 class="title">남자 배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제4회 Mnet 20's Choice</h1>
        <h3 class="title">가장 영향력 있는 스타 20인</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제31회 판타스포르토 국제영화제</h1>
        <h3 class="title">감독주간부문 남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제50회 대종상영화제</h1>
        <h3 class="title">남자인기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제34회 청룡영화상</h1>
        <h3 class="title">남우조연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제33회 한국영화평론가협회상</h1>
        <h3 class="title">CGV 스타상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제5회 올해의 영화상</h1>
        <h3 class="title">남우조연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제50회 백상예술대상</h1>
        <h3 class="title">영화부문 남자 조연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제51회 백상예술대상</h1>
        <h3 class="title">인스타일 베스트 스타일상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제24회 부일영화상</h1>
        <h3 class="title">남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제3회 마리끌레르 아시아 스타 어워즈</h1>
        <h3 class="title">올해의 배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제8회 스타일 아이콘 아시아</h1>
        <h3 class="title">스타일 아이콘상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2020 아시아 아티스트 어워즈</h1>
        <h3 class="title">AAA 올해의 배우(영화 부문)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제25회 소비자의 날 시상식</h1>
        <h3 class="title">2020 관객이 뽑은 올해의 배우</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2021 아시아 아티스트 어워즈</h1>
        <h3 class="title">AAA 올해의 배우</h3>
        <h3 class="title">AAA 페뷸러스</h3>
        <h3 class="title">AAA 핫트렌드</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제28회 미국 배우조합상</h1>
        <h3 class="title">TV부문 드라마 남자배우상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제37회 인디펜던트 스피릿 시상식</h1>
        <h3 class="title">TV부문 남자 최우수 연기상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제27회 크리틱스 초이스 시상식</h1>
        <h3 class="title">TV부문 드라마 남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제1회 청룡시리즈어워즈</h1>
        <h3 class="title">드라마부문 남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >2022 할리우드 비평가 협회 TV 어워즈</h1>
        <h3 class="title">스트리밍부문 드라마 남우주연상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제74회 프라임타임 에미상</h1>
        <h3 class="title">드라마부문 남우주연상</h3>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ["name",],
  }
</script>

<style scoped>
  @font-face {
    font-family: 'ONE-Mobile-POP';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/ONE-Mobile-POP.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  .APIscene{
    position: fixed;
    top: 2.5rem;
    background-color: #09030300;
    width: 85%;
    height: 80%;
    transform: translate(7%, 5%);

    border-radius: 8px;
  }
  .APIscene::-webkit-scrollbar {
    width: 10px;
  }
  .APIscene::-webkit-scrollbar-track {
    background-color: transparent;
  }
  .APIscene::-webkit-scrollbar-thumb {
    border-radius: 20px;
    background-color: rgb(219, 214, 214);
  }
  .APIscene::-webkit-scrollbar-button {
    width: 0;
    height: 0;
  }
  #profileimg{
    width: 100%;
    height: auto;
  }
  .title{
    text-align: center;
    margin-top:0rem;
    margin-right: 0;
    margin-left: 0;
  }
  h1{
    font-family: 'ONE-Mobile-POP';
    margin-top: 0;
  }
  h3{
    color: white;
  }
</style>