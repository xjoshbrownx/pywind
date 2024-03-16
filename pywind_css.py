import os
from bs4 import BeautifulSoup

class PywindCSS:
    def __init__(self):
        self.styles = {
            "text": {
                "sm": "font-size: 0.875rem;",
                "base": "font-size: 1rem;",
                "lg": "font-size: 1.125rem;",
            },
            "bg": {
                "white": "background-color: #fff;",
                "black": "background-color: #000;",
                "gray-100": "background-color: #f7fafc;",
                "gray-200": "background-color: #edf2f7;",
                # Add more colors as needed
            },
            # Add more style categories and their properties
        }

    def generate_css_class(self, prefix, category, value):
        return f".{prefix}-{category}-{value} {{ {self.styles[category][value]} }}"

    def generate_css(self, prefix):
        css = ""
        for category, values in self.styles.items():
            for value in values:
                css += self.generate_css_class(prefix, category, value) + "\n"
        return css

    def replace_tailwind_classes(self, html_file_path, output_path, prefix):
        with open(html_file_path, "r") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        for element in soup.find_all(class_=lambda x: x and x.startswith(f"{prefix}-")):
            classes = element["class"]
            for css_class in classes:
                if css_class.startswith(f"{prefix}-"):
                    category, value = css_class.split("-")[1], css_class.split("-")[2]
                    if category in self.styles and value in self.styles[category]:
                        element["style"] = f"{element.get('style', '')} {self.styles[category][value]}"
                    else:
                        print(f"Warning: Class {css_class} not found in styles.")
        
        with open(output_path, "w") as output_file:
            output_file.write(soup.prettify())

# Example usage:
if __name__ == "__main__":
    pywind = PywindCSS()
    prefix = "pywind"
    css = pywind.generate_css(prefix)
    print(css)

    # Replace Tailwind classes in HTML files
    input_dir = "input_html_files"
    output_dir = "output_html_files"
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith(".html"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)
            pywind.replace_tailwind_classes(input_file_path, output_file_path, prefix)