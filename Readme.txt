This tool is made for Filmora 9.x serie, and tested with Filmora 9.6 in Windows.
I don't know if it will work with other versions.

It fixes the missing effects in the Filmora interface after installing a
specific effect pack; example cases:
	- Installed effects don't appear at all.
	- Installed effects appear, but some default effects disappear.
	
This happens because Filmora has a fragile effects-organizing system, which
depends on the 'Config.json' file located in:
C:\ProgramData\Wondershare Filmora\Default Effects\DefaultPackage

This file keeps getting overwritten each time a new effect pack is installed.

What does this tool do is that it merges the config files of different effects pack
into one big config file that makes them visible to Filmora, it can also - as a side
effect - cover other non-installed effects (but they won't appear until they are installed).

Thanks to AI.
