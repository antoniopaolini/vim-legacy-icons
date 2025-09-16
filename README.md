# vim-legacy-icons
Restore old toolbar icons in Vim
***

On July 15, 2025, commit 2bd458a applied a patch 9.1.1529 in order to modify the icons in the Vim toolbar (the src/tools.bmp file was changed in the source code).

From https://github.com/dlejay/vim/commit/2bd458aa50b723e096a1e88225d5c1f371980628  
>patch 9.1.1529: Win32: the toolbar in the GUI is old and dated   
Problem:  Win32: the toolbar in the GUI is old and dated  
Solution: Include improved icons from Fatcow (CC by 3.0)  

***
If you think the toolbar with the new icons is garish and very distracting, and don't want too many whistle and bells in your editor, this plugin is for you!  
It simply replaces the toolbar icons with the old ones.

In the repo there's also instructions to make new icons from a file tools.bmp and some script for rename the icons so Vim can recognise them.

***

## Make icons from tools.bmp
There's some information in the documentation, but`:help toolbar-icon` is a bit cryptic and incomplete, in my opinion.

Then, I've learned:


1. No "png" for MS-Windows. For me doesn't work. We have to split "tools.bmp" in bmp files.
2.  Not just "any bitmap” format will do. The format accepted by ViM 's MS-Windows builds is BMP3 (see [here](https://imagemagick.org/script/formats.php)).
3. Furthermore, the bitmap must consist only of colours from the standard palette, but I didn't know what this standard palette was (I discovered that it is actually the definition of the [Microsoft Windows Standard VGA 16 Colour Palette](https://lospec.com/palette-list/microsoft-vga)).

## So if anyone wants to _“try it at home”_:

### Split tools.bmp 
`magick.exe tools.bmp -crop 18x18 +repage BMP3:BuiltIn%02d.bmp`
Note that you have to specify the BMP3 version in the command line,

In addition, if you start from others file or if you will resize the icon at a later time,   
you have to add: `-dither None -remap microsoft-vga-1x.png`, where " microsoft-vga-1x.png" is the palette, included in this repo (misc/microsoft-vga-1x.png)

then...

### Rename bitmap files
In "misc" folder there's some script in different languages for rename the icon files.


### Copy bitmap files
Replace icons in the "bitmap" folder and install the modified plugin as usual (for example with Pathogen).

***
And finally, here is our beloved editor, simple and without all those bright colours that distract the eyes from the buffer!



