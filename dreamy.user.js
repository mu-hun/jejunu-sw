// ==UserScript==
// @name     dreamy.index
// @version 20190819
// @updateURL https://github.com/x86chi/jejunu/raw/master/dreamy.user.js
// @downloadURL https://github.com/x86chi/jejunu/raw/master/dreamy.user.js
// @match https://dreamy.jejunu.ac.kr/frame/index.do*
// ==/UserScript==

window.onload = () => {
  if (document.getElementsByName('frmLogin').length) {
    // document.querySelector('#userid').value = 1234567890
    // document.querySelector('#password').value = 'dreamy.jejunu.ac.kr'
    document.getElementById('act_lgn').click()
  }
}
