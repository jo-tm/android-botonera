from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles

from kivy.core.audio import SoundLoader

# Docs
# https://towardsdatascience.com/building-android-apps-with-python-part-1-603820bebde8
# https://kivy.org/doc/stable/api-kivy.core.audio.html
# APK package https://kivy.org/doc/stable/guide/packaging-android.html
# https://kivymd.readthedocs.io/en/0.104.2/components/button/index.html
# https://www.geeksforgeeks.org/python-working-with-buttons-in-kivy/

# BUILD APK https://github.com/kivy/buildozer
# https://kivy.org/doc/stable/guide/packaging-android.html


class Main(MDApp):
    def build(self):
        screen = MDScreen()
        # https://kivymd.readthedocs.io/en/1.1.1/components/label/
        
        y = 0.95
        label1 = MDLabel(text="Botonera Doctrinaria de Guillermo Moreno v1.0",
                         halign="center",
                         #valign="top",
                         pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[3])
        screen.add_widget(label1)

        ############################
        ### DOCTRINA
        ############################

        ### LABEL
        y -= 0.05
        label2 = MDLabel(text="Doctrina",
                        halign="center",
                        valign="top",
                        pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[4])
        screen.add_widget(label2)

        ### BUTTONS
        y -= 0.05
        x = 0.2
        # Boton1
        btn = MDRectangleFlatButton(text="Solidaridad",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn.bind(on_release = self.callback6)
        screen.add_widget(btn) 
        # Boton2
        x += 0.15
        btn2 = MDRectangleFlatButton(text="Doctrina2",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn2.bind(on_release = self.callback2)
        screen.add_widget(btn2) 

        ############################
        ### CANCIONERO
        ############################

        ### LABEL
        y -= 0.05
        label2 = MDLabel(text="Cancionero",
                        halign="center",
                        valign="top",
                        pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[4])
        screen.add_widget(label2)

        ### BUTTONS
        y -= 0.05
        x = 0.2
        # Boton5
        btn5 = MDRectangleFlatButton(text="Traigan...",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn5.bind(on_release = self.callback8)
        screen.add_widget(btn5) 
        # Boton2
        x += 0.15
        btn2 = MDRectangleFlatButton(text="Compañero",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn2.bind(on_release = self.callback7)
        screen.add_widget(btn2) 


        ############################
        ### POLITICA
        ############################

        ### LABEL
        y -= 0.05
        label2 = MDLabel(text="Politica",
                        halign="center",
                        valign="top",
                        pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[4])
        screen.add_widget(label2)

        ### BUTTONS
        y -= 0.05
        x = 0.2
        # Boton1
        btn = MDRectangleFlatButton(text="Radical!",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn.bind(on_release = self.callback4)
        screen.add_widget(btn) 
        # Boton2
        x += 0.15
        btn2 = MDRectangleFlatButton(text="Politica2",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn2.bind(on_release = self.callback2)
        screen.add_widget(btn2) 


        ############################
        ### EPICA
        ############################

        ### LABEL
        y -= 0.05
        label2 = MDLabel(text="Epica",
                        halign="center",
                        valign="top",
                        pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[4])
        screen.add_widget(label2)

        ### BUTTONS
        y -= 0.05
        x = 0.2
        # Boton5
        btn5 = MDRectangleFlatButton(text="Futuro",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn5.bind(on_release = self.callback5)
        screen.add_widget(btn5) 
        # Boton2
        x += 0.15
        btn2 = MDRectangleFlatButton(text="Felices",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn2.bind(on_release = self.callback2)
        screen.add_widget(btn2) 

        ############################
        ### FOLKLORE
        ############################

        ### LABEL
        y -= 0.05
        label2 = MDLabel(text="Folklore",
                        halign="center",
                        valign="top",
                        pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[4])
        screen.add_widget(label2)

        ### BUTTONS
        y -= 0.05
        x = 0.2
        # Boton1
        btn = MDRectangleFlatButton(text="Tomatela",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn.bind(on_release = self.callback9)
        screen.add_widget(btn) 
        # Boton2
        x += 0.15
        btn2 = MDRectangleFlatButton(text="Pavadas",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn2.bind(on_release = self.callback10)
        screen.add_widget(btn2) 
    
        ############################
        ### ONOMATOPEYAS
        ############################

        ### LABEL
        y -= 0.05
        label2 = MDLabel(text="Onomatopeyas",
                        halign="center",
                        valign="top",
                        pos_hint={'center_x': 0.5, 'center_y': y},
                         font_style=theme_font_styles[4])
        screen.add_widget(label2)

        ### BUTTONS
        y -= 0.05
        x = 0.2
        # Boton1
        btn = MDRectangleFlatButton(text="Ono1",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn.bind(on_release = self.callback1)
        screen.add_widget(btn) 
        # Boton2
        x += 0.15
        btn2 = MDRectangleFlatButton(text="Ono2",
                                    pos_hint={'center_x': x, 'center_y': y}
                                    )
        btn2.bind(on_release = self.callback2)
        screen.add_widget(btn2) 



        ### END of BUILD()
        return screen
        ##  END of BUILD()
    

    # callback function tells when button pressed
    def callback1(self, event):
        sound = SoundLoader.load('audios/doctrina/futuro.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback2(self, event):
        sound = SoundLoader.load('audios/epica/dias.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback4(self, event):
        sound = SoundLoader.load('audios/politica/radical2.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback5(self, event):
        sound = SoundLoader.load('audios/epica/futuro.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback6(self, event):
        sound = SoundLoader.load('audios/doctrina/solidaridad.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback7(self, event):
        sound = SoundLoader.load('audios/cancionero/companero.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback8(self, event):
        sound = SoundLoader.load('audios/cancionero/traigan2.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback9(self, event):
        sound = SoundLoader.load('audios/folklore/tomatela.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    # callback function tells when button pressed
    def callback10(self, event):
        sound = SoundLoader.load('audios/folklore/pavadas.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()



Main().run()