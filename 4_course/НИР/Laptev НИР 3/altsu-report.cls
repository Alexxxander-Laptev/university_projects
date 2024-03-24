% altsu-report.cls
% Часть материала взято из шаблона для диссертаций. https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template
% Класс для оформления отчётов
% на кафедре Вычислительной техники и электроники Алтайского государственного университета.
% Автор Шмаков Игорь Александрович.
% Первая версия от 2021-06-08.
% Версия от 2021-11-29
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{altsu-report}[2021/11/29 version 0.2 AltSU Template for CSaE Report]

%% Extreport options
\DeclareOption{14pt}{
  \PassOptionsToClass{\CurrentOption}{extreport}
}

%% Execute default options
\ExecuteOptions{14pt}

%% Process given options
\ProcessOptions\relax

% Загрузка основного класса
\LoadClass[a4paper, oneside]{extreport}

% Загрузка дополнительных пакетов и настрока команд.
% Параметры полей для страницы.
\RequirePackage{xltxtra}
\RequirePackage{tikz}
\RequirePackage{setspace}
\RequirePackage[normalem]{ulem} %https://stackoverflow.com/questions/2553392/latex-rule-filling-the-line
%%% Интервалы %%%
%% По ГОСТ Р 7.0.11-2011, пункту 5.3.6 требуется полуторный интервал
%% Реализация средствами класса (на основе setspace) ближе к типографской классике.
%% И правит сразу и в таблицах (если со звёздочкой)
%\DoubleSpacing*     % Двойной интервал
%\OnehalfSpacing*    % Полуторный интервал
%\setSpacing{1.42}   % Полуторный интервал, подобный Ворду (возможно, стоит включать вместе с предыдущей строкой)
\onehalfspacing

%%% Макет страницы %%%
% Выставляем значения полей (ГОСТ 7.0.11-2011, 5.3.7)
\RequirePackage[a4paper, left=3cm,right=1.5cm,top=2cm,bottom=2cm, nofoot, nomarginpar]{geometry} %, heightrounded, showframe
\setlength{\topskip}{0pt}   %размер дополнительного верхнего поля
\setlength{\footskip}{12.3pt} % снимет warning, согласно https://tex.stackexchange.com/a/334346

%%% Выравнивание и переносы %%%
%% http://tex.stackexchange.com/questions/241343/what-is-the-meaning-of-fussy-sloppy-emergencystretch-tolerance-hbadness
%% http://www.latex-community.org/forum/viewtopic.php?p=70342#p70342
\tolerance 1414
\hbadness 1414
\emergencystretch 1.5em % В случае проблем регулировать в первую очередь
\hfuzz 0.3pt
\vfuzz \hfuzz
%\raggedbottom
%\sloppy                 % Избавляемся от переполнений
\clubpenalty=10000      % Запрещаем разрыв страницы после первой строки абзаца
\widowpenalty=10000     % Запрещаем разрыв страницы после последней строки абзаца
\brokenpenalty=4991     % Ограничение на разрыв страницы, если строка заканчивается переносом

% Математические дополнения от AMS
\RequirePackage{amsthm, amsmath, amscd, amsfonts, amssymb}

\RequirePackage{hyperref}
\RequirePackage{cleveref}

\RequirePackage{polyglossia}[2014/05/21]

\setmainlanguage{russian}
\setotherlanguage{english}
\defaultfontfeatures{Ligatures={TeX},Renderer=Basic}  %% свойства шрифтов по умолчанию. Для XeTeX опцию Renderer=Basic можно не указывать, о\на необходима для LuaTeX

\setmainfont[Ligatures={TeX,Historic}]{Times New Roman} %% задаёт основной шрифт документа. 
%\setkeys{russian}{babelshorthands=true}

\setromanfont[Mapping=tex-text]{Times New Roman}
\setsansfont[Mapping=tex-text]{Courier New}
\setmonofont[Mapping=tex-text]{Arial}

\newfontfamily{\cyrillicfont}{Times New Roman}
\newfontfamily{\cyrillicfontrm}{Times New Roman}
\newfontfamily{\cyrillicfonttt}{Courier New}
\newfontfamily{\cyrillicfontsf}{Arial}

\RequirePackage{graphicx}
\RequirePackage{float}

%%% Таблицы %%%
\RequirePackage{booktabs, longtable, ltcaption, tabulary, tabu}
% Улучшенное форматирование таблиц
\RequirePackage{multirow, makecell} 

