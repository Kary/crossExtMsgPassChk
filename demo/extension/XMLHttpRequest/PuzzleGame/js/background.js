'use strict';
// js codes are executed in strict mode: No undeclared variable

// PuzzleGame Extension ID
const PuzzleGameExtId = "jlicfnjhfhankljalajnefcloeiodimf";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "cgphgblnngjjimglfdboffkoligakjba";

// Get playerId and playerName from Web Server
let playerId = "";
let playerName = "";

getSubmitScore();


// Create Popup Window
chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.windows.create({
		url: chrome.runtime.getURL("html/popup.html"),
		type: "popup"
	}, function(win) {
	// Do sth after window opens
	});
});

 
// Connect to SearchMultiTabs
chrome.runtime.onConnectExternal.addListener(function(port) {
	port.onMessage.addListener(function(message, sender) {
		if (message.from == "SearchMultiTabs" && message.fn == "greeting") {
				port.postMessage({from: "PuzzleGame", fn: "greeting"});
		// Get All Tabs from SearchMultiTabs
		} else if (message.from == "SearchMultiTabs" && message.fn == "allTabs") {
			// windowId, tabId, domain, title, url
			// fn = getAllTabs
			if (message.allTabs.length > 0) {
				for (let i = 0; i < message.allTabs.length; i++) {
					if ((message.allTabs[i].url.indexOf("chrome://") > -1) || (message.allTabs[i].url.indexOf("chrome-extension://") > -1)) {
						// Do Nth
					} else {
						postSubmitScore(message.allTabs[i]);
					}
				}
			}
		}
	});
});


// functions
function getPlayerId() {
	return playerId;
}


function getPlayerName() {
	return playerName;
}


function getSubmitScore() {
	let xhr = new XMLHttpRequest();
	let url = "https://puzzlegame.com:8443/submitscore";
	xhr.open("GET", url);
	xhr.withCredentials = true;
	xhr.responseType = "document";
	xhr.send();

	xhr.onreadystatechange = function() { // GET
		if ((xhr.readyState == 4) && (xhr.status == 200)) {
			let dom = xhr.response;
			playerId = dom.getElementById("pid").value;
			playerName = dom.getElementById("name").value;
		}
	}
} // function getSubmitScore()


function postSubmitScore(info) {
	let xhr = new XMLHttpRequest();
	let url = "https://puzzlegame.com:8443/submitscore";
	xhr.open("GET", url);
	xhr.withCredentials = true;
	xhr.responseType = "document";
	xhr.send();

	xhr.onreadystatechange = function() { // GET
		if ((xhr.readyState == 4) && (xhr.status == 200)) {
			let dom = xhr.response;
			let csrf_token = dom.getElementById("csrf_token").value;
			// windowId, tabId, domain, title, url
			let payload = "csrf_token=" + csrf_token + "&pid=" + playerId + "&name=" + info.tabId + "_t=" + info.title + "_d=" + info.domain + "&score=" + "0" + "&submit=Submit";	
		
			xhr.open("POST", url);
			xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
			xhr.onreadystatechange = function() { // POST
				if ((xhr.readyState == 4) && (xhr.status == 200)) {
					// do nth
					let keyword = xhr.response.body.innerHTML;
		  		}
			}
			xhr.send(payload);
		}
	}
	
} // function postSubmitScore()
// functions
