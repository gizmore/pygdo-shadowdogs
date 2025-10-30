# Shadowdogs

Shadowdogs is a realtime mud/mmo for various chat networks.

The story was built upon my precious life,
which revealed so much wisdom and different worlds,
that i would never leave my spot as a crazy computer guy
in my hometown.

Even if they tell you the worst.
I would never ever vanish.

- gizmore@wechall.net


## Races

 - Dragon (NPC) +5 magic
 - Elve  +1 magic 
 - Human -2 magic (cannot learn it from beginning)
 - Animal (NPC) all zero
 - Ork -3 magic (can never learn magic)


## [Factions](../GDT_Faction.py)

## Combat

The combat happens in real time and actions can be done.
Every player has a one item stack,
where the last command gets executed after your cooldown is fine.

The default command is `$sdattack <rand>`, locking a random target.

Items and equipment can be used and changed, but it costs time.


### Weapons

#### Melee
 - Club
 - Mace
 - Short Sword

#### Firearms
 - Baretta
 - Magnum

### Mobs
 - Lamer (human, 2-4HP, Fists, all zero)

### Stats
 - Level 0-1000 (not reachable)
 - XP (
 - HP (10 is begin, +1 each level)
 - MP
 - height
 - weight
 - carry
 - max_carry

### Attributes
 - strength (carry kg)
 - quickness (cooldown time -1s per amt)
 - dexterity (dodge)
 - body (HP)
 - magic (MP)
 - intelligence (effect of spells and executables)
 - wisdom (duration of spells and executables)
 - charisma

### Skills
 - fight
 - hacking 
 - firearms


### Spells
 - calm - a little slow healing
 - heal - a medium slow healing
 - hummingbird - increase the quickness of a target
 - blow - move a target backwards
 - strike - damage an enemy by using MP
 

### Executables

Hacking executables are like magic spells but don't require time.
There are randomly N executables started, based on your hacking skill: hacking() / 4

 - tripwire L4 => target gets 1 damage because they tripped badly (oh nose).
 - reloc L5 => clears enemy combat stack
 - overload L6 => target erhält schaden basierend auf hacking (je besser der gegner hacken kann desto mehr schaden)
 - spoof L7 => makes enemy attack a friend
 - smartgun L8 => unload the targets weapon
 - sidechannel L9 => nuyen werden geklaut
 - reboot L14 => target player freezes for attacker hacking seconds.
 - essence L10 => target erhält schaden basierend auf intelligence (je mehr int, je mehr damage)
 - preload L18 => target uses a random item on a random target
 - dos L24 => Ltarget player cannot hack anymore

### Combat math

Example combat between a beginner and a lamer

Lamer: 3 HP atk 2 dmg 1-2 def 1
beginner: 10 HP atk 2 dmg 1-3 def 1

if rand(0, atk) >= rand(0, def)
    dmg = rand(min, max) - armor~~


### Newbie Section

If you are new to shadowdogs, just read the rules.

To login into the combat zone, just think to Alice:
"I want to login to the nexus my friend".

Believe what you hear.

Ask Questions and give feedback.

Enjoy!

