// ==UserScript==
// @name     dreamy.index
// @version 20190819
// @updateURL https://github.com/x86chi/jejunu/raw/master/dreamy.user.js
// @downloadURL https://github.com/x86chi/jejunu/raw/master/dreamy.user.js
// @match https://dreamy.jejunu.ac.kr/frame/index.do*
// ==/UserScript==

window.onload = () => {
  if (document.getElementsByName('frmLogin').length) {
    // document.getElementById('password').focus();
    document.getElementById('act_lgn').click()
  }
}
