import kivy, os, sys
from time import time
from stack import *
from eventmacro import *
from threading import Thread
import pyperclip
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.treeview import *
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserListView

class ConsoleLabel(Label):
    bcolor = ListProperty([.2, .2, .2, .8])
    
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    default_path = StringProperty(os.path.dirname(os.path.realpath(sys.argv[0])))

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    default_path = StringProperty(os.path.dirname(os.path.realpath(sys.argv[0])))
    
class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    tree_view = ObjectProperty(None)
    error_console = ObjectProperty(None)
    btn_play = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.t_Script = None
        self.playing = False
        self.NodesInst = {}
        Window.bind(on_dropfile = self._on_file_drop)

        self.popNodesDict()
        Clock.schedule_once(self.popTree, 2)
        for k,v in self.ids.items():
            print(str(k),str(v), sep=' ')

    def _on_file_drop(self, window, file_path):        
        with open(os.path.join(file_path)) as stream:
            self.text_input.text = stream.read()

    def stopCallBack(self):
        self.playing = False
        self.btn_play.disabled = False
        self.t_Script.join(100)
        self.error_console.text = 'Error Console'
        
    def playCallBack(self):
        self.playing = True
        self.btn_play.disabled = True
        script = ''
        slist = [i for i in self.text_input.text.replace('\t', '    ').split('\n')]
        for s in slist:
            script += s.replace('Halt()', 'self.playing = False') + '\n'
            if ('for ' in s or 'while ' in s) and ':' in s:
                spc = len(s) - len(s.lstrip()) + 4
                script += ' ' * spc + "if self.playing == False: break\n"
   
        self.t_Script = Thread(target=self.WorkingThread, args=(script,))
        self.t_Script.start()
        
    def WorkingThread(self, script):
        self.error_console.text = 'Error Console'
        try:
            exec(script)
        except Exception as e:
            self.error_console.text = '{0}: {1}'.format(e, e.args)
            quit(0)
        finally:
            self.playing = False
            self.btn_play.disabled = False
            
        
    def TVCallback(self, e):
        self.popNodesDict()
        for cat, nodes in self.NodesInst.items():
            for node, inst in nodes.items():
                inst.text = '[color=c8c8c8][ref={0}()]{0}()[/ref]: [ref={1}]{1}[/ref][/color]'.format(node, self.Nodes[cat][node])
                inst.bind(on_ref_press=self.CopyToClipboard)

    def popNodesDict(self):
        self.Nodes = {
            'Character Info' : {'CharPosX' : CharPosX(), 'CharPosY' : CharPosY(),
                                'CharPosZ' : CharPosZ(), 'CharDir' : CharDir(),
                                'CharID' : CharID(), 'CharType' : CharType(),
                                'BackpackID' : BackpackID()},
            
            'Status Bar' : {'CharName' : CharName(), 'Sex' : Sex(), 'Str' : Str(),
                            'Dex' : Dex(), 'Int' : Int(), 'Hits' : Hits(),
                            'MaxHits' : MaxHits(), 'Stam' : Stam(), 'MaxStam' : MaxStam(),
                            'Mana' : Mana(), 'MaxMana' : MaxMana(), 'MaxStats' : MaxStats(),
                            'Luck' : Luck(), 'Weight' : Weight(), 'MaxWeight' : MaxWeight(),
                            'DiffWeight' : DiffWeight(), 'MinDmg' : MinDmg(),
                            'MaxDmg' : MaxDmg(), 'Followers' : Followers(), 'MaxFol' : MaxFol(),
                            'AR' : AR(), 'FR' : FR(), 'CR' : CR(),
                            'PR' : PR(), 'ER' : ER(), 'TP' : TP()},
            
            'Container Info' : {'NextCPosX' : NextCPosX(), 'NextCPosY' : NextCPosY(), 'ContPosX' : ContPosX(),
                                'ContPosY' : ContPosY(), 'ContSizeX' : ContSizeX(), 'ContSizeY' : ContSizeY(),
                                'ContKind' : ContKind(), 'ContName' : ContName(), 'ContID' : ContID(),
                                'ContType' : ContType(), 'ContHP' : ContHP()},
            
            'Last Action' : {'LObjectID' : LObjectID(), 'LObjectType' : LObjectType(), 'LTargetID' : LTargetID(),
                             'LTargetX' : LTargetX(), 'LTargetY' : LTargetY(), 'LTargetZ' : LTargetZ(),
                             'LTargetKind' : LTargetKind(), 'LTargetTile' : LTargetTile(), 'LLiftedID' : LLiftedID(),
                             'LLiftedType' : LLiftedType(), 'LLiftedKind' : LLiftedKind(), 'LSkill' : LSkill(),
                             'LSpell' : LSpell()},
            #'Find Item' : {},
            'Extended Info' : {'SysMsg' : SysMsg(), 'CursKind' : CursKind()}, # 'TargCurs' : TargCurs())
            
            'Client Info' : {'CliCnt' : CliCnt(), 'CliNr' : CliNr(), 'CliLogged' : CliLogged(),
                             'CliXRes' : CliXRes(), 'CliYRes' : CliYRes(), 'CliLeft' : CliLeft(),
                             'CliTop' : CliTop(), 'CliVer' : CliVer(), 'CliLang' : CliLang(),
                             'CliTitle' : CliTitle()},
            
            'Combat Info' : {'LHandID' : LHandID(), 'RHandID' : RHandID(), 'EnemyHits' : EnemyHits(),
                             'EnemyID' : EnemyID()},
        
            #'Tile Info' : {},
            #'Time Info' : {},
            'Miscellaneous' : {'Shard' : Shard(), 'LShard' : LShard(), 'CursorX' : CursorX(),
                               'CursorY' : CursorY(), 'Random' : Random()} # 'PixCol' : PixCol())
            }

    def CopyToClipboard(self, inst, value):
        pyperclip.copy(value)
        
    def popTree(self, e):
        for cat, dic in self.Nodes.items():
            self.NodesInst[cat] = {}
            tmp = self.tree_view.add_node(TreeViewLabel(text=cat))
            if dic == {}: continue
            for k,v in dic.items():
                tvl = TreeViewLabel(text='[color=c8c8c8][ref={0}()]{0}()[/ref]: [ref={1}]{1}[/ref][/color]'.format(k, v), markup = True)
                tvl.bind(on_ref_press=self.CopyToClipboard)
                self.NodesInst[cat][k] = tvl
                self.tree_view.add_node(self.NodesInst[cat][k], tmp)

        #self.tree_view.bind(height=self.tree_view.setter('height'))
        Clock.schedule_interval(self.TVCallback, 1.0)
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()
        
class PyziUO(App):
    pass

Factory.register('Root', cls=PyziUO)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)
Factory.register('KivyB', module='ConsoleLabel')
if __name__ == '__main__':
    if Open():
        PyziUO().run()
