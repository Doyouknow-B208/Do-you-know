<template>
  <div class="APIscene" style="overflow:auto;">
    <div style="display: flex; justify-content: space-around; border-width: 2px; margin-top:3px; margin-bottom:3px;">
      <div v-if="name=='손흥민'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/손흥민_프로필.png">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >손흥민</h1>
        <h3 class="title">토트넘 홋스퍼 FC No. 7</h3>
        <h3 class="title">孫興慜 ｜ Son Heung-Min</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출생</h1>
        <h3 class="title">1992년 7월 8일 (30세) 강원도 춘천시 춘천시 후평동</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국적</h1>
        <h3 class="title">대한민국</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >본관</h1>
        <h3 class="title">밀양 손씨</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >학력</h1>
        <h3 class="title">가산초등학교 (전학)</h3>
        <h3 class="title">부안초등학교 (졸업)</h3>
        <h3 class="title">후평중학교 (전학)</h3>
        <h3 class="title">육민관중학교 (전학)</h3>
        <h3 class="title">동북중학교 (졸업)</h3>
        <h3 class="title">동북고등학교 (중퇴)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >신체</h1>
        <h3 class="title">183cm</h3>
        <h3 class="title">78kg</h3>
        <h3 class="title">255mm</h3>
        <h3 class="title">AB형</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >포지션</h1>
        <h3 class="title">윙어, 스트라이커, 세컨드 스트라이커</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >주발</h1>
        <h3 class="title">오른발 (양발)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >등번호</h1>
        <h3 class="title">대한민국 축구 국가대표팀 | 토트넘 홋스퍼 FC | 7번 </h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >유스클럽</h1>
        <h3 class="title">FC 서울 (2007~2008)</h3>
        <h3 class="title">함부르크 SV (2008~2010)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >프로클럽</h1>
        <h3 class="title">함부르크 SV (2010~2013)</h3>
        <h3 class="title">바이어 04 레버쿠젠 (2013~2015)</h3>
        <h3 class="title">토트넘 홋스퍼 FC (2015~ )</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국가대표</h1>
        <h3 class="title">104경기 35골</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >통산득점</h1>
        <h3 class="title">218골</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >병역</h1>
        <h3 class="title">예술체육요원</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >응원가</h1>
        <h3 class="title">Nice One Sonny</h3>
        <h3 class="title">Nice One Son</h3>
        <h3 class="title">Lemon Tree</h3>
      </div>
      <div v-else-if="name=='김연아'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/김연아.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출생</h1>
        <h3 class="title">경기도 부천시 중구 도당동</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국적</h1>
        <h3 class="title">대한민국</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >본관</h1>
        <h3 class="title">경주 김씨</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >신체</h1>
        <h3 class="title">164cm, 47kg, 240mm, O형</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >가족</h1>
        <h3 class="title">아버지 김현석(1958년생), 어머니 박미희(1958년생), 언니 김애라(1987년생)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >학력</h1>
        <h3 class="title">신흥초등학교 (졸업)</h3>
        <h3 class="title">도장중학교 (졸업)</h3>
        <h3 class="title">수리고등학교 (졸업)</h3>
        <h3 class="title">고려대학교 사범대학 (체육교육 / 학사)</h3>
        <h3 class="title">고려대학교 대학원 (체육학 / 석사과정 수료)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >종교</h1>
        <h3 class="title">가톨릭</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >소속</h1>
        <h3 class="title">올댓스포츠</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >종목</h1>
        <h3 class="title">피겨 스케이팅</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >상훈</h1>
        <h3 class="title">국민훈장 모란장(2012년 수훈)</h3>
        <h3 class="title">체육훈장 청룡장(2016년 수훈)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >MBTI</h1>
        <h3 class="title">ESFJ</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >은퇴</h1>
        <h3 class="title">2014년 2월 21일</h3>
      </div>
      <div v-else-if="name=='김연경'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/김연경.png">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출생</h1>
        <h3 class="title">1988년 2월 26일 (34세)</h3>
        <h3 class="title">경기도 안산시 초지동</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국적</h1>
        <h3 class="title">대한민국</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >학력</h1>
        <h3 class="title">안산서초등학교 (졸업)</h3>
        <h3 class="title">원곡중학교 (배구부 / 졸업)</h3>
        <h3 class="title">수원한일전산여자고등학교 (배구부 / 졸업)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >신체</h1>
        <h3 class="title">192cm, 72kg, 290mm, AB형</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >종교</h1>
        <h3 class="title">가톡릭</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >포지션</h1>
        <h3 class="title">레프트 | Outside Hitter</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국가대표</h1>
        <h3 class="title">대한민국 여자 배구 청소년 국가대표팀 (2004~2005)</h3>
        <h3 class="title">대한민국 여자 배구 국가대표팀 (2005~2021)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >소속구단</h1>
        <h3 class="title">천안 흥국생명 핑크스파이더스 2005~2009 / 대한민국)</h3>
        <h3 class="title">JT 마블러스 (2009~2011 / 일본)[임대]</h3>
        <h3 class="title">페네르바흐체 SK (2011~2017 / 터키)</h3>
        <h3 class="title">상하이 브라이트 유베스트 (2017~2018 / 중국)</h3>
        <h3 class="title">엑자시바시 비트라 (2018~2020 / 터키)</h3>
        <h3 class="title">인천 흥국생명 핑크스파이더스 (2020~2021 / 대한민국)</h3>
        <h3 class="title">상하이 브라이트 유베스트 (2021~2022 / 중국)</h3>
        <h3 class="title">인천 흥국생명 핑크스파이더스 (2020~2021 / 대한민국)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >직책</h1>
        <h3 class="title">대한민국 여자 배구 국가대표팀 주장 (2014~2021)</h3>
        <h3 class="title">FIVB 선수위원회 초대위원 (2016~2020)</h3>
        <h3 class="title">엑자시바시 비트라 주장 (2019~2020)</h3>
        <h3 class="title">인천 흥국생명 핑크스파이더스 주장 (2020~2021)</h3>
        <h3 class="title">2020 도쿄 올림픽 선수단 대표 (2021)</h3>
      </div>
      <div v-else-if="name=='이상한 변호사 우영우'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/이상한변호사우영우.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >언어별 제목</h1>
        <h3 class="title">한국어: 이상한 변호사 우영우</h3>
        <h3 class="title">영어: Extraordinary Attorney Woo</h3>
        <h3 class="title">중국어: 非常律師禹英禑</h3>
        <h3 class="title">일본어: ウ・ヨンウ弁護士は天才肌</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">법정, 휴먼, 드라마, 코미디</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >방송 시간</h1>
        <h3 class="title">수 · 목 / 오후 9:10 ~ 10:30</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >방송 기간</h1>
        <h3 class="title">2022년 6월 29일 ~ 2022년 8월 18일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >방송 횟수</h1>
        <h3 class="title">16부작</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작비</h1>
        <h3 class="title">약 150억 원</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출연</h1>
        <h3 class="title">박은빈, 강태오, 강기영, 하윤경, 주종혁 外</h3>
      </div>
      <div v-else-if="name=='태양의 후예'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/태양의후예.jpg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >방송 시간</h1>
        <h3 class="title">수요일, 목요일 오후 10:00 ~ 11:10</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >방송 기간</h1>
        <h3 class="title">2016년 2월 24일 ~ 2016년 4월 14일 (본방)</h3>
        <h3 class="title">2017년 11월 3일 ~ 2017년 12월 23일 (재방)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >방송 횟수</h1>
        <h3 class="title">16부작 (본편) 3부작 (스페셜)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">드라마, 로맨스, 액션, 코미디</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작비</h1>
        <h3 class="title">약 130억 원</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출연자</h1>
        <h3 class="title">송중기, 송혜교, 진구, 김지원, 온유 外</h3>
      </div>
      <div v-else-if="name=='오징어 게임'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/오징어게임.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">데스 게임, 서바이벌, 스릴러, 액션, 드라마, 피카레스크</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >공개일</h1>
        <h3 class="title">2021년 9월 17일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >공개 회차</h1>
        <h3 class="title">9부작</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >상영 길이</h1>
        <h3 class="title">476분 31초 (7시간 56분 31초)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작비</h1>
        <h3 class="title">253억 원</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출연</h1>
        <h3 class="title">이정재, 박해수, 위하준, 오영수, 정호연, 허성태, 김주령, 아누팜 트리파티, 유성주, 이유미 외</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >독점 스트리밍</h1>
        <h3 class="title">넥플릭스</h3>
      </div>
      <div v-else-if="name=='기생충'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/기생충.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">범죄, 스릴러, 드라마, 블랙 코미디, 피카레스크</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >감독</h1>
        <h3 class="title">봉준호</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >각본</h1>
        <h3 class="title">봉준호, 한진원</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출연</h1>
        <h3 class="title">송강호, 이선균, 조여정, 최우식, 박소담, 장혜진, 이정은, 박명훈 외</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작 기간</h1>
        <h3 class="title">2018년 5월 18일 ~ 2018년 9월 19일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >배급사</h1>
        <h3 class="title">CJ엔터테인먼트</h3>
        <h3 class="title">미국 Neon</h3>
        <h3 class="title">프랑스 The Jokers</h3>
        <h3 class="title">일본 Bitters End</h3>
        <h3 class="title">영국 CURZON</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >상영 시간</h1>
        <h3 class="title">132분(2시간 12분)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작비</h1>
        <h3 class="title">1,100만 달러</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >마케팅비</h1>
        <h3 class="title">1,500만 달러~1,750만 달러</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >월드 박스오피스</h1>
        <h3 class="title">$263,136,741</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >북미 박스오피스</h1>
        <h3 class="title">$53,369,749</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >대한민국 관객 수</h1>
        <h3 class="title">10,310,255명</h3>
      </div>
      <div v-else-if="name=='올드보이'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/올드보이.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">드라마, 미스터리, 범죄, 스릴러, 느와르, 피카레스크</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >감독</h1>
        <h3 class="title">박찬욱</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >원작</h1>
        <h3 class="title">츠치야 가론, 미네기시 노부아키 (올드보이)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작</h1>
        <h3 class="title">임승용, 김동주, 한재덕, 지영준</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출연</h1>
        <h3 class="title">최민식, 유지태, 강혜정 등</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작사</h1>
        <h3 class="title">㈜에그필름</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >배급사</h1>
        <h3 class="title">㈜쇼이스트, CJ엔터테인먼트 (재개봉)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작 기간</h1>
        <h3 class="title">2003년 3월 26일~2003년 7월 14일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >개봉일</h1>
        <h3 class="title">2003년 11월 21일, 2013년 11월 21일 (재개봉)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >상영 시간</h1>
        <h3 class="title">120분</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >대한민국 총 관객수</h1>
        <h3 class="title">3,269,000명</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >월드 박스오피스</h1>
        <h3 class="title">$15,255,474</h3>
      </div>
      <div v-else-if="name=='부산행'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/부산행.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">공포, 스릴러, 액션, SF, 어드벤처, 재난, 드라마, 좀비아포칼립스, 로드무비</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >감독</h1>
        <h3 class="title">연상호</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >각본</h1>
        <h3 class="title">박주석</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작</h1>
        <h3 class="title">이동하</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출연</h1>
        <h3 class="title">공유, 정유미, 마동석, 최우식, 안소희, 김의성, 김수안 등</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작사</h1>
        <h3 class="title">영화사 레드피터</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >배급사</h1>
        <h3 class="title">넥스트엔터테인먼트월드</h3>
        <h3 class="title">미국 Well Go USA</h3>
        <h3 class="title">프랑스 ARP SELECTION</h3>
        <h3 class="title">인도 MVP Entertainment India</h3>
        <h3 class="title">일본 TWIN</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >촬영 기간</h1>
        <h3 class="title">2015년 4월 26일 ~ 2015년 8월 19일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >상영 시간</h1>
        <h3 class="title">118분 (1시간 58분)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >제작비</h1>
        <h3 class="title">115억 원</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >북미 박스오피스</h1>
        <h3 class="title">$2,129,768</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >월드 박스오피스</h1>
        <h3 class="title">$129,228,466</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >대한민국 총 관객 수</h1>
        <h3 class="title">11,567,662명</h3>
      </div>
      <div v-else-if="name=='BTS'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/BTS.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >그룹명</h1>
        <h3 class="title">방탄소년단, BTS (영문)</h3>
        <h3 class="title">防彈少年團 (정자)</h3>
        <h3 class="title">防弹少年团fáng tán shào nián tuán (간체자)</h3>
        <h3 class="title">防弾少年団ぼうだんしょうねんだん (신자체)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >멤버</h1>
        <h3 class="title">진, 슈가, 제이홉, RM, 지민, 뷔, 정국</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >데뷔일</h1>
        <h3 class="title">2013년 6월 13일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >리더</h1>
        <h3 class="title">RM</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >장르</h1>
        <h3 class="title">랩/힙합, 댄스, 팝, 발라드, EDM, R&B/어반</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >소속사</h1>
        <h3 class="title">BIGHIT MUSIC</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >팬덤</h1>
        <h3 class="title">ARMY</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >훈장</h1>
        <h3 class="title">화관문호훈장</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >데뷔음반</h1>
        <h3 class="title">2 COOL 4 SKOOL</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >유통사</h1>
        <h3 class="title">[한]YG PLUS</h3>
        <h3 class="title">[미]유니버설 뮤직 그룹</h3>
        <h3 class="title">[일]유니버설 뮤직 재팬</h3>
      </div>
      <div v-else-if="name=='싸이'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/싸이.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >본명</h1>
        <h3 class="title">박재상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출생</h1>
        <h3 class="title">1977년 12월 31일 (44세)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >거주지</h1>
        <h3 class="title">서울특별시 용산구 한남동</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국적</h1>
        <h3 class="title">대한민국</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >본관</h1>
        <h3 class="title">밀양 박씨 (密城 朴氏)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >신체</h1>
        <h3 class="title">170.2cm, B형</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >학력</h1>
        <h3 class="title">서울반포초등학교 (졸업)</h3>
        <h3 class="title">반포중학교 (졸업)</h3>
        <h3 class="title">세화고등학교 (졸업)</h3>
        <h3 class="title">보스턴 대학교 (국제경영학 / 중퇴)</h3>
        <h3 class="title">버클리 음악대학 (명예 졸업)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >병역</h1>
        <h3 class="title">대한민국 육군 병장 만기전역(2007년 12월 17일 ~ 2009년 7월 11일)</h3>
        <h3 class="title">제52보병사단 통신병 (2008년 1월 25일 ~ 2009년 1월 12일)</h3>
        <h3 class="title">국방부 홍보지원대 (2009년 1월 12일 ~ 2009년 7월 11일)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >소속사</h1>
        <h3 class="title">P NATION (사내이사), SB Projects</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >활동 장르</h1>
        <h3 class="title">댄스, 랩, 락, 발라드</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >팬덤</h1>
        <h3 class="title">코 (Cho)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >데뷔</h1>
        <h3 class="title">2001년 1월 12일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >MBTI</h1>
        <h3 class="title">ENFP</h3>
      </div>
      <div v-else-if="name=='이정재'" style="width:60%; border-color:black; border-style: solid;">
        <img id="profileimg" src="../../assets/DYKC/이정재.jpeg">
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >출생</h1>
        <h3 class="title">1972년 12월 15일 (49세) 서울특별시</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >국적</h1>
        <h3 class="title">대한민국</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >본관</h1>
        <h3 class="title">전주 이씨</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >신체</h1>
        <h3 class="title">180cm, 70kg, B형</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >학력</h1>
        <h3 class="title">숭의국민학교(졸업)</h3>
        <h3 class="title">청담중학교(졸업)</h3>
        <h3 class="title">현대고등학교(졸업)</h3>
        <h3 class="title">동국대학교(연극영상학 / 학사)</h3>
        <h3 class="title">동국대학교 문화예술대학원(공연영상예술학/석사)</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >병역</h1>
        <h3 class="title">대한민국 육군 제52보병사단 상병 소집해제</h3>
        <h3 class="title">1994년 12월 26일 ~ 1996년 6월 27일</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >취미</h1>
        <h3 class="title">골프, 영화 감상</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >특기</h1>
        <h3 class="title">인테리어, 구기종목, 보디빌딩</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >소속사</h1>
        <h3 class="title">Artist COMPANY</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >데뷔</h1>
        <h3 class="title">1993년 SBS 드라마《공룡선생》</h3>
        <h1 class="title" style="background-color: rgb(153, 149, 149);" >별명</h1>
        <h3 class="title">염라언니, 재리</h3>
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