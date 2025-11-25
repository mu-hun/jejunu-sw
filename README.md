# Enjoy Campus Life

학교 수업 요약 정리, 과목별 과제, 개인 공부 노트 레포

## 교내 ICT 서비스 이용 팁

- [제주대학교 포털](https://portal.jejunu.ac.kr)

  - [SSO 로그인 자동화 유저스크립트](https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/portal.user.js) 설치
  - [mu-hun/jejunu-icalendar-server](https://github.com/mu-hun/jejunu-icalendar-server/)<br/>
    강의 시간표를 외부 캘린더에 구독하는 자동화 워크플로우

- [제주대학교 LMS (JNU CLASS)](https://jnuclass.jejunu.ac.kr)

  1. [로그인 페이지 리다이렉션 유저스크립트](https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/jnuclass-redirect-to-login.user.js) 설치
  2. [로그인 자동화 유저스크립트](https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/jnuclass-auto-login.user.js) 설치

## 실습 과제 모음

- 컴퓨팅 원리 및 패러다임 (컴퓨터 그래픽스를 바탕으로 한 전산학 개론)
  > 교수님: 두번째 과제는 회전 애니매이션 구현으로 할게요~<br/>
  > 나: https://github.com/mu-hun/strom 시공조아 제출합니다.
- 어데메 🔍 – 제주도내 다양한 장소를 알아보는 미니게임: https://github.com/eodeme/eodeme
- 디스코드 채팅 경험 바탕의 방공호 생존 게임 프로젝트
  - [게임 흐름도](https://gist.github.com/mu-hun/aaa84e2f1eef326062d542f8731940fb#file-flow-mmd), [시연 영상](https://gist.github.com/user-attachments/assets/0cd141f2-0b01-4b48-89df-9cc1ed79394b)
  - 디스코드 봇에 쓰일 [LLM 통신 어뎁터](https://gist.github.com/mu-hun/aaa84e2f1eef326062d542f8731940fb#file-agent_adapter-py)[^Adapter] 설계를 담당했습니다.
- 차트 UI를 응용한 웹 애플리케이션 과제: [제작 제안서 아웃 링크](https://speakerdeck.com/muhun/team-slicon)
  - 정렬 알고리즘 시각화 및 청각화 구현: https://github.com/ez-25/team-silicon/pull/1
  - 가상화폐 차트 데모 (코드리뷰): https://github.com/ez-25/team-silicon/pull/8
- 임베디드 소프트웨어 - 리듬게임 키 입력 LED 시각화 프로젝트: [PLATiNA-LED](https://github.com/mu-hun/PLATiNA-LED)

[^Adapter]: Ports & Adapters 패턴(aka. Hexagonal Architecture) 에서 유래한 아키텍쳐 용어로, Port는 내부를 뜻하고 Adapter는 외부를 뜻합니다. [앨리스테어 코어번(Alistair Cockburn)의 해당 패턴 소개 포스팅](https://web.archive.org/web/20140329201018/http://alistair.cockburn.us/Hexagonal+architecture)을 참고 바랍니다.

---

_This repository was inspired by [simnalamburt/snucse](https://github.com/simnalamburt/snucse)_

Original contents are copyrighted to Lecturer, and Notes is primarily distributed under the terms of the [GNU Affero General Public License v3.0](./LICENSE) or any later version. See [COPYRIGHT](./COPYRIGHT) for details.
