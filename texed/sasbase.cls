\ProvidesClass{sasbase}[2017/11/6 SaS base class]
\LoadClass[twocolumn]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[shortlabels]{enumitem}
\RequirePackage{environ}
\RequirePackage{geometry}
\RequirePackage{booktabs}
\RequirePackage{mathptmx}
\RequirePackage[12pt]{moresize}
\RequirePackage{array}
\RequirePackage{titlesec}
\RequirePackage[titles]{tocloft}
\RequirePackage[rm={lining,proportional},sf={lining, proportional},tt={lining, proportional, variable}]{cfr-lm}
\RequirePackage[T1]{fontenc}
\RequirePackage{indentfirst}
\RequirePackage{fancyhdr}
\RequirePackage{bm}
\RequirePackage{roboto}
\RequirePackage{varwidth}

% SET PAGE GEOMETRY
\geometry{
    left=13mm,
    right=13mm,
    top=8mm,
    bottom=8mm,
    includeheadfoot}

% ENABLE FANCY HEADERS
\pagestyle{fancy}
\fancyhf{}

% DISABLE HEADER RULE
\renewcommand{\headrulewidth}{0pt}

% ADD PAGE NUMBER TO TOP RIGHT / LEFT (ODD / EVEN)
\fancyhead[R]{\sffamily\bfseries\large{\textbf{\thepage}} \ifodd\value{page}\else\hfill\fi}

% SET COLUMN GAP OF TWOCOLUMN LAYOUT
\setlength{\columnsep}{6mm}