% для вертикального центрирования ячеек в tabulary
\def\zz {
  \ifx\[$\else\aftergroup\zzz\fi
}
%$ \] % <-- чиним подсветку синтаксиса в некоторых редакторах
\def\zzz {
  \setbox0\lastbox
  \dimen0\dimexpr\extrarowheight + \ht0-\dp0\relax
  \setbox0\hbox{\raise-.5\dimen0\box0}%
  \ht0=\dimexpr\ht0+\extrarowheight\relax
  \dp0=\dimexpr\dp0+\extrarowheight\relax 
  \box0
}

% Поддержка переносоустойчивых подчёркиваний и зачёркиваний
\RequirePackage{soulutf8}
% Запятая в десятичных дробях
\RequirePackage{icomma}
% Красная строка.
\RequirePackage{indentfirst}
\RequirePackage[labelsep=space]{caption}
% Пакет отвечающий за листинги.
\RequirePackage[newfloat]{minted}
\newenvironment{code}{\captionsetup{type=listing}}{}
\SetupFloatingEnvironment{listing}{name=Листинг}

%%% Счётчики %%%
% Счётчик рисунков и таблиц
\RequirePackage[figure,table]{totalcount}
% Пакет создания счётчиков на основе последнего номера подсчитываемого элемента (может требовать дважды компилировать документ)
\RequirePackage{totcount}
% Счётчик страниц, совместимый с hyperref (ссылается на номер последней страницы). Желательно ставить последним пакетом в преамбуле
\RequirePackage{totpages}

