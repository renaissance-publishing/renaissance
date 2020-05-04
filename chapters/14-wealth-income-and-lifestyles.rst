Wealth, Income, and Lifestyles
==============================

Wealth
------

Wealth is represented by a *wealth level*, and a number of *wealth
dots*. Characters have a wealth level between 0 and 5; these wealth
levels are described in the table below. (Note that the wealth scale is
“non-linear”; there is a very wide gap between the amount of wealth that
Wealth Level 4 represents and the amount of money that Wealth Level 5
represents.)

+--------+----------+-------------------------------------------------+
| Wealth | Name     | Desc                                            |
| Level  |          |                                                 |
+========+==========+=================================================+
| 0      | no       | You have no possessions                         |
|        | pos      |                                                 |
|        | sessions |                                                 |
+--------+----------+-------------------------------------------------+
| 1      | peasant  | You are poor, like a tenant farmer              |
+--------+----------+-------------------------------------------------+
| 2      | local    | You have a reliable income and some disposable  |
|        | artisan  | wealth                                          |
+--------+----------+-------------------------------------------------+
| 3      | merchant | You can afford a comfortable lifestlye          |
+--------+----------+-------------------------------------------------+
| 4      | local    | You are quite wealthy, perhaps the richest      |
|        | wealthy  | person within miles                             |
+--------+----------+-------------------------------------------------+
| 5      | noble    | You are exceptionally wealthy, possessed of a   |
|        |          | king’s fortune                                  |
+--------+----------+-------------------------------------------------+

You also have a certain number of *wealth dots*. Each dot has a wealth
level; you get three dots at your wealth level, and four dots at each
lower level. (Wealth Level 0 is specials: since it represents absolute
poverty—the lack of any meaningful wealth—you don’t get any level 0
wealth dots.)

As an example, Fire the scholar has wealth level 3—he’s an educated
professional, and he makes a comfortable living for himself. He gets 3
dots at level 3, 4 dots at level 2, and 4 dots at level 1—and, of
course, no dots at level 0, since there aren’t level 0 wealth dots.

Your wealth dots start out *full*, but they can also be *depleted*. A
depleted dot isn’t gone, it’s just taped-out; you’ve used the liquid
part of those assets, so they can’t be used in bartering (see Bartering
below). Depleted dots can be *restored*; one way to do this is by
working for an income (see Income, Investments and Lifestyles below)

Purchasing Things
-----------------

Characters in *Renaissance* can have widely varying wealth levels.
Sometimes a character may wish to acquire an item well within their
means; in these cases, success is nearly automatic. Other times, a
character may wish they could acquire an item well beyond their means;
in these cases, they’re out of luck. Still other times, though,
characters may wish to acquire an item expensive item that will stretch
their resources; then, they *barter*.

Each item has a *cost level*, according to its *cost category*: a
Trivial item is Cost Level 1, a minor item is Cost Level 2, and so on up
to Cost Level 5 for Extreme items (see the *Items* chapter). When you
wish to purchase an item (or service), compare its *cost level* to the
highest *wealth level* at which you have a full wealth dot.

-  If the item’s cost level is **more than 1 level lower** than the
   level of your highest full dot, then you acquire the item
   automatically. You don’t need to barter for it or deplete a dot of
   wealth; the cost of the item is so tiny compared to your wealth and
   resources that we don’t bother trying to track it.
-  If the item’s cost level is **1 level lower** than your highest full
   dot, then you can acquire the item, but the cost of the item is high
   enough that we’ll need to track the impact it has on your
   finances—that is, you’ll need to either deplete a dot to pay for it
   or *barter* (see below). If you do barter, you gain a +20 bonus to
   checks related to bartering for the item.
-  If the item’s cost level is **the same** as your highest full dot,
   then you must either deplete a dot or barter.
-  If the item’s cost level is **1 level higher** than your highest full
   dot, then you must either deplete a dot to pay for it or barter;
   however, you suffer a -20 penalty while bartering.
-  If the item’s cost level is **more than 1 level higher** than your
   highest full dot, then you can’t purchase the item; it’s simply
   beyond your means.
-  If you are **wealth level 0,** then you can’t purchase items—you
   don’t have any wealth, so you can’t pay for anything.

These rules are summarized in the table below:

+-------------------------------------------+---------------------------+
| Item Cost vs. Wealth Level                | Result                    |
+===========================================+===========================+
| Item cost is more than 1 less than wealth | don’t deplete dot         |
+-------------------------------------------+---------------------------+
| Item cost is 1 less than wealth level     | deplete dot or barter;    |
|                                           | barter at +20             |
+-------------------------------------------+---------------------------+
| Item cost is the same as wealth level     | deplete dot or barter     |
+-------------------------------------------+---------------------------+
| Item cost is 1 higher than wealth level   | deplete dot or barter;    |
|                                           | barter at -20             |
+-------------------------------------------+---------------------------+
| Item cost is more than 1 greater than     | cannot purchase           |
| wealth                                    |                           |
+-------------------------------------------+---------------------------+
| You are wealth level 0                    | cannot purchase           |
+-------------------------------------------+---------------------------+

.. raw:: html

   <aside class="designnote">

Character Wealth
~~~~~~~~~~~~~~~~

The wealth-and-trade system may seem a little odd to someone coming from
a game that measures wealth in gold, silver and copper; why is it put
together this way?

One simple reason is that this game is based partly on *Eclipse Phase*,
and *Eclipse Phase* uses a similar cost-level system. But that’s far
from the entire motivation!

Much like *Eclipse Phase*, we want players to be able to *choose* how
important wealth is to their character-concept, and to be able to play
characters with vastly different levels of wealth; players should be
able to start out wealthy (like Lady Katrine, the noble-born merchant)
or stay poor (like Aryn the hunter or Lohrs the folk-hero, both of whom
are as like as not to refuse a reward) without breaking a
“treasure-by-level” table. In particular, much like *Eclipse Phase*, we
want “the character who provides the party with things that they need”
to be a *player* role, and “being incredibly rich and just buying
things” is a valid strategy for succeeding in that role. This means that
our wealth system needs to *scale elegantly*, supporting everything from
destitute drifters to propertied nobles.

At the same time, as a design principle, we try to avoid making
characters keep track of *tedious and unimportant details*. This means
that we want our wealth system to allow a wealthy character (like Lady
Katrine or General Chandra) to purchase a wide variety of useful things
for the party, without bogging the game down with “cash-register math”
and *especially* without wasting time trying to figure out how Lady
Katrine “makes change” out of her immense estate to buy a meal.

That’s why we’ve designed our wealth system the way we have; we’ve
broken wealth levels and item costs down using a roughly *logarithmic*
scale, and we’ve designed our bartering system so that you only need to
keep track of *what level of item you start to have trouble paying for*,
and *how many of those items you can probably buy*.

Another consequence of this design is that we *don’t* measure character
power or advancement in magical items and wealth. That might be less
evident here—that’s why we’ve made minimal provision for *changing* your
wealth level—but it has more profound impact elsewhere.

.. raw:: html

   </aside>

Bartering
---------

Before the era of central banks and stable currencies, prices where
fluid and people *bartered.*

Mechanically, bartering is an *optional* step in the process for
*purchasing things* described above. Instead of simply depleting a dot,
you can attempt to *barter*; this gives you a chance ot acquire an item
without depleting a wealth dod, but it also puts you at risk of not
acquiring the item at all.

Normally, bartering is a one-minute Task Action that requires a Protocol
check; sometimes, however, the GM may allow (or require) the player to
speak with the merchant in character, or the GM may allow the player to
use their other social skills or professions. The GM may also take other
circumstances into account—such as the whether the player has made a
good impression by observing the merchant’s cultural traditions, or
whether the character has the Social Stigma trait.

If you score an Exceptional Success on your Protocol check—or do a
similarly good job talking with the merchant in-character—then you
acquire the item (or service) without depleting a wealth dot; this
represents you finding some way to pay the merchant that doesn’t
significantly impact your net wealth. However, if you score an
exceptional failure, you cannot acquire the item—maybe the merchant
doesn’t want anything you’ve got for trade, maybe they decide that they
just don’t like you, or something else happens to sour the deal.

How long do you have to wait before you can try again? That depends on
why you failed—which is largely up to the GM. If you didn’t have
anything that the merchant wanted, you might be able to head out into
the market and acquire something that they *would* want; in this case,
you could try again very quickly. If, on the other hand, you’ve grossly
offended the merchant, then they might not consider trading with you
again for some time.

Trade Goods and Currency
------------------------

The rules for wealth and bartering assume that you have access to all of
the assets that represent your wealth. For example, if you’re wealth
level 3, some of your wealth will be in the form of currencies, valuable
goods, properties (like your house), professional commitments, and so
on; the system above assumes that you can leverage all of these assets
to pay for something. Under some situations—notably, if you’re
travelling far from where your character lives—this might not be the
case. In these cases, you’ll need to either use *trade goods* to
represent the portion of your wealth that you’ve taken with you, or
you’ll need to use *currency.*

