from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)

    def run(self):

        # d1_foe_goal = abs(self.me.location.y - self.foe_goal.location.y)

        # d1_friend_goal = abs(self.me.location.y - self.friend_goal.location.y)

        # b1_foe_goal = abs(self.ball.location.y - self.foe_goal.location.y)

        # b1_friend_goal = abs(self.ball.location.y - self.friend_goal.location.y)

        # in_front_of_ball = d1_foe_goal < b1_foe_goal
        # behind_ball = d1_foe_goal >= b1_foe_goal

        if self.get_intent() is not None:
            return

        # Kickoff
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return

        targets = {
            "at_opponent_goal": (self.foe_goal.left_post, self.foe_goal.right_post),
            "away_from_friend_goal": (
                self.friend_goal.right_post,
                self.friend_goal.left_post,
            ),
        }

        hits = find_hits(self, targets)

        if len(hits["at_opponent_goal"]) > 0:
            self.set_intent(hits["at_opponent_goal"][0])
            print("at opponent goal")
            return

        if len(hits["away_from_friend_goal"]) > 0:
            self.set_intent(hits["away_from_friend_goal"][0])
            print("away from my goal")
            return

        if self.time % 2 == 0:
            print(hits)

        # self.set_intent(atba())

        # if in_front_of_ball:
        #     self.set_intent(goto(self.friend_goal.location))
        #     return

        # self.set_intent(short_shot(self.foe_goal.location))

        # self.set_intent(atba())
