// ==UserScript==
// @name     webmail
// @version  1
// @grant    none
// @match https://webmail.jejunu.ac.kr/login
// ==/UserScript==

window.onload = () => {
  if (document.getElementsByName('loginForm').length)
    document.querySelector('.login-btn > a').click()
}
