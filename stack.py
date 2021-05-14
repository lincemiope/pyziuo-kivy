from ctypes import WinDLL, string_at
import time, re
from random import randint
dll = WinDLL("uo")
handle = dll.Open()

def Open():
    v = dll.Version()
    if v != 3: return False
    dll.SetTop(handle,0)
    dll.PushStrVal(handle, "Set".encode('ascii'))
    dll.PushStrVal(handle, "CliNr".encode('ascii'))
    dll.PushInteger(handle, 1)
    return dll.Execute(handle) == 0

def Close():
    dll.Close()

def _executeCommand(ReturnResults, CommandName, *vars):
    dll.SetTop(handle, 0)
    dll.PushStrVal(handle, "Call".encode('ascii'))
    dll.PushStrVal(handle, CommandName.encode('ascii'))
    for var in vars:
        if type(var) is int:
            dll.PushInteger(handle, var)
        elif type(var) is str:
            dll.PushStrVal(handle, var.encode('ascii'))
        elif type(var) is bool:
            dll.PushBoolean(handle, var)
    dll.Execute(handle)
    if ReturnResults:
        results = read()
        return results
    
def write(*vars):
    dll.SetTop(handle, 0)
    for var in vars:
        if type(var) is int:
            dll.PushInteger(handle, var)
        elif type(var) is str:
            dll.PushStrVal(handle, var.encode('ascii'))
        elif type(var) is bool:
            dll.PushBoolean(handle, var)
    dll.Execute(handle)
 
def read():
    t = []
    result = True
    index = 1
    while result:
        tp = dll.GetType(handle, index)
        if tp is 0:
            result = False
        elif tp is 1:
            t.append(dll.GetBoolean(handle, index))
        elif tp is 3:
            t.append(dll.GetInteger(handle, index))
        elif tp is 4:
            t.append(string_at(dll.GetString(handle, index)).decode('utf-8', errors='ignore'))
 
        index += 1
        if index > 100:     # Just in case
            result = False  #
 
    return t

def GetVal(name):
    write("Get", name)
    res = read()
    if type(res) == str and len(res) == 0:
        return 'N/A'
    if type(res) == list and len(res) > 0:
        return res[0]
    if res != None:
        return res
    return 0

def SetVal(name, val):
    write("Set", name, val)
    res = read()
    if len(res) == 0:
        return 'N/A'
    if type(res) == list:
        return res[0]
    else:
        return res

# Char List
def OnlineCharlist():
    OriginalNr = CliNr()
    for i in range(1, CliCnt()):
        CliNr(i)
        EventMacro(8, 2)
        
    EUOWait(20)
    _ret = []
        
    for i in range(1, CliCnt()):
        CliNr(i)
        EventMacro(8, 2)
        _cID = CharID()
        _char = CharName()
        if _char == None or _char == '':
            _char = CharName()
        if _char != None and _char != '':
            _ret.append(CharName())

    CliNr(OriginalNr)
    return _ret
#--

# Character Info
def CharPosX():
    return GetVal("CharPosX")

def CharPosY():
    return GetVal("CharPosY")

def CharPosZ():
    return GetVal("CharPosZ")

def CharPos():
    cp = charpos(GetVal("CharPosX"),GetVal("CharPosY"),GetVal("CharPosZ"))
    return cp

def Distance(ItemOrID):
    Item = FindItem(ItemOrID, True, 0)[0] if type(ItemOrID) == int else ItemOrID   
    cp = CharPos()
    diff = [abs(cp.X - Item.X), abs(cp.Y - Item.Y), abs(cp.Z - Item.Z)]
    return max(d for d in diff)

def InRange(ItemOrID, Range):
    return Distance(ItemOrID) <= Range

def CharDir():
    return GetVal("CharDir")

def CharID():
    return GetVal("CharID")

def CharStatus():
    return GetVal("CharStatus")

def CharType():
    return GetVal("CharType")

def BackpackID():
    return GetVal("BackpackID")
# --

# Status Info
def CharName():
    return GetVal("CharName")

def Sex():
    return GetVal("Sex")

def Str():
    return GetVal("Str")

def Dex():
    return GetVal("Dex")

def Int():
    return GetVal("Int")

def Hits():
    return GetVal("Hits")

def MaxHits():
    return GetVal("MaxHits")

def DiffHits():
    return GetVal("MaxHits") - GetVal("Hits")

def Stam():
    return GetVal("Stamina")

def MaxStam():
    return GetVal("MaxStam")

def Mana():
    return GetVal("Mana")

def MaxMana():
    return GetVal("MaxMana")

