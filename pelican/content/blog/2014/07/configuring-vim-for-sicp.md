Title: Configuring Vim for SICP
Date: 2014-08-26 22:18
Tags: vim, sicp, racket, scheme, tmux
Slug: configuring-vim-for-sicp
Author: Richard Gray

For the past few months, I've been chipping away at *Structure and
Interpretation of Computer Programs*, MIT's classic textbook on the principles
of computer programming. It's not always an easy read, but it is rewarding
you're willing to put the time in, and especially if you work through the
exercises to reinforce your understanding. Having studied maths to a reasonable
level, and having done a reasonable amount of practical programming, I like the
way the book makes explicit the links between these disciplines.

However, other people more eloquent than I have written about the virtues of
*SICP* and why reading it and completing the exercises is a worthwhile use of
your time. Assuming then, that you've already decided to start your own SICP
quest, I hope maybe I can save some fellow Vim users a little time by describing
how I've setup my environment to make working through the exercises as easy as
possible. You do use Vim, right?

In a nutshell, I'm going to describe where to get SICP, which Scheme interpreter
to use, and how to send snippets of code from Vim to a REPL running in
a different tmux pane using tslime. For what it's worth, I'm using OS X 10.9.4,
but I think things should work equally well on Linux. Windows folks, good luck!

## Getting SICP

So first of all, you're going to need a copy of SICP, and you're in luck,
because it's not too hard to find. It's still in print, so if you want a paper
copy you should be able to pick one up on Amazon, or [directly from MIT
Press][1].

Alternatively, if an ebook is more to your liking, the full text is available
for free on MIT's [support page][2] for the book. However, I would highly
recommend Andres Raba's unofficial ebook version, which updates the original
with new typesetting, nice fonts, and SVG diagrams. It's available in EPUB3 and
PDF vserions [here][4], or online in HTML5 [here][5]. The HTML5 version is
a very lovely thing indeed, and it's this version I've been working from,
despite owning a copy of the dead tree version.

[1]: https://mitpress.mit.edu/books/structure-and-interpretation-computer-programs
[2]: https://mitpress.mit.edu/sicp/
[3]: http://sarabander.github.io/sicp/
[4]: http://sicpebook.wordpress.com/ebook/
[5]: http://sarabander.github.io/sicp/

## Choosing a Scheme implementation

To get the most out of SICP, you're going to need to do the exercises, and to do
the exercises, you're going to need a Scheme interpreter. Scheme being a variant
of the Lisp programming language invented by Gerald Sussman (along with Guy
Steele), one of the authors of SICP. There are several options available:

### Racket

I will go ahead and spoil the surprise, and recommend that you download and
install [Racket][6]. It's easy to install, includes a nice [REPL][7] with good
readline support, and includes a third-package to support users working through
SICP. The support package adds procedures like `inc` and `dec`, and variables
like `true`, `false`, and `nil`, which are assumed by the book, but not actually
included by default in most Scheme implementations. None of these are too
difficult to add yourself, but it's nice to not have to.

Once you've downloaded and installed Racket, add the application bin directory
to your path, and then start the REPL with the following command.

    racket -i -p neil/sicp -l xrepl

`-i` enables interactive mode. That is, it tells Racket to start a REPL and wait
for input.

`-p neil/sicp` enables use of the SICP package, downloading it from the Racket
PLaneT package repository if it is not already installed. I get an error
relating to internationalisation when this package is first installed, but it
doesn't seem to make any difference so far as I can tell. The package works fine
and there is no error on subsequent invocations.

Finally, `-l xrepl`, enables Racket's extended REPL mode, which amongst other
things, enables readline support. This means you get command history, tab
completion, and emacs/bash style key bindings.

If Racket is not to your taste for any reason, you have a few other options
available, which I have described below in brief.

[6]: http://racket-lang.org/
[7]: http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

### Petite Chez Scheme

