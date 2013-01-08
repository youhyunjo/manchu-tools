Image Tools
================================

* 현재 확보하고 있는 사진 촬영 또는 스캔한 원문 이미지 파일은 대개 JPEG 파일이다. 
* 이미지 상태에 따라 흑백으로 변환하거나 회색조로 변환하면 파일 크기는 상당히 줄어들고 품질은 전혀 변화없는 경우가 있다.
* PDF 또는 DjVu 파일로 변환하여 한 문헌을 하나의 파일로 묶고 목차를 넣는 것이 좋다.
* PDF에 비해 DjVu가 더 작은 파일을 생성한다.

이미지 변환
--------------------------------

이미지 파일을 변환에는 ImageMagick을 사용하는 것이 편리하다. 

* [http://www.imagemagick.org/](http://www.imagemagick.org/)

JPEG 파일을 흑백 PBM 파일로 변환

    $ convert page001.jpg page001.pbm



DjVu 도구
--------------------------------

DjVu 파일을 처리하는 데는 DjVuLibre 툴킷을 사용하는 것이 편리하다. 

* [http://djvu.sourceforge.net/](http://djvu.sourceforge.net/)

흑백 PBM 파일을  DjVu로 변환할 때 압축율이 매우 좋다. 하나씩 파일을 변환해야한다. 결과로 한 페이지짜리 djvu 파일이 생긴다. 기본 해상도는 300dpi이다. 옵션을 이용해 조절할 수 있다.

    $ cjb2 page001.pbm 001.djvu

이렇게 여러 개의 한 페이지짜리  djvu 파일을 생성한 후에 이들을 하나의 djvu 파일로 합친다. 다음 명령으로 page001.djvu, page002.djvu, page003.djvu를 합쳐서 all.djvu를 만들 수 있다.

    $ djvm -c all.djvu page001.djvu page002.djvu page003.djvu

파일이 합쳐졌지만 문제가 있을 수 있다. 뷰어로 열어보았을 때 일부 페이지에서 에러가 나는 경우가 있다. 다음 명령으로 문제 해결 (정확한 이유 파악 못함)

    $ djvmcvt all.djvu all2.djvu


### Outline 넣기

djvused를 이용하여 책갈피를 넣을 수 있다. 우선 다음과 같이 책갈피를 담은 파일을 만든다. 페이지 번호에는 #을 접두사로 붙인다. 아래 예에서 볼 수 있듯이 계층적인 구조도 가능하다.

    (bookmarks
            ("凡例" "#2")
            ("目錄" "#3")
            ("卷1" "#8"
                    ("天部" "#8")
                    ("時令部" "#16")
                    ("地部" "#24")
            )
            ("卷2" "#33"
                    ("帝王部" "#33")
                    ("諭旨部" "#35")
                    ("設官部" "#40")
                    ("政部上" "#58")
            )
    )

위 파일을 bookmarks.txt라고 하고 hancing.djvu 파일에 위 책갈피를 추가하고 싶다면 다음과 같이 한다.

    $ djvused -e 'set-outline bookmarks.txt' hancing.djvu

### Thumbnail 넣기

DjVu 파일을 뷰어에서 열었을 때 Thumbnail이 로딩되느라 시간이 지연되는 경우가 있다. 미리 thumbnail을 만들어 넣어놓으면 이런 지연을 피할 수 있다. 크기는 48에서 128픽셀로 하는 것이 일반적이다. hancing.djvu 파일이 128 픽셀 크기의 thumbnail을 추가하고 싶다면 다음처럼 한다.

    $ djvused -e 'set-thumbnails 128' hancing.djvu


PDF 도구
--------------------------------

PDF 파일은 pdftk를 이용하여 처리하는 것이 편리하다. 단순한 분리, 통합 등이 편리하다.

* [http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/](http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)

좀더 복잡한 처리에는 pdfrecycle도 유용하다.

* [http://www.florian-diesch.de/software/pdfrecycle/](http://www.florian-diesch.de/software/pdfrecycle/)


### PdfToDjVuGUI

윈도우즈용 pdf를 djvu로 변환하는 프로그램

* http://www.trustfm.net/GeneralTools/SoftwarePdfToDjvuGUI.php?b2=1에 들어가서 오른쪽 아래에서 Hotfile을 클릭합니다.
* REGULAR DOWNLOAD를 클릭하여 20초 정도 기다린 후, 새 화면에서 Click here to download를 클릭합니다.
* 다운 받은 파일의 압축을 해제하고, 변환할 pdf 파일을 PdfToDjvuGUI 폴더에 넣습니다.
* PdfToDjvuGUI 폴더 안의 Pdf To Djvu GUI를 클릭합니다.
* Pdf Input List 아래에 있는 Add PDF(s) 버튼을 클릭한 후, 나타나는 화면에서 변환할 pdf 파일을 클릭합니다. 여러 개의 파일들을 변환해야 한다면 한꺼번에 선택해도 됩니다.
* Generate DJVU 버튼을 클릭한 후 끝날 때까지(파일 크기에 따라 다를 것 같은데 118MB 짜리는 5분 정도 걸림) 기다립니다. 가능한 한 다른 작업은 하지 않는 게 좋습니다.
* 만들어진 djvu 파일은 PdfToDjvuGUI 폴더에 저장됩니다. 118MB 크기의 pdf 파일이 11.7MB 크기의 djvu 파일로 변환되었습니다.

