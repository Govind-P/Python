import sports
from pynotifier import Notification
Matchinfo=sports.get_sport("CRICKET")
Notification(title="IPL live score updates")
description=str(Matchinfo,duration=120).send()