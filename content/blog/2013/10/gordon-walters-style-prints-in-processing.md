Title: Gordon Walters Koru Patterns in Processing
Date: 2013-10-24 21:13
Tags: processing, art
Slug: gordon-walters-koru-patterns-in-processing
Author: Richard Gray

Gordon Walters was an artist and graphic designer, born in Wellington, New
Zealand in 1951. Though he produced works in a variety of styles, he is best
known for his koru series of prints, which are instantly recognisable to most
New Zealanders. They are some of my favourite pieces of art. One of his most
celebrated pieces, *Maheno*, is fairly typical of the series as a whole:

<img src="/images/Walters_Maheno.jpg" alt="Gordon Walters - Maheno">

The artworks take their name from the *koru*, a spiral pattern representing the
tight curl of a new fern frond. It is one of the primary motifs of Māori art,
particularly wood carving, and symbolises creation, life, and new growth.
I think Walters' modern abstraction of this traditional pattern retain the
symbolism, but it seems that the artist didn't see it that way himself. In [this
article](http://www.art-newzealand.com/Issues1to40/walters.htm) in *Art New
Zealand*, Walters is quoted:

> My work is an investigation of positive/negative relationships within
> a deliberately limited range of forms; the forms I use have no descriptive
> value in themselves and are used solely to demonstrate relations. I believe
> that dynamic relations are most clearly expressed by the repetition of a few
> simple elements.

Ultimately though, I like these prints not because of any implied meaning, but
simply because they're such striking images, and because they're fun to look at.
I like the way the black background of each white koru becomes the foreground of
a black koru as you scan across. It's obvious, but still seems to trick the eye,
kind of like a [Blivet](https://en.wikipedia.org/wiki/Blivet).  I am also
reminded of M. C.  Escher's [*Sky and Water
I*](https://en.wikipedia.org/wiki/Sky_and_Water_I), an interlocking grid of fish
and flying birds, where the negative space around the birds forms the images of
the fish, and vice versa.

Looking at Walters' work, I couldn't help but wonder how he made them. I'd
always assumed they were screen prints, and some of them are, but many more
still are painted directly on the canvas. He must have had a steady hand. I do
not have a steady hand, but I do know a little
[Processing](http://processing.org), so I thought it might be a fun exercise to
randomly generate koru patterns in Walters' style.

I feel like the way I approached the problem was almost cheating, but it works,
and I'm quite pleased with the results. Basically I start by filling the canvas
with alternating light and dark bars, then step through each bar adding the
round koru forms. By adding the koru forms, the current bar is broken and the
previous and following bars of the alternate colour are joined. Chosen purely at
random, koru (koru? korus? korae? What is the plural anyway?) can overlap with
those on the previous line. To avoid this, I used a simple mechanism to find the
usable range in each bar and then selecting a position randomly inside that
range.

This basic process resulted in images that were a reasonable likeness of
Walters' but there were features in some of his art that I wanted to capture as
well. First of all, every so often two koru will be separated by a small circle.
Drawing the circle is simple enough, and it required just a small update to the
positioning algorithm to account for the longer patterns. Next, I wanted some
bars to have multiple koru, breaking a line in several places. Fixed
probabilities determine whether there will be zero, one, or more koru on a line,
and whether any given koru pair will include a circle between them.

Here are some sample images.

<img src="/images/pkoru1.jpg" alt="Koru 1">
<img src="/images/pkoru2.jpg" alt="Koru 2">
<img src="/images/pkoru3.png" alt="Koru 3">
<img src="/images/pkoru4.png" alt="Koru 4">

As my first real Processing project I'm quite pleased with results, even if the
code is a bit fugly. I would quite like to rewrite it in Processing.js at some
point so it will run in a web browser without requiring Java. It would also be
fun to animate it, as a left-right infinite scroll sort of thing, or more
interactively, such that the koru avoid or are attracted to the mouse pointer.

If you'd like to take a look at the code, it's available on GitHub
[here](https://github.com/vortura/walters).
