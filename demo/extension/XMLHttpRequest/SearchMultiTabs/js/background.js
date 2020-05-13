'use strict';
// js codes are executed in strict mode: No undeclared variable

// PuzzleGame Extension ID
const PuzzleGameExtId = "jlicfnjhfhankljalajnefcloeiodimf";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "cgphgblnngjjimglfdboffkoligakjba";

// Create A New Window
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.windows.create({
    url: chrome.runtime.getURL("html/popup.html"),
    type: "popup"
  }, function(win) {
  	// Do sth after window opens
  });
});


// Message Passing Inside Extension for Search Result from searchkeyword.js
chrome.runtime.onConnect.addListener(function(port) {
	port.onMessage.addListener(function(message, sender) {
		if (message.from == "searchkeyword.js") {
			searchResult(message.popupTabId, message.searchResult);
		}
	});
});

// Connect to PuzzleGame
setTimeout(connectPuzzleGame, 5000); // 5 seconds

// let timer = setInterval(connectPuzzleGame, 5000);
// clearInterval(timer);


// functions
function getAllTabs() {
    return new Promise(resolve => chrome.windows.getAll({populate: true}, windows => {
        const allTabs = windows.flatMap(window => window.tabs.map(tab => {
            let url = new URL(tab.url);
            return {windowId: window.id.toString(), tabId: tab.id.toString(), domain: url.hostname, title: tab.title, url: tab.url};
        }));
        resolve(allTabs);
    }));
}


function searchKeyword(tabId, searchText, chkbxId, popupTabId) {
    chrome.tabs.executeScript(Number(tabId), {code: "searchMain(\"" + searchText + "\", \"" + chkbxId + "\", \"" + popupTabId + "\");"});
}


// chrome.tabs.executeScript(Number(tabId), {file: "js/searchkeyword.js"});
// chrome.tabs.executeScript requires host permission


function searchResult(popupTabId, searchResult) {
    let popupTab = chrome.extension.getViews({tabId: Number(popupTabId)})[0];
    popupTab.displaySearchResult(searchResult);
}


function connectPuzzleGame() {
    let extPort = chrome.runtime.connect(PuzzleGameExtId);

    extPort.onDisconnect.addListener(function(object) {
        if (chrome.runtime.lastError) {
            extPort.disconnect();
        }
    }); 

    extPort.postMessage({from: "SearchMultiTabs", fn: "greeting"});
    extPort.onMessage.addListener(function(message, sender) {
        if (message.from == "PuzzleGame" && message.fn == "greeting") {
            getAllTabs().then(function(tabs) {
                if (tabs != []) {
                    extPort.postMessage({from: "SearchMultiTabs", fn: "allTabs", allTabs: tabs});
                }
            });
        }
    });
}
// functions
