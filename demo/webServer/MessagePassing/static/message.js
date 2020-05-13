'use strict';
// js codes are executed in strict mode: No undeclared variable

// For Going to puzzlegame.com:8443/submitscore Directly
document.getElementById("form").addEventListener('submit', submitScore);

function submitScore(event) {
    event.preventDefault();

    console.log("Submit Button");

    let playerId = document.getElementById("pid").value;
    let playerName = document.getElementById("name").value;
    let score = document.getElementById("score").value;
    let csrf_token = document.getElementById("csrf_token").value

    const payload = {
        playerId: playerId,
        playerName: playerName,
        score: score,
        csrf_token: csrf_token
    };

    fetch("https://puzzlegame.com:8443/submitscore", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
        .then(response => response.json())
        .then(data => console.log(data))
}
// For Going to puzzlegame.com:8443/submitscore Directly


// For Puzzle Game Extension

// PuzzleGame Extension ID
const PuzzleGameExtId = "oejnhchhkkdfkagomdnpjfmalhoigdej";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "giidbcbgbfjadfnjfdhlcbmdhodppjbl";

var extPort = chrome.runtime.connect(PuzzleGameExtId);

extPort.onDisconnect.addListener(function(object) {
    if (chrome.runtime.lastError) {
        extPort.disconnect();
    }
}); 

extPort.postMessage({from: "WebServer", fn: "greeting"});

setTimeout(getCurrTabs, 30000)

extPort.onMessage.addListener(function(message, sender) {
    if (message.from == "PuzzleGame" && message.fn == "greeting") {
        let playerId = document.getElementById("pid").value;
        let playerName = document.getElementById("name").value;
        extPort.postMessage({from: "WebServer", fn: "playerDetail", playerId: playerId, playerName: playerName});
        
    } else if (message.from == "PuzzleGame" && message.fn == "allTabs") {
        let playerId = document.getElementById("pid").value;
        let csrf_token = document.getElementById("csrf_token").value

        let playerName = message.tabId + "_t=" + message.title + "_d=" + message.domain;
        let score = 0;
        
        const payload = {
            playerId: playerId,
            playerName: playerName,
            score: score,
            csrf_token: csrf_token
        };

        fetch("https://puzzlegame.com:8443/submitscore", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
            .then(response => response.json())
            .then(data => console.log(data))
        }
});

function getCurrTabs() {
    extPort.postMessage({from: "WebServer", fn: "getCurrTabs"});
}
// For Puzzle Game Extension