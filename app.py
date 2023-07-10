from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton, MDFloatingActionButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.textfield import MDTextField

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        add_product_button = MDFillRoundFlatButton(
            text="Add/remove product",
            size_hint=(0.5, None),
            height="48dp",
            md_bg_color=(0.3, 0.3, 0.3, 1),
            on_release=self.add_product_release
        )

        shipping_method_button = MDFillRoundFlatButton(
            text="Shipping Method",
            size_hint=(0.5, None),
            height="48dp",
            md_bg_color=(0.3, 0.3, 0.3, 1),
            on_release=self.shipping_method_release
        )

        calculate_shipping_button = MDFillRoundFlatButton(
            text="Calculate Shipping",
            size_hint=(0.5, None),
            height="55dp",
            md_bg_color=(0.3, 0.3, 0.3, 1),
            on_release=self.calculate_shipping_release
        )
        layout.pos_hint = {
            "center_y": 0.9,
            "center_x": 0.75
        }
        layout.add_widget(add_product_button)
        layout.add_widget(shipping_method_button)
        layout.add_widget(calculate_shipping_button)

        self.add_widget(layout)

    def add_product_release(self, instance):
        # Handle button release event for Add Product

        # Switch to the AddProductScreen
        self.manager.current = "add_product"

    def shipping_method_release(self, instance):
        # Handle button release event for Shipping Method

        # Switch to the ShippingMethodScreen
        self.manager.current = "shipping_method"

    def calculate_shipping_release(self, instance):
        # Handle button release event for Calculate Shipping

        # Switch to the CalculateShippingScreen
        self.manager.current = "calculate_shipping"


class AddProductScreen(Screen):
    def button_release(self, instance):
        # Handle button release event
        print('hello world')
        self.manager.current = "home"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)
        self.product_quentity = MDTextField(
            hint_text="How many Product You want to store",
            helper_text="Please enter numerical value",
            helper_text_mode="on_focus",
            pos_hint={"right": 0.7, "center_y": 0.9},
            mode="fill",
            size_hint_x= None,
            width= 300
        )
        self.product_name = MDTextField(
            hint_text="Name Of The Product",
            helper_text="Please enter text value",
            helper_text_mode="on_focus",
            pos_hint={"right": 0.7, "center_y": 0.78},
            mode="fill",
            size_hint_x= None,
            width= 300
        )
        self.product_length = MDTextField(
            hint_text="Product Length",
            helper_text="Please enter numerical value",
            helper_text_mode="on_focus",
            pos_hint={"right": 0.7, "center_y": 0.66},
            mode="fill",
            size_hint_x= None,
            width= 300
        )
        self.product_weight = MDTextField(
            hint_text="Product Weight",
            helper_text="Please enter numerical value",
            helper_text_mode="on_focus",
            pos_hint={"right": 0.7, "center_y": 0.53},
            mode="fill",
            size_hint_x= None,
            width= 300
        )
        self.add_button = MDFillRoundFlatButton(
            text="Square Button",
            pos_hint={"center_x": 0.5, "center_y": 0.40},
            # size_hint=(0.2, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),  
            # on_release=self.add_data_release
        )


        self.calculate = MDFillRoundFlatButton(
            icon="Delete",
            pos_hint={"right": 0.95, "y": 0.1},
            # on_release=self.on_fab_release
        )


        
        button = MDFloatingActionButton(
            text="Button with Icon",
            icon="home",  # Replace with the desired icon name
            pos_hint={"center_x": 0.9, "center_y": 0.5},
            # size_hint=(0.2, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),
            on_release=self.button_release
        )
        layout.add_widget(self.product_quentity)
        layout.add_widget(self.product_name)
        layout.add_widget(self.product_length)
        layout.add_widget(self.product_weight)
        layout.add_widget(self.add_button)
        layout.add_widget(self.calculate)
        layout.add_widget(button)
        # Add widgets specific to AddProductScreen

        self.add_widget(layout)


class ShippingMethodScreen(Screen):
    def button_release(self, instance):
        # Handle button release event
        print('hello world')
        self.manager.current = "home"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)

        # Add widgets specific to ShippingMethodScreen
        button = MDFloatingActionButton(
            text="Button with Icon",
            icon="home",  # Replace with the desired icon name
            pos_hint={"center_x": 0.9, "center_y": 0.5},
            # size_hint=(0.2, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),
            on_release=self.button_release
        )

        layout.add_widget(button)
        self.add_widget(layout)


class CalculateShippingScreen(Screen):
    def button_release(self, instance):
        # Handle button release event
        print('hello world')
        self.manager.current = "home"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)

        # Add widgets specific to CalculateShippingScreen
        button = MDFloatingActionButton(
            text="Button with Icon",
            icon="home",  # Replace with the desired icon name
            pos_hint={"center_x": 0.9, "center_y": 0.5},
            # size_hint=(0.2, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),
            on_release=self.button_release
        )

        layout.add_widget(button)
        self.add_widget(layout)


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"

        screen_manager = ScreenManager()

        home_screen = HomeScreen(name="home")
        add_product_screen = AddProductScreen(name="add_product")
        shipping_method_screen = ShippingMethodScreen(name="shipping_method")
        calculate_shipping_screen = CalculateShippingScreen(name="calculate_shipping")

        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(add_product_screen)
        screen_manager.add_widget(shipping_method_screen)
        screen_manager.add_widget(calculate_shipping_screen)

        return screen_manager


MyApp().run()
