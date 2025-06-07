% altsu-bachelor.cls
% Часть материала взято из шаблона для диссертаций. https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template
% Класс для оформления выпускно квалификационной работы (ВКР)
% на кафедре Вычислительной техники и электроники Алтайского государственного университета.
% Автор Шмаков Игорь Александрович.
% Первая версия от 2020-03-30.
% Версия от 2024-05-03 +fix (от Щербакова В.)
\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{altsu-bachelor}[2024/05/03 version 0.4 AltSU Template for CSaE Bachelor]

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
\RequirePackage[onehalfspacing]{setspace}
\RequirePackage[normalem]{ulem} %https://stackoverflow.com/questions/2553392/latex-rule-filling-the-line

%%% Интервалы %%%
%% По ГОСТ Р 7.0.11-2011, пункту 5.3.6 требуется полуторный интервал
%% Реализация средствами класса (на основе setspace) ближе к типографской классике.
%% И правит сразу и в таблицах (если со звёздочкой)
\setstretch{1.42}   % Полуторный интервал, подобный Ворду (возможно, стоит включать вместе с предыдущей строкой)

%%% Макет страницы %%%
% Выставляем значения полей (ГОСТ 7.0.11-2011, 5.3.7)
\RequirePackage[a4paper, left=3cm, right=1.5cm, top=2cm ,bottom=2cm, nofoot, nomarginpar, headheight=17pt]{geometry} %, heightrounded, showframe
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

\setromanfont[Mapping=tex-text]{Times New Roman}

\newfontfamily{\cyrillicfont}{Times New Roman}
\newfontfamily{\cyrillicfontrm}{Times New Roman}
\newfontfamily{\cyrillicfonttt}{Times New Roman}
\newfontfamily{\cyrillicfontsf}{Times New Roman}

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
\RequirePackage[labelsep=space,skip=6pt]{caption}
\setlength{\belowcaptionskip}{6pt plus 2pt minus 1pt}

% Пакет отвечающий за листинги.
\RequirePackage[newfloat]{minted}
\newenvironment{code}{\captionsetup{type=listing}\vspace{\parindent}}{}
\SetupFloatingEnvironment{listing}{name=Листинг}
\setminted{
  mathescape,
  linenos,
  frame=lines,
  breaklines,
  framesep=2.5mm,
  fontsize=\scriptsize,
  numbersep=5pt,
  xleftmargin=15pt
}

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
  \setlength{\parindent}{12.7mm}%{2.5em}                   % Абзацный отступ. Должен быть одинаковым по всему тексту и равен пяти знакам (ГОСТ Р 7.0.11-2011, 5.3.7).
}

\addto\captionsrussian{%
  %%% Переопределение именований %%%
  \renewcommand{\contentsname}{Содержание} % (ГОСТ Р 7.0.11-2011, 4)
  \renewcommand{\figurename}{Рис.} % (ГОСТ Р 7.0.11-2011, 5.3.9)
  \renewcommand{\tablename}{Таблица} % (ГОСТ Р 7.0.11-2011, 5.3.10)
  \renewcommand{\listfigurename}{Список рисунков}
  \renewcommand{\listtablename}{Список таблиц}
  \renewcommand{\thechapter}{\arabic{chapter}.}
  \renewcommand{\thesection}{\thechapter\arabic{section}.}
  \renewcommand{\thesubsection}{\thechapter\arabic{section}.\arabic{subsection}.}
}

% Правка 20230617
\renewcommand{\labelenumii}{\theenumii}
\renewcommand{\theenumii}{\theenumi.\arabic{enumii}.}
\renewcommand{\labelenumiii}{\theenumiii}
\renewcommand{\theenumiii}{\theenumi.\arabic{enumii}.\arabic{enumiii}}
% Правка 20240504
\renewcommand{\theequation}{\thechapter\arabic{equation}}

%%% Оглавление %%%
\usepackage[dotinlabels]{titletoc}
\usepackage[pagestyles]{titlesec}
\titleformat{\chapter}%
            {\centering} %\normalfont\bfseries\normalsize
            {\thechapter}
            {14pt}
            {\MakeUppercase}
\titleformat{\section}%
            {}
            {\thesection}
            {14pt}
            {}
