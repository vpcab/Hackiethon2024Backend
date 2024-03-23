# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from Game.gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = DashAttackSkill
# dash has 7 cooldown
SECONDARY_SKILL = Hadoken
# hadoken has 

#constants, for easier move return
#movements
JUMP = ("move", (0,1))
FORWARD = ("move", (1,0))
BACK = ("move", (-1,0))
JUMP_FORWARD = ("move", (1,1))
JUMP_BACKWARD = ("move", (-1, 1))

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = SECONDARY,
moves_iter = iter(moves)

# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
        
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
    
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])
        enemy_string_last = enemy.get_past_move(1)
        # enemy_last = enemy.get_last_move()
        # print("PAST", enemy_string_last, "LAST", enemy_last)
        # print(enemy.get_last_move())

        if get_stun_duration(player) >= 1:
            return BACK

        # TODO: change these to better cater to dash and hanoken attacks
        # Check if any skill is available and use it wisely
        if not primary_on_cooldown(player):
        # and abs(get_pos(player)[0] - get_pos(enemy)[0]) <= prim_range(player):
            return PRIMARY
        elif not secondary_on_cooldown(player):
        # and abs(get_pos(player)[0] - get_pos(enemy)[0]) <= seco_range(player):
            
            return SECONDARY
        elif not heavy_on_cooldown(player):
        # and abs(get_pos(player)[0] - get_pos(enemy)[0]) <= 1:
            return HEAVY

        # Defensive strategy if low on health or enemy is too close
        if get_hp(player) < 20 and get_hp(player) < get_hp(enemy):
            # print("we try to block") 
        #  #TODO: add this back to the conditional. DONE
        # or abs(get_pos(player)[0] - get_pos(enemy)[0]) < 2:
            # Block if enemy is close and likely to attack
            if abs(get_pos(player)[0] - get_pos(enemy)[0]) == 1:
                # if 
                if get_block_status(player) >= 5:
                    # print("we actually block")
                    return BLOCK
                else:
                    # print("we")
                    return BACK
            # Move away from the enemy if possible
            elif get_pos(player)[0] < get_pos(enemy)[0]:
                return BACK
            else:
                return FORWARD

        # Offensive strategy if player has more health
        if get_hp(player) > get_hp(enemy):
            # TODO: implement dash attack strategy
            # Close in on the enemy if not in attack range
            if abs(get_pos(player)[0] - get_pos(enemy)[0]) > 1:
                if get_pos(player)[0] < get_pos(enemy)[0]:
                    return FORWARD
                else:
                    return BACK
            # Use light attack if close and other attacks are on cooldown
            else:
                return LIGHT

        
        
        
        # if we are getting knockback, we move backwards


        
        # Default to light attack if nothing else is applicable
        return FORWARD

