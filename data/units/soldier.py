"""
Placeholder
"""

from .job import Job

class Soldier(Job):
    def __init__(self, teamColor):
        self.info = {
            "image_active_path": "characters/{team}/soldier/{team}-soldier.png".format(team=teamColor),
            "image_inactive_path": "characters/{team}/soldier/{team}-soldier-inactive.png".format(team=teamColor),
            "stats": {
                "name": "Soldier",
                "hp": 10,
                "strength": 4,
                "defense": 1,
                "accuracy": 90,
                "evasion": 10,
                "movement": 2,
            },
        }
        Job.__init__(self, self.info)
