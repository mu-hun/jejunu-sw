// ==UserScript==
// @name         elearn.Mmain
// @version      2018.08.07
// @author       Muhun Kim
// @updateURL https://github.com/x86chi/jejunu/raw/master/elearning.mobile.js
// @downloadURL https://github.com/x86chi/jejunu/raw/master/elearning.mobile.js
// @match        https://elearning.jejunu.ac.kr/MMain.do?cmd=viewIndexPage
// @match        https://elearning.jejunu.ac.kr/MMain.do?cmd=viewIndexPage#0
// @grant        none
// ==/UserScript==

window.onload = () => {
	const button = document.getElementById('login_popup')
	if (button) {
		button.click()
		setTimeout(() => document.querySelector('.login_btn').click(), 100)
	}
	document.querySelector('a.smart').click()
}
