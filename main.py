# ight this is whats gonna happen in the file
# take in a string input
# 1. reverse characters
# 2. shift 5-9 from starting to ending letter // spaces dont count or numbers
# 3. repeat every 4 times (goes back to 5)
# 4. then reverse again to have complete

import kivy
import string
from kivy.app import App
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

kivy.require("1.11.1")


class CipherApp(App):
    def build(self):

        # Basic Window Stuff
        Window.size = (500, 750)
        self.icon = "dog.png"
        self.title = "Super Epic Program"
        self.my_font = "ComicSansMSBold.ttf"

        # Keybinds to close, encrypt, decrypt, etc..
        Window.bind(on_keyboard=self.on_keyboard)  # bind our handler
        # Just declaring the bool for later use
        self.is_encrypt = True

        # button colors
        self.green = [0, 1, 0, 1]
        self.blue =  [0, 0, 1, 1]
        self.black = [0, 0, 0, 0]
        self.white = [1, 1, 1, 1]

        # layouts in order
        superBox = BoxLayout(orientation = 'vertical')
        HB = BoxLayout(orientation = 'horizontal', size_hint=(1, 0.3), padding=2)
        VB = BoxLayout(orientation = 'vertical')
        HB2 = BoxLayout(padding=10, spacing=20, orientation = 'horizontal', size_hint=(1, 0.5))
        VB2 = BoxLayout(orientation = 'vertical')
        VB3 = BoxLayout(orientation = 'vertical', size_hint=(1, 0.3))

        # First split the top into 4 horizontaly
        # put empty label at left and right so middle can be for title and input shifts
        # App title
        self.title_label = Label(text="SICK LAD", font_name=self.my_font, font_size=20)

        HB.add_widget(Label())
        HB.add_widget(self.title_label)

        # Create dropdown menu
        # dont need self for the delow screw what everyone says
        dropdown = DropDown()
        # Items in the menu
        shifts = [69420, 12345, 98765, 239234, 34343, 'custom number', 'custom word key']
        for item in shifts:
            btn = Button(text='%r' % item, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # Need self for the button so the other functions can access its text
        self.change_shift_button = Button(text='69420', size_hint=(1, 1), font_name=self.my_font, font_size=20)
        self.change_shift_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.change_shift_button, 'text', x))

        # Add that button
        HB.add_widget(self.change_shift_button)
        HB.add_widget(Label())

        # The input text
        self.input_text = TextInput(hint_text="Enter message here", multiline=True)
        VB.add_widget(self.input_text)

        # Buttons
        self.encrypt_btn = Button(text ="Encrypt",
                    background_color = self.green,
                    font_size = 25,
                    size_hint =(1, 1))

        self.decrypt_btn = Button(text ="Decrypt",
                    background_color = self.blue,
                    font_size = 25,
                    size_hint =(1, 1))

        # HB represents the horizontal boxlayout orientation
        self.encrypt_btn.bind(on_press=self.Crypt)
        HB2.add_widget(self.encrypt_btn)

        # there is probably a more efficient way but im used to using booleans to switch things
        self.decrypt_btn.bind(on_press=self.make_decrypt)
        self.decrypt_btn.bind(on_press=self.Crypt)
        HB2.add_widget(self.decrypt_btn)


        self.output_text = TextInput(hint_text="Output", multiline=True)
        VB2.add_widget(self.output_text)

        VB3.add_widget(Label(text="No joke 100% legit best encryption software on the web (Don't check)"))

        # superbox used to again align the orented widgets
        # this is nesting the layouts in another main layout
        superBox.add_widget(HB) #title
        superBox.add_widget(VB) #input
        superBox.add_widget(HB2) #buttons
        superBox.add_widget(VB2) #output
        superBox.add_widget(VB3) #bottom

        return superBox

    # the only working way that i came up with
    def make_decrypt(self, button):
        self.is_encrypt = False

    # keyboard shortcuts
    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        if modifier == ['ctrl'] and codepoint == 'q':
            self.stop()
        if modifier == ['shift'] and codepoint == ['enter']:
            Encrypt()


    def Crypt(self, button):
        #shifts = (list(self.change_shift_button.text))
        print(self.is_encrypt)

        shifts = list(map(int, self.change_shift_button.text))
        print(shifts)
        output = []
        iteration = 0

        upperCase = False
        alphabet = list(string.ascii_lowercase)

        if self.is_encrypt:
            r_list = list(self.input_text.text[::-1])
        else:
            r_list = list(self.input_text.text)

        symbols = list(string.punctuation)
        numbers = list(string.digits)
        spaces = list(string.whitespace)

        print("---------------------------")
        print("reversed / original:")
        print(r_list)

        for char in r_list:
            if char.isupper():
                upperCase = True

            if not r_list:
                break

            if char in spaces or char in numbers or char in symbols:
                output.append(str(char))

            else:
                letter = alphabet.index(char.lower())

                if self.is_encrypt:
                    letter += shifts[0]
                    if letter > 25:
                        overflow_letter = letter - 25
                        encryption = alphabet[overflow_letter]
                    else:
                        encryption = alphabet[letter]
                else:
                    letter -= shifts[0]
                    if letter < 0:
                        overflow_letter = letter + 25
                        encryption = alphabet[overflow_letter]
                    else:
                        encryption = alphabet[letter]

                if upperCase == True:
                    encryption = encryption.upper()

                output.append(str(encryption))
                iteration += 1
                shifts.pop(0)
                upperCase = False


                if iteration == 4 or not shifts:
                    shifts = [6, 9, 4, 2, 0]
                    iteration = 0

        if self.is_encrypt:
            print("Shifted:")
            print(output)
            print("---------------------------\n")

            self.ciphertext = ''.join(output)
            self.output_text.text = self.ciphertext

        else:
            output = output[::-1]
            print("Plaintext:")
            print(output)
            print("---------------------------\n")

            self.plaintext = ''.join(output)
            self.output_text.text = self.plaintext

        self.is_encrypt = True


if __name__ == '__main__':
    CipherApp().run()
