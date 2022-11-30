'''
Мои заметки
=============

Приложение для добавления, выполнения и удаления заметок

'''
import kivy
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import ILeftBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from func import add_notes, listNotesFunc, get_date, del_note, changeType_note, dateToday
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock #mainthread

Config.set('graphics','resizable',0)
Window.size = (500, 750)
# cnt=0
# cnt1=0
def create():
    # global cnt
    app = MDApp.get_running_app()
    res_list_widget = app.root.ids.search_res
    res_list_widget.clear_widgets()
    # res_list_widget.add_widget(
    #     MDLabel(
    #         text='Нужно сделать',
    #         halign="center",
    #         # adaptive_height = True,   
    #         font_size= 25,
    #     )
    # )
    for res in listNotesFunc():
        if res[3]==0:
            res_list_widget.add_widget(
                ListItemWithCheckbox(text=f"{res[1]} (создана: {get_date(res[2])})", noteId=res[0], done=res[3])
            )

def create1():
    app = MDApp.get_running_app()
    res_list_widget1 = app.root.ids.search_res1
    for res in listNotesFunc():
        if res[3]==1:
            res_list_widget1.add_widget(
                ListItemWithCheckbox1(text=f"{res[1]} (создана: {get_date(res[2])})", noteId=res[0], done=res[3])
            )

class MainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_list)
    def create_list(self, *args):
        create()
        create1()

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    def __init__(self, noteId, done, **kwargs):
        super(ListItemWithCheckbox, self).__init__(**kwargs)
        self.noteId = noteId
        self.done = done
    def delNote(self, noteId):
        if del_note(noteId):
            self.parent.remove_widget(self)
    def changeType(self, noteId, done):
        if changeType_note(noteId, done):
            self.parent.remove_widget(self)
            app = MDApp.get_running_app()
            res_list_widget = app.root.ids.search_res1
            res_list_widget.add_widget(
                ListItemWithCheckbox1(text=f"{self.text} (создана: {dateToday()})", noteId=noteId, done=done)
            )

class ListItemWithCheckbox1(OneLineAvatarIconListItem):
    def __init__(self, noteId, done, **kwargs):
        super(ListItemWithCheckbox1, self).__init__(**kwargs)
        self.noteId = noteId
        self.done = done
    def delNote(self, noteId):
        if del_note(noteId):
            self.parent.remove_widget(self)
    def changeType(self, noteId, done):
        if changeType_note(noteId, done):
            self.parent.remove_widget(self)
            app = MDApp.get_running_app()
            res_list_widget = app.root.ids.search_res
            res_list_widget.add_widget(
                ListItemWithCheckbox(text=f"{self.text} (создана: {dateToday()})", noteId=noteId, done=done)
            )

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass

class Notes(MDApp):
    def addNote(self, textNote):
        if add_notes(textNote):
            # app = MDApp.get_running_app()
            # res_list_widget = app.root.ids.search_res
            # res_list_widget.add_widget(
            #     ListItemWithCheckbox(text=f"{textNote} (создана: {dateToday()})", noteId=1000, done=0)
            # )
            create()
    def build(self):
        print(kivy.__version__)
        print(kivymd.__version__)
        return MainWindow()

Notes().run()