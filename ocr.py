import stack
# Class structures
class PetStats:
    def __init__(self):
        self.Stats = {'Hits' : 0, 'MaxHits' : 0, 'Stam' : 0, 'MaxStam' : 0,
                      'Mana' : 0, 'MaxMana' : 0, 'Str' : 0, 'Dex' : 0, 'Int' : 0,
                      'Barding' : 0.0, 'Loyalty' : ''}

        self.Res = {'AR' : 0, 'FR' : 0, 'CR' : 0, 'PR' : 0, 'ER' : 0}

        self.Dmg = {'AD' : 0, 'FD' : 0, 'CD' : 0, 'PD' : 0, 'ED' : 0,
                    'Min' : 0, 'Max' : 0}
        
        self.Skills = {'Wrestling' : 0.0, 'Tactics' : 0.0, 'ResistingSpells' : 0.0,
                       'Anatomy' : 0.0, 'Poisoning' : 0.0, 'Magery' : 0.0,
                       'EvalInt' : 0.0, 'Meditation' : 0.0}

        self.Misc = {'PreferredFood' : '', 'PackInstincts' : ''}
        
class OCRChar:
    def __init__(self, text = '', size = 0):
        self.Text = text
        self.Size = size

class BodInfo:
    def __init__(self):
        self.Item = ''
        self.Type = ''
        self.Quality = ''
        self.Material = ''
        self.Amount = ''
        self.Price = ''

class Rune:
    def __init__(self):
        self.Name = ''
        self.X = 0
        self.Y = 0

class Charges:
    def __init__(self):
        self.Number = 0
        self.Max = 0

class Runebook:
    def __init__(self):
        self.Runes = []
        self.TotalCharges = None
        self.PosX = 0
        self.PosY = 0
        self.Count = 0
#--
        
def CmpPix(XPos, YPos, PixOP, PixCmp):
    PixCmpTemp = ''
    PixCol = ''
    if PixOP in ['=', '==']:
        PixOP = 'in'
    if PixOP == '<>':
        PixOP = 'notin'
    PixCmpTemp = '_{0}_'.format(PixCmp)
    PixCol = str(stack.GetPix(XPos, YPos))
    if PixCol == "-1":
        return False
    PixCol = '_{0}_'.format(PixCol)
    if PixOP == 'in':
        if PixCol in PixCmpTemp:
            return True
        return False
    if PixOP == 'notin':
        if PixCol in PixCmpTemp:
            return False
        return True
    return False

