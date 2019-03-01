---
title: Skills and Special Numbers
rules:
- skills
---

| Skill      | Aptitude       | Categories       |
| ---------- | -------------- | ---------------- |
{% for skill in rules.skills -%}
| {{ skill.name }} | {{ skill.aptitude }} | 
{%- for cat in skill.categories -%}{{ cat }}{%- if not loop.last -%}, {% endif %}{% endfor %} |
{% endfor %}

## Unusual Skills

Sometimes you'll want your character to be able to do something that
isn't exactly covered by a skill---like tracking game through the
woods.

While players can use an Exotic Skill to take ranks in an unusual
skill, they are usually better served by taking an existing skill
with a descriptive specialization. For example, players would almost
always be better off taking Search [Tracking] than taking Exotic
Skill: Tracking.

The Knowledge and Profession skills can also be used to establish a
specific special skill-set for a character---for example,
Profession: Hunter or Interest: Tracking.

In addition to thinking about how you want to represent your
character's talents, think about how you want to be able to _use_
the skill during a game.

If you're unsure about a skill selection, you should discuss it with
the GM; make sure that the GM understands not only what you want the
skill to represent, but what you want to be able to _do_ with it,
and be sure that you and the GM agree with not only what the skill
is supposed to represent, but what it's supposed to do and how it's
supposed to work.

## Gotchas and Confusing Cases

-   Disguise only covers the _physical_ half of pretending to be someone
    else; for the social half -- that is, to talk to people without being
    discovered -- you'll also need Deception.
-   Search is used to actively search an area for something; it takes
    time, and you move around. Perception is usually used for noticing
    things quickly -- seeing things when you enter a room, as opposed to
    after looking around. Search is also used to track someone or
    something.
-   Control is used to manage your own magical energies, and to develop
    sleights; it should not be used to represent a characters "willpower," that's the WIL attribute.
-   Investigate is primarily a mental action: it can be used to solve a
    mystery, given clues that have already be found. To actually find
    clues (at a crime scene, for example), use Search.
-   Normally, solving a crime would be treated as Solving a Logic Puzzle
    (requiring a COG × 3 check, as below). If you would like to build a
    detective character, consider using Profession: Detective or
    Profession: Investigator to represent your character's ability to
    solve mysteries.

## Special Numbers:

Sometimes no skill applies: in these cases, use combinations of
Aptitudes. Some common examples follow:

-   Resist Intimidation / Overcome Fear: WIL × 2
-   Resist Social Manipulation: SAV + INT
-   Recall Personal Experience: COG × 3
-   Take a Chance, Get Lucky: Total Luck × 10 
-   Make A Guess (or Get a Hint): INT × 3
-   Solve a Logic Puzzle: COG × 3
-   Feat of Strength (bend bars, break down a door): SOM + STR
-   Feat of Endurance (endure a long march, resist disease, survive
    starvation): DUR + WIL
-   React Quickly/Catch Something: COO × 3

## Skill List

{% for skill in rules.skills %}
### {{ skill.name }} ({{ skill.aptitude }}{% if skill.fields %}, Field Skill{% endif %})
Categories: {% for cat in skill.categories -%}
{{ cat }}{%- if not loop.last -%}, {% endif %}
{% endfor %}

{{ skill.description }}

{% if skill.specializations %}
*Example Specializations:* {{ skill.specializations }}

{% endif %}

{% if skill.fields %}
*Example Fields:* {{ skill.fields}}

{% endif %}
{% endfor %}

-   Pointed Weapons (SOM)

    -   Active, Combat, Physical
    -   For putting spear in other man.

-   Pole-Arms (SOM)

    -   Active, Combat, Physical
    -   Skill used for pole-arms.
    -   Pole-arm classification "supersedes" other weapon
        classification---meaning that halberds and goedendags are
        pole-arms rather than bladed or blunt weapons.

-   Profession (COG, Field Skill)

    -   Passive, Technical, Trade
    -   Represents your knowledge and experience within a specific skill
        or trade.
    -   Used for checks testing your knowledge about a profession, or
        for your ability to operate as a professional for a long period
        of time.
    -   Can be used to represent you practice a trade for profit
        (particularly during down-time).
    -   For actually producing an item, see Craft
    -   Sample Fields: Brewer, Carpenter, Cobbler, Cook, Doctor,
        Explorer, Farmer, Mason, Merchant, Painter, Priest, Professor,
        Sailor, Scholar, Smuggler, Soldier, Thug, Trader

-   Projectile Weapons (COO)

    -   Active, Attack, Combat, Physical, Ranged Attack
    -   Used with bows and crossbows.
    -   Thrown weapons use _Thrown Weapons_

