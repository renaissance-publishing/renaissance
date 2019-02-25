---
title: Core System Rules
---

This system is inspired by Eclipse Phase's D% system.

## Some Rule 0's

-   When rounding, always round down.
-   Everything stacks unless it specifically says otherwise.

    -   That is, if you have several bonuses or penalties, they all
        apply; you might assume this would be the case, but it's worth
        pointing out, since some popular games don't work that way.

## Check Basics

Checks are at the heart of Renaissance.

-   Roll D%, compare to _target_: succeed if less than or equal to
    target, fail otherwise

    -   Conceptually, a D% is a dice that is numbered from 0 to 99. Such
        dice exist, but you can use anything that generates a number
        from 0 to 99 in an unbiased way---like two ten-sided dice, or a
        computer.
    -   Be careful! D% runs from 0 to 99, _not_ 1 to 100!

        -   this means that if you're using a computer random number
            generator and it gives you a result of 100, you should
            interpret that as 00---that is, as a critical _success_.

    -   Margin of Success (MoS) is die roll if success
    -   Margin of Failure (MoF) is (die roll -- target) if failure
    -   targets vary, but are usually either skill checks (see below) or
        some combination of your aptitudes (see Skills).

-   Target Limits:

    -   Your target can never be greater than 98; a 99 always fails, and
        is always a critical failure.
    -   Your target can never be less than 0; a 0 always succeeds, and
        is a critical success.
    -   If failure is impossible, simply waive the check, or use a
        Simple Check; if success is impossible, then simply declare that
        the character fails. See also When Should We Use Checks.

-   Special Results

    -   if you succeed and your MoS is over 30, then you have scored an
        exceptional success.
    -   If you succeed and your MoS is a "double"---that is, a multiple
        of 11---then you have scored a critical success.
    -   Likewise, if you fail and your MoF is over 30, then you have
        scored an exceptional failure, and if you fail and roll a
        double, then you have scored a critical failure.
    -   The results of this vary: some rules will spell out exactly what
        happens, while other times, it will be up to the GM's discretion
        to come up with an appropriate extra reward (for an Exceptional
        Success) or amazing bonus (for a critical success).
    -   Sometimes, for clarity, we'll call a success that is neither an
        exceptional or critical success a "normal success," and we'll
        call a failure that is neither an exceptional nor a critical
        failure a "normal failure".

-   Upgrading and Downgrading.

    -   Sometimes, you'll be able to upgrade (or required to downgrade)
        a given check.
    -   When you upgrade, your results are improved:

        -   a critical failure or exceptional failure becomes a normal
            failure
        -   a normal success becomes an exceptional success, and an
            exceptional success becomes a critical success.

    -   When you downgrade, your results are degraded:

        -   a critical success becomes an exceptional success, and an
            exceptional success becomes a normal success.
        -   A critical or exceptional success becomes a normal success.
        -   A normal failure becomes an exceptional failure, and an
            exceptional failure becomes a critical failure.

    -   Note that, when upgrading, a normal failure does not become a
        normal success, and when downgrading, a normal success does not
        become a normal failure. That would be a little too powerful!
    -   Also, your MoS and MoF don't actually change, so MoS- and
        MoF-dependant effects aren't changed.
    -   Upgrading and Downgrading are an exception to the "everything
        stacks" general rule: you can't upgrade or downgrade any one
        test more than once.

-   Skill Checks:

    -   skill checks are the most common type of check
    -   the target is: the Linked Aptitude for the skill + your Ranks in
        the skill + any modifiers
    -   For example, to if you have 40 ranks in Stealth, your
        Coordination (the linked aptitude for Stealth) is 20, and you
        have a magic cloak that gives you +20 to Stealth, then your
        target is 80; you would then roll a D100, and try to roll an 80
        or less. A 45 would succeed (Margin of Success: 45), while an 85
        would fail (Margin of Failure of 5).

-   Simple Checks: for a _simple_ check, success is assumed, and you are
    only rolling to determine how well you do (for example, to determine
    how long you take, or how impressive your results are).

    -   Commonly used when a character can simply try some task again
        and again until they succeed, or when the GM decides that a
        character could not reasonably fail at a given task.
    -   In a Simple Check, compute the target the same way you would for
        a normal check.
    -   If you roll less than or equal to your target, you _excel; _if
        you roll more than your target, you _stumble_. Come up with
        better words for this FFS.
    -   If you _excel_, then you have achieved what you were trying to
        achieve, and done a good job of it!
    -   If you _stumble,_ then you _still_ achieve what you wanted, you
        just do so less dramatically; maybe you make some embarrassing
        mistake along the way, or it takes longer than expected.
    -   Simple success checks can't be be Exceptional or Critical.

-   Opposed:

    -   used when two characters are opposing each other.
    -   One character will _win_, and the other will _loose_.
    -   Each character makes a (separate) check.
    -   If one character succeeds and other fails check, the character
        who succeeded wins the check.
    -   if both succeed, highest Margin of Success wins (reroll ties)
    -   if both fail, reroll the check

        -   For example, if a character is trying to outrun a pursuer,
            an Opposed Test might be called for, using both character's
            Athletics.
        -   Suppose that Alice (who has 30 Somatics and 30 ranks in
            Athletics) is chasing Bob (who has 25 Somatics and 40 ranks
            in Athletics). Alice rolls her D100, and gets a result of
            32; this is less than her target of 60, so she succeeds,
            with a Margin of Success of 32. Bob, however, rolls a 73,
            which is greater than his target of 65; bob has failed, with
            a Margin of Failure of 8. Alice has won the check, and might
            catch up to Bob.

    -   The two characters don't have to use the same skill -- very
        often, they won't!

        -   For example, if someone impersonating a servant is trying to
            talk their way past a palace guard, then an opposed test
            between the impostor's Disguise and the guard's Read skills
            would be appropriate.

    -   Ordered Checks: Sometimes, it only makes sense to call for one
        character's check if the other character has already succeeded;
        in this case, one character should roll first, and the other
        character should only roll their check if it is needed. We call
        this an _Ordered_ check.
    -   Variable Checks: Sometimes, it's possible for both characters to
        succeed on a task. When this happens, if both characters succeed
        on their checks, instead of declaring the highest MoS to be the
        winner, both characters should be awarded a partial success. We
        call this a _Variable_ check.

        -   For example, if a character is trying to sneak past a guard,
            a Variable check might be called for, pitting the sneaking
            character's Stealth against the guard's Perception. If both
            characters succeed, the GM might rule that the guard hasn't
            spied the sneaking character directly, but has noticed some
            disturbance they left behind -- perhaps a window they left
            open, or some furniture they disturbed -- and has begun
            looking for an intruder.

-   Sidebar: When should we use checks?

    -   When is a check called for, and what type? This depends on the
        situation.
    -   In unstructured play, the type of _consequences_ that the GM
        expects often determine the kind of check to use. If a check
        could have major consequences (like an attempt to hide an item
        you stole from the king while being searched by a guard), then a
        check is definitely called for. However, if the odds of failure
        are low, or the consequences of failure aren't interesting, then
        Simple Checks might be used, or the check might be waived
        all-together.
    -   Notably, most mundane actions don't require checks. A character
        can make the half-a-day's walk to a neighboring town, cook a
        meal or speak in a language they know without requiring a check.
    -   The rules for Initiative Order and Combat are more specific; in
        combat, the exact series of checks to use will usually be
        specified by the rules for combat, and the items and powers in
        use.
    -   Similarly, Down Time has more specific rules; see the rules for
        Down Time.

