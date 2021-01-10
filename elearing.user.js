// ==UserScript==
// @name         elearn.main
// @namespace    http://tampermonkey.net/
// @version      0.3.1
// @author       Muhun Kim
// @match        https://elearning.jejunu.ac.kr/
// @match        http://elearning.jejunu.ac.kr/
// @grant        localStorage.getItem
// ==/UserScript==

;(() => {
  'use strict'
  window.onload = () => {
    const userForm = document.querySelector('frame[name="main"]')
      .contentDocument.userForm

    if (userForm !== undefined) {
      const formBind = userForm.querySelector.bind(userForm)
      formBind('input#id').value = localStorage.getItem('student_no')
      formBind('input#pw').value = localStorage.getItem('student_pw')
      formBind('.loginBtn').click()
    }
  }
})()
