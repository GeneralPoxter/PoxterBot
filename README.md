# PoxterBot
<p align="center"><img src="poxter.jpg" width="100"/></p>

PoxterBot is a fork of [Pearl](https://github.com/defund/pearl). 

## Installation
Follow [Pearl#Prerequisites](https://github.com/defund/pearl#prerequisites).

## Usage
To start the bot, run `python poxter.py` or run the shell script [rebuild-poxter.sh](rebuild-poxter.sh) (this requires specifying the PoxterBot directory in the script).

In [hangouts](https://hangouts.google.com/), run `p.[command]` in any conversation to activate a PoxterBot feature.

In addition to plugins in Pearl, PoxterBot allows the user to:

**add files**
* Save all images/files in a folder named `files` in `custom`
* Send these images/files using the command `p.[filename]`

**automate responses**
* Add responses and their trigger strings (in lower case) accordingly to the [respond.json](poxter/custom/respond.json) in the form `response: [array of triggers]`
* Any message sent to you in hangouts that matches the triggers will cause poxter to send the appropriate response