[Petite Chez Scheme][8] is another good option for SICP, as it is fast,
similarly easy to install as Racket, and has good readline support in the REPL.
In many ways the REPL is nicer, with better indentation and visual highlighting
of matched parentheses. The only thing that bugs me about it is the way to
command line history works on multiline expressions, where it shows the first
line of an expression when navigating backwards through the history, but all
lines when navigating forwards. It's possible this is configurable through
`.inputrc`, but I have yet to find the appropriate option. If you can't use
Racket for any reason, Petite Chez Scheme is a decent alternative.

[8]: http://www.scheme.com/petitechezscheme.html

### The rest

[MIT Scheme][9] was the first interpreter I tried, figuring that it would be the
best option for working on exercises in an MIT textbook. I believe it's the
version of Scheme Abelman and Sussman used in their lectures. However, while
there's nothing especially wrong with it, there's not much to recommend it
either. At least in the homebrew version I'm using, I was unable to compile in
the readline support I wanted, so I promptly moved on to something else.

I also tried [Chicken Scheme][10], and [GNU Guile][11], but again, I didn't
really find anything that made them stand out in comparison to Racket. I don't
want to be dismissive, and it may well be that these interpreters have strengths
and weaknesses which are beyond the scope of my limited experience with Scheme.
For my narrow focus, however, as a beginner starting out with SICP, I found
Racket to be the easiest option to get up and running quickly.

[9]: http://www.gnu.org/software/mit-scheme/
[10]: http://www.call-cc.org/
[11]: http://www.gnu.org/software/guile/

## Tmux

You need to use tmux for this guide to work, but beyond that it doesn't really
matter much how you [configure it][12]. Minimally, you should familiarise
yourself with the ideas of sessions, windows, and panes, and the associated key
bindings to switch between them. [This][13] is a decent overview for beginners
if you're looking to learn.

I tend to use two panes side by side in a window with Vim running in one and the
REPL running in another, but you could just as easily put them in separate
windows or different sessions altogether.

[12]: https://github.com/vortura/dotfiles/blob/master/tmux.conf
[13]: http://robots.thoughtbot.com/a-tmux-crash-course

## Vim configuration

Vim has pretty good support for Scheme out of the box. The syntax highlighting
works, and the automatic indentation is not too bad. Not too bad, but not quite
perfect. There are a few edge cases where it gets caught out and fails to indent
a line correctly according to common convention for Lisp files. Dorai Sitaram
has an [excellent article][14] describing the problem, and a nice workaround. He
provides a small Racket script, [scmindent.rkt][15], that can be used to
supplant Vim's default indentation.

Download the script and put it somewhere in your path (I use `~/bin`), then add
the following to your `.vimrc`:

    autocmd filetype lisp,scheme,art setlocal equalprg=scmindent.rkt

The script is configurable through the presence of a file called `.lispwords` in
your home directory. I add `(if 3)` to that file to make the _if_ conditional's
_then_ and _else_ expressions align with the predicate.

[14]: http://www.ccs.neu.edu/home/dorai/scmindent/index.html
[15]: http://www.ccs.neu.edu/home/dorai/scmindent/scmindent.rkt

### Parentheses matching and highlighting

There's no escaping that Scheme programming involves typing a lot of
parentheses. Unless you are careful, it can be easy to get lost and lose track
of which opening and closing parentheses correspond to one another. Correct
indentation helps, but there are also a couple of vim plugins that make Scheme
files easier to work with.

The first of these is a rainbow parentheses plugin, which colourises matching
pairs of parentheses, brackets, and braces so it's easier to tell immediately
which pairs correspond. There are a few versions of this plugin that do more or
less the same thing, but the one I'm using is [vim-niji][16]. It works pretty
well out of the box, but I change the default colours to something slightly more
psychedelic for better contrast. You can do the same with something like this in
your `.vimrc`:

    :::vim
    let g:niji_dark_colours = [
        \ [ '81', '#5fd7ff'],
        \ [ '99', '#875fff'],
        \ [ '1',  '#dc322f'],
        \ [ '76', '#5fd700'],
        \ [ '3',  '#b58900'],
        \ [ '2',  '#859900'],
        \ [ '6',  '#2aa198'],
        \ [ '4',  '#268bd2'],
        \ ]¬

