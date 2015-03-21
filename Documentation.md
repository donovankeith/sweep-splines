**Sweep Splines 0.2**
Written for CINEMA 4D [R12](https://code.google.com/p/sweep-splines/source/detail?r=12).048

Copyright (C) 2011 by Donovan Keith (www.donovankeith.com)

# OVERVIEW: #
Sweep Splines takes the currently selected splines and sweeps them with rectangular splines.

# INSTALLATION: #
  1. Open up Cinema 4D
  1. Click on Python->User Scripts->Script Folder to open the folder
  1. Open your file browser to where these instructions are stored.
  1. Drag the "SweepSplines" folder into your "scripts" folder.
  1. Restart Cinema 4D.
  1. Confirm the installation was successful by going to: Python->User Scripts->Sweep Splines

# INSTRUCTIONS: #

## SWEEPING SPLINES: ##
  1. Select the spline objects you would like to Sweep
    * NOTE: Object Manager->Edit->Select Children is a quick way to select all splines under a Null
  1. Click on Python->User Scripts->Sweep Splines->Sweep Splines
  1. Your splines should now have dimension.

**NOTE:** In addition to the sweeps you will notice an "SS Control Objects" group, this contains your
master rectangle, and a "master instance" that drives all other instanced profiles.


## MODIFYING THE DEFAULT RECTANGLE: ##
By default after you run "Sweep Splines" the rectangle will be selected and editable in the attributes
manager. Any changes you make there will automatically propogate. If your rectangle was deselected:

  1. Locate the "SS Control Objects" object group in the Object Manager.
  1. Click on the "+" icon to the left of the group to expand it.
  1. Select "SS Rectangle"
  1. Make any changes you would like.

## SWAPPING IN A DIFFERENT PATH ##
Sometimes you might want a shape other than a rectangle, in those cases...

  1. Locate the "SS Control Objects" object group in the Object Manager.
  1. Click on the "+" icon to the left of the group to expand it.
  1. Click on the "SS Master Instance [Don't Delete]" object
  1. Drag the new profile spline into the "Reference Object" field in the object manager.