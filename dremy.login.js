// ==UserScript==
// @name     dreamy.index
// @version 20190807
// @updateURL https://github.com/x86chi/jejunu/raw/master/dreamy.login.js
// @downloadURL https://github.com/x86chi/jejunu/raw/master/dreamy.login.js
// @match https://dreamy.jejunu.ac.kr/frame/index.do*
// ==/UserScript==

window.onload = () => {
    if (document.getElementsByName('frmLogin').length) {
         // document.getElementById('password').focus();
        document.getElementById('act_lgn').click();
    }
}