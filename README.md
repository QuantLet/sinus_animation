# GIF animation

Run this command in the directory that contains frames/ directory (needs installed imagemagick)

    convert -delay 5 -loop 0 -dispose previous frames/*.png animation.gif