def MaxStats():
    return GetVal("MaxStats")

def Luck():
    return GetVal("Luck")

def Weight():
    return GetVal("Weight")

def MaxWeight():
    return GetVal("MaxWeight")

def DiffWeight():
    return int(GetVal("MaxWeight")) - int(GetVal("Weight"))

def MinDmg():
    return GetVal("MinDmg")

def MaxDmg():
    return GetVal("MaxDmg")

def Gold():
    return GetVal("Gold")

def Followers():
    return GetVal("Followers")

def MaxFol():
    return GetVal("MaxFol")

def AR():
    return GetVal("AR")

def FR():
    return GetVal("FR")

def CR():
    return GetVal("CR")

def PR():
    return GetVal("PR")

def ER():
    return GetVal("ER")

def TP():
    return GetVal("TP")
#--

# Client Info
def CliNr(n = 0):
    if n != 0:
        SetVal("CliNr", n)
    else:
        return GetVal("CliNr")

def CliCnt():
    return GetVal("CliCnt")

def CliLang():
    return GetVal("CliLang")

def CliVer():
    return GetVal("CliVer")

def CliLogged():
    return bool(GetVal("LObjectID"))

def CliLeft():
    return GetVal("CliLeft")

def CliTop():
    return GetVal("CliTop")

def CliXRes():
    return GetVal("CliXRes")

def CliYRes():
    return GetVal("CliYRes")

def CliTitle(s = ''):
    if len(s) > 0:
        SetVal("CliTitle", s)
    else:
        return GetVal("CliTitle")
#--

# Misc
def EnemyHits():
    return GetVal("EnemyHits")

def EnemyID():
    return GetVal("EnemyID")

def RHandID():
    return GetVal("RHandID")

def LHandID():
    return GetVal("LHandID")

def CursorX():
    return GetVal("CursorX")

def CursorY():
    return GetVal("CursorY")

def Random():
    return randint(1, 1000)

def CursKind():
    return GetVal("CursKind")

def TargCurs(bval = None): # bool
    if bval != None:
        SetVal("TargCurs", bval)
    else:
        return GetVal("TargCurs")

def Shard():
    return GetVal("Shard")

def LShard():
    return GetVal("LShard")

def SysMsg():
    return GetVal("SysMsg")
#--

# Cont
def NextCPosX():
    return GetVal("NextCPosX")

def NextCPosY():
    return GetVal("NextCPosY")

def ContPosX(val = None):
    return SetVal("ContPosX", val) if val != None else GetVal("ContPosX")

def ContPosY(val = None):
    return SetVal("ContPosY", val) if val != None else GetVal("ContPosY")

def ContSizeX():
    return GetVal("ContSizeX")

def ContSizeY():
    return GetVal("ContSizeY")

def ContSize():
    return (GetVal("ContSizeX"), GetVal("ContSizeY"))

def ContKind():
    return GetVal("ContKind")

def ContName():
    return GetVal("ContName")

def ContID():
    return GetVal("ContID")

def ContType():
    return GetVal("ContType")

def ContHP():
    return GetVal("ContHP")
#--

# Gumps
def WaitForGump(kind, timeout = 3000):
    tout = int(time.time() + timeout / 1000)
    while ContKind() != kind:
        if time.time() >= tout:
            SysMessage('Gump not found.', 33)
            return

def Crafting(cat, sub):
    craft = 20988
    cpos = [25, 50 + 20 * cat]
    page = int(sub / 10)
    ipos = [235, 50 + 20 * sub]
    Click(ContPosX() + cpos[0], ContPosY() + cpos[1])
    WaitForGump(craft)
    if page != 0:
        for i in range(page):
            Click(ContPosX() + 380, ContPosY() + 270)
            WaitForGump(craft)
    Click(ContPosX() + ipos[0], ContPosY() + ipos[1])
    WaitForGump(craft)
#--
# Last Action
def LObjectID(val = None):
    if val != None:
        SetVal("LObjectID", val)
    else:
        return GetVal("LObjectID")

def LObjectType(val = None):
    if val != None:
        SetVal("LObjectType", val)
    else:
        return GetVal("LObjectType")

def LTargetID(val = -1):
    if val != -1:
        SetVal("LTargetID", val)
    else:
        return GetVal("LTargetID")

def LTargetKind(val = None):
    if val != None:
        SetVal("LTargetKind", val)
    else:
        return GetVal("LTargetKind")

def LTargetTile(val = None):
    if val != None:
        SetVal("LTargetTile", val)
    else:
        return GetVal("LTargetTile")

def LTargetX(val = None):
    if val != None:
        SetVal("LTargetX", val)
    else:
        return GetVal("LTargetX")

