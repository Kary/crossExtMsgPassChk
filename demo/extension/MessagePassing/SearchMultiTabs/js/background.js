'use strict';
// js codes are executed in strict mode: No undeclared variable

// PuzzleGame Extension ID
const PuzzleGameExtId = "oejnhchhkkdfkagomdnpjfmalhoigdej";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "giidbcbgbfjadfnjfdhlcbmdhodppjbl";

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
chrome.runtime.onConnectExternal.addListener(function(extPort) {
    extPort.onMessage.addListener(function(message, sender) {
        if (message.from == "PuzzleGame" && message.fn == "greeting") {
            getAllTabs().then(function(tabs) {
                if (tabs != []) {
                    extPort.postMessage({from: "SearchMultiTabs", fn: "allTabs", allTabs: tabs});
                }
            });
        }
    });
});

// function
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


function searchResult(popupTabId, searchResult) {
    let popupTab = chrome.extension.getViews({tabId: Number(popupTabId)})[0];
    popupTab.displaySearchResult(searchResult);
}

// function
