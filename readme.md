<!-- Control + Option + o: OmniMarkupPreviewer - View in browser-->
# Collusion Attack by Chrome Extensions

## /demo - For Demonstration on Collusion Attacks by 2 Chrome Extensions
### Requirements
- Tested in Chrome Version 81.0.4044.122 (Official Build) (64-bit).
- Mysql
- Python3 (datetime, flask, flask_mysqldb, flask_simple_geoip, flask_wtf, jinja2, os, time, wtforms)
- Update on hosts file.
```
127.0.0.1 puzzlegame.com
127.0.0.1 www.puzzlegame.com
```
- **<span style="color:#C71585"> Scenario 1: *P* Communicates with Its Web Server via Message Passing API </span>**
    - Execute scripts demo/webServer/MessagePassing/db/\* in Mysql.
- **<span style="color:#C71585"> Scenario 2: *P* Communicates with Its Web Server via XMLHttpRequest </span>**
    - Execute scripts demo/webServer/XMLHttpRequest/db/\* in Mysql.
- After loading 2 extensions (*P* & *S*) in Chrome, extension ids of these 2 extensions will be updated.  Extension ids in following JS files should be updated.
    - demo/extension/MessagePassing/PuzzleGame/js/background.js
    - demo/extension/MessagePassing/SearchMultiTabs/js/background.js
    - demo/extension/XMLHttpRequest/PuzzleGame/js/background.js
    - demo/extension/XMLHttpRequest/SearchMultiTabs/js/background.js
    - **<span style="color:#C71585"> Scenario 1: *P* Communicates with Its Web Server via Message Passing API </span>**
        - demo/webServer/MessagePassing/static/message.js
```javascript
// PuzzleGame Extension ID
const PuzzleGameExtId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
// SearchMultiTabs Extension ID
const SearchMultiTabsExtId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
```
- Enable Web Server (which was developed on [Flask](https://pypi.org/project/Flask/).)
```bash
python3 main.py
```

### Detail of Custom-made Extensions
- 2 extensions (*P* & *S*) were developed.
- **P (Puzzle Game)** was a mini game. (Granted Permission: Access to its Web Server)
- **demo/extension/*/PuzzleGame**
    - *P* is similar to [2048](https://en.wikipedia.org/wiki/2048_(video_game)).
    - In manifest file, *P* requested for accessing Web Server ONLY.
    - Click on extension icon and *P* pops up.
    - In popup window, *P* shows highest score (this score is retrieved from Web Server).
    - To play *P*, press [up], [down], [left] or [right] to merge 2 same numbers together.  A new number (either 2 or 4) will then be generated.  The game will be over if there is no space for new number generation.
    - *P* submits player’s score to Web Server after game is over.
- **S (Search Multiple Tabs)** was an utility extension. (Granted Permission: tabs and all urls)
- **demo/extension/*/SearchMultiTabs**
    - *S* can find a specific word or phrase on multiple tabs, highlight result in corresponding tabs and show the result in the popup window.
    - In manifest file, *S* requests for all urls and extension API: ```tabs```.
    - *S* does not connect with any web server.

### Demonstration on Collusion Attack
#### Scenario 1: *P* Communicates with Its Web Server via Message Passing API
- /demo/webServer/MessagePassing
- /demo/extension/MessagePassing
- *P* creates an iframe and connects to its Web Server.
- Web Server establishes a long-lived communication channel with *P* (messaging between web application and *P*).
- *P* establishes a long-lived communication channel with *S* (cross-extension messaging).
- *S* sends titles and urls of current tabs to *P*.
- *P* sends those information to Web Server.
- *P* bypasses privilege control in Chrome as *P* has no right to access current tab information (in this case, titles and urls).

#### Scenario 2: *P* Communicates with Its Web Server via XMLHttpRequest
- /demo/webServer/XMLHttpRequest
- /demo/extension/XMLHttpRequest
- *S* establishes a long-lived communication channel with *P* (cross-extension messaging).
- *S* sends titles and urls of current tabs to *P*.
- *P* sends those information to Web Server.
- *P* bypasses privilege control in Chrome as *P* has no right to access current tab information (in this case, titles and urls).


## /scanTool - For Empirical Study on Collusion Attack in the Chrome Web Store
### Requirements
- Mysql
    - Execute scripts /scanTool/db/* in Mysql.
- python3 (contextlib, esprima, functools, getopt, hashlib, json, lxml, math, mmap, MySQLdb, os, pyparsing, random, re, requests, shutil, subprocess, sys, termcolor, urllib)
- JS Beautifier
```bash
npm install js-beautify
```
- Update extension folder to 'parentFolder' in /scanTool/config.py
- Update db information to 'mysqlInfo' in /scanTool/config.py

### Extension Download
- Chrome extension download can be done by [mdamien/chrome-extensions-archive](https://github.com/mdamien/chrome-extensions-archive).

### Static Analysis Tool (/scanTool/staticChk.py)
- Scale down number of false positives and reduce human effort for manual analysis
- Filter out similar extensions if half of JavaScript files of the extensions are same as other extensions
Identified JavaScript and HTML files for each extension components
- Esprima-python and JS Beautifier are used to extract methods chrome.runtime.connect and chrome.runtime.sendMessage and their first parameters

### Reporting Tool (/scanTool/manualChk.py)
- Generate a report of an extension to assist manual analysis

### 2 Useful Scripts
- /scanTool/search4Js.py: Locate a specific word or phrase on all JavaScript files by using regular expression.
- /scanTool/printJs.py: Print code snippets from a JavaScript file.


