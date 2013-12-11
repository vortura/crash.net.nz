Title: Completing the Matasano Crypto Challenges
Date: 2013-10-02 20:36
Tags: python, crypto
Slug: completing-the-matasano-crypto-challenges
Author: Richard Gray

Back in April sometime, Maciej Cegłowski [posted on his blog][1] about some
cryptography challenges he'd been working through, run by the nice people at
Matasano security. [The challenges][2] are a set of practical exercises to build
and then break various cryptographic constructions, aimed at people with some
programming experience, but otherwise no particular knowledge of cryptography.
It sounded like my cup of tea so I signed up, and five months later having just
finished all six sets, I thought I'd write about the experience, what I learned,
and the problems I ran into.

[1]: https://blog.pinboard.in/2013/04/the_matasano_crypto_challenges/
[2]: http://www.matasano.com/articles/crypto-challenges/

Each of the sets contains eight challenges, usually based around one or two
broad cryptographic themes. Having completed a set, you submit your answers via
email, and if they check out, you get to see the next set. If you've gotten
something wrong, or aren't quite sure how to handle a particular challenge, the
Matasano guys are super helpful and will point you in the right direction,
without ever spelling things out completely. If you're persistent and approach
the problems methodically though, you probably won't need too much assistance to
complete the sets. Each challenge builds on knowledge you've acquired in the
previous exercises, and there are plenty of useful hints scattered throughout,
so it never feels like you've been dropped in the deep end. The few times I got
stuck it was usually down to some stupid mistake rather than a misunderstanding
of the material.

While you should probably need some programming experience before starting the
challenges, they make an excellent opportunity to learn a new language, or to
solidify understanding of a language you know a little about. Often the hardest
part of learning a language is finding a practical project to work on to cement
the concepts that you might have picked up from a book, and these exercises fit
the bill perfectly. Even if I forget all the cryptography, the 6000 lines of
Python I wrote have given me a much better understanding of the language and
a decent slice of its standard library. As you might expect, I used the
`random` and `pycrypto` modules a lot, but I also parallelised tasks with
`multiprocessing`, built servers and clients with the `socket` module, and
implemented data structures with `pyasn1`.

A special mention too, for [ipython][3]. I've used ipython a bit in the past,
mainly as a nicer version of the default Python interactive interpreter.  This
was, however, the first time I'd used the [ipython notebook format][4], and
I have to say it's an amazing way of describing the operation of a piece of
code. It allows you to intersperse code and its output with text, graphs, and
other media, all manipulated using a handy web UI. I used it when I was stuck on
a problem, to describe my thought process, 'showing my working' at each step of
the way. It turned out that just writing up the exercise in this manner was
enough to illuminate where I'd gone wrong.

[3]: http://ipython.org/
[4]: http://ipython.org/notebook.html

There is a regular pattern in the challenges where you are asked first to
implement some cryptographic function or oracle, and then in subsequent
challenges to break that function by cracking a ciphertext, forging a signature,
etc. These are not obscure theoretical vulnerabilities we're talking about
either. In many cases, a quick search of GitHub turns up a selection of software
projects containing the exact same cryptographic misimplementations you've just
exploited. It's a little bit scary.

I can't help but be reminded of [Schneier's Law][5]:

> Anyone, from the most clueless amateur to the best cryptographer, can create
> an algorithm that he himself can't break.

[5]: https://www.schneier.com/blog/archives/2011/04/schneiers_law.html

Not that we're designing algorithms here, but over and over again the challenges
have you build an apparently secure system, only to immediately break the system
and demonstrate why it is not secure at all.  "Don't roll your own crypto" has
become a meme of sorts, and these challenges give you about 48 practical
examples of why it's a bad idea. 

Part of the problem with doing crypto well is that in many cases, the underlying
algorithms are deceptively simple and alluring to the curious programmer. For
example, the basic Diffie-Hellman and RSA algorithms are there for all to see on
Wikipedia, can be coded up in an hour or so. However, integrating these basic
cryptographic components into a larger system and selecting appropriate
parameter values is subtle and complex topic, with a multitude of interesting
ways to get it completely wrong. Intuition can be misleading to all but
experienced cryptographers, and even a small mistake can severely undermine the
security of the system you were seeking to protect. In a strange way, these
challenges have both piqued my interest to learn more about crypto, while at the
same time officially giving me The Fear&trade; of using it in any serious
project.

I did get stuck on a few of the problems, mostly because I'm an idiot. For
anyone currently doing the challenges, or about to do so, these are my words of
advice:

- Read the instructions. Read them again.
- Be careful with encodings. At least a couple of times I got stuck because
  I double-encoded something. e.g. Hex encoding a hex encoded string.
- Don't cheat, but don't overthink the problems either. An attacker is going to
  use the easiest possible means to break your system, so that's how
  I approached the problems. For example, if brute forcing something was quick
  enough, I didn't spend time hunting for a 'clever' solution.
- Watch out for dodgy arithmetic. At least once, I spent a long time stuck on
  a problem because I'd accidentally doubled the length of my RSA keys by
  failing correctly convert bits to bytes. Derp.
- Read the instructions. 

So, you should do the Matasano Crypto Challenges. You can sign up [here][6].
They're free, fun, and you're almost certain to learn something.

[6]: http://www.matasano.com/articles/crypto-challenges/