The second plugin is [paredit.vim][17], which keeps matched characters (such as
parentheses, quotes, braces, etc) balanced by automatically adding them in
pairs. When you type `(`, Paredit will automatically add a `)` and position the
cursor between the pair ready for further input. This is, at least, the most
obvious effect for the beginning Scheme programmer.

You might find it a little strange at first because it prevents you from
deleting characters that would unbalance an expression, but in a way, this is
Paredit's core feature in disguise. Paredit recognises the nested list structure
of Scheme (and other Lisp-ish) programs, and allows you to manipulate that
structure directly rather than treating it as freeform text. For example, you
can join adjacent lists, or splice the contents of a list into a parent list.
It's powerful, but you don't need to understand all of the features to make use
of it straight away, and the documentation is good when you're ready to learn
more.

[16]: https://github.com/amdt/vim-niji
[17]: https://github.com/vim-scripts/paredit.vim

### Tslime

The last piece of the puzzle is [tslime][18], a simple but clever plugin that
allows you to send snippets of text from a Vim buffer into a separate tmux pane.
It's perfect for working on Scheme code in Vim, because you can quickly
highlight and dispatch sections for evaluation in a REPL running in a separate
window. As I mentioned, I like to open two panes side by side with Vim in one
and my REPL in the other. I find this is the best way to get immediate feedback
on a piece of code without needing to shift focus significantly by switching
windows or anything like that. It's flexible though. You can use any tmux
configuration you like, and it works just fine if you're using a non-terminal
Vim like gvim or MacVim.

There are a few version of tslime floating around, but I would I recommend using
[Steve Losh's version][18], which has the best features and by far the best
documentation. By default, it uses <C-c><C-c> in normal or visual mode to send
text to a tmux pane, but I map this to `<localleader>t`, which is `\t` for my
setup. Using `ctrl-C` just doesn't feel right to me given that it usually kills
shell programs. Whatever key bindngs you choose, the first time you use it in
a session, you will be prompted for the tmux session, window, and pane you'd
like to target. You can hit tab for each prompt to get a list of possible
values.

In visual mode tslime sends the currently selected text into the specified tmux
pane. In normal mode, it sends the current paragraph, i.e. the contents of
`vip`. When using tslime with a REPL, you will likely also want to set
`g:tslime_ensure_trailing_newlines = 1` to ensure that at least one newline is
present at the end of any text sent to tmux. Without this, code will be sent to
the REPL, but not executed until you switch to the REPL pane and hit enter.

For reference, here's the tslime section from my `.vimrc`:

    :::vim
    " tslime {{{
    let g:tslime_ensure_trailing_newlines = 1
    let g:tslime_normal_mapping = '<localleader>t'
    let g:tslime_visual_mapping = '<localleader>t'
    let g:tslime_vars_mapping = '<localleader>T'
    " }}}

[18]: https://github.com/sjl/tslime.vim

## Putting it all together

So where am I going with this? The screencast below gives a simple example of
it all in action:

* Starting tmux and splitting the window into two panes.
* Starting the Racket REPL in the right pane, then Vim in the left pane.
* Writing a simple factorial function demonstrating Niji and Paredit.
* Reformatting the code with scmindent.rkt
* Sending the code to the REPL with tslime, using tab completion to select the
  session, window, and pane.
* Calling the function to demonstrate that it works.

<script type="text/javascript" src="https://asciinema.org/a/11700.js" id="asciicast-11700" async data-speed="2"></script>

## Wrap-up

And that's that. I hope some of this might be useful to others working on SICP,
or thinking of doing so. If you've got any questions about my setup, or
suggestions as to how it could be improved, I'd love to hear from you. Send me
an [email][19], or hit me up on [Twitter][20].

[19]: mailto:richard@crash.net.nz
[20]: https://twitter.com/elvortura
