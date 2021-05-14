""" EVENT MACROS """
import stack
from enum import Enum

EventMacro = stack.EventMacro

# SPEECH
def Say():
    EventMacro(1, 0)

def Emote():
    EventMacro(2, 0)

def Whisper():
    EventMacro(3, 0)

def Yell():
    EventMacro(4, 4)

# MOVEMENT
def Walk(Dir):
    _dir = ['NW', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W'].index(Dir)
    EventMacro(5, _dir)

# GUMP CONTROL
def WarPeace():
    EventMacro(6, 0)

def OpenConfiguration():
    EventMacro(8, 0)

def OpenPaperdoll():
    EventMacro(8, 1)

def OpenStatus():
    EventMacro(8, 2)

def OpenJournal():
    EventMacro(8, 3)

def OpenSkills():
    EventMacro(8, 4)

def OpenSpellbook():
    EventMacro(8, 5)

def OpenChat():
    EventMacro(8, 6)

def OpenBackpack():
    EventMacro(8, 7)

def OpenOverView():
    EventMacro(8, 8)

def OpenMail():
    EventMacro(8, 9)

def OpenPartyManifest():
    EventMacro(8, 10)

def OpenPartyChat():
    EventMacro(8, 11)

def OpenNecroSpellbook():
    EventMacro(8, 12)

def OpenPaladinSpellbook():
    EventMacro(8, 13)

def OpenCombatBook():
    EventMacro(8, 14)

def OpenBushidoSpellbook():
    EventMacro(8, 15)

def OpenNinjitsuSpellbook():
    EventMacro(8, 16)

def OpenGuild():
    EventMacro(8, 17)

def OpenSpellweavingSpellbook():
    EventMacro(8, 18)

def OpenQuestLog():
    EventMacro(8, 19)

def CloseConfiguration():
    EventMacro(9, 0)

def ClosePaperdoll():
    EventMacro(9, 1)

def CloseStatus():
    EventMacro(9, 2)

def CloseJournal():
    EventMacro(9, 3)

def CloseSkills():
    EventMacro(9, 4)

def CloseSpellbook():
    EventMacro(9, 5)

def CloseChat():
    EventMacro(9, 6)

def CloseBackpack():
    EventMacro(9, 7)

def CloseOverview():
    EventMacro(9, 8)

def CloseMail():
    EventMacro(9, 9)

def ClosePartyManifest():
    EventMacro(9, 10)

def ClosePartyChat():
    EventMacro(9, 11)

def CloseNecroSpellbook():
    EventMacro(9, 12)

def ClosePaladinSpellbook():
    EventMacro(9, 13)

def CloseCombatBook():
    EventMacro(9, 14)

def CloseBushidoSpellbook():
    EventMacro(9, 15)

def CloseNinjitsuSpellbook():
    EventMacro(9, 16)

def CloseGuild():
    EventMacro(9, 17)

def MinimizePaperdoll():
    EventMacro(10, 1)

def MinimizeStatus():
    EventMacro(10, 2)

def MinimizeJournal():
    EventMacro(10, 3)

def MinimizeSkills():
    EventMacro(10, 4)

def MinimizeSpellbook():
    EventMacro(10, 5)

def MinimizeChat():
    EventMacro(10, 6)

def MinimizeBackpack():
    EventMacro(10, 7)

def MinimizeOverview():
    EventMacro(10, 8)

def MinimizeMail():
    EventMacro(10, 9)

def MinimizePartyManifest():
    EventMacro(10, 10)

def MinimizePartyChat():
    EventMacro(10, 11)

def MinimizeNecroSpellbook():
    EventMacro(10, 12)

def MinimizePaladinSpellbook():
    EventMacro(10, 13)

def MinimizeCombatBook():
    EventMacro(10, 14)

def MinimizeBushidoSpellbook():
    EventMacro(10, 15)

def MinimizeNinjitsuSpellbook():
    EventMacro(10, 16)

def MinimizeGuild():
    EventMacro(10, 17)

def MaximizePaperdoll():
    EventMacro(11, 1)

def MaximizeStatus():
    EventMacro(11, 2)

def MaximizeJournal():
    EventMacro(11, 3)

def MaximizeSkills():
    EventMacro(11, 4)

def MaximizeSpellbook():
    EventMacro(11, 5)

def MaximizeChat():
    EventMacro(11, 6)

def MaximizeBackpack():
    EventMacro(11, 7)

def MaximizeOverview():
    EventMacro(11, 8)

def MaximizeMail():
    EventMacro(11, 9)

def MaximizePartyManifest():
    EventMacro(11, 10)

def MaximizePartyChat():
    EventMacro(11, 11)

def MaximizeNecroSpellbook():
    EventMacro(11, 12)

def MaximizePaladinSpellbook():
    EventMacro(11, 13)

def MaximizeCombatBook():
    EventMacro(11, 14)

def MaximizeBushidoSpellbook():
    EventMacro(11, 15)

def MaximizeNinjitsuSpellbook():
    EventMacro(11, 16)

def MaximizeGuild():
    EventMacro(11, 17)

# OPEN DOOR
def OpenDoor():
    EventMacro(12, 0)
    
# ACTION SKILLS
def UseSkill(skill):
    EventMacro(13, Skill[skill].value)
    
# SPELLS
def Cast(spell):
    EventMacro(15, spell)
    
# MISCELLANEOUS
def LastSpell():
    EventMacro(16, 0)

def LastObject():
    EventMacro(17, 0)
    
def Bow():
    EventMacro(18, 0)

def Salute():
    EventMacro(19, 0)

def QuitGame():
    EventMacro(20, 0)

def AllNames():
    EventMacro(21, 0)

def LastTarget():
    EventMacro(22, 0)

def TargetSelf():
    EventMacro(23, 0)

def ToggleLHand():
    EventMacro(24, 1)

def ToggleRHand():
    EventMacro(24, 2)

def WaitForTarget():
    EventMacro(25, 0)

def TargetNext():
    EventMacro(26, 0)

def AttackLast():
    EventMacro(27, 0)

def Delay(TimeOutMS):
    EventMacro(28, 0, TimeOutMS)

def CirrcleTrans():
    EventMacro(29, 0)
    
def CloseGumps():
    EventMacro(31, 0)

def AlwaysRun():
    EventMacro(32, 0)

def SaveDesktop():
    EventMacro(33, 0)

def KillGumpOpen():
    EventMacro(34, 0)

def PrimaryAbility():
    EventMacro(35, 0)

def SecondaryAbility():
    EventMacro(36, 0)

def EquipLastWeapon():
    EventMacro(37, 0)

# CLIENT'S RANGE CONTROL
def SetUpdateRange(Range):
    EventMacro(38, 0, Range)

def ModifyUpdateRange(Range):
    EventMacro(39, 0, Range)

def IncreaseUpdateRange():
    EventMacro(40, 0)

def DecreaseUpdateRange():
    EventMacro(41, 0)

def MaximumUpdateRange():
    EventMacro(42, 0)

def MinimumUpdateRange():
    EventMacro(43, 0)

def DefaultUpdateRange():
    EventMacro(44, 0)

def UpdateUpdateRange():
    EventMacro(45, 0)

def EnableUpdateRangeColor():
    EventMacro(46, 0)

def DisableUpdateRangeColor():
    EventMacro(47, 0)

def ToggleUpdateRangeColor():
    EventMacro(48, 0)

# INVOKE VIRTUES
def Invoke(virtue):
    v = ['Honor', 'Sacrifice', 'Valor',
         'Compassion', 'N/A', 'N/A',
         'Justice', 'N/A'].index(virtue.capitalize()) + 1
    EventMacro(49, v)
    
# TARGETING SYSTEM
# num(1,5): 1-hostile; 2-party members; 3-followers; 4-objects; 5-mobiles
def SelectNext(num):
    if num > 5: num = 5
    if num < 1: num = 1
    EventMacro(50, num)

def SelectPrevious(num):
    if num > 5: num = 5
    if num < 1: num = 1
    EventMacro(51, num)

def SelectNearest(num):
    if num > 5: num = 5
    if num < 1: num = 1
    EventMacro(52, num)
# --num

def AttackSelected():
    EventMacro(53, 0)

def UseSelected():
    EventMacro(54, 0)

def CurrentTarget():
    EventMacro(55, 0)

def ToggleTargetingSystem():
    EventMacro(56, 0)

def ToggleBuffWindow():
    EventMacro(57, 0)
    
def BandageSelf():
    EventMacro(58, 0)

def Bandage():
    EventMacro(59, 0)

# GARGOYLE
def ToggleFly():
    EventMacro(60, 0)

# ENUMS
class Skill(Enum):
    Anatomy = 1
    AnimalLore = 2
    AnimalTaming = 35
    ArmsLore = 4
    Begging = 6
    Cartography = 12
    DetectHidden = 14
    Discordance = 15
    EvalInt = 16
    ForensicEval = 19
    Hiding = 21
    Inscription = 23
    ItemIdentification = 3
    Meditation = 46
    Peacemaking = 9
    Poisoning = 30
    RemoveTrap = 48
    SpiritSpeak = 32
    Stealing = 33
    Stealth = 47
    TasteIdentification = 36
    Tracking = 38
    LastSkill = 0
# --EOF
