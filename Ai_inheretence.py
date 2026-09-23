# =====================================================================
# Assignment: OOP Inheritance & Method Overriding
# File: ai_model_inheritance.py
# =====================================================================

# --- Parent Class ---
class BaseAIModel:
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version

    def get_info(self):
        return f"Model: {self.model_name}, Version: {self.version}"


# --- Child Class 1 ---
class TextModel(BaseAIModel):
    def generate_text(self, prompt):
        return f"Generated text from {self.model_name}: '{prompt}'"

    # Overriding get_info
    def get_info(self):
        return f"[TextModel] {self.model_name} v{self.version}"


# --- Child Class 2 ---
class ImageModel(BaseAIModel):
    def generate_image(self, description):
        return f"Generated image from {self.model_name}: '{description}'"

    # Overriding get_info
    def get_info(self):
        return f"[ImageModel] {self.model_name} v{self.version}"


# --- Program Execution & Demonstration ---
if __name__ == "__main__":
    # Parent object
    parent_model = BaseAIModel("GenericModel", "1.0")
    print(parent_model.get_info())

    # Child object 1
    text_model = TextModel("GPT", "4.0")
    print(text_model.get_info())
    print(text_model.generate_text("Hello world!"))

    # Child object 2
    image_model = ImageModel("DALL-E", "3.0")
    print(image_model.get_info())
    print(image_model.generate_image("A cat sitting on a sofa"))
