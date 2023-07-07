class GroundScrew:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight


class ShippingMethod:
    def __init__(self, name, max_length, max_weight, fixed_cost=None):
        self.name = name
        self.max_length = max_length
        self.max_weight = max_weight
        self.fixed_cost = fixed_cost


class TGVLogisticsMethod(ShippingMethod):
    def __init__(self, name, variable_costs_by_distance):
        super().__init__(name, None, None)
        self.variable_costs_by_distance = variable_costs_by_distance


class ShippingCalculator:
    def __init__(self, products, shipping_methods):
        self.products = products
        self.shipping_methods = shipping_methods

    def calculate_shipping_costs(self):
        cheapest_method = None
        cheapest_cost = float('inf')
        packages_count = {method.name: 0 for method in self.shipping_methods}
        
        for method in self.shipping_methods:
            total_cost = 5
            for product in self.products.values():
                if self.is_product_within_limits(product, method):
                    if method.fixed_cost is not None:
                        total_cost += method.fixed_cost
                    elif isinstance(method, TGVLogisticsMethod):
                        distance = self.calculate_distance()  # Implement distance calculation logic
                        cost_per_km = self.get_variable_cost_by_distance(method, distance)
                        total_cost += cost_per_km * distance
                    packages_count[method.name] += 1

            if total_cost < cheapest_cost:
                cheapest_cost = total_cost
                cheapest_method = method

        return cheapest_method, packages_count, cheapest_cost
    


    def is_product_within_limits(self, product, method):
        if method.max_length and product.length > method.max_length:
            return False
        if method.max_weight and product.weight > method.max_weight:
            return False
        return True

    def get_variable_cost_by_distance(self, method, distance):
        for dist, cost in method.variable_costs_by_distance.items():
            if distance <= dist:
                return cost
        return cost

    def calculate_distance(self):
        customer_postcode = '900'
        your_postcode = "0"  # Replace with your address postcode

        # Assume postcodes are numeric and have the same length
        distance = abs(int(customer_postcode) - int(your_postcode))
        return distance






shipping_methods_data = {
    "PostNL Regular Package": ShippingMethod("PostNL Regular Package", 100, 23, fixed_cost=10.0),
    "PostNL Large Package": ShippingMethod("PostNL Large Package", 175, 30, fixed_cost=15.0),
    "TGV Logistics": TGVLogisticsMethod("TGV Logistics", 
                                        variable_costs_by_distance={
                                            50: 12.0,
                                            100: 18.0,
                                            150: 24.0
                                        }
                                    ),
}

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
        screen = MDScreen()
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
            text="Add To Data",
            pos_hint={"center_x": 0.5, "center_y": 0.40},
            size_hint=(0.2, 0.1),
            md_bg_color=(0.3, 0.3, 0.3, 1),  
            on_release=self.add_data_release
        )


        self.calculate = MDFloatingActionButton(
            icon="plus",
            pos_hint={"right": 0.95, "y": 0.1},
            on_release=self.on_fab_release
        )


        screen.add_widget(self.product_quentity)
        screen.add_widget(self.product_name)
        screen.add_widget(self.product_length)
        screen.add_widget(self.product_weight)
        screen.add_widget(self.add_button)
        screen.add_widget(self.calculate)
        return screen




if __name__ == "__main__":
    ShippingApp().run()
