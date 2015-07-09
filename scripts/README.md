Scripts
=======

Helper scripts for interacting with Scarabs.


click_to_scarab.py
---------------

This allows `rviz` to publish goals to the scarabs by using the
"Publish Point" feature in `rviz`.

Install:

    sudo pip install pyaml sh

Use:

    rostopic echo /clicked_point | python click_to_scarab.py

