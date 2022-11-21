Useful unicode characters:

* — the em-dash
* – the en-dash
* × the multipliction symbol
* ÷ the division symbol
* … the ellipsis

Custom elements that we have.
I *think* this are enumerated in gatsby-config.js\?

* example
* designnote
* gmguidance
* playerguidance
* clarification
* fiction
* optionalrule
* hook
* abstract
* note (added one in 4.2 Dragonshire)

As a reminder, these look like this:

```
[[clarification | when does armor apply?]]
|
```

I think that the first blank-line pipe is optional; omitting it doesn't seem to do anything.

It looks like the process to set up a dev environment is:
- install npm
- `npm install -g gatsby-cli yarn` (and yes, that's -g for global, but that's how it's designed to work.)
- `yarn` in the top-level development directory (the one with yarn.lock)
- and then `yarn run develop` to start up the dev server.

Also, it looks like the custom blocks are defined in 'gatsby-config.js'.

Used dehyphenizer.sed to replace all the --s and get the spacing consistent.
Hopefully.
RegExes are always fun.

We were using [IM Fell Double Pica](https://fonts.google.com/specimen/IM+Fell+Double+Pica#license) before.
And I think still can, in principle, without dealing with Google's fuckery, because it's an open font.
The [Mozilla page](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts) on web-fonts looks fairly practical, honestly.