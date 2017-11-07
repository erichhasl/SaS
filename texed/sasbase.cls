\ProvidesClass{sasbase}[2017/11/6 SaS base class]
\LoadClass[twocolumn]{article}

\RequirePackage[utf8]{inputenc}
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

% SET PAGE GEOMETRY
\geometry{
	left=12mm,
    right=12mm,
	top=8mm}

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

\renewcommand{\arraystretch}{2.5}

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
    {\thesection}
    {1em}
    {}

% -----------------
% TABLE OF CONTENTS
% -----------------

% DISABLE BOLD
\renewcommand{\cftsecfont}{\normalfont}

% ONLY SHOW SECTIONS IN TOC
\setcounter{tocdepth}{1}

% HIDE NUMBERING OF SECTIONS
\setcounter{secnumdepth}{0}

% DEFINE OWN COLUMN TYPE
\newcolumntype{P}[1]{>{\centering\arraybackslash}p{#1}}

% DEFINE SPACING BETWEEN ITEMS
\setlength{\cftbeforesecskip}{-3mm}

\setlength{\cftbeforetoctitleskip}{0mm}
\setlength{\cftaftertoctitleskip}{-10mm}

% SET DOTS FOR SECTIONS
\renewcommand{\cftsecdotsep}{\cftdotsep}

%\setlength{\cftsecnumwidth}{0mm}

% Redefinition of ToC command to remove heading
\makeatletter
\renewcommand\tableofcontents{%
    \vspace{-4mm}
    \@starttoc{toc}
}
\makeatother

\newcommand{\mycontents}{%
    \ostyle
    \begin{tabular}{lp{.9\textwidth}}
        \textbf{Inhalt:} & \tableofcontents \\
    \end{tabular}
    \vspace*{-5cm}
}

% ---------------------------------------
% TITLE (THIS IS WHERE THE MAGIC HAPPENS)
% ---------------------------------------

\setlength{\arrayrulewidth}{.3mm}

\makeatletter
\def\@maketitle{
    \begin{center}
        \textbf{\ostyle{\HUGE{\@title}}}
    \end{center}
    \vspace{5mm}
    \begin{tabular}{P{\dimexpr.1\textwidth-2\tabcolsep}|P{\dimexpr.8\textwidth-2\tabcolsep}|P{\dimexpr.1\textwidth-2\tabcolsep}}
        \hline
        \large \ostyle{\TheLastWord{\@datum}} &
        \large \ostyle{Ausgegeben in {\@place} am {\@datum}} &
        \large \ostyle{Nr. 1}
        \\ \hline
        \multicolumn{3}{p{\textwidth}}{\mycontents} \\ \hline
    \end{tabular}

    \vspace{10mm}
}
\makeatother