\titleformat{\subsection} % command
            [hang]                 % shape
            {} % format
            {\thesubsection}       % label
            {1em}                  % Spacing between label and title
            {}                     % before code

%\titlespacing{\subsection}% Set the spacing around the title
%{0pt}                  % Left
%{0pt}                  % Above
%{0pt}                  % Below
\titlespacing{\chapter}{0pt}{*0}{15pt}
\titlespacing{\section}{\parindent}{10pt}{10pt}
\titlespacing{\subsection}{\parindent}{8pt}{8pt}

\setlength{\parindent}{1.27cm}
\setlength{\parskip}{0cm}

% Изменение отступов в содержании
\usepackage[titles]{tocloft}
\setlength{\cftbeforechapskip}{0pt} % 6pt
\setlength{\cftsecindent}{0pt}
\setlength{\cftsubsecindent}{0pt}
\renewcommand{\cftchapdotsep}{\cftdotsep}
\renewcommand{\cftsecdotsep}{\cftdotsep}
\renewcommand\cftchapfont{\mdseries}
\renewcommand\cftchappagefont{\mdseries}
%\renewcommand{\cftsecdotsep}{\cftnodots} % Убрать точки

% Отступы в рисунках и таблицах
\captionsetup[table]{font={stretch=1.42}}
\captionsetup[figure]{font={stretch=1.42}}
\captionsetup[listing]{font={stretch=1.42}}
% \captionsetup{font={stretch=1.42}}

\RequirePackage{fancyhdr}
\pagestyle{fancyplain}
\fancyhf{}
\fancyhead[R]{\thepage} % номер страницы в правом верхнем углу \fancyhead[R]{\normalfont\bfseries\textbf{\thepage}}
\renewcommand{\headrulewidth}{0pt} % без линии

\RequirePackage{csquotes}
\RequirePackage{epigraph}
\RequirePackage{enumitem} %https://tex.stackexchange.com/questions/6081/reduce-space-between-enumerated-items
%\setlist{nosep,labelindent=\parindent,leftmargin=*} %nolistsep deprecated
\setlist[enumerate,1]{nosep,labelindent=\parindent,leftmargin=*}
\setlist[enumerate,2]{nosep,labelindent=0pt,leftmargin=*}
\setlist[enumerate,3]{nosep,labelindent=0pt,leftmargin=*}
\setlist[itemize,1]{nosep,labelindent=\parindent,leftmargin=*}
\setlist[itemize,2]{nosep,labelindent=0pt,leftmargin=*}
\setlist[itemize,3]{nosep,labelindent=0pt,leftmargin=*}

\RequirePackage[
  backend=biber, 
  sorting=none,
  bibstyle=gost-numeric,%gost-authoryear,
  citestyle=gost-numeric%gost-authoryear
]{biblatex}
\urlstyle{same}

% Добавление пакета SVG для подключения векторных рисунков - 20230618
\RequirePackage{svg}

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