-   Sidebar: Repeated, Individual Skill Checks

    -   Sometimes, there are situations where several members of the
        party could attempt the same task in sequence; for example, if
        the players are trying to search a room, then each person could
        make their own Search test, one after the other.
    -   This is usually not a good idea; this makes it very difficult
        for the party to fail, since they'll have several separate
        attempts; it makes each individual test less interesting, since
        the next person will just try if the current person fails; and
        it can slow the game down dramatically.
    -   Instead, we recommend the GM require one character make one test
        on behalf of the party; that character---usually the one with
        the highest rating in the skill in question---should "take the
        lead," and the other party-members should assist (at least, the
        ones that are _eligible_ to assist, see _Skill Modifiers_).

## Modifiers

-   Being assisted: +10 per character assisting, maximum +30. Assisting
    characters must have 10 Ranks in a useful skill (but it doesn't
    have to be the _same_ skill). The GM may rule that certain tests
    cannot be _assisted_. (Attack Tests cannot be assisted, but see the
    Soldier class.)
-   \-10 for Trying Again. The GM determines if you can _try again_.

    -   This rule dose not apply to attacking a target in combat.

-   Related Skill:

    -   receive a bonus on one Test for having ranks in a related skill
        (for example, Knowledge: Theology might assist Profession:
        Cleric)
    -   10-25 Ranks: +10
    -   25-40 Ranks: +20
    -   41+ Ranks: +30
    -   You may only use one related skill.

-   Specialization:

    -   skills can have _specializations_.
    -   Character recieves +10 when Specialization applies; there is _no
        effect _(including _no penalty_) when Specialization does not
        apply
    -   Any given skill can only be specialized once. You can't buy both
        a \[Short Swords] and a \[Knives] Specialization for Bladed
        Weapons, for example.
    -   You can acquire specializations for your skills during character
        creation: see also _Character Creation_.

-   Clarification: you can also acquire specializations for field
    skills, for example:
    Art: Painting \[Landscapes], where Art is a field skill, Painting
    is the field, and \[Landscapes] is the specialization.
-   Difficulty Modifiers

    -   Run from Very Easy (+30) to Very Hard (-30), and all shades
        in-between.

-   Taking your Time and Rushing:

    -   only applies to Task Actions and Jobs
    -   Taking your Time: for every +50% increase in timeframe, +10 to
        the check (up to +150% time for +30)
    -   Rushing: for every -25% _reduction_ in timeframe, -10 to the
        check (up to -75% for -30)

-   Situational Modifiers

    -   Lots of other things might provide modifiers! The GM may assign
        modifiers from situation as appropriate.

-   Passive Tests: Usually, characters will use their skills actively.
    Sometimes, the GM will roll a test on behalf of the player---for
    example, to see if they have noticed something (a Perception test),
    realized something (a COG\*3 test), or has some piece of knowledge
    (a Profession, Craft or Knowledge check). These are _Passive Tests_,
    since they are made "automatically" on the player's behalf. Passive
    checks have a -20 penalty (the players should be proactive in using
    their skills, after all). Generally, Passive tests are made in
    secret by the GM; if a player later makes an appropriate test, then
    the result of the test that the player made takes precedence
    (although events may unfold in such a way that a player cannot call
    for such a check later).
-   Common Knowledge: if a player has 10 or more ranks in a given skill,
    they can be assumed to have common knowledge appropriate to that
    skill (that is, without being required to make a test).

## Actions

Types of actions

-   Standard actions

    -   An action that doesn't take much time, but that you need to
        focus on.
    -   Examples: attacking with a weapon, knocking over a dresser,
        kicking in a door.

-   Quick actions

    -   An action that doesn't take much time, and that you don't need
        to focus on.
    -   Examples: moving, yelling something, retrieving a stored item,
        drawing a weapon.

-   Task actions

    -   An action that takes time (but less than a day), and that you
        need to focus on.
    -   Examples: brewing a potion, picking a lock, buying goods in town
    -   Note: Tasks that take 8 hours of work or more should generally
        be handled as Jobs and done during Down-Time.

-   Sustained actions

    -   An action that takes time, but that you don't need to focus on,
        so you can do it while doing something else.
    -   Examples: keeping an eye out for a mark during an opera, leaving
        a trail of bread-crumbs while traveling, memorizing a route
        while being forced to march, _sustaining powers._
    -   You can take other actions while maintaining a Sustained Action,
        and you can maintain more than one Sustain action at a time.

        -   However, maintaining multiple Sustained Actions is
            distracting; you take a -10 penalty to all tests for each
            Sustained Action you maintain beyond the first.
        -   So, for example, if you maintain three Sustained Actions,
            you take a -20 penalty to all tests.

    -   Sustain actions don't have a specific upper limit for how long
        you can maintain them, but your GM might not allow you to
        maintain them for more than a reasonable amount of time, or
        might require additional checks or impose additional
        consequences.

-   Jobs

    -   Jobs have time-frames measured in _shifts._ A shift is one
        continuous eight-hour work day.
    -   Used mainly during Down-Time Play

-   Since the MoS (and MoF) of a test can determine how long an action
    takes, If a Task Action or Job requires a check, that check should
    be made when the action is _begun._

    -   If the check is failed, the character in question works for 25%
        of the Task Action's timeframe or Job's shifts (on a Failure),
        or 50% (on an Exceptional Failure), before realizing that the
        task will fail (and, presumably, stopping).

## Modes of Play

Renaissance has the following modes of play

