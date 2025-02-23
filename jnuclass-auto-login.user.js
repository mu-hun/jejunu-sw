// ==UserScript==
// @name     https://jnuclass.jejunu.ac.kr/xn-sso/login.php auto login
// @version  1
// @grant    none
// @version 20241227
// @match https://jnuclass.jejunu.ac.kr/xn-sso/login.php*
// @updateURL https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/jnuclass-auto-login.user.js
// @downloadURL https://github.com/mu-hun/jejunu-sw/raw/refs/heads/master/jnuclass-auto-login.user.js
// @run-at document-end
// ==/UserScript==

const id = ''
const pw = ''

;(() => {
  function getCookie(name) {
    var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)')
    return v ? v[2] : null
  }

  const form = document.querySelector('#form1')

  form.querySelector('#login_user_id').value = id
  form.querySelector('#login_user_password').value = pw
  form.querySelector('#login_form1_csrf_token').value = getCookie(
    'xn_sso_csrf_token_for_this_login'
  )

  form.action =
    'https://jnuclass.jejunu.ac.kr/xn-sso/gw-cb.php?from=&login_type=standalone&return_url=https%3A%2F%2Fjnuclass.jejunu.ac.kr%2Flogin%2Fcallback'
  form.target = '_top'
  form.submit()
})()