Trade Goods
~~~~~~~~~~~

Trade goods work much like wealth dots; they have an associated *wealth
level,* and can be used in place of a (full) wealth dot in the rules for
purchasing items above. However, trade goods *cannot* be depleted;
instead, you *spend* them, and once you do, they’re gone.

Creating a *trade good* requires converting some of your various assets
into portable valuables—currencies, valuable commodities, gems and
jewelry, and the like. This requires some time (see the table below),
and that you deplete a wealth dot of the same level as the trade good
that you’re producing.

The process can also be reversed: a trade good can be *spent* to refresh
a depleted wealth dot; this takes the same time as producing a trade
good of the same level.

===== ==================
Level Time
===== ==================
1     2 hour Task Action
2     4 hour Task Action
3     1 shift Job
4     2 shift Job
5     5 shift Job
===== ==================

Note that *level 5 Trade Goods,* for example, represent very small and
very valuable items—rare gems, legendary jewelry, priceless relics,
deeds to valuable lands and so on. Carrying around this kind of wealth
might make a character a target for bandits, and may tempt even the most
honest to theft.

Currency
~~~~~~~~

Sometimes it’s just easiest to price things in a *currency.* Though
central banks and stable currencies are centuries off, there do still
exist banks issuing bank notes, and the Commonwealth, the Kingdoms of
Men and the Goblin Empire have all minted coins of precious metals.

For simplicity, we’ll give prices in *copper* and *gold* pieces, with
one gold piece equal to 100 copper pieces. (GMs may introduce other
coins, like silver, electrum or platinum; for simplicity, we usually
recommend recording these as their converted value in copper and gold
values.) Similar to trade goods, you can deplete dots of wealth to
produce currency, and you can expend currency to refresh a depleted
wealth dot (use the same time-spans as for creating trade goods).

===== ============= ==========
Level Price Range   Wealth Dot
===== ============= ==========
1     1–9 copper    5 copper
2     1–9 gold      5 gold
3     10–49 gold    25 gold
4     50–499 gold   250 gold
5     500–5000 gold 2500 gold
===== ============= ==========

Income, Investments and Lifestyles
----------------------------------

Most characters need to work for a living—even those who are
independently wealthy have likely put their wealth to work by investing.

Income
~~~~~~

You can work for income during down-time; working for income is a
20-shift *job*. (This is intended to line up roughly with one month of
work; your GM may adjust this time-scale based on how many days you work
in a given week, how long you work each day, and other factors.) You
must have at least 20 ranks in a Profession to work for income, although
a check using one of your profession skills is not required under normal
circumstances (under exceptional circumstances, a check may be
required—for example, if you are a farmer and there is a drought).

After completing all 20 shifts of work, you are credited with your
income; you may either refresh one of your highest-level wealth dots, or
any three lower-level wealth dots.

Note that we don’t have any particular rules for how large a wealth dot
you can fill—we haven’t assigned wealth levels to different skills, and
we don’t require certain numbers of ranks to refill dots of a certain
level. This doesn’t mean that you can use 20 ranks in Profession: Farmer
to refill a Level 5 wealth dot; the GM has the prerogative to limit the
highest level of wealth dot that you can fill with a certain skill.

.. raw:: html

   <aside class="playerguidance">

If you want to be able to use your skills to *work for income*, it’s a
good idea to talk about that with your GM *during character creation*,
so that you’ll know if your skill selection is going to work for that.

.. raw:: html

   </aside>

.. raw:: html

   <aside class="gmguidance">

While you *can* restrict a player from using an inappropriate skill to
work for income, we encourage you to be lenient; we intend for players
to be able to recharge their wealth dots during down-time, and we chose
not to build “hard” requirements into the system.

.. raw:: html

   </aside>

Investments
~~~~~~~~~~~

Your character can put their wealth to work producing more wealth.

Investments represent planted fields, stakes in businesses, trade
caravans loaded with your goods, and so on. Like wealth dots and trade
goods, they have an associated level, from 1 to 5.

Investments aren’t liquid assets, so you can’t deplete them like wealth
dots or spend them like trade goods. Instead, investments *generate*
wealth for you. At the end of each month, for each investment that you
have, you may refresh one dot of wealth of the same level, or three dots
at a lower level (much as if you had *worked for income* as above,
except that the dot or dots you can deplete depends on the
*investment’s* level and not *your* wealth level).

