# I wanna be the scratch engine olin edition
## Introduction
This is an I wanna be the guy fangame engine made and playable entirely in Scratch 3.

### Credits
- Kayin, for making the original I wanna be the guy
- YoYoYoDude1 for making the GameMaker fangame engine this references for a lot of its features.

## Creating & editing levels
First off, it's important to create a copy of the engine on Scratch and set the `debug_mode` variable to `true`. This enables the D keybind, whicfh lets you enter a new game string holding all of your game's objects. How you get that game string is up to you (and I'll even help you understand its rules later so you can use all your favorite level editors), but the easiest way to do it is using the LDtk project and Python importer.

### with the LDtk Project
After downloading the project, feel free to rename it (from within LDtk), add as many rooms as you like (though keep their resolution at 480x360), and make whatever changes you want. Make sure every room has a `player_start` object, and, unless it's the final room, at least one `warp` object to make your way onto the next one. <p>
After that, make sure you have the Python interpreter and the pyperclip module installed, and launch the importer. It should automatically copy the game string generated from your LDtk project to your clipboard, allowing you to paste it into your Scratch project with the D keybind. Make sure there is a matching backdrop and song for all your rooms and voila! All the objects you placed in LDtk have been ported into Scratch form.

### manually/through your own automation
The syntax for game strings is pretty simple. A game string is comprised of rooms, which are comprised of objects, which are comprised of values. Rooms are the arrangements of stuff that your game loads one of at a time; objects are the individual features of rooms that your player interacts with, like blocks or delicious fruit; and values are like Scratch variables, they can hold any number or string of text, and describe the information that is passed to the object manager so it can place all the right objects at all the right places with all the right properties. <p>
Here is an example game string we'll use to make a few observations.

```
player_start,0,16;block,0,0,12;sign,0,16,This\, right here\, is what the sign says.;warp,0,48,2,(null);&player_start,96,0;
```

- Values are separated by commas, objects are separated by semicolons, and levels are separated by ampersands.
- Objects don't end in commas, and whole game strings don't end in ampersands, but rooms always end in semicolons.
- Strings with characters that the game string system already uses can be communicated by escaping the character with a backslash.
- An empty value is communicated as `(null)`
- The default object structure goes "Sprite ID, X position, Y position", but they can be longer by passing parameters into the object.

#### Parameters
Parameters are values passed for the making of your objects _besides_ their IDs and positions, such as the destination of a warp, or the text of a sign. In the game string, they are simply the values of an object starting from the fourth one. <p>

Here is a table of all the parameters of the built-in objects that have them.

| Sprite ID | Parameter 1 | Parameter 2 |
| --- | --- | --- |
| `trigger` | Trigger key (String) |
| `block` | Costume # (Integer) | 
| `spike` | Direction (String\|null) |
| `delicious_fruit` | Trigger key (String) |
| `save` | Max difficulty (String) |
| `warp` | Room number (Integer) | Set difficulty (String\|null) |
| `sign` | Sign text (String) |

## Creating your own objects
Creating an object is as simple as duplicating the template sprite and setting the object ID in the spawn routine (where it by default says `OBJECT NAME HERE`). If you want any parameters to be passed to your object, read from the list `place_object.parameters`. <p>
If you are using the LDtk importer, you will also have to create a matching entity for it in the LDtk app, as well as describe it in the `objects.json` file in the Python script's working directory.

### How to make an `objects.json` entry
An object in `objects.json` is represented by a JSON object (as in the little thing represented by {}s). <p>

The key for that object should be the ID of the matching entity **in your LDtk project**. <p>
The string with a key of `sprite_id` should be the ID of the matching sprite **in Scratch**. <p>
The array with a key of `fields` can hold strings, numbers, and nulls. It represents the parameters that are passed onto your object, in order. If a string in it starts with `$`, what follows it is a macro, meaning that string will be replaced by a field matching the macro name, pulled from the object in your LDtk level.

### Tags
Certain shared behaviors between sprites can easily be toggled on or off by adding or removing your sprite's name from a Scratch list. There are 4 built-in tags, here are the names and functions of each one:

| Tag list name | Description |
| --- | --- |
| tag.bullet_blocker | Makes bullets disappear upon collision |
| tag.hazard | Makes the player die upon collision |
| tag.semisolid | Makes the player land on, yet go through a platform |
| tag.solid | Makes the player land on, run into and bonk on a platform |