def LTargetZ(val = None):
    if val != None:
        SetVal("LTargetZ", val)
    else:
        return GetVal("LTargetZ")

def LTargetY(val = None):
    if val != None:
        SetVal("LTargetY", val)
    else:
        return GetVal("LTargetY")

def LLiftedID(val = None):
    if val != None:
        SetVal("LLiftedID", val)
    else:
        return GetVal("LLiftedID")

def LLiftedKind(val = None):
    if val != None:
        SetVal("LLiftedKind", val)
    else:
        return GetVal("LLiftedKind")

def LLiftedType(val = None):
    if val != None:
        SetVal("LLiftedType", val)
    else:
        return GetVal("LLiftedType")

def LSkill(val = None):
    if val != None:
        SetVal("LSkill", val)
    else:
        return GetVal("LSkill")

def LSpell(val = None):
    if val != None:
        SetVal("LSpell", val)
    else:
        return GetVal("LSpell")
#--

# Custom Helper Commands
def SetAbility(ability): # 1 = primary, 2 = secondary
    EventMacro(34+ability, 0)
    
def ScanJournal(OldRef):
    results = _executeCommand(True, "ScanJournal", OldRef)
    if not results: return
    j = journalscan()
    j.NewRef = int(results[0])
    j.Cnt = int(results[1])
    return j

def GetJournal(index):
    results = _executeCommand(True, "GetJournal", index)
    if not results: return
    return journalentry(str(results[0]), int(results[1]))

journalRef = 0
def InJournal(StringsToFind):
    global journalRef
    journal = []
    jf = ScanJournal(journalRef)
    if jf.NewRef > journalRef:
        for i in range(journalRef, jf.NewRef):
            journal.append(GetJournal(i).Line)
        journalRef = jf.NewRef
    found = next(s for s in journal if StringsToFind.lower() in s.lower())
    if found:
        return True
    else:
        return False

def Now():
    return int(time.time())

def FromNow(seconds):
    return int(time.time()) + seconds

def DiffTime(timestamp):
    return int(timestamp - time.time())

def Wait(seconds):
    time.sleep(seconds)

def WaitMS(milliseconds):
    time.sleep(milliseconds / 1000)
    
def EUOWait(euotime): # 20 = 1s
    time.sleep(euotime * .05)

def Target(TimeOutMS = 2000):
    out = time.time() + TimeOutMS / 1000.
    while time.time() < out:
        if TargCurs(): return True
    return False

def HideItem(ID):
    _executeCommand(False, "HideItem", ID )

def ScanItems(VisibleOnly = True):
    return int(_executeCommand(True, "ScanItems", VisibleOnly)[0])

def FindItem(TypeOrID, VisibleOnly = True, containerID = 0):
    itmcnt = ScanItems(VisibleOnly)
    items = []
    if itmcnt == 0: return -1
    for i in range(0, itmcnt):
        item = GetItem(i)
        if item.ID != None and item.ID != 0:
            if (item.Type == TypeOrID or item.ID == TypeOrID) and (containerID == 0 or item.ContID == containerID):
                items.append(item)
                continue
            if TypeOrID == -1 and item.ContID == containerID != 0:
                items.append(item)
                
    return items
    
def Key(Key, Ctrl, Alt, Shift):
    _executeCommand(False, "Key", Key, Ctrl, Alt, Shift)

def Move(X, Y, Accuracy, TimeOutMS):
    res = _executeCommand(True, "Move", X, Y, Accuracy, TimeOutMS)
    if res == None or res == '':
        return False
    if str(res).lower() == 'true':
        return True
    return False

def Msg(msg, send = True):
    _executeCommand(False, "Msg", msg)
    if send: Key('enter', False, False, False)

def HeadMsg(msg, color = 0, font = 3):
    ExMsg(CharID(), font, color, msg)

def PublicMsg(msg):
    Msg('[c {0}'.format(msg))

def GuildMsg(msg):
    Msg('[g {0}'.format(msg))

def VendorMsg(msg):
    Msg('[v {0}'.format(msg))

def MapMsg(msg):
    Msg('--{0}'.format(msg))

def GetCont(index):
    res = _executeCommand(True, "GetCont", index)
    if len(res) != 0:
        return container(res)

def ContTop(index):
    _executeCommand(False, "ContTop", index)

def TileInit(NoOverRides):
    res = _executeCommand(True, "TileInit", NoOverRides)
    if len(res) != 0:
        return bool(res[0])
    return False

