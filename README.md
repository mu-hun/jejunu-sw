# Enjoy Campus Life

학교 수업 요약 정리, 과목별 과제, 개인 공부 노트 레포

### 교내 ICT 서비스 이용 팁

- `*.jejunu.ac.kr/*` - HTTPS 리다이렉트

  [HTTPS Eveywhere](https://www.eff.org/https-everywhere) 사용

- [하영드리미](https://dreamy.jejunu.ac.kr) - `submit()` 이후 하단의 유저 스크립트 적용
 
  ```js
  const D = document
  const $ = D.querySelector.bind(D)

  window.onload=function() {
    $('#act_lgn').click();
  }
  ```

- [제주대학교 웹 메일](https://webmail.jejunu.ac.kr/) - 메일 클라이언트 설정

  POP 프로토콜 사용, 송/수신 서버 주소는 `webmail.jejunu.ac.kr` 로 같음. SSL 사용 안함(...)

  > **Mac OS 기본 메일 클라이언트**에서
  >
  > `v11.2` 기준으로 사용자 이름이 제멋대로 공란이 되는 버그가 있음. Sign in 버튼 누르기 직전에 ID 재입력.
  >
  > <img src="mail-setup.png" width="300em"/>

[Autofill Forms]: https://mybrowseraddon.com/autofill-forms.html

---
_This repository was inspired by [simnalamburt/snucse](https://github.com/simnalamburt/snucse)_

_jejunu_ is primarily distributed under the terms of the [GNU Affero General Public License v3.0](./LICENSE) or any later version. See [COPYRIGHT](./COPYRIGHT) for details.