Creating an investment involves converting some of your liquid wealth
into an illiquid form—that is, essentially, you have to lose a Wealth
Dot to create an Investment. Converting a wealth do to an investment is
a 5 shift job and requires a successful Protocol check, Profession:
Investor check, or other reasonable check

Conversely, you can *liquidate* an investment, turning it back into a
wealth dot; this is also a 5-shift job, and also requires a Protocol
check, Profession: Investor check, or other reasonable check. (Note that
“liquidating an investment” might involve quite a bit of misery for
whoever you had invested in, which might turn into an interesting
roleplaying moment, or possibly even an adventure hook!)

Investments can be handled in the abstract, but cinematically-minded
players may wish to detail the businesses that they have invested in;
cooperative GMs might use this information to inform how their
investments function. Note that, in this case, choosing to liquidate an
investment could become particularly impactful.

Lifestyles
~~~~~~~~~~

Your character lives a certain lifestyle, which incurs expenses.

Lifestyles have levels from 0 to 5, just like wealth; see the table
below for descriptions. At the beginning of each month, you pick your
level of lifestyle; you must then deplete a dot of the same level to pay
for it.

+---------------------+------------------------------------------------+
| Level               | Description                                    |
+=====================+================================================+
| 0 (begger)          | You live off what you can beg, steal or        |
|                     | scrounge, dwelling in alleys, woods and caves. |
+---------------------+------------------------------------------------+
| 1 (peasant)         | You live a humble life, with long hours of     |
|                     | work and no luxuries; you know want and hunger |
|                     | well.                                          |
+---------------------+------------------------------------------------+
| 2 (poor)            | Though poor, your basic needs are met, and you |
|                     | may have access to the occasional luxury.      |
+---------------------+------------------------------------------------+
| 3 (comfortable)     | Your needs are reliably met, you have some     |
|                     | amount of leisure time, and you have access to |
|                     | modest luxuries. You likely own your own       |
|                     | house.                                         |
+---------------------+------------------------------------------------+
| 4 (wealthy)         | You have amassed significant wealth, enough    |
|                     | that you can afford a luxurious lifestyle for  |
|                     | quite some time.                               |
+---------------------+------------------------------------------------+
| 5 (noble)           | You own a king’s fortune, perhaps literally;   |
|                     | if managed wisely, you and your descendants    |
|                     | will not need to work for generations.         |
+---------------------+------------------------------------------------+

Changing your Wealth Level
--------------------------

While your character *can* work hard enough and earn enough money to *go
up a wealth level*, doing so isn’t easy—CY 830 is not a time of high
social mobility.

Mechanically, advancing from one wealth level to the next wealth level
is a *Job* done during Down-Time and requiring a successful check; on a
success, you advance a wealth level, but you don’t suffer any particular
penalty if you fail—other than your wasted time.

====== =========================== =======================
Change Job Length                  Check
====== =========================== =======================
0 → 1  60 Shifts (about 3 months)  profession check at +10
1 → 2  120 Shifts (about 6 months) Profession check
2 → 3  240 Shifts (about 1 year)   Profession check
3 → 4  480 Shifts (about 2 years)  Profession check at -20
4 → 5  1200 Shifts (about 5 years) Profession check at -30
====== =========================== =======================

Note that *changing your wealth-level* and *working for income* are two
separate jobs. You’ll need to juggle both of them—possibly by accepting
a lower level of lifestyle than you’re used to—while you’re trying to
gain a wealth level (building up wealth requires sacrifices, like long
working hours and skipped meals).

Alternatively, you might *acquire* wealth that you can use to improve
your circumstances—this is slightly more common for the kind of
characters that often have fantastic adventures (and *survive* them). If
you acquire *trade goods*, *investment* or a *large amount of cash*, you
can *expend* them to make the process of advancing a wealth level
easier.

For each higher-level *asset* (a trade good, investment or large amount
of cash) you expend, you reduce the duration of the Job by a third, and
you gain a +20 bonus on your check. In order to be useful, the asset you
expend must be higher than your current wealth level. (You can determine
the wealth level for “a large amount of cash” using the table for
*restoring wealth dots with cash* above.)

Note that expending an *investment* in this way doesn’t necessarily
imply that you’ve *liquidated* it; mechanically, you’ll still lose the
investment, but it will be because it’s directly incorporated into your
wealth, not because you’ve withdrawn your investment. The difference
between these two outcomes might be *significant* to the people that you
have invested in.
