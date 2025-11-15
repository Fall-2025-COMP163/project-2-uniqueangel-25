"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Angel Drake
Date: 11.14.2025

AI Usage: AI used to help with inhertiance implementations and debugging.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

# Base Class for all characters.
# Root of inheritance hierachy. Holds the common attributes and methods.
class Character:
    
    def __init__(self, name, health, strength, magic):
        """Initializes core character atttributes shared by all subclasses"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic        
        
    def attack(self, target):
        """Base attack method. Applies damage equal to the character's strength"""
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)       
        
    def take_damage(self, damage):
        """Reduced health by daamge amount. Ensures health does not go below 0."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! (HP: {self.health})")        
        
    def display_stats(self):
        """
        Prints the character's current core stats in a formatted way.
        """
        print("---------Character Stats---------")
        print(f"Name:      {self.name}")
        print(f"Health:    {self.health}")
        print(f"Strength:  {self.strength}")
        print(f"Magic:      {self.magic}")
        print("---------------------------------")

# --- PARENT CLASS (inherits from Character) ---
class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Uses super() tp call the Character constrctor and adds
        player-specific attributes (level,experience, class)
        """      
        super().__init__(name,health,strength,magic)        
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        """
        Overrides the parent methond. First calls Character.display_stats()
        using super() and then prints the Player-Specific info.
        """
        super().display_stats()
        print(f"Class:         {self.character_class}")
        print(f"Level:         {self.level}")
        print(f"Experience:    {self.experience}")
        print(f"--------------------------------")

# --- CHILD CLASS (inherits from Player) ---
class Warrior(Player):
    """
    Warrior class focused on hish physical damage and health.
    Overrides the attach method for unique combat behavior
    """
    
    def __init__(self, name):
        """
        Initializes the Warrior with fixed, high physical stats."
        """
        super().__init__(name, "Warrior",120, 15, 5)        
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
       Excutes a phydical slash with bonus damage based on strength.
        """
        damage = self.strength + 5
        print(f"{self.name} slashes {target.name} for {damage} damage!")
        target.take_damage(damage)        
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = (self.strength * 2) + 10
        print(f"{self.name} unleashes a POWER STRIKE on {target.name} for {damage} damage")
        target.take_damage(damage)

# --- CHILD CLASS (inherits from Player) ---
class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """Initializes the Mage with fixed, high magic stats"""
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        """Overrides Character/Player attack. Excutes a magic attack"""

        damage = self.magic + 3
        print(f"{self.name} casts a magic attack on {target.name} for {damage} damage!")
        target.take_damage(damage)      
        
    def fireball(self, target):
        """Special mage ability - a powerful magical attack."""
        damage = (self.magic * 2) + 5
        print(f"{self.name} casts a magic attack on {target.name} for {damage} damage!")
        target.take_damage(damage)

# --- CHILD CLASS (inherits from Player) ---
class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Initalizes teh Rogue with balanced stats suitable for a sneeaky role"""
        super().__init__(name, "Rogue", 90, 12, 10)     
        
    def attack(self, target):
        """
        Overrides Character/Player attack. Introduces a chance of 
        30% for a critial hit(double damage).
        """
        import random
        damage = self.strength
        if random.randint(1,10) <= 3:
            damage*= 2
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)        
        
    def sneak_attack(self, target):
        """Special rogue ability - guaranteed critical hit."""
        damage = self.strength * 2
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)

# --- COMPOSITION CLASS ---
class Weapon:
    """
    A seperate class used by characters via composition(has-arelationship)."""
    
    def __init__(self, name, damage_bonus):
        """Initializes weapon name and its damage bonus value"""
        self.name = name
        self.damage_bonus = damage_bonus
          
    def display_info(self):
        """Prints the weapon's attributes."""
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}") 

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
