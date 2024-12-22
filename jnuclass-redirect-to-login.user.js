// ==UserScript==
// @name     https://jnuclass.jejunu.ac.kr/ to redirect login page
// @version  1
// @grant    none
// @version 20241227
// @match https://jnuclass.jejunu.ac.kr/
// @updateURL https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/jnuclass-redirect-to-login.user.js
// @downloadURL https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/jnuclass-redirect-to-login.user.js
// @run-at document-start
// ==/UserScript==

window.location.href = '/login'