def ReadChar(XPos, YPos, PixOP, PixCmp, TextOrNum = "text"):
    PixOP = PixOP.lower()
    if CmpPix(XPos, YPos + 5, PixOP, PixCmp):
        if CmpPix(XPos, YPos + 13, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 3, PixOP, PixCmp):
                    if CmpPix(XPos, YPos + 2, PixOP, PixCmp):
                        return OCRChar('[', 4)
                    if CmpPix(XPos, YPos + 15, PixOP, PixCmp):
                        return OCRChar('|', 2)
                    return OCRChar('(', 4)
                if CmpPix(XPos + 2, YPos + 4, PixOP, PixCmp):
                    if CmpPix(XPos + 2, YPos + 8, PixOP, PixCmp):
                        if CmpPix(XPos + 2, YPos + 13, PixOP, PixCmp):
                            if CmpPix(XPos + 4, YPos + 5, PixOP, PixCmp):
                                return OCRChar('B', 8)
                            return OCRChar('E', 7)
                        return OCRChar('F', 7)
                    if CmpPix(XPos + 2, YPos + 9, PixOP, PixCmp):
                        if CmpPix(XPos + 2, YPos + 10, PixOP, PixCmp):
                            return OCRChar("R", 8)
                                
                        return OCRChar("P", 8)
                    
                    if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                        return OCRChar("D", 8)
                    
                    return OCRChar("%", 10)
                
                if CmpPix(XPos + 2, YPos + 8, PixOP, PixCmp):
                    if CmpPix(XPos + 2, YPos + 6, PixOP, PixCmp):
                        if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                            return OCRChar("N", 8)
                        
                        return OCRChar("X", 8)
                    
                    if CmpPix(XPos + 2, YPos + 9, PixOP, PixCmp):
                        return OCRChar("K", 8)
                    
                    return OCRChar("H", 8)
                
                if CmpPix(XPos, YPos + 11, PixOP, PixCmp):
                    if CmpPix(XPos + 2, YPos + 5, PixOP, PixCmp):
                        return OCRChar("M", 10)
                    
                    if CmpPix(XPos + 2, YPos + 13, PixOP, PixCmp):
                        return OCRChar("L", 7)
                    
                    return OCRChar("I", 3)
                
                return OCRChar("!", 3)
            
            if CmpPix(XPos + 2, YPos + 11, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
                    if CmpPix(XPos, YPos + 8, PixOP, PixCmp):
                        return OCRChar("k", 6)
                    
                    return OCRChar("2", 8)
                
                return OCRChar(">", 8)
            
            if CmpPix(XPos + 2, YPos + 8, PixOP, PixCmp):
                if CmpPix(XPos + 2, YPos + 13, PixOP, PixCmp):
                    return OCRChar("b", 6)
                
                return OCRChar("h", 6)
            
            if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                return OCRChar("l", 3)
            
            return OCRChar("i", 3)
        
        if CmpPix(XPos, YPos + 11, PixOP, PixCmp):
            if CmpPix(XPos + 3, YPos + 8, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                    if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
                        return OCRChar("5", 8)
                    
                    if CmpPix(XPos, YPos + 8, PixOP, PixCmp):
                        return OCRChar("G", 8)
                    
                    return OCRChar("S", 8)
                
                if CmpPix(XPos, YPos + 10, PixOP, PixCmp):
                    return OCRChar("8", 8)
                
                return OCRChar("3", 8)
            
            if CmpPix(XPos + 4, YPos + 5, PixOP, PixCmp):
                if CmpPix(XPos + 3, YPos + 9, PixOP, PixCmp):
                    return OCRChar("Q", 9)
                
                if CmpPix(XPos + 5, YPos + 8, PixOP, PixCmp):
                    if TextOrNum.lower() == "number":
                        return OCRChar("0", 8)
                    
                    return OCRChar("O", 8)
                
                return OCRChar("C", 8)
            
            if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
                return OCRChar("U", 8)
            
            return OCRChar("6", 8)
        
        if CmpPix(XPos + 2, YPos + 9, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                    if CmpPix(XPos + 6, YPos + 4, PixOP, PixCmp):
                        return OCRChar("V", 8)
                    
                    return OCRChar("W", 12)
                
                return OCRChar("Y", 9)
            
            if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                    return OCRChar("9", 8)
                
                return OCRChar("?", 7)
            
            return OCRChar("1", 4)
        
        if CmpPix(XPos + 1, YPos + 6, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
                    return OCRChar("4", 8)
                
                return OCRChar("'", 3)
            
            return OCRChar('\\', 9)
        
        if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
            if CmpPix(XPos + 1, YPos + 4, PixOP, PixCmp):
                return OCRChar("`", 3)
            
            return OCRChar(Chr(34), 4)
        
        if CmpPix(XPos, YPos + 3, PixOP, PixCmp):
            return OCRChar("°", 5)
        
        return OCRChar("7", 8)
    
    if CmpPix(XPos, YPos + 9, PixOP, PixCmp):
        if CmpPix(XPos + 4, YPos + 13, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 8, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 12, PixOP, PixCmp):
                    if CmpPix(XPos, YPos + 13, PixOP, PixCmp):
                        if CmpPix(XPos + 5, YPos + 8, PixOP, PixCmp):
                            return OCRChar("m", 9)
                        
                        return OCRChar("n", 6)
                    
                    return OCRChar("y", 6)
                
                if CmpPix(XPos, YPos + 7, PixOP, PixCmp):
                    return OCRChar("@", 12)
                
                if CmpPix(XPos, YPos + 10, PixOP, PixCmp):
                    return OCRChar("w", 8)
                
                return OCRChar("x", 6)
            
            if CmpPix(XPos + 2, YPos + 11, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 10, PixOP, PixCmp):
                    return OCRChar("e", 6)
                
                return OCRChar("<", 8)
            
            if CmpPix(XPos + 3, YPos + 14, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 15, PixOP, PixCmp):
                    return OCRChar("g", 6)
                
                return OCRChar("q", 6)
            
            if CmpPix(XPos + 3, YPos + 5, PixOP, PixCmp):
                return OCRChar("d", 6)
            
            return OCRChar("a", 6)
        
        if CmpPix(XPos, YPos + 12, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 13, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
                    return OCRChar("A", 8)
                
                if CmpPix(XPos, YPos + 14, PixOP, PixCmp):
                    return OCRChar("p", 6)
                
                return OCRChar("r", 6)
            
            if CmpPix(XPos, YPos + 8, PixOP, PixCmp):
                return OCRChar("u", 6)
            
            if CmpPix(XPos + 3, YPos + 11, PixOP, PixCmp):
                return OCRChar("o", 6)
            
            return OCRChar("c", 6)
        
        if CmpPix(XPos, YPos + 8, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 10, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 11, PixOP, PixCmp):
                    return OCRChar("v", 6)
                
                return OCRChar("^", 10)
            
            return OCRChar("+", 7)
        
        if CmpPix(XPos, YPos + 10, PixOP, PixCmp):
            return OCRChar("s", 6)
        
        if CmpPix(XPos + 1, YPos + 4, PixOP, PixCmp):
            return OCRChar("{", 5)
        
        return OCRChar("-", 6)
    
    if CmpPix(XPos + 1, YPos + 13, PixOP, PixCmp):
        if CmpPix(XPos, YPos + 13, PixOP, PixCmp):
            if CmpPix(XPos + 1, YPos + 11, PixOP, PixCmp):
                if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
                    return OCRChar("Z", 8)
                
                return OCRChar("z", 6)
            
            if CmpPix(XPos, YPos + 12, PixOP, PixCmp):
                if CmpPix(XPos + 1, YPos + 14, PixOP, PixCmp):
                    return OCRChar(",", 3)
                
                return OCRChar(".", 3)
            
            return OCRChar("j", 6)
        
        if CmpPix(XPos, YPos + 11, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
                return OCRChar(";", 3)
            
            if CmpPix(XPos + 1, YPos + 5, PixOP, PixCmp):
                return OCRChar("&", 11)
            
            return OCRChar("J", 8)
        
        if CmpPix(XPos, YPos + 2, PixOP, PixCmp):
            return OCRChar(")", 4)
        
        if CmpPix(XPos, YPos + 3, PixOP, PixCmp):
            return OCRChar("}", 5)
        
        return OCRChar("f", 6)
    
    if CmpPix(XPos + 2, YPos + 9, PixOP, PixCmp):
        if CmpPix(XPos + 1, YPos + 10, PixOP, PixCmp):
            if CmpPix(XPos, YPos + 8, PixOP, PixCmp):
                return OCRChar("t", 6)
            
            if CmpPix(XPos, YPos + 10, PixOP, PixCmp):
                return OCRChar("#", 12)
            
            return OCRChar("/", 9)
        
        if CmpPix(XPos, YPos + 2, PixOP, PixCmp):
            return OCRChar("]", 5)
        
        if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
            return OCRChar("T", 7)
        
        return OCRChar("$", 9)
    
    if CmpPix(XPos + 1, YPos + 11, PixOP, PixCmp):
        if CmpPix(XPos, YPos + 4, PixOP, PixCmp):
            return OCRChar("*", 10)
        
        if CmpPix(XPos, YPos + 6, PixOP, PixCmp):
            return OCRChar(":", 3)
        
        return OCRChar("=", 6)
    
    if CmpPix(XPos, YPos + 1, PixOP, PixCmp):
        return OCRChar("~", 6)
    
    if CmpPix(XPos, YPos + 15, PixOP, PixCmp):
        return OCRChar("_", 8)
    
    return OCRChar(" ", 8)

def ReadText(XPos, YPos, PixOP, PixCmp, TextOrNum, XOff, Delim = ''):
    retval = ''
    XOff = XOff + XPos
    if len(Delim) == 0:
        Delim = ' '
    while XPos <= XOff:
        ocr = ReadChar(XPos, YPos, PixOP, PixCmp, TextOrNum)
        retval += ocr.Text
        XPos += ocr.Size
    if Delim in retval:
        retval = retval[1:retval.index(Delim) - 1]
    return retval
                                   
def TextScan(XPos, YPos, PixOP, PixCmp, TextOrNum = 'text', Delim = ''):
    retval = ''
    if Delim == '':
        Delim = ' '
    while Delim in retval:
        ocr = ReadChar(XPos, YPos, PixOP, PixCmp, TextOrNum)
        retval += ocr.Text
        XPos += ocr.Size
    return retval[1:retval.index(Delim) - 1]
