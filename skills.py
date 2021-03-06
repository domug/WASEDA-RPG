## Skill Class
class Skill:
    """Skill class"""

    def __init__(self, name, damage, cost_mp):
        self.name = name
        self.damage = damage
        self.cost_mp = cost_mp

    def __str__(self):
        return "< {} >: damage({}), mp({})".format(self.name, self.damage, self.cost_mp)


###############################################################################################
###############################################################################################


# Skills

double_slash = Skill("Double Slash", 7, 5)
triple_slash = Skill("Triple Slash", 12, 7)
quadruple_slash = Skill("Quadruple Slash", 16, 9)
firebolt = Skill("Fire Bolt", 20, 10)
icestrike = Skill("Ice Strike", 20, 10)
meteor = Skill("Meteor", 50, 20)
iceage = Skill("Ice Age", 50, 20)


skill_dict = {
    "Triple Slash": str(triple_slash),
    "Quadruple Slash": str(quadruple_slash),

    "Fire Bolt": str(firebolt),
    "Ice Strike": str(icestrike),
    "Meteor": str(meteor),
    "Ice Age": str(iceage)
}