\newcommand{\@countWorkPage}{\#}
\newcommand{\countWorkPage}[1]{\edef\@countWorkPage{{#1}}}
\newcommand{\@countWorkImg}{\#}
\newcommand{\countWorkImg}[1]{\edef\@countWorkImg{{#1}}}
\newcommand{\@countWorkLit}{\#}
\newcommand{\countWorkLit}[1]{\edef\@countWorkLit{{#1}}}
\newcommand{\@countWorkTab}{\#}
\newcommand{\countWorkTab}[1]{\edef\@countWorkTab{{#1}}}

% Правка для таблицы, оформление по требованиям кафедры.
\def\fnum@table{\hfill\tablename~\thetable\\}
% Правки для рисунка, таблицы и листинга, оформление по требованиям кафедры.
\renewcommand{\thefigure}{\thechapter\arabic{figure}}
\renewcommand{\thetable}{\thechapter\arabic{table}}
\def\fnum@table{\hfill\tablename~\thetable\\}
\renewcommand{\thelisting}{\thechapter\arabic{listing}}
\def\fnum@listing{\hfill\listingname~\thelisting\\}

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
    
    \@institute
    \vspace{0.5cm}
    
    \@department~(\@shortdepartment)
    \vspace{0.5cm}
    \begin{flushleft}
      УДК \@UDC
    \end{flushleft}
    \vspace{0.5cm}
    
    \noindent
    
    \begin{minipage}{1\textwidth}
      \noindent
      \begin{minipage}{0.48\textwidth}
        Работа защищена\\
        «\underline{\hspace{0.7cm}}» \underline{\hspace{2cm}} \the\year~г.\\
        Оценка \underline{\hspace{\ML}}\\
        Председатель ГЭК, \@ChairmanOfTheStateCertificationCommissiondegree\\
        \underline{\hspace{\ML}} \@ChairmanOfTheStateCertificationCommission
      \end{minipage}%
      \hfill
      \noindent
      \begin{minipage}{0.48\textwidth}
        Допустить к защите\\
        «\underline{\hspace{0.7cm}}» \underline{\hspace{2cm}} \the\year~г.\\
        Заведующий кафедрой ВТиЭ,\\
        \@departmentchiefdegree\\
        \underline{\hspace{\ML}} \@departmentchief\\
      \end{minipage}%
    \end{minipage}%

    \vspace{1cm}
    
    {\MakeUppercase{\@title}}
    \vspace{0.5cm}
    
    \textsc{ПОЯСНИТЕЛЬНАЯ ЗАПИСКА К ВЫПУСКНОЙ КВАЛИФИКАЦИОННОЙ РАБОТЕ}
    % \vspace{1.0cm}
  \end{center}
  
  \bigskip
  
  \begin{center}
    \uline{\hfill \@docname.\@groupnumber.\@GradebookNumber~ПЗ \hfill}
  \end{center}
  
  \noindent Студент группы \uline{ \mbox{\hspace{\ML}} \@groupnumber \hfill \@author}
  \vspace{0.5cm}
  
  \noindent Руководитель работы \uline{ \mbox{\hspace{1cm}} \@supervisordegree \hfill \@supervisor}
  \vspace{0.5cm}
  
  \noindent Консультанты: \@Consultantdegree \hfill \@Consultant
  \vspace{0.5cm}
  
  \noindent Нормоконтролер \uline{ \mbox{\hspace{2cm}} \@NormControllerdegree \hfill \@NormController}
  \vspace{0.5cm}
  
  %\hfill
  \vfill
  
  \begin{center}
    Барнаул~\@date
  \end{center}

  \newpage
}

% Определение страницы с рефератом.
\def\makeabstract {
  \newpage

  \begin{center}
    РЕФЕРАТ
  \end{center}
  
  Объем работы листов \hfill \@countWorkPage
    
  Количество рисунков \hfill \@countWorkImg
    
  Количество используемых источников \hfill \@countWorkLit
    
  Количество таблиц \hfill \@countWorkTab

  {\MakeUppercase{\@keysRU}}.
  
  \@abstractRU
  
  %Дипломная работа оформлена с помощью системы компьютерной вёрстки \TeX{} и его расширения \XeTeX{} из дистрибутива \textit{TeX Live}.
  
  % \begin{center}
  %   ABSTRACT
  % \end{center}
  
  % % The total amount of work is \formbytotal{TotPages}{page}{}{}{'s}, include \formbytotal{totalcount@figure}{image}{}{}{'s} and \formbytotal{totalcount@table}{table}{}{}{'s}.
  % The amount of work sheets \hfill \@countWorkPage

  % Number of images \hfill \@countWorkImg

  % Number of sources used \hfill \@countWorkLit

  % Number of tables \hfill \@countWorkTab

  % {\MakeUppercase{\@keysEN}}.
  
  % \@abstractEN
    
  % Thesis is framed using the computer layout system \TeX{} and its extension \XeTeX{} from the distribution \textit{TeX Live}.
}

% Определение последней страницы.
\def\makelastpage {
  \newpage
  \thispagestyle{empty}
  
  \begin{center}
    ПОСЛЕДНИЙ ЛИСТ ВКР
  \end{center}
  
  Выпускная квалификационная работа выполнена мной совершенно самостоятельно.
  Все использованные в работе материалы и концепции из опубликованной научной литературы и других источников имеют ссылки на них.\\
  
  «\underline{\hspace{0.7cm}}» \underline{\hspace{4cm}} \the\year~г.\\
  
  \underline{\hspace{5cm}} \underline{\@author}
}  
\endinput
