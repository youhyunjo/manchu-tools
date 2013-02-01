Notepad++ PythonScripts
================================

프로젝트를 위해 Notepad++에 Python Script를 이용한 추가 기능을 제공하고 있습니다.

PythonScript 설치
--------------------------------

우선 다음과 같이 준비가 되어 있어야 추가 기능을 사용할 수 있습니다.

* 메뉴에서 "플러그인 > Plugin Manager > Show Plugin Manager"를 선택하세요. 
* "Available" 탭의 목록 중에서 "Python Script"를 선택하고 "Install" 버튼을 누르세요.

이것으로 추가 기능을 사용할 수 있는 기본적인 준비가 되었습니다. 개별 기능은
별로로 설치해야 합니다.

추가 기능 목록
--------------------------------

* 만주 관리자: [manchu-manager.py](manchu-manager.py)
* 만영 사전 검색: [manchu-dic.py](manchu-dic.py). 사전 파일은 저작권 문제로 공개하지 않습니다.
* 만한 정렬 형식 검사: [manchu-validate-align.py](manchu-validate-align.py)


설치 방법
--------------------------------

만주 관리자 `manchu-manager.py`를 다운받아 Notepad++ Python Script 폴더에
넣으시면 됩니다. 다른 추가 기능들은 만주 관리자를 통해 자동으로 설치하고
업데이트할 수 있습니다.

### 다운로드

다음 링크를 이용하여 `manchu-manager.py`를 다운로드합니다.

* [manchu-manager.py](https://raw.github.com/youhyunjo/manchu-tools/master/notepad++/PythonScripts/manchu-manager.py)


### 설치할 폴더 찾기

* 메뉴에서 "플러그인 > Python Script > New Script"를 선택하세요. 
* 파일 저정하기 위한 창이 뜹니다. 여기에서 "저장 위치" 드롭다운 메뉴를 눌러서 폴더의 정확한 위치를 확인하세요. 경로가 굉장히 길 겁니다. 잘 기억해 두세요.
* 내 컴퓨터로 들어가서 방금 기억한 폴더를 여세요.

### 파일 넣고 Notepad++ 재실행

* 다운로드 받은 `manchu-manager.py`를 폴더에 넣으세요.
* Notepad++을 재실행하세요.
* 메뉴에서 "플러그인 > Python Script > Scripts"에 들어가 보시면 복사해서 넣은 `manchu-manager`가 추가된 것을 보실 수 있습니다.

### 만주 매니저 실행

* `manchu-manger`를 실행하시면 자동으로 새로운 플러그인, Asepll 만주어 사전 등이 설치되고 업그레이드됩니다.
* 설치가 완료되었다는 팝업창이 뜰 때까지 기다리세요.
* 경우에 따라 새로운 기능은 Notepad++을 재실행한 후에 사용할 수 있습니다.


단축키 설정
--------------------------------

플러그인을 매번 마우스로 클릭하여 실행하는 것이 불편할 경우에는 단축키를 설정할 수
있습니다. `manchu-dic.py`를 예로 들어 설명하겠습니다.


* 메뉴에서 "플러그인  > Python Script > Configuration"을 선택하세요. 
* 윗쪽 창에 manchu-dic.py가 있습니다. "manchu-dic.py"를 선택하고 "Menu items"에 "Add"버튼을 놀러서 추가해 주세요.
* 이제 메뉴에서  "플러그인 > Python Script"를 보시면 manch-dic 메뉴가 추가된 것을 보실 수 있습니다.
* Notepad++을 재실행하세요.
* 메뉴에서 "실행 > 단축키 바꾸기/명령 삭제..."을 선택하세요. 
* 설정 창이 뜨면 "Plugin commands" 버튼을 클릭하세요. 
* 목록을 쭉 아래로 내려보시면 "manchu-dic"을 찾으실 수 있습니다. 더블클릭하세요.
* 적당한 단축키를 할당하세요. 자유롭게 설정하세요. 다만 이미 다른 기능에 해당 단축키가 매핑되어 있으면 안 될 수가 있습니다. 



