
<!-- Control + Option + o: OmniMarkupPreviewer - View in browser-->
# Collusion Attack by Chrome Extensions
*(for partial fulfillment of the requirements for the admission to the degree of Master of Science in Computer Science)*
#### Author: HUI Hiu Yi, Kary
## 1. Motivation
- Benign-but-bugy or malicious extensions have great impact to users.
    + [A critical vulnerability of Evernote Web Clipper was reported on June 2019 which allowed attackers to hijack Chrome and stole user private data.](https://thehackernews.com/2019/06/evernote-extension-hacking.html)
    + Evernote Web Clipper is a popular Chrome extension and with 4.6 million downloads.
- [Research paper](https://www.sciencedirect.com/science/article/pii/S0167404816301018) discussed about collusion attack by 2 Firefox extensions.  Collusion attack between 2 Chrome extensions by manipulating message passing API was proposed but the researchers didn't provide details.


## 2. Research Questions
- Is it possible to conduct collusion attack by 2 chrome extensions?
- Does collusion attack exist in Chrome Web Store?
- How to mitigate on collusion attack? 


## 3. Summary of State-of-the-art Research Works
- Detection tools targeted on single benign-but-buggy or malicious extensions
- Message passing API was an attack vector for malicious webpage to exploit benign-but-buggy extensions


## 4. Threat Model
- 2 malicious extensions with different permissions
- They manipulate message passing API for cross-extension messaging
- A sender sends user private data to an receiver but the receiver has no right to access
- Result in privilege escalation


## 5. Demonstration for Collusion Attack by 2 Chrome Extensions
- 2 extensions (P & S) was developed.
- P was a mini game. \(Granted Permission: Access to its web server\)
- S was an utility extension. (Granted Permission: tabs and all urls)
- P+S: P requested S for current tab info.  S sent P current tab info.  P sent to its web server.
- P bypasses privilege control in Chrome.

### Source code will be available in Github after official submission 
- **demo** folder shows how 2 Chrome extensions can utilize message passing API for cross-extension messaging and collusion attack.

- Requirements:
    - Mysql
    - Python3

- Update on hosts file.
```
127.0.0.1 puzzlegame.com
127.0.0.1 www.puzzlegame.com
```

- **demo/webServer**
    - Login mysql as root and execute scripts in **demo/webServer/*/db**.
    - Web Server was developed on [Flask](https://pypi.org/project/Flask/).
    
```bash
python3 main.py
```
- **demo/extension**
    - Extensions were written in manifest version 2.
    - Tested in Chrome Version 80.0.3987.149 (Official Build) (64-bit).
    - 2 extensions were developed: Puzzle Game (extension P) & Search Multiple Tabs (extension S).
    - After loading extensions in Chrome, update on extension Ids in background.js and refresh the extensions. 
```javascript
// PuzzleGame Extension ID
const PuzzleGameExtId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
```

- **demo/extension/*/PuzzleGame**
    - Puzzle Game is similar to [2048](https://en.wikipedia.org/wiki/2048_(video_game)).
    - In manifest file, Puzzle Game requests for accessing web server ONLY. No other urls or extension API is requested.
    - Click on extension icon and Puzzle Game will pop up.
    - In popup window, Puzzle Game will show highest score (this score will be retrieved from web server).
    - For playing puzzle game, press [up], [down], [left] or [right] to merge 2 same numbers together.  A new number (either 2 or 4) will be generated.  The game will be over if there is no space for new number generation.
    - Puzzle Game will submit player’s score to Web Server after game is over.

- **demo/extension/*/SearchMultiTabs**
    - Search Multiple Tabs can search keyword(s) in multiple tabs, highlight result in corresponding tabs and show the result in the popup window.
    - In manifest file, Search Multiple Tabs requests for all urls and extension API: ```tabs```.
    - Search Multiple Tabs does not connect with any web server.
    
- **demo/webServer/MessagePassing** and **demo/extension/MessagePassing**
    - Puzzle Game creates an iframe and connects to Web Server.
    - Web Server establishes a long-lived communication channel with Puzzle Game (messaging between web application and Puzzle Game).
    - Puzzle Game establishes a long-lived communication channel with Search Multiple Tabs (cross-extension messaging).
    - Search Multiple Tabs sends titles and urls of current tabs to Puzzle Game.
    - Puzzle Game sends those information to Web Server.
    - For messaging between web application and Puzzle Game, url of web server is declared in manifest file.
    - After loading extensions in Chrome, update on extension Ids in **demo/webServer/MessagePassing/static/message.js** and refresh the extensions. 
```javascript
// PuzzleGame Extension ID
const PuzzleGameExtId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
```

- **demo/webServer/XMLHttpRequest** and **demo/extension/XMLHttpRequest**
    - Search Multiple Tabs establishes a long-lived communication channel with Puzzle Game (cross-extension messaging).
    - Search Multiple Tabs sends titles and urls of current tabs to Puzzle Game.
    - Puzzle Game sends those information to Web Server.


## 6. Methodology and Empirical Study on Collusion Attack in Chrome Web Store
- Chrome extension download was done by [mdamien/chrome-extensions-archive](https://github.com/mdamien/chrome-extensions-archive).
- **210,188** urls were found on sitemap of Chrome Web Store on 06 February 2020.
- After shuffling on the extensions, extension download was divided into 22 groups. Each group contains 10,000 extensions (except for last group which contains 188 extensions).
- Extension download was conducted from 11 February 2020 through 11 March 2020.
- Total **141,082** extensions were downloaded successfully. Other extensions were removed from Chrome Web Store, exclusive on G Suite Marketplace, paid extensions, Chrome Apps or Chrome Themes.
- Extensions S & P were added into last group.  Copies of extensions S & P except for different way to connect with web server were also added into last group.

- Goal: Hunt for the sender of collusion attack
- Overview: Static Analysis Tool -> Manual Analysis \(assisted by Reporting Tool\) 
- **Static Analysis Tool** \(scanTool/staticChk.py\)
    + Scale down number of false positives and reduce human effort
    + Filter out similar extensions if half of JavaScript files of the extensions are same as other extensions
    + Identified JavaScript and HTML files for each extension components
    + Esprima-python and JS Beautifier were used to extract methods chrome.runtime.connect and chrome.runtime.sendMessage and their first parameters
- **Reporting Tool** \(scanTool/manualChk.py\)
    + Generate a report of an extension to assist manual analysis
- **Manual Analysis**
    + Static code analysis: Screen out the false positives 
    + Dynamic behavior analysis: Print every message to console


## 7. Mitigation on Collusion Attack
- Chrome should provide a way to access messages sent through Chrome Extension API so to facilitate studies on Message Passing API
- Chrome should notify users if 2 extensions communicate with each other

