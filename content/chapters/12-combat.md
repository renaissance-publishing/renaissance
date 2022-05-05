---
title: "Combat"
---

Unlike other parts of the game, *Combat* has fairly specific rules.

## Taking Turns

Combat is a special case of *Turn Order* play (see *Basic Rules*) using the following structure:

- **Initiative Modifier**: in combat, a character's *Initiative Modifier* (INIT) is their (INT + COO) ÷ 5 (see the Derived Stat in *Character Creation*).
- **Action allotment**:
  - either one *Standard Action* and one *Quick Action*, or
  - three Quick Actions.

Since *Task Actions* are not given in the action allotment, Task Actions are not tracked during Combat; see *Turn Order Play*.
In combat, a turn is about 3 seconds; therefore, there are about 20 turns in a minute.

## The Combat Grid

We usually track positions and movement in combat using a *square grid*, with each square being 1m to a side.
Most creatures (those that are Small-, Normal- or Large-sized) usually take up one square, and can reach (and thus threaten) the adjacent squares.
Distances (like ranges for attacks) are usually measured directly and then rounded to the nearest whole meter.
(That is, we usually use a *euclidian* metric; this is different from some other games.)
Distances while moving are also directly measured, although they depend on the exact path travelled (if you can't easily measure a path, you can break it into "cardinal" and "diagnoal" steps, and assume that a "diagonal step" covers 1.5 meters).

Traditionally, the direction a character is *facing* is not tracked.

[[designnote]]
|Though we will assume a combat grid with one-meter squares in this guide, nothing prevents you from using other combat systems — like hex-grids or miniatures — as long as the rules for measuring distance and determining movement are well-defined.
|Supporting these kinds of scenarios are why we've tried to give all distances in *meters* rather than *squares*.

## Moving Around

### Movement Modes

As a quick action, a character may *move* using one of their *movements modes*.
Movement modes have a *base* and *full* rate; they can move up to their *full rate*, but if they move more than their *base* rate, they take a -10 penalty to all physical actions until the beginning of their next turn.
(Essentially, you can walk or run, but running imposes a -10 penalty.)

### Stunts

Characters can also perform *stunts*.
**Stunts** are used when your character attempts unusual, difficult maneuvers — when they jump, tumble, flip, climb (if they don’t have Climb as a movement mode), swing and so on.

The details of stunts are largely left open to the imagination of players and the discretion of GMs.
The type of action varies: rolling under a hazard might be a quick action, but climbing a trellis might be a standard action (again, for a character without Climb as a movement mode).
Similarly, how far the character is moved will also vary (in general, GMs should move characters by either their base or full rates).
Stunts almost always require a test using an appropriate movement skill (this is usually Athletics for humanoid creatures).

Stunts may have other affects besides simply moving a character; a dive-and-roll may allow a character to end their turn prone behind cover, for example, or a flip off a table may allow a character to vaults over an enemy and land facing their back.

Examples for a *Humanoid* character are given in the table below:

| Stunt | Check | Result |
| ----- | ----- | ------ |
| Vaulting a *fence* or *counter* | Athletics (Parkour) at +10 | Clear obstacle while keeping *momentum* |
| Diving Roll | Athletics (Parkour) | Advance several spaces while avoiding attacks, clear a low obstacle |
| Corner Wall Kick | Athletics (Parkour) | Move around a character quickly, attacking from behind |

### Unusual Movement

Sometimes, characters might attempt to move in a way that isn't directly covered by one of their *Movement Modes*; we call this **unusual movement**.
If a Human climbs a tree, a Herder crawls along the ground, or a Clay Man attempts to support itself on two psuedopods and "walk" like a humanoid, then they are using *unusual movement*.

Unlike a *stunt*, unusual movement isn't necessarily difficult, and so it usually *doesn't* require a check — although it might require *basic proficiency* in an appropriate skill (like *Athletics*), and it might require a specific *proficiency*.

Unusual Movement is usually less efficient than movement directly covered by a movement mode.
Characters using unusual movement usually move at half the base rate for their *most applicable* movement.
(For a *Humanoid* character, this is usually their *Foot* movement.)
Unusual movement is also often exhausting; characters can't usually use unusual movement to cover great distances (at least without requiring an athletics check).

Of course, the unusual movement that a character wants to use has to be physically possible; a Human character can't choose to *flap their arms and fly* as an unusual movement.

Examples for a *Humanoid* character are given in the table below:

| Unusual Movement | Rate                | Tags       |
| ---------------- | ------------------- | ---------- |
| Climbing         | (Base for Foot) ÷ 2 | Exhausting |
| Swimming         | Base for Foot       | Exhausting |
| Crawling         | (Base for Foot) ÷ 2 |            |

[[clarification | Difficult Terrain]]
| Difficult terrain can also be a factor when moving around in combat; We cover *difficult terrain* in *Common Hazards*

### Charging

Sometimes you want to have some momentum behind a blow.
A character can declare a *charge* before they move; they can then move up to the *Full* rate for the movement mode they're using to charge.
Because a charging character is attempting to build up momentum, they will always be treated as if they had moved more than their *base* rate (and thus take a -10 penalty to their physical actions) regardless of how far they actually move.
(A "charging move" otherwise uses all the normal rules for movement, and is a Quick Action)

After declaring a charge, if the character then moves *far enough to build up speed* (usually 3m), they then deal +DB DV to all their (physical, melee) attacks for the remainder of their turn.

[[playerguidance]]
|There are some "they cans" and "if thens" above; let's walk through that.
|A turn is a *Quick Action* and a *Standard Action*; that means that, in practice, a player declares a charge, moves up to their full movement (a Quick Action), and then makes an attack (a Standard Action).
|That attack check has a -10 penalty (for the Full movement), but deals +DB DV.
|
|Note that they deal +DB DV to *all* their physical attacks.
|If a character makes *more than one attack* (as they can if they have *more than one weapon*, see below), then each attack gets the +DB DV (and each attack check takes the -10 penalty for the movement, on top of any other penalties for wielding multiple weapons and making multiple attacks).

[[designnote]]
|This implementation of charging is a bit out of place.
|
|Most mechanisms we've been able to package into fairly atomic actions; charging is an exception.
|Charging isn't one action; instead, it's a thing you declare at the beginning of your turn, that then adjusts your damage at the end, *if* you meet some conditions.
|
|Charging is something of a least-bad design; we're working on it.

Characters can *brace* to receive a charge; see *Receiving a Charge*, below.

### The "Single-Movement" Rule

Normally, a character is only allowed to use *one* of their *actions* to move in any given turn; that is, they cannot use three Quick Actions to move with a Movement Mode three times, for example.
We call this the **Single-Movement Rule**.

The Single-Movement Rule is subject to the **Follow-Through Exception**.
At the GM's discretion, a character can use one of their *Movement Modes* immediately before or after using some *Stunts*.
For example, a character could use a Quick Action to *run*, and then use another *Quick Action* to perform a *hand-spring* (as a *Stunt*); or they could use a *Quick Action* to vault a counter (as a *Stunt*), and then break into a run (as a *Quick Action*).

## Attacking

### Attack Basics

Attacking a target — whether in melee, with a ranged weapon, or some other way — is a Standard Action requiring an Ordered Opposed Check.
First, the attacker rolls a check using their attack skill; then, if the attacker succeeded, the defender rolls a check using their defence skill.
If the attacker wins, then the attack hits, and the defender takes the given *damage value* (DV) (most weapons, natural weapons, and powers will list their damage; it is usually partly random, requiring a die roll); if the defender wins, the attack missed, and the defender takes no damage.

If the attacker has an MoS of 30 or more, they gain +5 DV.
If their MoS was 60 or more, they gain an *additional* +5 DV (for a total of +10 DV).
If the attacker scores a *critical success*, then the die-roll is *maximized* — for example, if the DV is 1d10+5, the defender would take 15 damage.

- Attacker MoS \> 30: +5 DV
- Attacker MoS \> 60: +5 more DV (+10 DV total)
- Attacker critical success: *maximize* dice

### Attack and Defense Skills

Generally, when attacking, characters use the *attack skill* appropriate to the weapon.
For most melee weapons, this will be either *Melee Weapons* or *Pole-Arms*.
For unarmed attacks (like punches, kicks, grabs, or throws) or attacks with natural weapons (like bites or claws), this is usually Unarmed Combat.

Defenders sometimes have a choice of skills.
Fray is the most general defense skill; it can be used to defend against most attacks (and many other hazards).
Defenders can also use their own melee attack skills to defend against melee attacks (assuming they have an appropriate weapon, of course); we refer to this as *parrying*.
For example, a character with a sword could use their *Melee Weapons* to defend against someone attacking them with a halberd.
Characters with *basic proficiency* in *Unarmed Combat* can also defend with that skill, although they will take a penalty when defending against an armed opponent (see *Unarmed Combat*, below).

Sometimes — for example, when moving evasively — characters can defend with *movement skills* (like Athletics).

Usually these methods of defense aren't *reactions*; see below.

### Melee Attacks

In order to make a melee attack against a character, you normally need to be *armed* with a melee weapon, and they need to be within reach (but see also *Unarmed Combat* below).
Most melee weapons can be used against characters up to 1m away (in a combat grid with 1m squares, this means that you can attack characters in adjacent squares); some weapons have the *Reach* tag, and can be used against more distant targets (see the tag's description in *Items*).

You **threaten** any character that you could make a melee attack against.

### Ranged Attacks

Ranged attacks (projectile weapons, thrown weapons, and some powers) generally use the same rules as other types of attacks, with a few additions.

#### Range

Ranged attacks have **range increments**; they are given below, with their associated penalty.

- short: no modifier
- medium: -10
- long: -20
- extreme: -30

Most weapons and powers will list their ranges.
The categories are often given in order, separated by slashes.
For example, "Range: 50m/100m/150m/200m" would mean that *short range* is up to 50m, *medium range* is up to 100m, *long range* is up to 150m, and *extreme range* is up to 200m.

You can use the following guidelines for thrown attacks, adjusted for the weight and aerodynamics of the projectile:

- short: up to 5 meters
- medium: up to 15m
- long: up to 30m
- extreme: up to 45m

#### Scatter

Ranged attacks that miss may **scatter**.

We provide a certain amount of flexibility in determining scatter; mainly, it just needs to be random and reasonable.
GMs may use one of the following methods for scatter, or invent their own:

- Method 1: roll 2d10. One d10 indicates the scatter direction (with 1 being north, and counting around; for a square grid, there are 8 adjacent squares, so discard 9 and 10 results), and the other the distance (in meters).
- Method 2: with a physical table, roll 1d10. The result is the distance in meters, and the direction the dice is pointing indicates the scatter direction.

Scatter is mainly a concern when the weapon also has the Blast property; we usually don’t worry about where an arrow scatters to.

#### Point-Blank Attacks

A ranged attack against a target at point-blank range (that is, against a target in an adjacent space) suffers a -20 penalty.

#### Ammunition

Projectile weapons (like bows) require *ammunition*.

For most weapons, we don't track *common ammunition*; that is, they do not need to purchase ammunition separately, or keep track of how much they have and how much they have used.
We assume that ammunition is readily available enough that characters can always have *enough*.

We do, however, track *special ammunition*; this includes ammunition that is made of special materials, that is expensive, that is magical, or that is otherwise unusual.
It must be purchased separately, and must keep track of it as they expend it.

Additionally, some unusual weapons have costly or unusual ammo, and this must be also be purchased and tracked separately.
(If a weapon's normal ammunition has to be tracked, it will say so in its rules.)

#### Reloading

A weapon's description will specify what kind of action is required to reload the weapon (or that it cannot be reloaded, should that be the case).
Some weapons don't require a *discrete* action to be reloaded; *readying* an arrow, for example, is part of making an attack with a bow.

### Touch-Only and Indicate-Only Attacks

Sometimes, notably when using some powers, an attacker only needs to touch their target.
These use all the normal rules for an attack, except that they are easier: the attacker may use either COO+SOM+SOM or their Unarmed Combat skill (no proficiency required), and they receive a +20 bonus.
The defender takes a -20 penalty to their defence.

Similarly, sometimes, notably when using some Powers, an attacker only needs to direct an effect to a target – by pointing at their target, for example, or by fixing their gaze on the target.
These attacks work like normal ranged attacks, except that the attacker may use either 3×COO or their Ranged Weapons skill (no proficiency is required), and they receive a +20 bonus.
The defender takes a -20 penalty.

### Un-Aware Targets

Characters who are not aware that they are being attacked cannot defend 
The attacker must still roll their attack check, but it is *unnoposed*, and the defender takes damage if the attacker succeeds.
(PCs and major NPCs should usually be allowed a Perception Check to notice a hidden attacker.
Also, people usually take notice after they have been attacked.)

### Blind Attacks

Normally, characters don't threaten targets that they can't see; any attempt to hit such a target will fare little better than chance.
This means that an attack against a target that the attacker cannot see must either make a check for a *Stroke of Luck* or use a TN of 50, whichever is *worse*.

## Armor and Armor Penetration

Some characters have an **armor value** (*AV*); *Armor Values* usually come from either *worn armor*, *racial traits* (like Gnoll's *Thick Hide*), or *powers* (like *Master*).
Conversely, some damage sources (like *weapon attacks*) have an **armor penetration** (*AP*).

When a character takes *attack damage*, first subtract the attacks' *armor penetration* from the defenders *armor value*, then subtract the *remaining armor value* from the attack's *damage value*; the defender takes the remaining DV.
That is:

Defender's Damage = attack's *Damage Value* - (defender's *Armor Value* - attack's *Armor Penetration*)

See *Armors* in *Items* for further rules for worn armor.

[[clarification | When Does Armor Apply?]]
| Note that we specifically said *attack damage* above.
| The general rule is that armor applies to *attack damage*, but not to other sources of damage; a quilted doublet and mail won't help you if you've fallen from the top of a parapet, you're drowning, you're starving, or you're freezing to death.
| There are exceptions, of course, and your GM can always rule that armor applies (or doesn't) in a specific circumstance.

## Special Actions in Combat

### Drawing and Dropping Weapons

Drawing or sheathing a weapon is *Quick Action*; dropping a weapon is a *Free Action*.

### Aiming

A character can *aim* at a target (that they can see) as a *Quick Action*.
After doing so, they gain a +10 bonus to attacks against the target that they aimed at until the end of their turn.

(Note that the attack *does not* need to be a ranged attack; you can use the rules for *aiming* to carefully place a melee attack, for example.)

### Full Defense

During your turn, you may take a Standard Action to focus on defending yourself.
If you do, until your next turn starts, you receive a +20 bonus to checks to defend.

### Bracing

Weapons with the **Brace** tag can be used to prepare to receive a charge.

*Bracing* such a weapon to receive a charge is a *Standard Action*.
After bracing, until your next turn, if anyone *charges* you (see *Charging*), they provoke an *Attack of Opportunity* from you (see *Reactions*).
If you hit a charging character with a braced weapon, you deal +DB DV; however, you do not prevent them from completing the charge (by attacking you), unless you incapacitate them with your attack (by disabling them, or by dealing a wound and knocking them prone, for example).

### Strikes

A **strike** is a modification to a normal attack.
To make a strike, you take a penalty on your attack; if you score an Exceptional Success, in addition to the normal affects of the attack, you gain the listed Result.

You decide if your attack is going to be a strike before you make it (since you have to take a penalty on the attack).
An attack can only be one kind of Strike.
(You can’t take a -20 penalty to have an attack be both a Called Shot and a Knock Down, for example.)

- Called Shot
  - Penalty: -10
  - Result: you strike the target in a specified location (you pick the location before your attack).
  - This one is a catch-all, with results up to the GM.
  - Special: the attack gains the Precision tag

- Knock Down
  - Penalty: -10
  - Result: your opponent must attempt a SOM×2 check or be knocked *prone*.
  - Special: must be a melee attack.

- Maim
  - Penalty: -20
  - Result: You maim your opponent, removing a specific limb.
    You can use this to lop off a hand, break a knee or gouge out an eye.
  - Special: the attack gains the Precision tag.

- Mighty Blow
  - Penalty: -10
  - Result: You strike your opponent with particular force; you gain +DB to your DV.
  - Special: must be a melee attack.

- Strike an Armor Gap
  - Penalty: -10
  - Result: You strike a weak spot in the opponent’s Armor; you gain +DB to your AP.
  - Special: the attack gains the Precision tag.

### Maneuvers

A **maneuver** is like an attack, but it doesn't deal *damage*; instead, if the attacker succeeds, it has some other effect.
Each maneuver will list the type of action required, the check, and the results.

The following list is by no means exhaustive; players and GMs should feel free to devise and attempt new during play.

- Disarm
  - Action: Standard Action
  - Test: Attacker's *Melee attack* vs. defender's *Melee Attack* or Fray
  - Result: If the attacker wins, the defender is *disarmed*, forcing them to drop one held item (like a weapon or shield).
  - Special: the attacker picks the items to be dropped before the check is rolled.

- Feint
  - Action: Quick Action
  - Test: Attacker's *Deception* vs. defender’s *Resist Social Manipulation* or *Read*
  - Result: if the attacker wins, until the beginning of their next turn, the defender takes a -20 penalty to their defense.

- Grab
  - Action: Standard Action
  - Test: Attacker's *Unarmed Combat* vs. defender's *Fray* or *Unarmed Combat*.
  - Result: if the attacker wins, they *grab* the opponent.  The opponent cannot easily move or act.
    - The results are at the GM’s discretion, but normally grabbed characters cannot take any other actions besides attempting to escape the grab.
  - A grabbed character can attempt to break a grapple; this is an opposed check, the grabbed character's *Unarmed Combat* or *STR+SOM* versus the grabbing character's *Unarmed Combat* or *STR+SOM*.
    If the grabbed character wins, they break free.

- Trip
  - Action: Standard Action
  - Test: Attacker's *Melee Attack* vs. defender's *Fray*
  - Result: If the attacker wins, the defender falls *prone*.

### Special

- Catch
  - Some weapons are designed to *catch* an opponent’s weapon; these weapons have the *catch* tag.
  - When you are attacked while wielding a weapon with the *catch* tag, rather than defending as normal, you can decide to attempt to *catch* your opponent’s weapon.
  - This works like normal defence, except that you take a -10 penalty.
    If you win and score an exceptional success, then you have *caught* your opponent’s weapon (in addition to successfully defending against their attack).
  - While you have caught an opponent’s weapon, neither you nor they can attack with the involved weapons or move.
  - During your turn, you may release your opponent’s weapon as a Free Action.
    You may also attempt to *Disarm* the weapon that you have caught; if you do, you gain a +10 bonus.
  - Your opponent may let go of the caught weapon as a Free Action; alternatively, they may attempt to break the weapon free as a Quick Action with SOM+STR check.
  - Attempting to catch is a *reaction*, see *Reactions* in *Combat*.

- Dismount
  - I’m honestly at a bit of a loss as to how to write this one.
    Maybe we shouldn’t?
  - Should we make it a modified version of bracing to receive a charge?
    A special attack?
    An action you can attempt any time you strike a mounted rider?

- Shield Bash
  - A character can attempt to attac an opponent with their *shield*.
  - This is resolved as an attack with a melee weapon (the character needs to have *basic proficiency* in *Melee*, but not specific *proficiency* is required).
  - A *shield bash* does 1d10+1+DB DV, and has AP 0.
  - Note that the construction or use of some shields might make a *shield bash* impossible.
  - Shields are often held in the *off hand*, and so appropriate penalties would apply (see *Multiple Weapons and Multiple Attacks*).

### Examples

A goblin gang-member has figured out that she cannot get past Chandra’s armor, so she decides to *strike an armor gap*.
She attacks Chandra, rolling her One-Handed Weapons (normally 60, but 50 with the penalty for the trick) against Chandra’s Fray (60).
The goblin ganger rolls a 21, and Chandra rolls a 73; the Goblin hits Chandra and deals damage like normal, but she doesn’t get the bonus to AP she was hoping for, since she didn’t score an Exceptional Success.

Track is fighting a monster that attacked the party in a frozen monastery.
The fight isn’t going well, so he decides he needs to knock it down and get away.
He tries to Knock it Down, and rolls his One-Handed Weapons (normally a 70, but a 60 with the penalty for the trick) against it’s Fray (70).
He scores a 41, and the monster scores a 13; Track gets to deal his normal damage — including the +5 bonus for scoring an exceptional success — and then the monster has to roll its SOM×2 or be knocked prone.

Note: there’s no reason you can’t spend moxie on these checks. 
As an example: Lady Katarina has snuck up behind a watchman guarding a slaver encampment; she wants to dispatch him quickly, so she decides to throw a knife at his neck using Maim.
She rolls her Ranged Weapons (normally 60, but 40 with the penalty), and gets a 21: she hit him, but she didn’t strike the mortal blow she wanted.
(He doesn’t get to defend, because he’s un-aware of her, see *Un-Aware Targets* in *Combat*.)
She decides she really needs to dispatch him, so she spends a Luck to upgrade her attack to an Exceptional Success; now, not only will she get the +5 DV for an exceptional success, but she’s hit him in the neck — a fatal blow\!

## Multiple Weapons and Multiple Attacks

Under some circumstances, characters can make multiple attacks at once; for example, a character wielding multiple weapons could choose to attack with each weapon that they are wielding.
When making multiple attacks, only one Standard Action is required, but each attack is resolved separately (using all the normal rules for attacks); each attack suffers a -10 penalty.

When making multiple attacks, each attack does not have to have the same target; instead, each attack can be directed at a specific target.
When attacking multiple targets in this way, each attack suffers an additional -10 penalty.

[[clarification]]
|These rules only cover attacking multiple targets with multiple single-target attacks; they do not cover blast or splash weapons, for example.

Off-Hand Weapons: most characters (i.e. those without an appropriate Trait or Racial ability) have a dominant hand and an off-hand.
Attacks made with the off-hand suffer a -10 penalty.
If the weapon you are using in your off-hand does not have the *Off-Hand* tag, you suffer an additional -10 penalty.

[[example]]
|If you’re humanoid, you have the Ambidextrous trait and you are wielding two one-handed weapons, then you can make two separate attacks against the same target as a Standard Action.
|Each attack suffers -10 penalty (for making Multiple Attacks).
|
|If you don’t have the Ambidextrous trait, but the weapon in your off hand has the Off-Hand tag, then you can make one attack at -10 (with the weapon in your main hand, suffering the Multiple Attacks penalty) and one attack at -20 (with the weapon in your off-hand, suffering both the Off-Hand and Multiple Attacks penalties).
|
|If you don’t have the Ambidextrous trait, you're wielding two one-handed weapons, and the weapon in your off-hand doesn't have the *Off-Hand* tag, then you'll make your attacks at -10 (your main hand) and -30 (your off hand), respectively.

## Resistance and Vulnerability

Some creature, objects or armors have special **Resistances** or **Vulnerabilities**.
The Resistance or Vulnerability will name the *Tags* to which they apply, and what affect the resistance or vulnerability has; any attack or effect that matches the *tag* will then be modified as specified.
For example, "Resistance: Fire (DV÷2)" would mean that any damage done with an attack (or effect) with the *Fire* tag is halved; "Vulnerability: Cold (DV+3)" would mean that attacks with the *Cold* tag deal an extra 3 DV.

Of course, resistances and vulnerabilities can do things other than modify DV.
A spirit of snow and frost might have *Vulnerability: Fire (Melts)", for example.
Likewise, a creature that's particularly resistant to psychic manipulation might have "Resistance: Sleights (+WIL to checks to resist)".

Sometimes a *Resistance* or *Vulnerability* might say to modify a property that an attack or effect doesn't *have*.
For example, "Resistance: Fire (DV÷2)" would not effect an attack with the *Fire* tag if that attack didn't actually deal *damage*.
Normally, in this case, that part of the *Resistance* or *Vulnerability* simply doesn't apply; you can't half the DV of an attack that doesn't have a DV, after all, so you would just ignore that effect.

In special circumstances, a GM might decide that a resistance or vulnerability has some other effect.
If a creature has "Resistance: Fire (Immune)", a GM might declare that a power that uses fire to *frighten* its target would not affect that creature.

[[designnote]]
|We need a Resistance and Vulnerability system that's light-weight and unobtrusive when it isn't needed, but (ideally) that's flexible enough to represent a lot of different effects and results — not just changing damage.
|
|We're not there yet, but we're getting closer.

## Reactions

Under some situations, you can take an action (or you will be *forced* to take an action) even though it isn’t your turn.
An action taken outside of your turn is called a **reaction**.
Once you take a *reaction*, you cannot take *another* reaction until the end of your next turn.
(Roughly, you only get one reaction per turn cycle.)

### Readied Actions

If you'd like to prepare a response to something that might happen later, you can *ready an action*.
When you **ready an action**, you must specify another *Standard Action* and a *condition* or *event*; if the *condition or event* occurs before your next turn, you may choose to take the action that you specified.

Readying an action is a *Standard Action*; activating a *readied action* is a *Reaction*.

### Attacks of Opportunity

If a character who you *threaten* attempts to move *away from you* or *past you*, you may make an attack against them (using all the normal rules for an attack).

Hitting an opponent with an attack of opportunity doesn’t necessarily hinder their movement, unless you also incapacitate them with your attack (by knocking them down, for example).

An Attack of Opportunity is a Reaction.

### Reacting to Events

Sometimes events may demand an immediate response: you might want to grab hold of a rope if the floor breaks beneath you, or you might want to catch something that someone has thrown to you.
These are also *Reactions*.

### Special Defence

Normally, defending against an attack — with Fray, or by parrying — is *not* a reaction.
However, most *special defenses* are reactions: defending with a *strike* or a *maneuver* usually requires a reaction, for example, and most *powers* that trigger on a successful defense require a reaction.
(For example, some of the links in a *Chain* are *Reactions*, and the Quick Break power is a *Reaction*; see the *Classes* and *Powers* chapters.)

## Unarmed Combat and Natural Weapons

Some characters have learned to fight without a weapon, by striking opponents with punches, kicks, and other unarmed attacks; other characters have *natural* weapons, like claws, fangs, or spiked tails.

[[designnote]]
|
|The original intent was that Unarmed Combat would be treated no differently than any other style of combat, without any special rules (and without anything like a “mandatory feat chain” required to make it useful).
|
|This proved confusing, as many players assumed (not unreasonably\!) that they could not fight an armed character while unarmed, and even wanted to take Powers to allow them to do so\!
|
|The rules given here are an attempt at a minimal viable treatment of Unarmed Combat, which will explicitly allow characters who invest ranks in *Unarmed Combat* to effectively fight against an armed and armored opponent — without requiring any particular powers.

### Unarmed Combat

Most *unarmed attacks* — punches, kicks, and other strikes — works work much like any other attack.
Attacks with punches, kicks, and so on have the *Unarmed Attack* tag; note that some creatures and armors may have resistance to *unarmed* attacks.
The base damage for an *unarmed attack* is 1d10+DB DV with no AP.

A character who is unarmed is at a disadvantage against an armed or armored opponent.
A character who does not have *basic proficiency* (see *Basic Rules*) in *Unarmed Combat* does not *threaten* opponents next to them, and they cannot use the *Unarmed Combat* skill to defend themselves against an armed opponent.
A character who *does* have basic proficiency in *Unarmed Combat* can use that skill to fight an armed opponent, but they take a -10 penalty when attacking, and a -20 penalty when defending.
A character who attempts to strike an *armored* opponent while unarmed is at risk of injury (for obvious reasons); if they score an exceptional failure on their attack, they take 1d10÷2 DV.
Note that this applies to *strikes*, but not to grapples, throws, sweeps, or similar maneuvers.

Conversely, characters wearing armor will do additional damage with an unarmed attack.
Characters gain AV÷3 bonus damage to unarmed attacks, for the highest AV among the armors that they’re wearing.

### Natural Weapons

Some characters have natural weapons, like claws, fangs, or a spiked tail.

Attacks with natural weapons have the *Natural Weapon* tag (and don’t have the *Unarmed Attack* tag).
Natural weapons don't use the base damage for an unarmed attack; instead, they will list their own damage an AP (like an artificial weapon does).

A character with a natural weapon is generally treated like an armed character; they threaten characters next to them, and can attack and defend against armed and armored characters.
A character using a natural weapon takes only a -10 penalty when defending against an armed character.

Attacks with natural weapons still use the Unarmed Combat skill; each natural weapon requires a specific proficiency (for example, Unarmed Combat (Claws), or Unarmed Combat (Fangs)).

## Mounted Combat

  - Mounted warriors are highly effective combatants: they are highly
    mobile; they can wear heavy armor and carry heavy weapons; they are
    harder to strike, as the rider is out of easy reach of a combatant
    on foot; and they are capable of mighty charges.

  - For simplicity, we do not give the mount a separate turn from its
    rider, or track its actions separately; instead, the rider simply
    uses the mount’s movement modes, and can use the mount’s attacks
    (should it have any).

  - If the user is proficient in riding, then no test is required to use
    the mount’s normal movement (and attacks); Ride is a Movement Skill,
    see *Movement Skills*.
    
      - However, in order to be ridden in combat, the mount has to have
        been trained for war — or has to be from a species that is not
        frightened by battle.

  - The mount and rider can be attacked separately, and mounts can be
    wounded using all the normal rules.
    
      - The rider, however, is difficult to attack, being above and
        out-of-reach for most normal-sized characters. Attacks against
        the rider suffer a -20 penalty.
      - A mount’s wounds apply penalties to its actions, including its
        attacks and any checks caused by its movement, but not to the
        rider’s attacks.
      - If a mount falls — either because it is wounded and fails its
        check to remain standing, or for some other reason — then the
        rider may be thrown off, or even pinned under it. The rider
        should make a COO+COO+SOM test; if they succeed, they are thrown
        clear; if they fail, they may be trapped in their saddle — or even
        pinned under the mount.

  - Mounted charges are particularly vicious.
    
      - A mounted charge uses all the normal rules for a charge, except
        that the charging character gains an *additional* +DB on their
        attack, and they may use the mount’s STR rather than their own
        to compute their DB.
    
      - A charging character doesn’t have to *end* their movement after
        attacking; instead, they can continue to ride along, attacking
        characters as they ride pass. These are called *ride-by
        attacks*.
        
          - These attacks use all the rules for a charge, as well as for
            making *multiple attacks* against *multiple targets*, as
            above.
          - That is, under normal conditions, they gain an additional
            +DB to their attack, can use the mounts STR to compute their
            DV, and suffer both the -10 penalty for making multiple
            attacks and the -10 penalty for attacking multiple targets.
          - Note: it’s a ride-by attack if you attack during the middle
            of your movement instead of the end, even if you only attack
            on target.

  - Some weapons are not well-suited for use while mounted; weapons
    without the Cavalry tag take a -20 penalty when used while riding a
    mount.

## Blast and Splash Attacks

Some attacks cover an *area*, rather than affecting a single target; these usually have the *Blast* or *Splash* tags.

Attacks with the **Blast** tag do their listed damage where the attack *emanates from*, and 2 DV less for every meter away from that point.
(Note that this means that the rolled DV *effectively* determines the size of the blast produced by the blast effect.)
People in area of affect of a Blast Attack usually will not be able to *Defend* against it — you’re either in the explosion or you aren’t\!

Some attacks cover an area, but they don't (immediately) do *damage*; these attacks usually have the **Splash** tag.
Instead, those within the area of the *splash attack* are affected by it.
Since they don't deal DV, *splash* attacks usually list a *radius* (like 1d10÷3m for a thrown canister of *scour*, see *Scour* in *Items*).
Like Blast attacks, creatures in the area of a Splash Attack cannot usually defend — they're either in the area or they aren't.

These abilities are common with *projectile* and *thrown* weapons (or powers that work similarly).
When this happens, the point that the attack "emanates form" is the point that the projectile landed — either where the player was aiming, or where the projectile *scattered to* (see Ranged Attacks above).

## Size and Combat

We do not have extensive rules for how sizes impact combat; some general guidelines are provided below.

- Ranged attacks against *small* targets receive a -10 penalty; however, attempts to grapple small targets are made at +10.
- Ranged attacks against *large* targets receive a +10 bonus; however, attempts to grapple large targets are made at -10.
- Greater bonuses and penalties may be used for larger size differences.
- see *Sizes* in *Senses, Movements and Special Abilities*.

## Being Prone

You may drop *prone* as a Quick Action.
Some effects will force you to become prone (without requiring an action), like failing a SOM×3 check after being wounded, or being tripped.
Getting up from a prone position is a Quick Action.

While **prone**,

- you may move up to half your base movement as a Standard Action;
- melee attackers receive a +10 bonus against you, and
- ranged attackers take a -10 penalty against you.
- Most weapons are more difficult to use, imposing a -30 penalty attack; this does not apply to weapons with the *prone* tag.

## Cover

Characters can *take cover*, using solid obstructions to prevent and attacker from being able to reach them.
We generally divide cover into three types: minimal, partial, and total; the effects of each are described below.

- **Minimal cover** doesn't really conceal the defender from the attacker, but it does make the attack slightly more awkward.  A support-beam, banister, cattle-fence, or young tree might provide minimal cover.
- **Partial cover** obscures about half of the defender, providing them substantial protection from attacks.  For example, a bench, a solid fence, shallow trench, or half-opened door might provide partial cover.
- **Total cover** completely obscures the target from the attacker, preventing a direct attack.  Solid walls and deep trenches might provide total cover.

| Cover   | Effect                              |
| ------- | ----------------------------------- |
| Minimal | -10 to the attack                   |
| Partial | -30 to the attack                   |
| Total   | Attacker does not threaten defender |

Note that the benefits of cover can depend on several factors, including how the characters is positioned, whether the character is prone, crouching or standing, where the opponent is, and the kind of weapon that they are using.
This is why we do not talk about a character being "in cover" absolutely, but instead talk about a character "having *partial cover* against a particular attack."

Note that characters trying to move while crouching or prone behind cover are probably using *unusual movement*, as described above.
Also, characters crouching behind many kinds of *partial cover* might be able to *brace* a weapon with the *Prone* tag, like a crossbow or hand-cannon; this would generally provide a +10 bonus to attacks.
