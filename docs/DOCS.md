# Shadowdogs

Shadowdogs is a realtime mud/mmo for various chat networks.


## Races

 - Dragon (NPC) +5 magic
 - Elve  +1 magic 
 - Human -2 magic (cannot learn it from beginning)
 - Animal (NPC) all zero
 - Ork -3 magic (can never learn magic)


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
 - freeze.exe (freeze the target by frying nanochips)
 - dillusion.exe (change the target combat target to a random target (also friends))
 - jam.exe (unload a target weapon)
 - poison.exe (damage targets with their own MP)

### Combat math

Example combat between a beginner and a lamer

Lamer: 3 HP atk 2 dmg 1-2 def 1
beginner: 10 HP atk 2 dmg 1-3 def 1

if rand(0, atk) >= rand(0, def)
    dmg = rand(min, max) - armor~~
