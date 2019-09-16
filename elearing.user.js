// ==UserScript==
// @name         elearn.main
// @namespace    http://tampermonkey.net/
// @version      0.3
// @author       Muhun Kim
// @match        https://elearning.jejunu.ac.kr/
// @match        http://elearning.jejunu.ac.kr/
// @grant        none
// ==/UserScript==

;(() => {
  'use strict'
  window.onload = () => {
    const userForm = document.querySelector('frame[name="main"]')
      .contentDocument.userForm

    if (userForm !== undefined) {
      const formBind = userForm.querySelector.bind(userForm)
      formBind('input#id').value = 201812345
      formBind('input#pw').value = 'password'
      formBind('.loginBtn').click()
    }
  }
})()
