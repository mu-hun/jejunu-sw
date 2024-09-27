// ==UserScript==
// @name     https://portal.jejunu.ac.kr auto login
// @version  1
// @grant    none
// @version 20240927
// @updateURL https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/portal.user.js
// @downloadURL https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/portal.user.js
// @match https://portal.jejunu.ac.kr/login.htm*
// @run-at document-end
// ==/UserScript==

;(() => {
  const form = document.querySelector('#form-login')

  const password = document.querySelector('#userPswd').value
  const userId = document.querySelector('#userId').value

  form.querySelector('input[name="pw"').value = password
  form.querySelector('input[name="userId"]').value = userId

  form.setAttribute('action', '/sso/ssoLogin.jsp')

  form.requestSubmit()
})()
