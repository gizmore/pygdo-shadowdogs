# Hacking Minigame

This is the shadowdogs hacking minigame.

In your Home you can `#hack computer`.

Inside the game try `#x move r` twice.


## Rulez

- The game field is X*3 cells "high" `.`.
- Fog of war tiles are rendered `#`.
- You start at a random field `S` with your icon being a `P`.
- The main vault, a green `$`, will allow exit.exe to run.
- Sinks `v` will log you out with damage.
- Passwords `§` will log you out with 4 damage and eat up all your cpu and scramble your map unless you have the pass.
- if your cpu power goes below zero you will get damage (rand(max(0,amt_below_zero-hacking), amt_below_zero+1)
- if you move out of the map you get 2 damage and log you out.
- cpu power recovers slowly, but only outside the hacking attempts.
- Traps (ring) `0`-`3` deal damage and cost cpu cycles.
You will get moved to the start or your last backdoor.
Your backdoor will be gone.
If you had a backdoor, the trap will not reposition.
- `0`: 3 dmg 10cc
- `1`: 2 dmg  8cc
- `2`: 1 dmg  6cc
- `3`: 0 dmg  4cc
- Wall `W` just blocks your way.


## Executables

clock cycles reduce cpu.

- move.exe udlr (2 cc u/d, 3cc r/l) - Usually built into the deck.
- strafe.exe ur/dr/dl/ul (4cc) - Move diagonally.
- exit.exe (0 cc) - Only works on vaults
- flee.exe (6 cc) - 
- ping4/6.exe   (2/1 cc) udlr - check if a field beside is out of bounds.
- trace[1-3].exe (4-2 cc) udlr - reveal a field beside you
- nmap4/6.exe (0 cc) - reveals (4/6) out of 8 adjacent squares after login. 0cc threaded.
- hydra.exe (10 cc) - Tries to bruteforce a password.
- map.exe (5 cc) - print the full automap so far discovered.
- backdoor.exe -  (6 cc) - Mark a field as backdoor recovery field when you hit a trap `3` or `2`. The trap will not reposition.
- rootkit.exe  -  (8 cc) - Mark a field as backdoor recovery field when you hit any trap. The trap will reposition.
- modkit.exe   - (10 cc) - Mark a field as backdoor recovery field when you hit any trap.
- dma.sys - (5 + N cc) - Teleport to a memory address N steps away, also diagonally.



