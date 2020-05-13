'use strict';

let searchResult = [];

function searchMain(searchText, chkbxId, popupTabId) {
	// Create a Long Lived Channel
	const port = chrome.runtime.connect({name: "searchKeyword"});

	searchResult = [];

	// HTML
	searchChildNodes(document.documentElement, searchText.toLowerCase(), chkbxId);

	// Send Back to background.js
	port.postMessage({
		from: "searchkeyword.js",
		searchResult: searchResult,
		popupTabId: popupTabId
	});

} // End of function searchMain(searchText)

function searchChildNodes(node, searchText, chkbxId) {
	if (node.hasChildNodes()) {
		for (let childNode of node.childNodes) {
			if (childNode.nodeType == 1) { // Element Node
				searchChildNodes(childNode, searchText, chkbxId);

			} else if (childNode.nodeType == 2) { // Attribute Node 
				// Ingore Attribute Node

			} else if (childNode.nodeType == 3) { // Text Node
				// console.log("Text Node: " + childNode.tagName + " " + childNode.nodeName);
				// childNode.textContent;
				// or childNode.nodeValue
				if (childNode.textContent.toLowerCase().indexOf(searchText) != -1) {
					childNode.parentNode.style.backgroundColor = "yellow";

					searchResult.push({chkbxId: chkbxId, content: childNode.textContent});
				} 

			} else if (childNode.nodeType == 8) { // Comment Node
				// Ingore Comment Node
				
			}
		}
	} else {
		// Do Nth
	}
}