% SET PLACE COMMAND
\makeatletter
\newcommand{\place}[1]{
    \def\@place{#1}
}
\makeatother

% SET DATE COMMAND (COLLIDES WITH BUILTIN)
\makeatletter
\newcommand{\datum}[1]{
    \def\@datum{#1}
}
\makeatother

% SET NUMBER COMMAND (COLLIDES WITH BUILTIN)
\makeatletter
\newcommand{\edition}[1]{
    \def\@edition{#1}
}
\makeatother

% HELPER TO EXTRACT YEAR FROM DATE
\newcommand*\TheLastWord[1]{\expandafter\xreverseit\expandafter{\expandafter}#1 \relax}
\def\xreverseit#1#2 #3{%
	\ifx\relax#3%
	#2%
	\expandafter\xthree
	\fi
	\xreverseit{#1 #2}#3% 
}
\def\xthree#1#2#3{}

% ------------------
% SECTION FORMATTING
% ------------------

\titleformat
    {\section}
    {\centering\normalfont\bf\large\ostyle}
    {\thesection}
    {1em}
    {}
    
\titleformat
    {\subsection}
    {\centering\normalfont\bf}
    {\thesubsection}
    {1em}
    {}

\titleformat
    {\subsubsection}
    {\normalfont\bf}
    {\thesubsubsection}
    {1em}
    {}

% -----------------
% TABLE OF CONTENTS
% -----------------

% DISABLE BOLD
\renewcommand{\cftsecfont}{\normalfont\ostyle}

% ONLY SHOW SECTIONS IN TOC
\setcounter{tocdepth}{1}

% HIDE NUMBERING OF SECTIONS
\setcounter{secnumdepth}{0}

% DEFINE SPACING BETWEEN ITEMS
\setlength{\cftbeforesecskip}{1mm}

\setlength{\cftbeforetoctitleskip}{0mm}
\setlength{\cftaftertoctitleskip}{5cm}

% SET DOTS FOR SECTIONS
\renewcommand{\cftsecdotsep}{\cftdotsep}

% Redefinition of ToC command to remove heading
\makeatletter
\renewcommand\tableofcontents{%
    \vspace{-4mm}
    \@starttoc{toc}
}
\makeatother

% CUSTOM TOC COMMAND
\newcommand{\mycontents}{%
    \vspace{4mm}
    \ostyle
    \begin{tabular}{lp{.9\textwidth}}
        \textbf{Inhalt:} & \tableofcontents \\
    \end{tabular}
}

% ---------------------------------------
% TITLE (THIS IS WHERE THE MAGIC HAPPENS)
% ---------------------------------------

% SET WIDTH OF RULES IN TABULAR
\setlength{\arrayrulewidth}{.3mm}

% SET CELL HEIGHT
%\renewcommand{\arraystretch}{2.5}

% DEFINE OWN COLUMN TYPE
\newcolumntype{P}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}

\makeatletter
\def\@maketitle{
    \vspace*{-10mm}
    \begin{center}
        \textbf{\ostyle{\HUGE{\@title}}}
    \end{center}
    \vspace{5mm}
    \begin{tabular}{M{\dimexpr.1\textwidth-2\tabcolsep}|M{\dimexpr.8\textwidth-2\tabcolsep}|M{\dimexpr.1\textwidth-2\tabcolsep}@{}m{0pt}@{}}
        \hline
        \large \ostyle{\TheLastWord{\@datum}} &
        \large \ostyle{Ausgegeben in {\@place} am {\@datum}} &
        \large \ostyle{Nr. {\@edition}}
        &\\[5mm] \hline
        \multicolumn{3}{m{\dimexpr\textwidth-2\tabcolsep}}{\mycontents} \\ \hline
    \end{tabular}

    \vspace{10mm}
    %\thispagestyle{fancy}
}
\makeatother

\newcommand{\mytitle}{
    \maketitle
    \thispagestyle{fancy}
}

% ---------------------------
% DEFINITION OF USEFUL MACROS
% ---------------------------

% OPTION TO ENABLE SQUARE BRACKETS OR ADDITIONS TO THE ARTICLES NAME
\newif\ifsquare\squarefalse

\newcommand{\squarestyle}{\squaretrue}
\newcommand{\parensstyle}{\squarefalse}

% ARTICLE COUNTER
\newcounter{articleno}
\setcounter{articleno}{1}

\makeatletter
\newenvironment{article}[1][nil]{
    \begin{@paraorarticle}{#1}{Artikel} 
}
{
    \end{@paraorarticle}
}
\makeatother

\makeatletter
\newenvironment{lawparagraph}[1][nil]{
    \begin{@paraorarticle}{#1}{§}
}
{
    \end{@paraorarticle}
}
\makeatother

\makeatletter

% A GENERAL ARTICLE, PARAGRAPH, etc. ENVIRONMENT
\newenvironment{@paraorarticle}[2]{
    \def\val{#1}
    \def\null{nil}
    \ifsquare
        \subsubsection{#2 {\thearticleno}}
        \ifx\val\null
        \else
            \vspace*{-2mm}
            \noindent\bracketed{\textbf{#1}}
        \fi
    \else
        \subsubsection{#2 {\thearticleno} \ifx\val\null\else(#1)\fi}
    \fi
    \stepcounter{articleno}
    \begin{enumerate}[(1)]
}
{
    \end{enumerate}
}
\makeatother

% LAW COMMAND
\newcommand{\law}[1]{
    \section{#1}
    \setcounter{articleno}{1}
}

% JUST TO MAKE CLEAR WHICH LEVEL TO USE
\newcommand{\segmentoflaw}[1]{\subsection{#1}}

% TEXT IN SQUARE BRACKETS
\newcommand{\bracketed}[1]{$\left[\varwidth{\linewidth}#1\endvarwidth\right]$}

% INCREASE HEIGHT OF BRACKETS
\setlength\delimitershortfall{-2pt}

% ---
% FAQ
% ---

\newcommand{\topic}[1]{\subsection{#1}}

% QUESTION ENVIRONMENT
\newenvironment{question}[1]{
    \subsubsection{Q: #1}
    \noindent\textbf{A:}
}
{
}

% ----------
% WIRTSCHAFT
% ----------

\newcounter{total}

\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}

\newenvironment{kostenrechnung}[0]{
    \setcounter{total}{0}
    \begin{tabular}{p{2cm}p{4.5cm}p{8.5cm}R{2cm}}
        \toprule
        Posten & Berechnung & Kommentar & Kosten in €\\
        \midrule
}
{
        \bottomrule
        Gesamt & & & \thetotal \\
        \bottomrule
    \end{tabular}
}

\newenvironment{lohnrechnung}[0]{
    \setcounter{total}{0}
    \begin{tabular}{p{8cm}p{3.5cm}p{3.5cm}R{2cm}}
        \toprule
        Stelle & Anzahl & Lohn pro Tag & Gesamt in €\\
        \midrule
}
{
        \bottomrule
        Gesamt & & & \thetotal \\
        \bottomrule
    \end{tabular}
}

\newcommand{\posten}[4]{\addtocounter{total}{#4} #1 & #2 & \textit{#3} & { \raggedleft #4 } \\}
