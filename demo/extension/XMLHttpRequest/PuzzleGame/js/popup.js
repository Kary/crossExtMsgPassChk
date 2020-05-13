'use strict';

// Logical Grid
let logGrid = {
	"c11": 0, "c12": 0, "c13": 0, "c14": 0, "c15": 0,
	"c21": 0, "c22": 0, "c23": 0, "c24": 0, "c25": 0,
	"c31": 0, "c32": 0, "c33": 0, "c34": 0, "c35": 0,
	"c41": 0, "c42": 0, "c43": 0, "c44": 0, "c45": 0,
	"c51": 0, "c52": 0, "c53": 0, "c54": 0, "c55": 0
};

let currentScore = 0;

const bgpage = chrome.extension.getBackgroundPage();

let	playerName = bgpage.getPlayerName();
const playerId = bgpage.getPlayerId();

main();


function main() {

	// 01. New Game
	newGame();
	showHighestScore();

	// 02. Add Event Listener for Keyboard
	document.addEventListener("keydown", function(event) {
		if (event.code == "KeyW" || event.code == "KeyA" || event.code == "KeyS" || event.code == "KeyD" || event.code == "ArrowUp" || event.code == "ArrowLeft" || event.code == "ArrowDown" || event.code == "ArrowRight") {

			if (event.code == "KeyW" || event.code == "ArrowUp") {
				goUp();
			} else if (event.code == "KeyA" || event.code == "ArrowLeft") {
				goLeft();
			} else if (event.code == "KeyS" || event.code == "ArrowDown") {
				goDown();
			} else if (event.code == "KeyD" || event.code == "ArrowRight") {
				goRight();
			}

			if (!checkIfGameOver()) {
				genNum();
			} else {
				alert("Game Over");

				// 03. Get Player Name
				if (playerName == null || playerName == "" || playerName == "Dummy") {
					playerName = window.prompt("Please enter your name", "");

					if (playerName == null || playerName == "" || playerName == "Dummy") {
						alert('Player Name is mandatory for submitting score');
					} else {
						postSubmitScore(currentScore);
					}
				} else {
					postSubmitScore(currentScore);
				}
				newGame();
			}
		}
	});

	// 04. Add Event Listener for newGameButton
	let newGameButton = document.getElementById("newGameButton");
	newGameButton.addEventListener("click", function() { newGame(); }, false);	
} // function main()


function showHighestScore() {
	let xhr = new XMLHttpRequest();
	let url = "https://puzzlegame.com:8443/highestscore";
	xhr.open("GET", url);
	xhr.responseType = "document";
	xhr.send();

	xhr.onreadystatechange = function() {
		if ((xhr.readyState == 4) && (xhr.status == 200)) {
		    let dom = xhr.response;
		    let pname = dom.getElementById("highestscore").rows[1].cells[0].innerHTML;
		    let pscore = dom.getElementById("highestscore").rows[1].cells[1].innerHTML;

			document.getElementById("highestScore").innerHTML = pscore.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + " (" + pname + ")";
		}
	}
} // function showHighestScore()


function postSubmitScore(score) {
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
			let payload = "csrf_token=" + csrf_token + "&pid=" + playerId + "&name=" + playerName + "&score=" + score.toString() + "&submit=Submit";	
		    
		    xhr.open("POST", url);
		    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		    xhr.onreadystatechange = function() { // POST
				if (xhr.readyState == 4) {
		  			showHighestScore();
		  		}
			}
			xhr.send(payload);
		}
	}
} // function postSubmitScore()