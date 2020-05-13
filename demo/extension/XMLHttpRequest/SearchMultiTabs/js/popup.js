'use strict';

// Permissions: tabs
// The majority of the chrome.tabs API can be used without declaring any permission. 
// However, the "tabs" permission is required in order to populate the 
// ** url, pendingUrl, title, and favIconUrl ** properties of Tab.

let popupTab = new Promise (function(resolve, reject) {
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		resolve(tabs[0]);
	});
});

let popupTabId = "";
let popupWinId = "";

popupTab.then(function(tab) {
	popupTabId = tab.id;
	popupWinId = tab.windowId;
});

main();


function main() {
	
	const bgpage = chrome.extension.getBackgroundPage();
	const allTabs = bgpage.getAllTabs();

	// 01. Display Tabs
	allTabs.then(function(tabs) {
		tabs.forEach(displayTabs);
	});
	
	
	// 02. Search Button
	searchButton(bgpage)


	// 05. Reset Button
	resetButton()
}


function searchButton(bgpage) {

	const searchButton = document.getElementById("searchButton");
	searchButton.addEventListener("click", function() {
		if ((document.getElementById("resultList") != null) && (document.getElementsByTagName("li") != null)) {
			// remove
			document.getElementById("resultList").remove();

			// Create resultList
			let ol = document.createElement("ol");
			ol.setAttribute("id", "resultList");
			document.body.appendChild(ol);

		} else if (document.getElementById("resultList") == null) {
			// Create resultList
			let ol = document.createElement("ol");
			ol.setAttribute("id", "resultList");
			document.body.appendChild(ol);
		}

		const searchText = document.getElementById("searchText").value;
		if (searchText) {
			const chkbxes = document.getElementsByName("chkbx");

			// 1 - 3 Tabs
			if ((document.querySelectorAll('.chkbx:checked').length > 0) && (document.querySelectorAll('.chkbx:checked').length < 4)){
				// Get Selected Tabs
				for (let i = 0; i < chkbxes.length; i++) {
					if (chkbxes[i].checked) {
						// chkbxes[i].value;
						// chkbx_window.id_tab.id
						// windowId: chkbxValue[1]
						// tabId: chkbxValue[2]
						let chkbxId = chkbxes[i].value;
						let chkbxValue = chkbxId.toString().split("_");

						bgpage.searchKeyword(chkbxValue[2], searchText, chkbxId, popupTabId);
					}
				}
				
			} else {
				alert ("Select 1 - 3 Tabs");
			}
			
		} else {
			alert ("Input Keywords for Search");
		}

	}, false);
}


function displaySearchResult(searchResult) {
	let ol = document.getElementById("resultList");

	// Add items
	searchResult.forEach(function(item) {
		let li = document.createElement("li");
	
		let tabNameSpan = document.createElement("span");
		tabNameSpan.style.fontStyle = "italic";
		tabNameSpan.style.fontWeight = "bold";

		let chkbx = document.getElementById(item.chkbxId);
		let chkbxTitle = chkbx.nextSibling.innerHTML;
		let tabNameTextNode = document.createTextNode(chkbxTitle);
		tabNameSpan.appendChild(tabNameTextNode);
		
		let spaceSpan = document.createElement("span");
		let spaceTextNode = document.createTextNode("\xa0\xa0\xa0\xa0\xa0\xa0\xa0");
		spaceSpan.appendChild(spaceTextNode);

		let resultSpan = document.createElement("span");
		let resultTextNode = document.createTextNode(item.content);
		resultSpan.appendChild(resultTextNode);

		li.appendChild(tabNameSpan);
		li.appendChild(spaceSpan);
		li.appendChild(resultSpan);
		ol.appendChild(li);
	});	
}


function displayTabs(tab) {
	if ((tab.url.indexOf("chrome://") > -1) || (tab.url.indexOf("chrome-extension://") > -1)) {
		// Do Nth
	} else {
		// Insert Tab Records
		const searchForm = document.getElementById("searchForm");

		let chkbx = document.createElement("input");
		chkbx.setAttribute("id", "chkbx_" + tab.windowId.toString() + "_" + tab.tabId.toString());
		chkbx.setAttribute("name", "chkbx");
		chkbx.setAttribute("class", "chkbx");
		chkbx.setAttribute("value", "chkbx_" + tab.windowId.toString() + "_" + tab.tabId.toString());
		chkbx.setAttribute("type", "checkbox");
		searchForm.appendChild(chkbx);

		let title = document.createElement("span");
		title.innerHTML = tab.title;
		searchForm.appendChild(title);

		let br = document.createElement("br");
		searchForm.appendChild(br);
	}
}

function resetButton() {
	const resetButton = document.getElementById("resetButton");
	resetButton.addEventListener("click", function() {
		if ((document.getElementById("resultList") != null) && (document.getElementById("resultList") != "")) {
			document.getElementById("resultList").remove();
		}

		document.getElementById("searchText").value = "";

		const chkbxes = document.getElementsByName("chkbx");
		if (chkbxes.length > 0) {
			for (let chkbx of chkbxes) {
				chkbx.checked = false;
			}	
		}
	});
}