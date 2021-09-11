---
title: "Basic Rules"
---

## The Rule(s) 0

There are two quick "Rules 0" to cover:

- When rounding, always round down.
- Everything "stacks" unless it specifically says it doesn’t.
  - That is, if you have several bonuses or penalties, they all apply.
    You might assume this would be the case, but it’s worth pointing out because some popular games don’t work this way.

## Checks

Check (and skills) are central to *Renaissance*; while other games may use a wide variety of different dice rolls with different rules, *Renaissance* uses skills and D% checks for almost everything.

### Check Basics

To make a **check**, roll a D% and compare the result to the *target number* (TN): you succeed if your result was less than or equal to the target, and you fail otherwise.
By "D%", we mean a randomly-generated number between 0 and 99 inclusive, as you would get with a *hundred-sided die* whose faces are numbered from 0 to 99.
Such dice exist, but you can use anything that generates a number from 0 to 99 in an unbiased way — like two ten-sided dice, one for the one's-place and one for the ten's-place, or a computer.

[[clarification]]
|
|Be careful\! D% runs from 0 to 99, *not* 1 to 100\!
|
|Some random number generators give you a number between 1 and 100; you'll need to remember to interpret that 100 as "actually" being a 00.
|


The **Margin of Success** (MoS) for a check is the *value you rolled* if you succeeded.
The **Margin of Failure** (MoF) is the *die roll* minus the *target* (D%−TN)) if you failed.