def TileCnt(X, Y, Facet):
    res = _executeCommand(True, "TileCnt", X, Y, Facet)
    if len(res) != 0:
        return int(res[0])
    return 0

def TileGet(X, Y, index, Facet):
    res = _executeCommand(True, "TileGet", X, Y, index, Facet)
    if len(res) != 0:
        return tile(res)
    return None

def CliDrag(ItemID): # use click function to drop
    _executeCommand(False, "CliDrag", ItemID)

def Property(ItemID):
    p = pinfo()
    o = None
    while o is None or type(o) != list or len(o) < 2:
        o = _executeCommand(True, "Property", ItemID)
    p.Name = o[0]
    p.Info = o[1]
    return p

def ContextMenu(ItemID, x = None, y = None):
    if x and y:
        _executeCommand(False, "Popup", ItemID, x, y)
    else:
        _executeCommand(False, "Popup", ItemID)
    
def Drag(ItemID, Amount):
    _executeCommand(False, "Drag", ItemID, Amount)

def DropC(ContID, x = None, y = None):
    if x and y:
        _executeCommand(False, "DropC", x, y)
    else:
        _executeCommand(False, "DropC")

def DropG(x, y, z):
    _executeCommand(False, "DropG", x, y, z)

def ExMsg(ItemID, FontID, Color, Message):
    _executeCommand(False, "ExMsg", ItemID, FontID, Color, Message)

def Pathfind(x, y, z):
    _executeCommand(False, "Pathfind", x, y, z)

#def UseLObject():
#    EventMacro(17, 0)

def RenamePet(ID, name):
    _executeCommand(False, "RenamePet", ID, name)

def Click(x, y, left = True, down = True, up = True, middle = False): # z ??
    _executeCommand(False, "Click", x, y, left, down, up, middle)

def GetItem(index):    
    temp = _executeCommand(True, "GetItem", index)
    if not temp or len(temp) < 10: return None
    return founditem(temp[0], temp[1], temp[2], temp[3], temp[4],
                     temp[5], temp[6], temp[7], temp[8], temp[9])

def GetPix(x, y):
    res = _executeCommand(True, "GetPix", x, y)
    if len(res) == 0: return 'N/A'
    if type(res) == list:
        return res[0]
    else:
        return res

def GetSkill(sk):
    #s = Skill[sk].value
    res = _executeCommand(True, "GetSkill", sk)
    return skill(res)

def SkillLock(skill, status):
    if skill.lower() == 'stealth':
        skill = 'Stlt'
    elif skill.lower() == 'animal lore':
        skill = 'Anil'
    else:
        skill = skill[0:4]
    s = ['up', 'down', 'locked'].index(status)
    _executeCommand(False, "SkillLock", skill, s)

def StatLock(stat, status):
    stat = stat[0:3].capitalize()
    s = ['up', 'down', 'locked'].index(status)
    _executeCommand(False, "StatLock", stat, s)
#--

# Event Macro
def EventMacro(Par1, Par2, Par3 = None):
    if Par3 != None:
        _executeCommand(False, "Macro", Par1, Par2, Par3)
    else:
         _executeCommand(False, "Macro", Par1, Par2)
#--

# SysMessage
def SysMessage(msg, hue = 0):
    _executeCommand(False, "SysMessage", msg, hue)
#--

# Addons
def UseType(Type, Color = 'any', Cont = 0):
    Cont = Cont if Cont != 0 else BackpackID()
    if Color == 'any':
        itm = next(i.ID for i in FindItem(Type, True, Cont))
    else:
        itm = next(i.ID for i in FindItem(Type, True, Cont) if i.Col == Color)
    if itm:
        LObjectID(itm)
        EventMacro(17, 0)

def UseObject(ID):
    LObjectID(ID)
    EventMacro(17, 0)

def GetProperties(ItemID):
    plist = Property(ItemID).Info.split('\r\n')
    res = []
    for s in plist:
        pDict = pdict()
        temp = s.replace("%","").replace(":","").replace("+","").strip()
        dpos = re.search('\d', s)
        if plist.index(s) < 2:
            pDict.Name = temp
            pdict.Value = 0
        elif dpos:
            pDict.Name = temp[0:dpos.start()].strip()
            pDict.Value = temp[dpos.start():].strip()
        else:
            continue
        res.append(pDict)
    return res

def WaitForProps(ItemID, TimeOutMS):
    t = time.time() + TimeOutMS / 1000.
    props = []
    while props == []:
        if time.time() > t:
            return None
        p = GetProperties(ItemID)
        if not p is None and p != []:
            props = p
    return props

