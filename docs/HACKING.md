# Hacking Minigame



## Rulez

- The playfield is X*3 cells "high" `.`.
- You start at a random field `P`.
- The main vault, a green `$`, will allow exit.exe to run.
- Sinks `v` will log you out with damage.
- Passwords `§` will log you out with 4 damage and eat up all your cpu and scramble your map unless you have the pass.
- if your cpu power goes below zero you will get damage (rand(max(0,amt_below_zero-hacking), amt_below_zero+1)
- if you move out of the map you get 3 damage and log you out.
- cpu power recovers slowly, but only outside the hacking attempts.
- Traps (ring) `0`-`3` deal damage and cost cpu cycles.
- `0`: 3 dmg 10cc
- `1`: 2 dmg  8cc
- `2`: 1 dmg  6cc
- `3`: 0 dmg  3cc


## Executables

clock cycles reduce cpu.

- move.exe udlr (1 cc) - Usually built into the deck.
- exit.exe (0 cc) - 
- flee.exe (4 cc)
- ping4/6.exe   (2/1 cc) udlr - check if a field beside is out of bounds.
- scan[1-3].exe (4-2 cc) udlr - reveal a field beside you
- map.exe - print the full automap
- backdoor -  (6 cc) - Mark a field as backdoor recovery field when you hit a trap `3` or `2`. The trap will reposition.
- rootkit  -  (8 cc) - Mark a field as backdoor recovery field when you hit any trap. The trap will reposition.
- modkit   - (10 cc) - Mark a field as backdoor recovery field when you hit any trap.