The *target number* is selected by the GM.
Target numbers vary, but they are almost always either the *skill target* for a given *skill checks*, or some combination of your aptitudes; see the table below.
(Additionally, any check's TN can include *modifiers*; see *Modifiers*, below.)

[[designnote]]
|
|The authors could not resist using the phrase "linear combination of aptitudes"; the best we could do is wall it off in this little aside.
|


[[example]]
|
|For example, the GM tells Fire (a Shifter mage) to roll (against) his WIL×3.
|Fire's WIL stat is 25, so his *target number* (TN) for the check is 75.
|His player roles a D%, and gets 65; Fire has succeeded, and his *margin of success* (MoS) is 65.
|If his player had rolled an 89, Fire would have failed, and his *margin of failure* (MoF) would have been 14.
|


There are limits to what a *target number* can be.
A TN can never be greater than 98; a 99 always fails (and is always a critical failure at that; see below).
Similarly, a TN can never be less than 1; a 0 always succeeds (and is a critical success).

[[gmguidance]]
|
|You don't always have to roll a check!
|If success is either guaranteed or impossible−and if the character isn't competing with another character−you can just waive the check.
|
|Further guidance is given in the sidebar *When Should We Use Checks* and *Picking Checks*.
|


[[clarification]]
|
|Not all characters are player characters, so we'll usually try to speak in terms of "a character" rather than "you" as a player or GM.
|


### Special Results

If a character succeeds on a check and their MoS is 30 or more, then they have scored an **exceptional success**.
If they succeed and their MoS is a “double” — that is, a multiple of 11, like 22 or 55 — then they have scored a **critical success**.
(For completeness sake, we also call an MoS of 29 or less — that isn't a crit — a **basic success**.)
Conversely, if they fail and their MoF is 30 or more, then they have scored an exceptional failure; if they fail and they rolled a double, then they have scored a critical failure; and if they fail but their MoF is 29 or less, then they have scored a basic failure.

The effects of *exceptional* and *critical* results vary: some rules will spell out exactly what happens, but more often, it will be up to the GM’s discretion.
Generally, exceptional successes should get a noticeable bonus, while exceptional failures should carry some extra consequence.
Critical successes and failures should be particularly impactful.

[[example]]
|
|Lady Katarina the wealthy Ratfolk socialite (and smuggler) is trying to sneak in to a guarded palace, and she's stumbled into the same room as a guard.
|Fortunately for her, he's distracted and bored; if she can dive behind cover quick enough, the guard might not notice her.
|The GM tells her player to roll a COO×3 check to *react quickly* and dive behind cover.
|
|Her COO is 30, so her TN is a respectable 90.
|She rolls a 33, scoring a *critical success*; Katarina darts behind a well-upholstered couch, and the guard is never the wiser.
|Furthermore, the couch is long, and the back is much taller than a Ratfolk; because of her critical success, it is positioned such that it will hide Katarina from the guard for almost the whole way to a side door that leads out of the room.
|
|Had she rolled a 99, she would have scored a *critical failure*; in this case, she might have dove *into* the arm of the couch, which would make a nice, loud, guard-alerting *whack* and knock her to the floor.
|


### Upgrading and Downgrading

Sometimes, you’ll be able to *upgrade* (or required to *downgrade*) a given check; this can occur if you have a special ability, for example, or if you spend a *Luck Point* to change the outcome of a check.

When you **upgrade**, your results are improved:

- a critical failure or exceptional failure becomes a normal failure;
- a normal success becomes an exceptional success; and
- an exceptional success becomes a critical success.

When you **downgrade**, your results are degraded:

- a critical success becomes an exceptional success, and an exceptional success becomes a normal success;
- a critical or exceptional success becomes a normal success; and
- a normal failure becomes an exceptional failure, and an exceptional failure becomes a critical failure.

Note that, when upgrading, a normal failure does not become a normal success, and when downgrading, a normal success does not become a normal failure — that is, when upgrading and downgrading, you can't turn a failure into a success, or vise-versa.
That would be a little too powerful\!
Also, your MoS and MoF don’t actually change, so MoS- and MoF-dependent effects aren’t affected by upgrading and downgrading.

Upgrading and Downgrading are an exception to the "everything stacks" general rule: you can’t upgrade or downgrade the result of any one check more than once.

### Skill Checks

**Skill checks** are the most common type of check; characters use a *skill check* when they're trying to do something that's covered by a skill that they have.
(See the *Skills* chapter for a list of skills).

The *target number* for a *skill check* is the *Linked Aptitude* for the skill, plus the character's ranks in that skill (that is, Linked Apt + Ranks).

We refer to the total of a character's *ranks in a skill* pluss that skill's *linked aptitude* — that is, their target number for that skill, before any modifiers are applied — as their **rating** in that skill.

[[example]]
|
|In order to pay for a few nights at an inn, Aryn the *Haffan* monster-hunter has volunteered her services to a town; she's trying to track down a *bear* that's been picking off the locals' sheep.
|To track it, the GM calls for a *Search* check from Aryn.
|Aryn is *very good* at tracking, so she has 50 ranks in *Search*; *Search* is linked to the INT aptitude, and Aryn's INT is 25.
|Her player asks the GM if any particular modifiers apply; the GM says that none do.
|
|The TN for this check is 75 — her 50 ranks in *Search* plus her linked aptitude of 25.
|
|Aryn's player rolls a 26, so Aryn gets a *basic success*; the GM decides that she does track the bear down, but it takes her most of the day.
|


### Simple Checks

A **simple check** is used when success can be assumed, but it might still matter how well a character does (for example, if you need to know how well a character does, or how long they take); this might be the case if a character can simply make an attempt over and over again until they succeed, for example.

*Simple checks* work the same way normal checks do, except the character is always assumed to succeed.
If the character rolls at-or-below their TN, then they *excel*—they've achieved what they where trying to do, and done a great job of it\!
If they character rolls more than their target, then they *stumble*—they've still achieved their objective, but they didn't do particularly well, possibly having to try several times, or having to work exceptionally slowly, or making several embarrassing mistakes, or producing a slightly-flawed-but-still-usable result.

*Simple checks* can never be *exceptional* or *critical*.

### Opposed Checks

**Opposed checks** are used — as the name implies — when two characters are competing against each other; one character will *win*, and the other will *loose*.

To make an *opposed check*, each character makes a (separate) check:

- If one character *succeeds* on their check and other *fails*, then the character who succeeded wins the opposed check.
- If both characters succeed, then the highest MoS wins the opposed check (reroll ties)
- If both characters fail, reroll the check.

Note that the two characters don’t have to use the *same* skill–in fact, very often they won’t\!

[[example]]
|
|Chandra the bronze-armed Drake *Lord-General* is trying to punch a goblin slaver.
|To resolve the *attack* (see the *Combat* chapter), the GM asks Chandra to roll his *Unarmed Combat* against the Goblin's Fray.
|Chandra's *Unarmed Combat* is 80, and his player rolls a 63.
|The Goblin's Fray is 65, and the GM rolls a 21 for him (ordinarily, the GM wouldn't reveal to the players what the Goblin's TN was, what his stats where, or what he rolled).
|
|They both succeeded, so the GM compares Chandra's 63 to the Goblin's 21; Chandra has clearly won the opposed check.
|


#### Variable Checks

Sometimes, when both characters are competing, it’s possible for both characters to partly succeed; we call these *Variable Checks*.
**Variable checks** work just like other opposed checks, with one exception: if both characters succeed on their checks, instead of declaring the highest MoS to be the winner, both characters are awarded a partial success.

[[example]]
|
|Aryn the aforementioned *Haffan* monster-hunter is now trying to sneak up on the bear she was hunting; the GM calls for a *variable check*, her *Stealth* versus the bear's *Perception*.
|The TN for Aryn's Stealth check is 65, and the TN for the bear's Perception is 55.
|Aryn's player rolls 51, while the GM rolls a 42 for the bear, so both Aryn and the bear partially succeed.
|The GM decides that Aryn makes a little too much noise, which spooks the bear — it hasn't spotted her *yet*, but it's aware that something is off and will begin looking around to see what's wrong.
|


#### Ordered Checks

Sometimes it only makes sense to call for one character’s check if the other character has already succeeded (or failed); we call these **ordered checks**.
When making an ordered check, one character rolls their check first, and the other character only roll their check if it is needed.
(Note that the result of the first character's roll might determine *what kind* of check the second character needs to roll.)

### Defaulting

Sometimes a character doesn’t have the specific skill that they’d need to make a check — for example, a character might be trying to argue a legal case without having ranks in *Protocol*, *Knowledge: Law* or *Profession: Lawyer*; or a character might be trying to sneak past a guard without having ranks in *Stealth*.
In these cases, the character might be allowed to use a *related* skill at a penalty, or they might be allowed to use the *linked aptitude* for the skill that they don’t have; we call this **defaulting**.

The GM decides whether or not a character can default, and what they will default to.

In the first case, the GM might decide that the character can default to their *Persuasion*, with a -30 penalty (large penalties are normal when defaulting, as the character is being allowed to cheat the skill system a bit).
In the second case, the GM might allow the character to roll a check against their COO (that is, COO×1), since anybody can *try* to move stealthily, trained sneak-thief or no.
(When a character defaults to an *aptitude*, a smaller penalty is usually used, or the penalty might be waived entirely — if the character has no ranks in the skill, they're already in enough trouble\!)

[[gmguidance | When should we use checks]]
|
|When is a check called for, and what type? This depends on the situation.
|
|In unstructured play, the type of *consequences* that the GM expects often determine the kind of check to use.
|If a failure could have major consequences (like an attempt to hide an item you stole from the king while being searched by a guard), or two characters are *competing*, then a check is definitely called for.
|However, if the odds of failure are low, or the consequences of failure aren’t interesting, or the character can simply try again and again until they succeed (see *Trying Again*, below), then Simple Checks might be used, or the check might be waived all-together.
|
|Most mundane actions don’t require checks.
|A character can make the half-day’s walk to a neighboring town, cook a meal or speak in a language they know without requiring a check.
|
|Characters can also perform simple tasks using skills that they have *basic proficiency* in without requiring a check — we say that a character has *basic proficiency* in a skill if they have 10 ranks in that skill.
|Someone with 10 ranks in Profession: Cook can make a simple meal, someone with 10 ranks in Unarmed Combat can strike a target dummy, and someone with 10 ranks in Search can identify some obvious hiding spots without requiring a check.
|
|The rules for Initiative Order (and Combat) and Down Time are more specific; see Initiative Order and Down-Time below, and the *Combat* chapter for more information.
|


[[gmguidance | Trying Again]]
|
| Sometimes, if there is no particular consequence for failing, players might be able to simply repeat a test until they succeed; in these cases, it is often better to use a *simple-success check*.
| 
| For example, if a character is trying force open a door partly blocked by rubble, a *Feat of Strength* check might be called for.
| However, if nothing is threatening the players, they might be able to simply try again and again until they succeed.
| In this case, you should consider calling for a simple-success check; success might mean that they succeed easily or quickly, while failure would mean that many tries are required, or that some minor consequence is incurred (like fatigue, or damage to the door so that it can't' be closed).
|
| Similarly, if the players are trying to solve a riddle that will open a magic door, but there is nothing that would stop them from simply trying again and again, it might be a better idea to use one simple success check to find out how long it takes them to solve the riddle.
|
| As an optional rule, in a situation where individual checks are called for, in order to prevent abuses, GMs may apply a cumulative -10 penalty for each time a player *tries again*.
| This makes some sense, as a character that failed a check presumably failed for a reason, and that reason likely still applies if circumstances have not changed.


[[gmguidance | Repeated Individual Skill Checks]]
|
| Sometimes, there are situations where several members of the party could attempt the same task in sequence; for example, if the players are trying to search a room, then each person could make their own Search test, one after the other.
|
| This is usually not a good idea; this makes it very difficult for the party to fail, since they’ll have several separate attempts; it makes each individual test less interesting, since the next person will just try if the current person fails; and it can slow the game down dramatically.
|
| Instead, we recommend the GM require one character make one test on behalf of the party; that character — usually the one with the highest rating in the skill in question — should “take the lead,” and the other party-members should assist (if they can, see *Skill Modifiers*).


[[gmguidance | Picking a Check]]
|
|So, you’ve decided that a check is called for — but what check should you
|use? Sometimes it can be tricky to decide.
|
|One question to ask yourself is, “is the thing my character is doing the
|kind of thing that someone could have *learned* how to do, coming from
|their background?” Plenty of things are, like riding a horse, bartering
|with a bar-keep, sneaking through a dark alley, or negotiating a
|treaty — but, some things *aren’t*, like fighting off a disease (which
|people don’t learn to do — or do consciously at all\!) or solving a
|mystery (“detective” is certainly a job a person could learn to have,
|for example, but it is not a common one in the world of *Renaissance*).
|
|In the first case — for something that someone could have learned to do — a
|skill check is appropriate. Note that you don’t necessarily have to pick
|one single, correct skill; the skill system has a degree of overlap, so
|your players might have more than one skill they could choose from. It’s
|also perfectly acceptable to ask them what skills they have that they
|think might apply, and to vary the results they get based on which skill
|they ultimately. For example, if Ven has both Knowledge: Natural
|Philosophy and Spellcraft, she could use either to attempt to analyze a
|note with strange, technical writing on it, and she might glean
|different insights from it based on which she decides to use.
|
|In the second case — the player is trying to do something that most people
|don’t need to learn to do, or do consciously at all — a check against some
|combination of aptitudes is usually the right idea. You can pick from
|the *sample checks* above, or make up your own. To pick the combination
|of aptitudes you want to use, think about the mental faculties (or
|physical properties) that they’re going to need to succeed. If
|self-control is important, WIL should be included; if quick reflexes
|help, COO should be a factor; if their physical resiliency is being
|tested, then DUR can be used; and so on. Most of the time, it’s a good
|idea to mix 2 or 3 aptitudes.
|
|Note that some rules reference types of sample checks specifically. For
|example, some traits give you bonuses to *resist fear* or *feats of strength* checks. It’s a good idea to let players keep the benefits of those traits (for example) on checks that could reasonably be called a *feat of strength*, even if you don’t use the *feat of strength* check as it’s listed. (A player might ask, “is this a feat of strength?”, or you could tell them to “roll SOM×2, as a feat of strength” or “feat-of-strength effects apply”.)
|
|In unusual cases, you can have players make a check against a single
|aptitude (as in, a WIL×1 check). Such a check is very difficult to pass,
|and thus should represent a powerful force (like a spirit). However, it
|is worth noting that very powerful beings like spirits might produce
|magical effects that cannot be resisted at all; not every effect has to
|allow a player to check to resist.
|
|You also *can* have players mix aptitudes in more complex ways — having
|people use four aptitudes and divide by two, for example — but this is
|almost always a bad idea, since the increase in complexity is pretty
|much never worth the increase in fidelity (that is, in better
|representing just exactly what is being tested).
|
|In the last case — a player is trying to do something that isn’t covered
|by a skill that they have, possibly a skill that it would be unusual for
|anyone to have — you can allow a player to *default* (see above), either
|to a related skill that they do have, or to the aptitude that would be
|linked to the skill they don’t have. Don’t rush *too* quickly to the
|decision that a character needs an exotic skill; if the player is trying
|to do something that someone in the Commonwealth could reasonably have
|learned to do, then they shouldn’t need an exotic skill.
|
|The reverse, of course, can also be true; if the skill-set the character
|is trying to have is bizarre, unusual and difficult-to-explain for
|someone from the Commonwealth, then it probably should have been an
|exotic skill. Somewhere, someone in the Commonwealth *could possibly* be
|working on a Babbage Engine, and so a player character *could possibly*
|take ranks in Exotic Skill: Programming — but programming a Babbage Engine
|certainly isn’t covered by either Knowledge: Math or Craft: Clockwork.
|This is why players should discuss their characters with their GMs
|before starting play.


### Common Checks

The table below lists several *common checks* and their associated TNs.

| Check | Target Number (TN) |
| ----- | ------------------ |
| Skill Check | Skill's Linked Aptitude + Ranks in Skill |
| Resist Intimidation | WIL + SAV |
| Overcome Fear | WIL × 2 |
| Resist Social Manipulation | SAV + INT |
| Difficult Recall | COG × 3 |
| Take a Chance, Stroke of Luck | Luck × 10 |
| Make A Guess | INT × 3 |
| Get a Hint | INT × 3 |
| Solve a Puzzle | COG × 3 |
| Feat of Strength | SOM + STR |
| Feat of Endurance | DUR + WIL |
| React Quickly | COO×3 |
| Catch Something | COO×3 |
| Difficult use of Language | INT×3 |

Of course, any check can have modifiers (see below).
*Proficiencies* and *specializations* may also apply to some skill checks (again, see below).

Note that *Luck* above refers to the character's *Luck stat*, not the number of *Luck Points* that the character currently has.

Of course, this list is not exhaustive; GMs can call for other types of checks.

*Skill checks* are the most common type of check; they're describe above, and more details are provided below and in the *Skills* chapter.

*Resist Intimidation* is used when one character wants to resist another character's attempt to *intimidate* them, with the *Intimidate* skill.
*Overcome Fear* is normally called for when a character encounters something particularly terrifying (which includes some *Spirits* and *Powers*, see *The Supernatural*, *Cheating Reality*, *Classes*, and *Powers*.)

*Difficult Recall* is called for when a character attempting to recall something that would be difficult to remember — like a minor detail they may not have noticed, something that occurred when they where distracted, or something that happened long ago.
(Normally, the character can be assumed to remember anything that the *player* remembers — or wrote down in their notes; this test is appropriate if some detail is so minor or arbitrary that it is unlikely that a character would have remembered it, or if the player has forgotten something that they should have remembered and needs the GM to remind them.)

Is that dropped crossbow loaded?
Does that guard speak Commonwealth Standard?
A character has challenged a Great Spirit to a dice game; do they win?
You can *Take a Chance* or hope for a *Stroke of Luck* in situations like these.

Sometimes a character just needs to make a guess; other times, the players might just be stuck, and they need a hint.
When this happens, they can *Make a Guess* or *Get a Hint* from the GM.

Whether it's a simple *number-puzzle* or a complex *cypher*, sometimes a character just needs to apply their intellect to solve a puzzle; when this happens, they're *Solving a Puzzle*.

Sometimes, characters need to perform some heroic *feat of strength*; they might need to break down a door, bend the bars of a jail window, or rip the stake they're tied to out of the wall.
Other times, they might need to perform some *feat of endurance* to endure a great hardship (see *Common Hazards*).

Sometimes characters just need to *react quickly* to their environment — maybe to dive out of the way of some falling debris or catch the ledge on the way to a fall.
Or they may just need to catch something.

*Difficult uses of Language* include trying to recognize a language that the character doesn't know (but might have seen), trying to get the gist of a text written in a language that is *related to* one that the characters speak (as Weal is related to Old Imperial, see *Languages*), or trying to speak or write in a particular accent or style.

### Modifiers

Modifiers might apply to any check.
Some modifiers might come from special features that a character has; these modifiers apply whenever the feature says that they do.
Other modifiers might represent a particular task being *more* or *less* difficult, while others might represent some circumstance that impedes or aids a character; these modifiers apply at the GM's discretion.

  - Being assisted: +10 per character assisting, maximum +30. Assisting
    characters must have 10 Ranks in a useful skill (but it doesn't have
    to be the *same* skill). The GM may rule that certain tests cannot
    be assisted.
    
      - Attack, Stealth and Perception tests normally cannot be
        assisted.

  - Related Skill:
    
      - receive a bonus on one Test for having ranks in a related skill
        (for example, Knowledge: Theology might assist Profession:
        Cleric)
      - 10-24 Ranks: +10
      - 25-39 Ranks: +20
      - 40+ Ranks: +30
      - You may only use one related skill.

  - Specialization:
    
      - skills can have *specializations*.
    
      - Character recieves +10 when Specialization applies; there is *no
        effect *(including *no penalty*) when Specialization does not
        apply
    
      - Any given skill can only have one specialization. You can’t have
        both a \[Short Swords\] and a \[Knives\] Specialization for
        One-Handed Weapons, for example.
    
      - You can acquire specializations for your skills during character
        creation: see also *Character Creation*.
    
      - Field Skills and Proficiency Skills can also have
        specializations, for example:
        
          - Art: Painting \[Landscapes\], where Art is a field skill,
            Painting is the field, and \[Landscapes\] is the
            specialization.
          - One-Handed Melee Weapons \[Swords\], where Swords is one of
            the proficiencies that the character has.

  - Proficiencies:

      - When using a proficiency skill, you take a -20 penalty if you don't have an appropriate *proficiency* for what you are trying to do; see *Proficiency Skills* in *Skills*.

  - Difficulty Modifiers
    
      - Run from Very Easy (+30) to Very Hard (-30), and all shades
        in-between.

  - Taking your Time and Rushing:
    
      - only applies to Task Actions and Jobs
      - Taking your Time: for every +50% increase in timeframe, +10 to
        the check (up to +150% time for +30)
      - Rushing: for every -25% *reduction* in timeframe, -10 to the
        check (up to -75% for -30)

  - Situational Modifiers
    
      - Lots of other things might provide modifiers\! The GM may assign
        modifiers from situation as appropriate.

  - Passive Tests: Usually, characters will use their skills actively.
    Sometimes, the GM will roll a test on behalf of the player — for
    example, to see if they have noticed something (a Perception test),
    realized something (a COG\*3 test), or has some piece of knowledge
    (a Profession, Craft or Knowledge check). These are *Passive Tests*,
    since they are made “automatically” on the player’s behalf. Passive
    checks have a -20 penalty (the players should be proactive in using
    their skills, after all). Generally, Passive tests are made in
    secret by the GM; if a player later makes an appropriate test, then
    the result of the test that the player made takes precedence
    (although events may unfold in such a way that a player cannot call
    for such a check later).

  - Common Knowledge: if a player has 10 or more ranks in a given skill,
    they can be assumed to have common knowledge appropriate to that
    skill (that is, without being required to make a test).

## Actions

Types of actions

  - Standard actions
    
      - An action that doesn’t take much time, but that you need to
        focus on.
      - Examples: attacking with a weapon, knocking over a dresser,
        kicking in a door.

  - Quick actions
    
      - An action that doesn’t take much time, and that you don’t need
        to focus on.
      - Examples: moving, yelling something, retrieving a stored item,
        drawing a weapon.

  - Task actions
    
      - An action that takes time (but less than a day), and that you
        need to focus on.
      - Examples: brewing a potion, picking a lock, buying goods in town
      - Note: Tasks that take 8 hours of work or more should generally
        be handled as Jobs and done during Down-Time.

  - Sustained actions
    
      - An action that takes time, but that you don’t need to focus on,
        so you can do it while doing something else.
    
      - Examples: keeping an eye out for a mark during an opera, leaving
        a trail of bread-crumbs while traveling, memorizing a route
        while being forced to march, *sustaining powers.*
    
      - You can take other actions while maintaining a Sustained Action,
        and you can maintain more than one Sustain action at a time.
        
          - However, maintaining multiple Sustained Actions is
            distracting; you take a -10 penalty to all tests for each
            Sustained Action you maintain beyond the first.
          - So, for example, if you maintain three Sustained Actions,
            you take a -20 penalty to all tests.
    
      - Sustain actions don't have a specific upper limit for how long
        you can maintain them, but your GM might not allow you to
        maintain them for more than a reasonable amount of time, or
        might require additional checks or impose additional
        consequences.

  - Jobs
    
      - Jobs have time-frames measured in *shifts.* A shift is one
        continuous eight-hour work day.
      - Used mainly during Down-Time Play

  - Since the MoS (and MoF) of a test can determine how long an action
    takes, If a Task Action or Job requires a check, that check should
    be made when the action is *begun.*
    
      - If the check is failed, the character in question works for 25%
        of the Task Action’s timeframe or Job’s shifts (on a Failure),
        or 50% (on an Exceptional Failure), before realizing that the
        task will fail (and, presumably, stopping).

## Modes of Play

*Renaissance* has three main modes of play: *Unstructured*, *Turn Order* and *Down-Time*.

**Unstructured** play is the "normal" mode; it works a little like a conversation between the GM and the players.
In Unstructured Play, the GM describes the scene and situation — possibly with the aid of a map, drawing, or other visual aide.
The players then ask questions and declare actions.
The GM then answers those questions and "resolves" those actions (by telling player what effects their actions have).
Of course, players don't always succeed; if success is uncertain — or if two characters are competing — the GM can call for a *check* (see above).

As the name implies, in unstructured play, there are no particular rules about action allotment  or turn order (as opposed to Turn Order and Down-Time).
However, the GM may limit the actions allowed in a given situation (for example, a character can’t try to build a tool as a one-hour Task Action if they’re in a building that’s burning down.)

In **turn-order** play, players take *turns* in *initiative order*.
To determine what order players take turns in, they roll their *initiative*; each player gets a *turn* in decreasing order of initiative (that is, the character with the highest initiative roll goes first).
To roll their **initiative**, a player rolls 1d10 and adds their *Initiative Modifier*.
The GM breaks ties arbitrarily (it's common to let the highest *initiative modifier* before lower initiative modifiers).

Each turn gets a specific **action allotment**—that is, the number and type of actions that a character is allowed to attempt during their turn (see *Actions* above).

When GM's begin **turn order** play, they should tell player what formula to use for their *initiative modifier*, and what *action allotment* each turn is going to get.
If the GM includes Task Actions in the action allotment, then the GM should specify *how much time* a character can contribute to a Task Action during their turn–for example, the GM might include “Five minute task actions” in the action allotment.
On the other hand, if the GM doesn’t include Task Actions in the action allotment, then progress towards Task Actions won't be tracked during that turn-order sequence; a player who wishes to continue working on a Task Action simply looses their turn(s).
Likewise, Jobs aren’t tracked during Turn Order; a player who wants to keep working on a Job during Turn Order simply looses their turn(s).

Combat is a special case of Turn Order play with extensive rules, including a specific initiative modifier and action allotment; see *Combat*.

Finally, **Down-Time** focuses on long-term actions.
Down-Time is measured in *shifts*: on any day, a character can spend 8 hours working on a Job; if they do, that Job is one Shift closer to being complete.

Your GM might allow you to work more or less time, and to earn shifts more slowly or quickly; this is entirely at the GM's discretion.
In particular, races that don’t need to sleep have an obvious opportunity to earn more than one Shift in a day.

As an alternative to working on a Job, a player can spend a shift to complete one or more task actions — recall that Task Actions should take less than 8 hours, so you should always be able to finish at least one Task Action per day.

[[clarification | Interrupting Actions]]
|
|Sometimes it’s possible to interrupt an action — if one character breaks into the workshop where another character is working, for example.
|We don’t provide fixed rules for this, because no fixed set of rules could be comprehensive without being unwieldy.
|GMs are encouraged to adjudicate such situations as they arise.


## Duration of Play

We usually break games up into *adventures*, *sessions* and *scenes*.
An adventure consists of one "story ark"—for example, the party's attempt to determine why a *forrest of rapidly-growing trees consumed a town*, or *to defeat a supernatural, ichor-spreading monster*.
A *session* is one continuous play-session — from the time that the players meet to when they go home.
A *scene* is one specific scenario in an adventure — one large fight, one social encounter, or one infiltration attempt.
(Note that we mean "scene" in an informal sense — you aren't expected to divide your scenarios into explicit scenes, and you don't need to tell your players when a scene begins or ends).

The "archetypical" Renaissance adventure is assumed to consist of between 5 and 9 sessions, with each session taking about 4 hours and having between three and six scenes in each session.
Of course, not every group will break their adventures up the way the authors normally do; some may prefer, for example, much longer sessions.

Some game mechanisms depend on *adventures*, *sessions* and *scenes*—for example, characters gain one *Luck Point* at the beginning of each *session* (see *Luck* in *Cheating Reality*).
If your group plays very long (or very short) sessions, your GM may need to adjust how often session-dependent events occur.
The GM can declare a *session break* (or "long rest," if you prefer); this is treated like a normal break between sessions, during which, for example, characters will gain a *Luck Point*.

[[clarification]]
|
|Here, "session break" is a special keyword that is important to the rules; we're not saying that the GM has to give you a Luck Point every time the group takes a five-minute bathroom break.