def GetSop(ItemID):
    p = Property(ItemID)
    plist = p.Info.split('\n')
    s = singlesop()
    s.Serial = ItemID
    if type(p.Name) != str or not "Scroll Of" in p.Name: return None
    skillList = ["Anatomy", "Animal Lore", "Animal Taming", "Archery",
                "Blacksmithy", "Bushido", "Chivalry", "Discordance", "Eval Intelligence",
                "Fencing", "Fishing", "Focus", "Healing", "Imbuing", "Mace Fighting",
                "Magery", "Meditation", "Musicianship", "Mysticism", "Necromancy",
                "Ninjitsu", "Parrying", "Peacemaking", "Provocation", "Resisting Spells",
                "Spellweaving", "Spirit Speak", "Stealing", "Stealth", "Swordsmanship",
                "Tactics", "Tailoring", "Throwing", "Veterinary", "Wrestling"]

    s.Skill = next(n for n in skillList if n.lower() in p.Name.lower())
    valList = [105,110,115,120]
    s.Value = next(v for v in valList if str(v) in p.Name)
    s.Days = int(plist[-1].replace("Days Until Deletion", "").strip())
    return s

def WaitForContext(ItemID, Choice, TimeoutMS = 2000):
    ContextMenu(ItemID)
    WaitForGump(39204, TimeoutMS)
    Click(80, 20 * Choice)

def CountType(Type, Color, Cont = 0):
    Cont = Cont if Cont != 0 else BackpackID()
    items = FindItem(Type, True, Cont)
    if items is None or type(items) == list and len(items) == 0:
        return 0
    
    if not Color in [-1, 'any', 'all']:
        return sum(i.Stack for i in items if i.Col == Color)
    else:
        return sum(i.Stack for i in items)

#--
# Supporting Classes
class tile:
    def __init__(self, data = []):
        if len(data) == 4:
            self.Type = int(data[0])
            self.Z = int(data[1])
            self.Name = str(data[2])
            self.Flags = int(data[3])
        else:
            self.Type = self.Z = self.Flags = 0
            self.Name = ''

class container:
    def __init__(self, data = []):
        if data == [] or len(data) < 8:
            self.Kind = self.X = self.Y = self.SX = self.SY = self.ID = self.Type = 0
            self.Name = ''
        else:
            self.Kind = int(data[0])
            self.X = int(data[1])
            self.Y = int(data[2])
            self.SX = int(data[3])
            self.SY = int(data[4])
            self.ID = int(data[5])
            self.Type = int(data[6])
            self.Name = str(data[7])
            
class charpos:
    def __init__(self, x, y, z):
        self._x, self._y, self._z = x, y, z
    @property
    def X(self):
        return self._x
    @property
    def Y(self):
        return self._y
    @property
    def Z(self):
        return self._z

class journalscan:
    def __init__(self, newref = 0, cnt = 0):
        self.NewRef = newref
        self.Cnt = cnt

class pinfo:
    def __init__(self, name = '', info = ''):
        self.Name = name
        self.Info = info

class pdict:
    def __init__(self, name = '', value = ''):
        self.Name = name
        self.Value = value

class props:
    def __init__(self, dictlist = []):
        self.Props = dictlist
        
class singlesop:
    def __init__(self, value = 0, skill = '', days = 0, serial = 0):
        self.Value = value
        self.Skill = skill
        self.Days = days
        self.Serial = serial

class founditem:
    def __init__(self, _id = 0, _type = 0, kind = 0, contid = 0, x = 0, y = 0,
                 z = 0, _stack = 0, rep = 0, col = 0):
        self.ID = _id
        self.Type = _type
        self.Kind = kind
        self.ContID = contid
        self.X, self.Y, self.Z = x, y, z
        self.Stack = _stack
        self.Rep = rep
        self.Col = col

class skill:
    def __init__(self, data):
        if len(data) < 4:
            self.Normal = self.Real = self.Cap = self.Lock = 0
        else:
            self.Normal = data[0]
            self.Real = data[1]
            self.Cap = data[2]
            self.Lock = data[3]
  
class journalentry:
    def __init__(self, line = 0, col = 0):
        self.Line = line
        self.Col = col

class journalscan:
    def __init__(self, ref = 0, cnt = 0):
        self.NewRef = ref
        self.Cnt = cnt
        
class gump:
    def __init__(self, name, width, height):
        self.Name = name
        self.Size = (width, height)

class Gump:
    def __init__(self):
        self.Gumps = {'runebook' : gump('generic gump', 452, 236)}

    def __getitem__(self, key):
        if key in self.Gumps:
            return self.Gumps[key]
        return gump('generic gump', 452, 236) #runebook
#-- EOF
