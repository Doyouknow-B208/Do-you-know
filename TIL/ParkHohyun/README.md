## 명예의 전당 페이지 기능 구현

#### 인트로 페이지

- ~~백그라운드~~
  - ~~비디오 loop 사용해서 백그라운에서 계속 재생 -> **video 태그** [공식문서](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video)~~
- title 
  - 이쁜 폰트 사용(fontawesome, googlefont 사용)
- ~~메인 페이지 진입하는 버튼~~
  - ~~버튼 이미지 입체적인 트로피~~ 
  - ~~마우스 호버 효과~~

#### 메인 페이지

- ~~공통~~
  - ~~사운드 넣기 -> [참고 사이트](https://curryyou.tistory.com/337)~~

- ~~intro~~
  - ~~백그라운드~~
    - ~~비디오 한번 재생 -> **비디오 태그**~~

- main
  - ~~nav bar~~
  - ~~백그라운드~~
    - ~~비디오 loop 사용해서 백그라운드에서 계속 재생 -> **video 태그**~~
    - ~~동영상 뿌옇게 효과 주기~~
  - title
    - 이쁜 폰트 사용(fontawesome, googlefont 사용)
  - side bar
    -  주제별로 분류
    - 왼쪽에 위치
  - ~~sound~~
    - ~~버튼으로 on/off~~
  - card
    - 마우스 올리면 뒤집히는 효과 -> **카드 3d 애니매이션 효과** [참고 링크](https://goddino.tistory.com/185)
    - youtube, 해당 기사 링크

 

ex) 피파 명예의 전당

- intro

```html
<section class="intro transformCenterX" style="opacity: 0;">
				<div class="video transformCenterX active" style="opacity: 1;">
					<video id="introVideo" width="2000" height="1000" preload="auto">
						<source src="http://fifa4.vod.nexoncdn.co.kr/2018/event/history_intro.mp4" type="video/mp4">
					</video>
					<div class="dimmed" style="opacity: 0;"></div>
				</div>
            </section>
```

- main

```html
<section class="main transformCenterX active" style="opacity: 1;">
                <div class="inner">
                    <div class="video transformCenterX active" style="opacity: 1;">
                        <div id="temple">
							<video id="mainVideo" width="2000" height="1000" preload="auto" loop="">
								<source src="http://fifa4.vod.nexoncdn.co.kr/2018/event/history_temple.mp4" type="video/mp4">
							</video>
						</div>
						<div class="dimmed"></div>
                    </div>
				</section>
```