%%http://www.linux.org.ru/forum/general/6993203#comment-6994589 (используется totcount)
%\makeatletter
\def\formbytotal#1#2#3#4#5{%
  \newcount\@c
  \@c\totvalue{#1}\relax
  \newcount\@last
  \newcount\@pnul
  \@last\@c\relax
  \divide\@last 10
  \@pnul\@last\relax
  \divide\@pnul 10
  \multiply\@pnul-10
  \advance\@pnul\@last
  \multiply\@last-10
  \advance\@last\@c
  \total{#1}~#2%
  \ifnum\@pnul=1#5\else%
  \ifcase\@last#5\or#3\or#4\or#4\or#4\else#5\fi
  \fi
}
%\makeatother

\AtBeginDocument{%
  %% регистрируем счётчики в системе totcounter
  \regtotcounter{totalcount@figure}
  \regtotcounter{totalcount@table}       % Если иным способом поставить в преамбуле то ошибка в числе таблиц
  \regtotcounter{TotPages}               % Если иным способом поставить в преамбуле то ошибка в числе страниц
  \setlength{\parindent}{12.5mm}%{2.5em}                   % Абзацный отступ. Должен быть одинаковым по всему тексту и равен пяти знакам (ГОСТ Р 7.0.11-2011, 5.3.7).
}

\addto\captionsrussian{%
  %%% Переопределение именований %%%
  \renewcommand{\contentsname}{Содержание} % (ГОСТ Р 7.0.11-2011, 4)
  \renewcommand{\figurename}{Рис.} % (ГОСТ Р 7.0.11-2011, 5.3.9)
  \renewcommand{\tablename}{Таблица} % (ГОСТ Р 7.0.11-2011, 5.3.10)
  %  \renewcommand{\chaptername}{}
  \renewcommand{\listfigurename}{Список рисунков}
  \renewcommand{\listtablename}{Список таблиц}
  \renewcommand{\thechapter}{\arabic{chapter}}
  \renewcommand{\thesection}{\thechapter.\arabic{section}}
}
\renewcommand{\labelenumii}{\theenumii}
\renewcommand{\theenumii}{\theenumi.\arabic{enumii}.}
\renewcommand{\labelenumiii}{\theenumiii}
\renewcommand{\theenumiii}{\theenumi.\arabic{enumii}.\arabic{enumiii}}

%%% Оглавление %%%
\usepackage[dotinlabels]{titletoc}
\titlecontents{chapter}
              [1.5em]
              {\addvspace{\baselineskip}}
              {\contentslabel{1.5em}\hspace*{0em}}
              {}
              {\titlerule*[1pc]{.}\contentspage}

\usepackage[pagestyles]{titlesec}
\titleformat{\chapter}%
            {\centering\normalfont\bfseries}
            {\thechapter.}
            {14pt}
            {\MakeUppercase}

\titleformat{\section}%
            {\centering\normalfont\bfseries}
            {\thesection.}
            {14pt}
            {}
   
\titleformat{\subsection} % command
            [hang]                 % shape
            {\centering\bfseries\normalsize} % format
            {\thesubsection.}       % label
            {1em}                  % Spacing between label and title
            {}                     % before code
%\titlespacing{\subsection}% Set the spacing around the title
%{0pt}                  % Left
%{0pt}                  % Above
%{0pt}                  % Below
\titlespacing{\chapter}{0pt}{*0}{15pt}
\titlespacing{\section}{0pt}{10pt}{10pt}

\setlength{\parindent}{1.27cm}
\setlength{\parskip}{0cm}

% Пакет для оформления исходного кода
\usepackage{minted}

\usepackage[titles]{tocloft}
\setlength{\cftbeforechapskip}{6pt}
% Изменение отступов в содержании
\setlength{\cftsecindent}{0pt}
\setlength{\cftsubsecindent}{0pt}
\renewcommand{\cftchapdotsep}{\cftdotsep}
\renewcommand{\cftsecdotsep}{\cftdotsep}
\renewcommand\cftchapfont{\mdseries}
\renewcommand\cftchappagefont{\mdseries}
%\renewcommand{\cftsecdotsep}{\cftnodots} % Убрать точки

\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\rhead{\thepage} % номер страницы в правом верхнем углу
\renewcommand{\headrulewidth}{0pt} % без линии
\fancypagestyle{plain}{
  \fancyhf{}
  \rhead{\thepage}
  \renewcommand{\headrulewidth}{0pt}
}

\RequirePackage{csquotes}
\RequirePackage{epigraph}
\RequirePackage{enumitem} %https://tex.stackexchange.com/questions/6081/reduce-space-between-enumerated-items
\setlist{nolistsep}
%\renewcommand{\@listI}{%
%\leftmargin=25pt
%\rightmargin=0pt
%\labelsep=5pt
%\labelwidth=20pt
%\itemindent=0pt
%\listparindent=0pt
%\topsep=0pt plus 2pt minus 4pt
%\partopsep=0pt plus 1pt minus 1pt
%\parsep=0pt plus 1pt
%\itemsep=\parsep}

\RequirePackage[
  backend=biber, 
  sorting=none,
  bibstyle=gost-numeric,%gost-authoryear,
  citestyle=gost-numeric%gost-authoryear
]{biblatex}
\urlstyle{same}

%% Additional TeX/LaTeX code...
% Объявление переменных
\newcommand{\@ministry}{\#}
\newcommand{\ministry}[1]{\edef\@ministry{{#1}}}
\newcommand{\@country}{\#}
\newcommand{\country}[1]{\edef\@country{{#1}}}
\newcommand{\@fulluniversityname}{\#}
\newcommand{\fulluniversityname}[1]{\edef\@fulluniversityname{{#1}}}
\newcommand{\@institute}{\#}
\newcommand{\institute}[1]{\edef\@institute{{#1}}}
\newcommand{\@department}{\#}
\newcommand{\department}[1]{\edef\@department{{#1}}}
\newcommand{\@departmentchief}{\#}
\newcommand{\departmentchief}[1]{\edef\@departmentchief{{#1}}}
\newcommand{\@departmentchiefdegree}{\#}
\newcommand{\departmentchiefdegree}[1]{\edef\@departmentchiefdegree{{#1}}}
\newcommand{\@shortdepartment}{\#}
\newcommand{\shortdepartment}[1]{\edef\@shortdepartment{{#1}}}
\newcommand{\@supervisort}{\#}
\newcommand{\supervisor}[1]{\edef\@supervisor{{#1}}}
\newcommand{\@supervisordegree}{\#}
\newcommand{\supervisordegree}[1]{\edef\@supervisordegree{{#1}}}
\newcommand{\@ChairmanOfTheStateCertificationCommission}{\#}
\newcommand{\ChairmanOfTheStateCertificationCommission}[1]{\edef\@ChairmanOfTheStateCertificationCommission{{#1}}}
\newcommand{\@ChairmanOfTheStateCertificationCommissiondegree}{\#}
\newcommand{\ChairmanOfTheStateCertificationCommissiondegree}[1]{\edef\@ChairmanOfTheStateCertificationCommissiondegree{{#1}}}
\newcommand{\@groupnumber}{\#}
\newcommand{\groupnumber}[1]{\edef\@groupnumber{{#1}}}
\newcommand{\@keysRU}{\#}
\newcommand{\keysRU}[1]{\edef\@keysRU{{#1}}}
\newcommand{\@keysEN}{\#}
\newcommand{\keysEN}[1]{\edef\@keysEN{{#1}}}
\newcommand{\@UDC}{\#}
\newcommand{\UDC}[1]{\edef\@UDC{{#1}}}
\newcommand{\@docname}{\#}
\newcommand{\docname}[1]{\edef\@docname{{#1}}}
\newcommand{\@GradebookNumber}{\#}
\newcommand{\GradebookNumber}[1]{\edef\@GradebookNumber{{#1}}}
\newcommand{\@Consultant}{\#}
\newcommand{\Consultant}[1]{\edef\@Consultant{{#1}}}
\newcommand{\@Consultantdegree}{\#}
\newcommand{\Consultantdegree}[1]{\edef\@Consultantdegree{{#1}}}
\newcommand{\@NormController}{\#}
\newcommand{\NormController}[1]{\edef\@NormController{{#1}}}
\newcommand{\@NormControllerdegree}{\#}
\newcommand{\NormControllerdegree}[1]{\edef\@NormControllerdegree{{#1}}}
\newcommand{\@abstractRU}{\#}
\newcommand{\abstractRU}[1]{\edef\@abstractRU{{#1}}}
\newcommand{\@abstractEN}{\#}
\newcommand{\abstractEN}[1]{\edef\@abstractEN{{#1}}}


% Определение титульной страницы.
\def\maketitle {
  \newlength{\ML}
  \settowidth{\ML}{«\underline{\hspace{0.7cm}}» \underline{\hspace{2cm}}}
  
  \newpage
  
  \thispagestyle{empty}
  \begin{center}
    \@ministry~\@country
    \vspace{0.5cm}
    
    \MakeUppercase{\@fulluniversityname}
    \vspace{0.5cm}
    \vfill
    
    \@institute
    \vspace{0.5cm}
    
    \@department~(\@shortdepartment)
    \vspace{2cm}
    \vfill
    
    % \textsc{Отчёт по:}
    % \vspace{0.5cm}
    
    {\MakeUppercase{\@title}}
    \vspace{1.0cm}
    \vfill
    
  \end{center}
  
  \bigskip

  \settowidth{\ML}{«\underline{\hspace{0.7cm}}» \underline{\hspace{2cm}}}
  \hfill\begin{minipage}{0.45\textwidth}
  Выполнил студент \@groupnumber~группы:\\
  \underline{\hspace{\ML}} \@author\\
  % «\underline{\hspace{0.7cm}}» \underline{\hspace{2cm}} \the\year~г.
  \end{minipage}%
  \bigskip
  
  \hfill\begin{minipage}{0.45\textwidth}
  Проверил: \@supervisordegree\\
  \underline{\hspace{\ML}} \@supervisor\\
  «\underline{\hspace{0.7cm}}» \underline{\hspace{2cm}} \the\year~г.
  \end{minipage}%
  
  \vfill
  
  \begin{center}
    Барнаул~\@date~г.
  \end{center}
  
  \newpage
  
}

% Определение страницы с рефератом.
\def\makeabstract {
  
  \newpage
  
  \begin{center}
    РЕФЕРАТ
  \end{center}
  
  Полный объём работы составляет \formbytotal{TotPages}{страниц}{у}{ы}{}, включая
  \formbytotal{totalcount@figure}{рисун}{ок}{ка}{ков} и
  \formbytotal{totalcount@table}{таблиц}{у}{ы}{}.
  
  \@abstractRU
  
  Ключевые слова: \@keysRU.
  
  Отчёт оформлена с помощью системы компьютерной вёрстки \TeX{} и его расширения \XeTeX{} 
  из дистрибутива \textit{TeX Live}.
  
%  \begin{center}
%    ABSTRACT
%  \end{center}
%  
%  The total amount of work is \formbytotal{TotPages}{page}{}{}{'s}, include
%  \formbytotal{totalcount@figure}{image}{}{}{'s} and \formbytotal{totalcount@table}{table}{}{}{'s}.
  
%  \@abstractEN
  
%  Keyword: \@keysEN.
  
%  Report is framed using the computer layout system \TeX{} and its extension \XeTeX{}
%  from the distribution \textit{TeX Live}.
}

\endinput