-   Unstructured: the "normal" mode, which works like a conversation
    with the GM

    -   GM describes scene / situation
    -   players ask questions, declare actions
    -   GM answers questions, resolves player actions; often calls for
        tests.
    -   As the name implies, no particular rules about action allotment
        (as opposed to Turn Order and Down-Time). However, the GM may
        limit the actions allowed in a given situation (for example, you
        can't try to build a tool as a one-hour Task Action if you're in
        a building that's burning down.)

-   Turn Order: each player rolls _initiative_, and gets a turn in order
    of their initiative (Highest initiative roll first, and then in
    descending order. GM breaks ties arbitrarily, but generally a good
    idea to let highest base-initiative go first.)

    -   Initiative is 1d10 + _Initiative Modifier_. The GM will pick an
        appropriate _Initiative Modifier_.
    -   Each turn should have a specific _action allotment_, which the
        GM will pick when Turn Order play is begun.

        -   If the GM includes Task Actions in the action allotment,
            then the GM should specify _how much time_ a character can
            contribute to a Task Action -- for example, "Five minute
            task actions".
        -   If the GM doesn't include Task Actions in the action
            allotment, then progress towards Task Actions are not
            tracked; a player who wishes to continue working on a Task
            Action simply looses their turn(s).
        -   Likewise, Jobs aren't tracked during Turn Order; a player
            who wants to keep working on a Job during Turn Order simply
            looses their turn(s).

    -   Combat is a special case of Turn Order play; see _Combat_,
        below.

-   Down-Time: focuses on long-term actions. Down-Time is measured in\*
    \*days. On any day, a character can spend 8 hours working on a Job;
    if they do, that Job is one Shift closer to being complete.

    -   Your GM might allow you to work more or less time, and to earn
        shifts slower or quicker; this is entirely at GM discretion.

        -   In particular, races that don't need to sleep have an
            obvious opportunity to earn more than one Shift in a day.

    -   As an alternative to working on a Job, a player can spend a day
        to complete one or more task actions (recall that Task Actions
        should take less than 8 hours, so you should always be able to
        finish at least one Task Action per day).

-   Sidebar: Interrupting Actions

    -   Sometimes it's possible to interrupt an action---if one
        character breaks into the workshop where another character is
        working, for example. We don't provide fixed rules for this,
        because no set of rules could be comprehensive without being
        unwieldy. GMs are encouraged to adjudicate such situations as
        they arise.

## Combat

Combat is a special case of Turn Order play, using the following rules:

-   Initiative Modifier: your initiative modifier (INIT) is (INT + REF)
    ÷ 5

    -   see the Derived Stat in _Character Creation_.

-   Action allotment

    -   one Standard Action and one Quick Action, or
    -   three Quick Actions
    -   since Task Actions are not given in the action allotment, Task
        Actions are not tracked during Combat; see _Turn Order Play_.

-   If you are maintaining any Sustained Actions, you must spend one
    Quick Action to do so (meaning you would normally have either one
    Standard Action or two Quick Actions remaining),

    -   but, you only need to spend one Quick Action, no matter how many
        Sustained Actions you are maintaining.

-   In combat, a turn is about 3 seconds; therefore, there are 20 turns
    in a minute.
-   Unlike many other areas of the game, Combat has fairly specific
    rules about what characters can and cannot do.

### Useful Terms

-   These aren't really useful here, but having them defined will make
    some powers a little easier to write. Remove / move?
-   Threatened: we say that you _threaten_ an opponent if you could make
    a melee attack against them; you usually threaten opponents if they
    are next to you.
-   Bloodied: we say that a character is _bloodied_ if they have taken
    DV exceeding half their DUR.

### The Combat Grid and Movement

-   Combat Grid

    -   positions in combat are usually tracked using a _square grid_,
        with each square representing a 1 meter square.
    -   Most creatures (those that are Small-, Normal- or Large-sized)
        usually take up one square, and can reach the adjacent squares
        (to attack them, for example).
    -   Distances (like ranges) are usually measured directly and then
        rounded to the nearest whole meter. Distance while moving
        depends on the exact path traveled (in this case, "diagonal
        steps" count as traveling 1.5 meters).
    -   Traditionally, _facing_ is not tracked.
    -   Though we will assume a combat grid with one-meter squares in
        this guide, nothing prevents you from using other combat
        systems---like hex-grids or miniatures---as long as the rules
        for measuring distance, determining reach and tracking movement
        are well-defined.

-   Movement

    -   Collectively, the following are called Movement Actions. You may
        only use one Movement Action during your turn.
    -   As a quick action, you may _move_: you may move up to your base
        movement rate.
    -   As a quick action, you may _move quickly_: you may move up to
        your full movement rate. After doing so, you suffer a -10
        penalty to all Physical skill tests until your next turn.
    -   As a quick action, you may _charge_: you may move up to your
        full movement rate, and you suffer a -10 penalty to all Physical
        skill tests until your next turn. See _Charging_ and _Bracing_
        below for more information.
    -   You may also perform _Stunts_.

        -   "Stunts" are used when your character attempts unusual,
            difficult maneuvers---they jump, tumble, flip, climb (if
            they don't have a climb speed), swing and so on.
        -   The type of action varies: rolling under a hazard might be a
            quick action, but climbing a trellis might be a standard
            action (for a character without a climb speed).
        -   How far the character is moved will also vary (in general,
            GMs should move characters by either their base or full
            rates).
        -   Stunts almost always require a test using an appropriate
            movement skill (this is usually Athletics for humanoid
            creatures).
        -   Stunts may have other affects as well (a dive-and-roll may
            allow you to end your turn prone behind cover, a flip off a
            table may allow you to cross over an enemy and land facing
            their back).

### Attacking

-   Attacking a target

    -   a Standard Action (whether in melee or using a ranged weapon)
    -   roll an Ordered Opposed Check, first the attacker and then the
        defender

        -   Attacker Wins: Defender takes attack damage (listed damage
            for a weapon or power)
        -   Defender Wins: Defender takes no damage

    -   Exceptional Results:

        -   Attacker MoS > 30: +5 DV
        -   Attacker MoS > 60: +5 more DV (+10 DV total)
        -   Attacker critical success:s

            -   ~~ignore defender's armor.~~ This might be a little
                strong; they did away with this in EP2, for example. And
                I might also add rules for deliberately targeting a weak
                spot, which would make this sort of redundant.
            -   Roll damage dice twice, take best result. I like that
                better.

    -   Attack Skills: use the attack skill appropriate to the weapon;
        some attacks will specify an Attack Skill.
    -   Defense Skills: you can defend with many different skills

        -   Fray is the most general defense skill. It can be used to
            defend against most attacks. (Among it's other uses, see
            Skills).
        -   You can use your own melee attack skills to defend against
            melee attacks---you can use your Bladed Weapons to defend
            against someone attacking with Pole Arms, for example. This
            represents you parrying or deflecting their attacks.

            -   Since Unarmed is a melee attack skill, you can use it to
                defend; see Unarmed Combat for more information.

        -   Sometimes---when using the Weave power, for example---you
            can defend with movement skills, like Athletics.

-   Ranged Attacks: ranged attacks (projectiles, thrown weapons and some
    powers) use the rules for _attacking a target_, with the following
    addition:

    -   Range: ranged attacks have range categories: you are in a given
        range category if your distance to the target is the listed
        distance or less. Each range category has a modifier, which
        applies to the attack test:

        -   short: no modifier
        -   medium: -10
        -   long: -20
        -   extreme: -30

    -   base ranges for throwing things:

        -   short: up to 5 meters
        -   medium: up to 15m
        -   long: up to 30m
        -   extreme: up to 45m
        -   adjust for weight, aerodynamics of object

    -   Scatter: ranged attacks may scatter.

        -   Multiple methods for scatter, like EP.
        -   Method 1: roll 2d10. One d10 indicates the scatter direction
            (there are 8 adjacent squares, so discard 9 and 10 results),
            the other the distance (in meters).
        -   Method 2: with a physical table, roll 1d10. The result is
            the distance in meters, and the direction the dice is
            pointing indicates the scatter direction.
        -   Scatter is mainly a concern when the weapon also has the
            Blast property; you usually don't worry about where an arrow
            scatters to.

-   Touch-Only Attacks: sometimes, notably when using some powers, an
    attacker only needs to touch their target.

    -   Treat this as an attack against the target, using the attacker's
        Unarmed skill; the attacker gets a +COO bonus, and the defender
        takes a -30 penalty.
    -   Treat this as an attack, using the standard rules. The attacker
        may use either COO+REF+SOM or their Unarmed Combat; they receive
        a +20 bonus. The defender takes a -20 penalty.

-   Indicate-Only Attacks: sometimes, notably when using some Powers, an
    attacker only needs to direct an effect to a target -- by pointing
    at the target, for example, or fixing their gaze on the target.

    -   Treat this as a ranged attack against the target, using the
        attacker's Projectile Weapons skill; the attacker gets a +COO
        bonus, and the defender takes a -30 penalty.
    -   Treat this as a ranged attack, using the standard rules. The
        attacker may use either COO+COO+REF, their Projectile Weapons
        skill or their Thrown Weapons skill; they receive a +20 bonus.
        The defender takes a -20 penalty.

-   Still working on these two. I'm torn between the roll needing to be
    make-able, especially to a caster-character that might have bad
    physical stats -- but at the same time, I don't want to stick them
    with a raw ability check that they can't use ranks to improve. And
    if we can manage to sync the rules up, so much the better.

    -   One thing I particularly want to avoid are two checks that both
        have low odds of success, so you just have to keep re-rolling
        them. And if a caster character has lousy physical stats,
        COO+REF+SOM might be 30 or so, which is low.
    -   But I also don't want to saddle casters with a "pointing skill"
        that only they have to spend ranks on.
    -   I took the rules I just had and added a +20 bonus; that will be
        close enough for the next play session.
    -   Does anyone have any feedback on these?

-   Un-Aware Target: targets who are not aware that they are being
    attacked cannot defend. (The attacker must still roll to hit their
    target.) (PCs and major NPCs should usually be allowed a Perception
    Check to notice a hidden attacker. Also, people usually take notice
    after they have been attacked.)

### Armor and Armor Penetration

-   Armor and Armor Penetration: if the defender has Armor, subtract
    their (total) Armor Rating from the attack's DV. However, if the
    attack has Armor Penetration (AP) -- usually because the weapon in
    use has armor penetration -- subtract the Armor Penetration from the
    Armor. Armor Penetration and Damage Values can't be negative.

    -   Damage inflicted is then: DV -- (Armor -- Armor Penetration)

-   Armor Penalty: some armors have a listed Armor Penalty; you take the
    listed penalty while wearing the armor.

    -   Didn't get good feedback on people with heavy armor having a
        skill penalty; we need to figure out some other mechanism.

### Strikes and Maneuvers

The combat system in Renaissance is intended to be light-weight and
flexible; characters should be able to attempt a variety of attacks,
maneuvers and tricks, and GMs (ideally) should adjudicate these
on-the-fly. _However,_ players and Gms both can benefit greatly from
some guidance on the kinds of things that are possible; we therefore
refer you to the _Special Attacks_ section in _Alternate Rules: _those
rules are optional, but _useful_ and _recommended_.

-   Any skilled melee combatant will have developed a repertoire of
    useful tricks, more than simply _sticking pointy end in other
    fighter._ We call these _strikes_ and _maneuvers_.

    -   A _strike_ is a modification to a normal attack. To make a
        strike, you take a penalty on your attack; if you score an
        Exceptional Success, in addition to the normal affects of the
        attack, you gain the listed Result.

        -   You decide if your attack is going to be a strike before you
            make it (since you have to take a penalty on the attack).
        -   An attack can only be one kind of Strike. (You can't take a
            \-20 penalty to have an attac be both a Called Shot an Knock
            Down.)

    -   A _maneuver_ isn't made as part of an attack.

        -   Each maneuver will list the type of action required, the
            check, and the result if you succeed.

-   Strikes:

    -   Called Shot

        -   Penalty: -10
        -   Result: you strike the target in a specified location (you
            pick the location before your attack).
        -   This one is a catch-all, with results up to the GM.
        -   Special: the attack gains the Precision tag

    -   Knock Down

        -   Penalty: -10
        -   Result: your opponent must attempt a SOM×2 check or be
            knocked _prone_.
        -   Special: must be a melee attack.

    -   Maim

        -   Penalty: -20
        -   Result: You maim your opponent, removing a specific limb.
            You can use this to lop off a hand, break a knee or gouge
            out an eye.
        -   Special: the attack gains the Precision tag.

    -   Mighty Blow

        -   Penalty: -10
        -   Result: You strike your opponent with particular force; you
            gain +DB to your DV.
        -   Special: must be a melee attack.

    -   Strike an Armor Gap

        -   Penalty: -10
        -   Result: You strike a weak spot in the opponent's Armor; you
            gain +DB to your AP.
        -   Special: the attack gains the Precision tag.

-   Maneuvers:

    -   Disarm

        -   Action: Standard Action
        -   Test: Your melee attack skill vs. target's melee attack
            skill or Fray
        -   Result: If you succeed, then you disarm your opponent,
            forcing them to drop one held item (like a weapon or
            shield).

    -   Feint

        -   Action: Quick Action
        -   Test: Your Deception vs. target's Resist Social Manipulation
            or Read
        -   Result: until the beginning of their next turn, the target
            takes a -20 penalty to their defense.

    -   Grabbing

        -   Action: Standard Action
        -   Test: your Unarmed Combat vs. target's Fray or Unarmed
            Combat.
        -   Result: you grab the opponent, impeding them. They cannot
            easily act.
        -   The results are at the GM's discretion, but normally grabbed
            characters cannot take any other actions besides attempting
            to escape the grab.
        -   A grabbed character can attempt to break a grapple, using
            either their Unarmed Combat or their STR+SOM, versus the
            Unarmed Combat of the character grabbing them. If they win,
            they break free.

    -   Trip

        -   Action: Standard Action
        -   Test: your melee attack skill vs. target's Fray
        -   Result: You trip your opponent, causing them to fall prone.

-   Examples

    -   A goblin gang-member has figured out that she cannot get past
        Chandra's armor, so she decides to _strike an armor gap._ She
        attacks Chandra, rolling her Bladed Weapons (normally 60, but 50
        with the penalty for the trick) against Chandra's Fray (60). The
        goblin ganger rolls a 21, and Chandra rolls a 73; the Goblin
        hits Chandra and deals damage like normal, but she doesn't get
        the bonus to AP she was hoping for, since she didn't score an
        Exceptional Success.
    -   Track is fighting a monster that attacked the party in a frozen
        monastery. The fight isn't going well, so he decides he needs to
        knock it down and get away. He tries to Knock it Down, and rolls
        his Blunt Weapons (normally a 70, but a 60 with the penalty for
        the trick) against it's Fray (70). He scores a 41, and the
        monster scores a 13; Track gets to deal his normal
        damage---including the +5 bonus for scoring an exceptional
        success---and then the monster has to roll its SOM×2 or be
        knocked prone.
    -   Note: there's no reason you can't spend moxie on these checks.
        As an example: Alexis has snuck up behind a watchman guarding a
        slaver encampment; she wants to dispatch him quickly, so she
        decides to throw a knife at his neck using Maim. She rolls her
        Thrown Weapons (normally 60, but 40 with the penalty), and gets
        a 21: she hit him, but she didn't strike the mortal blow she
        wanted. (He doesn't get to defend, because he's un-aware of her,
        see Un-Aware Target below.) She decides she really needs to
        dispatch him, so she spends a Luck to upgrade her attack to an
        Exceptional Success; now, not only will she get the +5 DV for an
        exceptional success, but she's hit him in the neck---a fatal
        blow!

### Multiple Weapons and Multiple Attacks

-   Multiple Attacks: under some circumstances, characters can make
    multiple attacks (when wielding multiple weapons, for example). When
    a character attacks, they may make one attack with each weapon they
    are wielding; such an attack is still one Standard Action. Resolve
    each attack separately, using the normal procedure for each attack.
    When making Multiple Attacks, each attack suffers a -10 penalty.

    -   Multiple Targets: when making multiple attacks, each attack can
        have a different target. When attacking multiple targets, each
        attack suffers an additional -10 penalty.

        -   I'm trying to decide if I should word this as a general
            rule, or just make it specific to when you're also making
            Multiple Attacks. The only other time I can see it applying
            is for a Cleave-like power.
        -   Clarification: attacks with the Blast property are not
            considered "multiple-target attacks".

-   Off-Hand Weapons: most characters (i.e. those without an appropriate
    Trait or Racial ability) have a dominant hand and an off-hand.
    Attacks made with the off-hand suffer a -10 penalty.

    -   If the weapon you are using in your off-hand does not have the
        _off-hand_ tag, you suffer an additional -10 penalty

-   Some Examples:

    -   If you're humanoid, you have the Ambidextrous trait and you are
        wielding two one-handed weapons, then you can make two separate
        attacks against one target as a Standard Action. Each attack
        suffers -10 penalty (for making Multiple Attacks).
    -   If you don't have the Ambidextrous trait, but the weapon in your
        off hand has the Off-Hand tag, then it's one attack at -10 (the
        main hand, with the Multiple Attacks penalty) and one attack at
        \-20 (the off-hand, with the Off-Hand and Multiple Attacks
        penalties).
    -   If you don't have the Ambidextrous trait, and you're holding two
        one-handed-but-not-off-hand weapons, you can still choose to
        make only one attack, and that attack will have no penalty (main
        hand), or a -20 penalty
        (off-hand-attack-without-offhand-tagged-weapon, if you make your
        one attack with your off hand, for some reason).

-   Feedback required!

    -   These rules are complicated and have lots of cumulative
        penalties; carefully watch how this works out.

### Resistance and Vulnerability

-   Resistance and Vulnerability:

    -   some creature, objects or armors will have a Resistances and
        Vulnerabilities
    -   The Resistance or Vulnerability will name the keywords to which
        they apply -- for example, Resistance: Fire or Vulnerability:
        Cold. If an attack is _resisted_, then its effects are reduced;
        if a creature is _vulnerable_ to an attack, then its affects
        will be increased.
    -   Option 1:

        -   Attacks, powers and other affects will specify what happens
            when they are _resisted_, or when a target is _vulnerable_
            to them.
        -   Normally, if an attack does DV, then:

            -   the DV is _halved_ if it is _resisted_, or
            -   the DV will be _doubled _if the target is _vulnerable_.

        -   In some ways the ideal version, but bad because now every
            power has to have Resist and Vulnerable lines; just don't
            wanna fuck with it.

    -   Option 2: if the target is Vulnerable, they get -20 to their
        check; if they are Resistant, they get a +20 bonus. That spare
        me having to do Vulnerable and Resisted lines for each power.

        -   Problem is that some powers don't have checks. Also it's
            just not very exciting.

    -   Option 3:

        -   ~~if the defender is Vulnerable to a power, then Success are
            treated as Exceptional Successes, and Exceptional Successes
            are treated as Criticals.~~ If the defender is vulnerable to
            an attack, effect or power, then the attacker's checks are
            Upgraded.
        -   ~~If the defender is Resistant to an effect, then
            Exceptional Successes and Criticals are treated as regular
            Successes.~~ If the defender is Resistant to an effect, then
            the attacker's checs are Downgraded.
        -   This sounds both Exciting and Easy without introducing new
            rules, but it's vulnerable to the same thing that Option 2
            is; not every power will have a check (or a specific result
            on a critical).

    -   Option 4

        -   D&D 5 stye
        -   if you resist, roll damage dice twice and take the lowest.
        -   If you are vulnerable, roll damage dice twice and take the
            highest.

### And Unsorted Rules

-   Full Defense: during your turn, you may take a Standard Action to
    focus on defending yourself. If you do, until your next turn starts,
    you receive a +10 bonus when you Defend.

    -   Nobody did this either, and it's also now covered by the Weave
        power.
    -   Someone, I think Sauce, suggested I add it back. I'd like to
        keep the rules as simple as possible, and this is a real corner
        case, but if people think it might be useful, I'll un-remove it.

-   Blast: a Blast Attack (an Attack with the Blast property) does its
    listed damage at the center of the blast, and 2 DV less for every
    meter away from the center. (In this way, the DV scored by the
    attack determines the radius of the blast.)

    -   People in area of affect of a Blast Attack usually will not be
        able to Defend -- you're either in the explosion or you aren't!

-   Splash: similar to Blast attacks, some attacks cover an area, but do
    not directly cause damage (a thrown jar of Scour, for example; see
    Items). Attacks with the Splash property cover a given area (like
    1D10 meters).

    -   Like Blast attacks, creatures in the area of a Splash Attack
        cannot usually defend.

-   Point-Blank Attacks: using a Thrown or Projectile Weapon at
    point-blank range (that is, against a target in an adjacent space)
    gets a -20 penalty
-   Grabbing: as a Standard Action, a character may attempt to _grab_
    another character. Make an attack test using your Unarmed Combat
    skill: if you succeed and your MoS exceeds the target's STR, then,
    instead of doing damage, you _grab_ the opponent. A grabbed opponent
    normally cannot take physical actions (beyond attempting to escape
    the grab). Attempting to escape the grab is a standard action
    requiring an opposed check, with escaping character using either
    their Unarmed Combat or their STR+SOM against the grabber's Unarmed
    Combat.

    -   We do not attempt to provide extensive rules for grabbing and
        grappling; your GM may apply additional affects, modifiers and
        penalties as appropriate to the situation.

-   Size and Combat

    -   Ranged attacks against _small_ targets receive a -10 penalty;
        however, attempts to grapple small targets are made at +10.
    -   Ranged attacks against _large_ targets receive a +10 bonus;
        however, attempts to grapple large targets are made at -10.
    -   Greater bonuses and penalties may be used for larger size
        differences.
    -   see _Sizes_

-   Natural Attacks: Natural Attacks are attacks made with "weapons"
    with the Natural tag (which is to say, claws, bites and so on).
    Natural attacks use the same rules as attacks with weapons.

    -   Clarification: most Natural Attacks have the off-hand tag. This
        is the same off-hand tag that light weapons have; it means that
        the Natural Attack does not suffer the additional -10 penalty
        when made with a non-dominant hand.
    -   _This could use some adjustment; feedback is appreciated._

-   Unarmed Combat:

    -   Unarmed Attacks have a base DV of 1d10+DB (Damage Bonus, see
        _Vital Statistics_), with no AP.

        -   Unarmed Attacks have the Natural and Off-Hand tags.
        -   Unarmed Attacks are punches, kicks and other similar
            attacks. Mechanically, they are those that are made without
            a Weapon or a listed Natural Attack.

    -   An Unarmed Attack made against an opponent with a weapon (or
        natural attack) suffers a -10 penalty.
    -   When using the Unarmed skill to defend against a weapon or
        natural attack, you take a -10 penalty.
    -   I'm not actually sure I want or need either of those rules.

-   Charge: when you use the Charge move action, if you end your move at
    least (twice your walking rate) from where you started, then you
    gain +DB DV on your attacks for the rest of your turn.

    -   This is still more awkward than I want it to be, but it's
        getting there.

-   Brace: Weapons with the Brace tag can be used to prepare to receive
    a charge.

    -   You need to have a weapon with the Brace tag.
    -   Bracing to receive a charge is a Standard Action.
    -   After bracing, until your next turn, if anyone _charges_ you
        (see _Charge_ above), you may attack them first, before they
        attack you. (Resolve the attack normally; the charging character
        can still defend, for example.)
    -   If you hit the charging character, you deal +DB damage.
    -   You do not prevent them from completing the charge (by attacking
        you), unless you incapacitate them with your attack (by
        disabling them, or by dealing a wound and knocking them prone,
        for example).

-   Prone:

    -   You may drop prone as a Quick Action.
    -   Some effects will force you to become prone (without requiring
        an action).

        -   Like failing a SOM×3 check after being wounded, or being
            tripped.

    -   Getting up from a prone position is a Quick Action.
    -   While prone,

        -   you may move up to your Walking movement as a Standard
            Action,
        -   melee attackers receive a +10 bonus against you, and
        -   ranged attackers take a -10 penalty against you.

## Injury

We use the same rules for taking damage, regardless of if the damage is
inflicted by a weapon attack, a disease, or something else.

Characters who are injured receive Damage, in an amount given by the
source's Damage Value (DV). (If you are attacked by a weapon, this
would be the weapon's DV, for example.) When the amount of damage that
you have taken equals your DUR, you are disabled; you are too badly
injured to take action, and likely unconscious. When the amount of
damage that you have taken reaches your Death Rating (DR), your
character has been killed.

Any time you take damage, you might also suffer _wounds_. If the amount
of damage you take at one time exceeds your Wound Threshold, then one
wound is inflicted. If you take damage that equals or exceeds twice your
Wound Threshold, you take two wounds, and so on; so, if your DUR was 30
and your WT was 6, and you then took 15 damage, you would also take 2
wounds.

When a wound is inflicted, you must roll SOM \*3; if you fail, you are
knocked down.

For every wound that has been inflicted, you suffer a -10 penalty to all
actions (not just physical actions, since wounds are painful and
distracting). Specific wounds might inflict other effects, as determined
by the GM; a wound to the head might render you unconscious, for
example.

Sometimes, you will have the ability to _Negate_ a wound. When this
happens, you may ignore the -10 penalty inflicted by that one wound.
Note that the wound is not healed, you are simply not hindered by it.
Only the -10 penalty is negated, any other effects persist; you cannot,
for example, _negate_ having your hand chopped off in order to wield a
two-handed weapon.

Mental stress works much like physical damage. Difficult circumstances
can inflict _stress _according to their Stress Value (SV); when your
stress exceeds your Lucidity (LUC), your character succumbs to the
enormous strains they are under; they cannot act until their Stress is
lowered below their Lucidity. If your stress exceeds your Insanity
Rating (IR), your character is irreparably traumatized (they are removed
from the game as surely as if they had died).

If you receive stress at one time that exceeds you Trauma Threshold
(TT), you suffer a Trauma. (Like wounds, you can receive multiple
Traumas at a time, if you receive enough Stress at one time to exceed a
multiple of your Trauma Threshold.) Like Wounds, you suffer a -10
penalty to all actions for each Trauma that you have. When you receive a
Trauma, you must roll WIL\*3 or be stunned for one round.

When stress is inflicted, characters may roll WIL \* 3. If they succeed,
they are not affected; if they fail, they take the given Stress value.
Some sources of stress have two Stress Values, one that is taken if the
WIL \* 3 check is failed (like normal), and one (usually lesser) Stress
Value that is inflicted _even if the check is passed_.

Like wounds, the GM may sometimes decide that a Trauma has a specific
effect on a character -- such as the overpower urge to avoid the source
of Stress that caused the Trauma. These effects are generally meant to
be roll-played. These effects generally last until the Trauma itself has
been healed.

The penalties from Traumas and Wounds stack. Like wounds, sometimes
Traumas can be _negated_. When this occurs, the Trauma is not healed,
the character is simply able to function effectively in spite of it.

## Healing

-   Characters heal naturally:

    -   1 DV per Day. One Wound per week that you do not receive any DV,
        after all DV has been healed.
    -   1 SV per Day. One Trauma per month that you do not receive any
        SV, after all SV has been healed.

-   See also _Fast Healing_, in _Abilities_
-   Binding Wounds: characters can use Medicine to attempt to treat and
    bind wounds.

    -   This is a Medicine Task Action with a time frame of 10 minutes.
    -   Roll Medicine: on a success, recover 1d10 DV, and you _negate
        _one wound
    -   (the wound must ultimately heal naturally)
    -   This check may only be attempted once per wound.

-   Long-Term Care

    -   A character who rests and receives care heals more quickly.
    -   Instead of their natural healing, for each day a character
        spends resting and recovering, they recover 3 DV; they heal one
        wound every 4 days, after all damage has been healed.
    -   Likewise, a character who spends time resting and processing
        their traumas recovers more quickly.
    -   Instead of their natural healing, they heal 3 SV per day. They
        heal one Trauma in one week, after all stress has been healed.
    -   Long-Term Care could provide physical care, mental care or both.
        A character convalescing at a peaceful temple could receive both
        physical and mental care at the same time, for example.

-   Some Powers and Items also provide physical or mental healing; each
    Item or Power will have its own rules for doing so.

## Conditions, Potions, Poisons and Diseases

### conditions

-   I'm not sure if I actually need rules for this; I want to keep the
    number of "rules and systems" to the minimum necessary. And if I add
    rules for conditions, then everything that could be a condition
    should be---and I don't want to commit to that.
-   Conditions have _effects_ that persist while the condition applies
    to you, and rules for _removing_ the condition it (which might be as
    simple as a _duration, _after which the condition ends).
-   Bleeding:

    -   effects:

        -   1 DV every minute.
        -   Bleeding characters are easy to follow; pursuers gain a +20
            bonus on Search and Perception checks.

    -   end:

        -   successful First Aid check, as a 1 minute Task Action

### Potions and Poisons

-   Both are chemicals that affect characters.
-   Both have _effects_ which persists for the potion or poison's
    _duration_.
-   They may have an _onset time_ before the effects occur, and they may
    allow _resistance checks_ to partially resist the potion's effects.
-   Potions:

    -   are usually beneficial, and
    -   are usually drunk (you can retrieve and drink a potion as a
        Quick Action).

-   Poisons:

    -   are usually harmful, and
    -   are often either added to food or drink, or are coated on
        weapons.
    -   If a poison is coated on a weapon, then, on the first attack
        that causes a wound,

        -   the wounded target is effected by the poison, and
        -   the poison on the weapon is consumed
        -   (traces may linger, so handling the weapon may be dangerous,
            and the poison may still be detectable if the weapon is
            examined).

-   For sample Potions and Poisons, see the _Items_ section.

### Diseases

-   Diseases have an _resistance check_, and _onset time,_ a _duration,
    effects_ and possibly _treatment_.
-   Some diseases may have effects based on how long the character has
    been infected---that is, the effects may proceed through _stages_.
-   When a character is first exposed to a disease, they make their
    _resistance check_; if they succeed, then they have not been
    infected.
-   If infected, once the _onset time_ has passed, the symptoms of the
    disease manifest; at this point, the _effects_ of the disease apply.
-   The symptoms then last for the _duration_; once this has passed, the
    disease and its effects end.
-   Finally, some diseases have a specific _treatment_. The effects of
    treatment vary, ranging from curing the disease entirely, to
    allowing an additional Resistance check, to shortening the duration.

    -   Of course, some powers, potions and means magical and medical
        can also be used to cure diseases.

-   Characters can be deliberately exposed to disease: weapons can be
    coated with the blood and viscera of the infected, food can be made
    from tainted meat, and the infected can choose to enter and mingle
    among a population to spread their disease, for example.

-   Flu

    -   Resistance: DUR × 2
    -   Onset: 1 Day
    -   Duration: 3 Days
    -   Effects: fatigue, aches and nausia

-   Black Death

    -   Resistance: DUR
    -   Onset: 3 Days
    -   Duration: 1 week
    -   Effect: high fever, delerium, unconsciousness; 1d10 DV / day

-   Raking Cough

    -   Resistance: DUR × 2
    -   Onset: 1 Month
    -   Duration: permanent
    -   Effect: Sever cough, especially after exertion. Loss of stamina.

        -   Raking Cough progresses: characters suffer -5 DUR / month.
            When characters reach their DUR, they die.

## Using Magic

-   I've been moving this section around a lot. I've removed it before,
    when it was just talking about rituals, and then I added it back in
    the character guide. But, now that it's also talking about mages and
    psions, I've decided to put it back in the mechanical section.
-   In general, magical abilities that you have ready access to are best
    represented as either powers, classes or items (see Powers below,
    and in Character Options).
-   As above, powers represent some action that you can perform: this
    might be a sleight that increases your armor, a spell that allows
    you to shield yourself with ice, or a blessing bestowed on you by a
    spirit that allows you to strike fear into their enemies.
-   Classes can be used to represent magical effects that aren't
    actions. The Corpse-Herd class is an example of this: it represents
    the magical ability to build a corpse-minion that will serve you,
    but it's presented as a class rather than a power because presumably
    you'll only perform the action of making it occasionally (unless you
    get your corpse minion killed a lot).
-   Finally, items are useful to represent magical devices that you've
    created---like a bow that fires bolts of fire.

### Creating Magical Effects

-   What else can your character do with magic? Presumably, if you're a
    skilled mage (i.e. if you have 40 or 50 ranks in Spellcraft), then
    surely you have other magical resources besides the powers that you
    have (or the ability to put on light shows, if you have the Mage
    class).
-   Indeed, skilled magic users, be they mages, psions or priests, can,
    with study and preparation, produce a wide variety of magical
    effects.

    -   These effects are usually "one-off" events; they usually requrie
        (at least) a task action of several hours to achieve, and an
        appropriate skill check (either spellcraft or control for mags
        and psions, the situations being somewhat more complicated for
        priests).
    -   We don't provide detailed rules for exactly what kinds of
        effects can be created. The intent is that characters should be
        able to specify any magical effect (within reason) and then
        realize that result as a one-off effect with appropriate
        preparation.
    -   The GM is the final arbiter for what is "within reason," of
        course. This might even change: such is the nature of magic,
        that what is possible at one time in one area might not be
        workable in another.

-   Mages

    -   Mages can produce a wide variety of useful effects. They usually
        do this by acquiring texts describing the manipulation of magic,
        researching and planning, preparing reagents and ultimately
        casting their spell.

        -   For power effects, this process might be long and
            involved---it could even be an adventure unto itself!
        -   Mechanically, this usually involves at least a spellcraft
            check to design the ritual, and another spellcraft check to
            perform it.
        -   knowledge: magic, profession: mage and research might all
            also be required, especially for complex, unusual or
            powerful rituals.

    -   With a few hours of study and preparation, a mage might produce
        a great fireball or freeze over the surface of a lake.
    -   With a few days of work, a mage might raise a shield over a
        house, or blight a field.
    -   With weeks or months of works, mages might render a tower nearly
        indestructible, unleash a plague on a city, or construct a
        permanent bridge of light.

-   Psions

    -   Psions can create powerful affects through meditation,
        concentration and mental discipline.

        -   Psions often achieve this with hours of meditation and
            mental conditioning; this usually requires a control check.

    -   With a few hours of preparation, a psion could suspend the
        progress of a disease, listen to the thoughts of someone nearby,
        render themselves immune to a hostile environment (as long as
        they can maintain their trance) or solve a complex logic puzzle.
    -   With a few days of meditation and quiet contemplation, a psion
        could render themselves nearly immune to damage (as long as they
        can sustain the trance), cast their mind far from their bodies,
        or heal their wounded psyches (regaining some stress and trauma
        much like the rules for first aide).
    -   With weeks or months of quiet contemplation and meditation,
        psions could make themselves younger, regrow limbs, modify their
        physical forms (growing a carapace, adding limbs), or probe the
        minds of distant enemies.

-   Priests

    -   Priests can strike deals with spirits. Spirits are powerful, but
        also mysterious and mercurial: this makes this form of magic
        both incredibly powerful, but also incredibly complex and
        dangerous.

        -   Bargaining with spirits is the _most powerful_ form of magic
            available, especially if a suitably powerful spirit is
            contacted; however, it is also the most difficult and
            dangerous. See _Spirits_ and the sections that follow it for
            more information.
        -   More than designing a spell or meditating, striking a
            bargain with a spirit is best handled "cinematically." A
            well-struck bargain can change the course of an adventure,
            but it's also an intense encounter with a very powerful and
            (possibly) very alien being, and no two such encounters are
            alike.
        -   Bargains with spirits are frequently local: different areas
            have different spirits, so any deal struck will depend on
            the spirits in an area that can be bargained with, and what
            abilities they have to offer. (Remember that spirits have a
            hierarchy: the spirits whose basin is a local glade might be
            relatively easy to bargain with, but also not very powerful;
            a spirit whose basin is an entire mountain might be
            extraordinarily powerful, but also almost impossible to bend
            to mortal wishes, or even to contact.)

    -   Dealing with a spirit generally uses the following procedure:

        -   Research Local Spirits

            -   if you aren't a priest in the area, you probably don't
                know how the local spirits operate; even if you are,
                checking the library for any "gotchase" is wise.
            -   Pay special attention to any binds that the spirits may
                have; messing up a bind with an uncooperative spirit
                might kill you!
            -   Normally an 8 hour Task Action, requiring a Research
                check, with Knowledge: Theology, Profession: Priest or
                similar as a related skill.

        -   Design the Ritual

            -   Normally a 4 hour Task Action, requiring a Profession:
                Priest or similar check.
            -   Knowledge: Theology is a related skill, and an
                Exceptional or Critical Success on your Research test
                may help.

        -   Perform the Ritual

            -   a one hour Task Action, requiring a Profession: Priest
                or similar check.

        -   Bargain with the Spirit

            -   Once summoned---assuming it was summoned correctly---you
                can now bargain with the spirit. This is done
                in-character, using your social skills.
            -   Rituals don't have error messages; it's possible that
                things can go completely wrong in ways that might not be
                obvious.

## Powers

General rules for powers

-   Powers represent some interesting _ability_ that a character has.
    They can represent magical powers, unique physical abilities,
    martial maneuvers, or other abilities.
-   Powers usually either

    -   represent an action (in which case they'll say what type of
        action they require to perform, and how to resolve them), or
    -   modify other powers.

-   Powers can be taken from the example list, but players can also
    develop their own. GMs must approve powers developed by players;
    this process usually takes the form of a conversation between the GM
    and the player, trying to achieve the effect that the player wants
    in a way that is reasonable and that works within the rules of the
    game.
-   Here are some good guidelines to follow for designing powers:

    -   Powers should usually be D10 based; this is a D% system, and
        players are likely to have D10s handy.
    -   Powers should either require ranks in a Skill, or be linked to
        some other power that requires ranks in a Skill, or both.
    -   In general, when a power adversely affects another character, an
        opposed check should be made. Usually only one check should be
        called for; more than one is unfair to the attacker, fewer than
        one is unfair to the defender.

        -   Note that the "opposed check" doesn't have to be the skill
            that the power is linked to. The "opposed check" for
            Fireball, for example, is the Thrown Weapon attack to hit a
            target with it.

    -   Since characters will get few powers (compared to D&D, for
        example), each power should be _versatile_. Clever players
        should be able to find a number of uses for their powers.
    -   Conversely, to keep things interesting and to give other
        characters a chance to contribute, each power should have
        situations where it clearly _does not_ apply.
    -   Powers can build on one another; if you're having trouble
        building a power, it might help to split it into two powers in a
        sequence.
    -   Powers should not negate the need for a given skill; for
        example, a "tongues" power is a bad idea, because it sidesteps
        the 'languages system' and removes any incentive players might
        have to learn other languages.

        -   This is why fireball is treated as a normal held object, so
            the Thrown Weapons skill is required to make best us of it.
        -   it's also why we have Blur and not Invisibility; to use Blur
            effectively, you still need ranks in Stealth.

    -   Avoid Powers (especially maneuvers) that represent things that
        any expert should be able to do. Remember that a character with
        40 ranks in Bladed Weapons is a master swordsman; they shouldn't
        need to purchase any specific powers to do things that any
        skilled swordsman would be able to do.
    -   Avoid Powers that would be "mandatory" for any given character
        design. There shouldn't be a power that every social character
        needs to take to be functional, for example.
    -   A "full invisibility" power is a real bad idea.
    -   Also avoid D&D-style instant heals; healing is supposed to be
        difficult, and wounds sustained in combat are supposed to have a
        real impact (for the rest of the combat at least, and preferably
        into at least the next scene).

-   Some useful definitions:

    -   Spell: a power that requires ranks in the Spellcraft skill;
        assumed to draw power from ambient magical energies.
    -   Sleight: a power that requires ranks in the Control skill;
        assumed to draw power from personal magical energies.
    -   Maneuver: a power that requires ranks in a Combat skill; a
        combat maneuver achieved by great skill, without the aid of
        magic (unless it's also a spell, sleight or boon)
    -   Boon, Blessing: a power that has been granted by a Spirit,
        possibly drawing power from them or their Basin.

## Luck

Characters (Player Characters and major NPCs) have a Luck stat, and a
certain numbr Luck Points. All characters acquire 1 Luck for free, and
characters can purchase more Luck during Character Creation. Luck
represents an extra edge, an extra bit of fortune and favor that
characters can use to make sure they get the job done despite the odds.

A player's Luck stat is the maximum number of luck points they may have
(and the number of Luck Points they start with); the number of luck
points they currently have will fluctuate over the course of a game.
Players may spend Luck Points to do the following:

-   After a check:

    -   "Flip" a check result (i.e. replace a 94 with a 49)
    -   Upgrade the result

-   Before a check:

    -   Ignore the negative modifiers to a test

Players have several ways to regain luck points:

-   Players regain 1 luck point at the start of a session
-   Players may be awarded 1 luck point for achieving a major success
    that contributes to one of their motivations
-   Players may be awarded 1 luck point for excellent roll-playing

Finally, players may loose luck points for:

-   A major failure relating to one of their motivational goals
-   Exceptionally poor roll-playing (only in extreme circumstances!)

Sidebar: How many Luck Points can you spend on a check?

-   As far as the rules go, there is no set limit: a player could spend
    a point of luck to remove all penalties, then spend a luck point to
    flip a test from an 81 to a 18 to pass the test, and then spend a
    luck point again to upgrade that to an exceptional success.
-   However, GMs who want to produce a tougher game for their
    players---or who don't want their players to dump Luck Points at the
    end of a game---may limit their use of luck, allowing only one point
    to be spent on a test (for example).

Thought: rename this\* \*back to Moxie, or something else more general,
and make it do more things. I already have a couple of abilities that
allow you to do stuff with Luck, and I like them; I have a couple more I
wanted to add, except that linking them to "Luck" doesn't make much
sense.

## Size

Most characters will be roughly the same size as a human---that is, size
Medium. Some are larger, up to the size of a bear (size Large), while
others are smaller, roughly

## Characters

Characters have the following:

-   Aptitudes

    -   represents a character's fundamental mental abilities---how
        intelligent they are, how intuitive they are, etc.
    -   Each Aptitude has a _rating_ between 5 and 40, representing your
        character's ability with that aptitude.
    -   Cognition (COG): your characters ability to analyze, reason and
        plan.
    -   Coordination (COO): your characters ability to manage their
        posture and balance, their ability to get their body into
        different configurations.
    -   Intuition (INT): your character's ability to pick up on
        patterns, to master "unwritten rules" and pick up on
        subconscious queues.
    -   Reflexes (REF): your character's ability to react quickly.
    -   Savvy (SAV): your character's ability to manage social
        situations.
    -   Somatics (SOM): your character's ability to manage your body.
    -   Willpower (WIL): your character's self-discipline.
    -   Sidebar: Somatics is a mental aptitude?

        -   Somatics (SOM) sounds like some kind of "mental strength
            score." How does that make sense?
        -   Partly, that's just to make the skill system work: some
            physical skills (like Unarmed Combat) need an attribute to
            be linked to---or else we'd need to build special cases for
            them into the rules. We inherited that from Eclipse Phase.
        -   However, that's also how the body _actually works_. The
            central nervous system has to learn to recruit and manage
            the muscles of the body, and some people really do learn to
            do this better than others!

-   A race, which gives you

    -   Health and Strength values,

        -   which represent that race's physical strength and
            durability.

    -   Aptitude bonuses,

        -   which represent faculties that the race is particularly good
            (or bad) at.

    -   Senses and movement modes
    -   A size

        -   playable races are usually size Medium, about human sized;
            they are sometimes Large or Small.

    -   special characteristics,

        -   which represent unique quirks or abilities that the race
            has---like a Gnoll's thick hide, or a Shifter's ability to
            change shape.

-   Ranks in skills

    -   representing the things your character has learned to do.
    -   (Your character's ability to speak different languages is
        represented by the Language skill.)

-   Traits

    -   represent quirks your character has, like being ambidextrous.

-   Powers

    -   representing special abilities that your character has.
    -   Like a special sword maneuver that your character is good at, or
        having the ability to manifest a ball of fire.

-   A Background

    -   represent where your character is from.
    -   provides you with ranks in skills, and sometimes other benefits.

-   Classes

    -   represent associations your characters has
    -   these either represent some organization that you can call on
        for aide, or they let you "break a rule" in an interesting way.
    -   I'm worried point A could be done with traits, and point B could
        be done with powers

-   Vital Statistics (which are derived from your other choices)

    -   Durability (DUR)

        -   determined by your race, possibly adjusted by effects,
            traits or Tweak Points)

    -   Wound Threhsold (WT)

        -   DUR ÷ 5

    -   Death Rating (DR)

        -   DUR × 2

    -   Lucidity (LUC)

        -   WIL × 2

    -   Trauma Threshold (TT)

        -   LUC ÷ 5

    -   Insanity Rating (IR)

        -   LUC × 2

    -   Initiative Score (INIT)

        -   (INT + REF) ÷ 5
        -   Well, that's the _Combat_ initiative score.

    -   Damage Bonus (DB)

        -   (SOM + STR) ÷ 10

    -   Luck and Luck Points

        -   (you start with 1 Luck, and can purchase more during
            character creation.)
