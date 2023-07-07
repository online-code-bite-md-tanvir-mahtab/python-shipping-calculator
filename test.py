from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from app import *

from kivymd.uix.dialog import MDDialog





class ShippingApp(MDApp):
    
    def add_data_release(self, instance):
        self.products_data = {}
        self.quentiry = int(self.product_quentity.text)
        for _ in range(self.quentiry):
            name = self.product_name.text
            max_length = int(self.product_length.text)
            max_weight = int(self.product_weight.text)
            self.products_data[name] = GroundScrew(length=max_length,weight=max_weight)
        self.calculate.icon = 'equal'
    
    
    def on_fab_release(self, instance):
        # Create instances of the classes
        products = {name: product for name, product in self.products_data.items()}
        shipping_methods = [method for name, method in shipping_methods_data.items()]
        # Create the ShippingCalculator instance
        shipping_calculator = ShippingCalculator(products, shipping_methods)

        # Calculate the shipping costs
        cheapest_method, packages_count, cheapest_cost = shipping_calculator.calculate_shipping_costs()
        cheapest_cost = cheapest_cost * self.quentiry
        text= f'Cheapest Shipping Method: {cheapest_method.name}\n Package Count: {packages_count}\n Total Cost: {cheapest_cost}'
        dialog = MDDialog(
            title="Dialog Box",
            text=text,
            size_hint=(0.8, 0.4),
        )
        dialog.open()

    def build(self):
        self.theme_cls.theme_style = "Light"
        menu_Screen = MDScreen()
        self.add_button = MDFillRoundFlatButton(
            text="Add/remove product",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint=(0.5, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),  
            on_release=self.add_data_release
        )
        
        self.shipping_method = MDFillRoundFlatButton(
            text="Shipping Method",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.5, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),  
            on_release=self.add_data_release
        )
        
        
        self.calculate_shipping = MDFillRoundFlatButton(
            text="Calculate Shipping",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            size_hint=(0.5, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),  
            on_release=self.add_data_release
        )
        # self.product_quentity = MDTextField(
        #     hint_text="How many Product You want to store",
        #     helper_text="Please enter numerical value",
        #     helper_text_mode="on_focus",
        #     pos_hint={"right": 0.7, "center_y": 0.9},
        #     mode="fill",
        #     size_hint_x= None,
        #     width= 300
        # )
        # self.product_name = MDTextField(
        #     hint_text="Name Of The Product",
        #     helper_text="Please enter text value",
        #     helper_text_mode="on_focus",
        #     pos_hint={"right": 0.7, "center_y": 0.78},
        #     mode="fill",
        #     size_hint_x= None,
        #     width= 300
        # )
        # self.product_length = MDTextField(
        #     hint_text="Product Length",
        #     helper_text="Please enter numerical value",
        #     helper_text_mode="on_focus",
        #     pos_hint={"right": 0.7, "center_y": 0.66},
        #     mode="fill",
        #     size_hint_x= None,
        #     width= 300
        # )
        # self.product_weight = MDTextField(
        #     hint_text="Product Weight",
        #     helper_text="Please enter numerical value",
        #     helper_text_mode="on_focus",
        #     pos_hint={"right": 0.7, "center_y": 0.53},
        #     mode="fill",
        #     size_hint_x= None,
        #     width= 300
        # )
        # self.add_button = MDFillRoundFlatButton(
        #     text="Square Button",
        #     pos_hint={"center_x": 0.5, "center_y": 0.40},
        #     size_hint=(0.2, 0.1),
        #     md_bg_color=(0.3, 0.3, 0.3, 1),  
        #     on_release=self.add_data_release
        # )


        # self.calculate = MDFloatingActionButton(
        #     icon="plus",
        #     pos_hint={"right": 0.95, "y": 0.1},
        #     on_release=self.on_fab_release
        # )


        # screen.add_widget(self.product_quentity)
        # screen.add_widget(self.product_name)
        # screen.add_widget(self.product_length)
        # screen.add_widget(self.product_weight)
        menu_Screen.add_widget(self.add_button)
        menu_Screen.add_widget(self.shipping_method)
        menu_Screen.add_widget(self.calculate_shipping)
        # screen.add_widget(self.calculate)
        return menu_Screen




if __name__ == "__main__":
    ShippingApp().run()
