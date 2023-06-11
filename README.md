# zhtErrorFix for Dragon's Dogma

If your Dragon's Dogma game crashes with the error "failed to open *_zht.gmd" at any point (startup, mid game, etc...), this fix should help.

## Usage

[Download the mod here](https://www.nexusmods.com/dragonsdogma/mods/884?tab=files)

**If you are using Vortex:**
    - Open Vortex
    - Go to the mods section
    - Open Mods staging folder
    - Copy all the files (`ARCtool.exe, findzht.py, run.cmd`) to the root of the staging folder **if you don't know which mod is causing the problem**.
    - Copy all the files (`ARCtool.exe, findzht.py, run.cmd`) to the mod folder **if you know which specific mod is causing the problem**.
    - Run `run.cmd`

**If you are not using vortex**
You could just copy all the files (`ARCtool.exe, findzht.py, run.cmd`) to the `nativePC` folder and run `run.cmd`. But this would unpack all of the games' arc files, which might take a while. If you know which mod is causing the error, its best to copy the files to that mod's folder and run `run.cmd`.