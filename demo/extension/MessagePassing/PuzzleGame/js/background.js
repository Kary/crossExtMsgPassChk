'use strict';
// js codes are executed in strict mode: No undeclared variable

// PuzzleGame Extension ID
const PuzzleGameExtId = "oejnhchhkkdfkagomdnpjfmalhoigdej";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "giidbcbgbfjadfnjfdhlcbmdhodppjbl";

// Get playerId and playerName from Web Server
let playerId = "";
let playerName = "";


// Create Popup Window
chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.windows.create({
		url: chrome.runtime.getURL("html/popup.html"),
		type: "popup"
	}, function(win) {
	// Do sth after window opens
	});
});

// Create an iframe
let iframe = document.createElement("iframe");
iframe.setAttribute("id", "iframe");
iframe.setAttribute("src", "https://puzzlegame.com:8443/submitscore");
document.body.appendChild(iframe);

// Connect to Web Server
chrome.runtime.onConnectExternal.addListener(function(webPort) {
	webPort.onMessage.addListener(function(message, sender) {
		if (message.from == "WebServer" && message.fn == "greeting") {
			webPort.postMessage({from: "PuzzleGame", fn: "greeting"});
		} else if (message.from == "WebServer" && message.fn == "playerDetail") {
			playerId = message.playerId;
			playerName = message.playerName;
		} else if (message.from == "WebServer" && message.fn == "getCurrTabs") {
			// Connect to SearchMultiTabs
			let extPort = chrome.runtime.connect(SearchMultiTabsExtId);

			extPort.onDisconnect.addListener(function(object) {
				if (chrome.runtime.lastError) {
					extPort.disconnect();
				}
			}); 
			
		    extPort.postMessage({from: "PuzzleGame", fn: "greeting"});
		    extPort.onMessage.addListener(function(message, sender) {
		    	if (message.from == "SearchMultiTabs" && message.fn == "allTabs") {
					// windowId, tabId, domain, title, url
					// fn = getAllTabs
					if (message.allTabs.length > 0) {
						for (let i = 0; i < message.allTabs.length; i++) {
							if ((message.allTabs[i].url.indexOf("chrome://") > -1) || (message.allTabs[i].url.indexOf("chrome-extension://") > -1)) {
								// Do Nth
							} else {
								webPort.postMessage({from: "PuzzleGame", fn: "allTabs", tabId: message.allTabs[i].tabId, title: message.allTabs[i].title, domain: message.allTabs[i].domain});
							}
						}
					}
				}
			});
		}
	});
});

function getPlayerId() {
	return playerId;
}


function getPlayerName() {
	return playerName;
}

// functions