-   Protocol (SAV)

    -   Passive, Knowledge, Social
    -   Used to represent your ability to handle the unwritten rules of
        social interaction, both simple and complex.
    -   Can be used to navigate complex social situations, estimate or
        follow social protocols, make a good impression in social
        interaction.
    -   Can be used to negotiate, for example in a legal debate or
        hostage negotiation.
    -   Can be used to _recover gracefully_ after a roll-playing error
        (like saying something that your character would never say).
    -   Very exotic, unusual or secretive cultures use the Exotic
        Culture skill.
    -   Negotiating prices and trading uses the Barter skill.

-   Read (SAV)

    -   Active, Social
    -   As in, Read Body Language; appraise others' motives in social
        situations.
    -   Used _unopposed_ when used to assess someone's mood.
    -   Used to oppose Deception.

-   Research (COG)

    -   Active, Knowledge, Mental
    -   Primarily covers searching for information in books,
        collections, museums or libraries.
    -   For finding interesting items -- including searching for clues
        \-- use Search.
    -   For drawing conclusions and analyzing evidence, use
        Investigation.
    -   For drawing conclusions from technical information, use an
        appropriate Knowledge or Profession skill.

-   Ride (REF)

    -   Active, Movement, Physical
    -   Ride checks represent your skill at riding steeds (and possibly
        other conveyances, magical and mundane).
    -   A character with basic competence (that is, 10 ranks in ride)
        doesn't need to make a Ride check for normal movement with a
        mount: if you know how to ride a horse, you don't need to make a
        test to ride to town.
    -   Ride is a "movement skill," commonly used either for difficult
        maneuvers or for chases (see _Movement Modes_).
    -   Can specialize in an individual creature (like Horses) or an
        individual task (Racing).
    -   Very unusual creatures should use the Exotic Mount skill, see
        the Exotic Skill.

-   Search (INT)

    -   Active, Physical
    -   Used to find interesting, possibly-hidden items (including
        artifacts at a ruin, evidence at a crime scene, a secret door
        hidden in a library).
    -   Can also be used to search someone for concealed items (opposed
        by their Sleight of Hand if they have actually attempted to
        conceal something).
    -   Can also be used to track another creature (opposed by their
        Stealth if they're trying to avoid being followed).
    -   Search is used when you are going to move around an area and
        investigate over time. For "at a glance" tests, use Perception.

-   Sleight of Hand (COO)

    -   Active, Physical
    -   Used for pick-pocketing, hiding (or retrieving) objects on your
        person, misdirection and simple tricks and illusions.
    -   Can be opposed by the Perception of anyone watching you.
    -   Example Specializations: illusions, pick-pocketing.

-   Spellcraft (COG)

    -   Active, Physical, Mental, Technical
    -   Your ability to manipulate magic to create spells.
    -   Used to design, learn and cast spells.
    -   Knowledge about the workings of magic is represented by
        Knowledge: Magic, while skill as a professional spellcaster is
        represented by Profession: Mage.
    -   Example Specializations: by power, by type of magic
        (conjuration, teleportation, etc.).

-   Sport (SOM, Field)

    -   Active, Physical
    -   Represents your skill in a specific sport.
    -   Example Fields: by specific sports

-   Survival (INT)

    -   Active, Physical
    -   Represents your ability so survive in the wilds, away from
        civilization.
    -   Can be used to build shelters, hunt, find food and water in the
        wild, identify hazardous natural features, know how to survive
        in hostile environments like deserts and tundras.
    -   Special: you can use Survival \[Urban] to represent a
        character's ability to survive on the streets of a large city.
    -   Example Specializations: by terrain type (woodlands, jungles,
        deserts, tundras, etc.)

-   Stealth (COO)

    -   Active, Combat, Physical
    -   Represents your ability to go unnoticed.
    -   Used for sneaking about; if you're trying to sneak past an
        observer, used opposed by the guard's Perception.
    -   Can be used to blend in to a crowd, in which case it's usually
        used unopposed.
    -   If you are trying to follow someone without being noticed, then
        it is opposed by that person's Perception.
    -   Can be used to travel without leaving a trail.
    -   To avoid being seen, you normally need something to hide behind;
        it's hard to hide from someone if they can plainly see you.
    -   Some sense (like Scent or Mage Sight) might also render Stealth
        impractical.
    -   Sample Specializations: Sneaking, Blending In

-   Thrown Weapon (COO)

    -   Active, Attack, Combat, Physical, Ranged Attack
    -   Used to attack a target by throwing something at them.
    -   Used to throw explosives, daggers, darts and axes.

-   Unarmed (SOM)

    -   Active, Attack, Combat, Melee Attack, Physical
    -   Used to represent your skill at hand-to-hand combat.
    -   Covers natural weapons too (like claws and fangs).
