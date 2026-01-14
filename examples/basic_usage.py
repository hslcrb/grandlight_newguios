"""
Example: Basic GrandLight Usage

This example demonstrates how to create a simple glassmorphic application
using the GrandLight library.
"""

# Note: This is a conceptual example for documentation purposes.
# The actual implementation will be developed as the library grows.

"""
from grandlight import Window, GlassPanel, GlassButton, GlassLabel
from grandlight.effects import GlassTheme


def main():
    # Create the main window with a gradient background
    window = Window(
        title="GrandLight Demo",
        size=(800, 600),
        background_gradient=["#667eea", "#764ba2"]
    )
    
    # Create a centered glass panel
    panel = GlassPanel(
        size=(400, 300),
        position="center",
        effect=GlassTheme.light()
    )
    
    # Add a title label
    title = GlassLabel(
        text="Welcome to GrandLight",
        font_size=24,
        font_weight="bold",
        color=(50, 50, 50, 255)
    )
    panel.add(title, padding=(20, 20))
    
    # Add a description
    description = GlassLabel(
        text="A modern glassmorphism GUI library for Python",
        font_size=14,
        color=(80, 80, 80, 255)
    )
    panel.add(description, padding=(20, 10))
    
    # Add interactive buttons
    btn_primary = GlassButton(
        text="Get Started",
        effect=GlassTheme.colorful((100, 150, 255)),
        hover_effect=GlassTheme.frosted(),
        on_click=lambda: print("Getting started...")
    )
    panel.add(btn_primary, padding=(20, 20))
    
    btn_secondary = GlassButton(
        text="Learn More",
        effect=GlassTheme.light(),
        on_click=lambda: print("Opening documentation...")
    )
    panel.add(btn_secondary, padding=(20, 10))
    
    # Add the panel to the window
    window.add(panel)
    
    # Run the application
    window.run()


if __name__ == "__main__":
    main()
"""

print("""
╔════════════════════════════════════════════════════════════╗
║                    GrandLight Example                      ║
╚════════════════════════════════════════════════════════════╝

This example is for documentation purposes.
The full implementation is under development.

To get started with GrandLight:

1. Install: pip install grandlight
2. Import: from grandlight import Window, GlassPanel, GlassButton
3. Create beautiful glassmorphic UIs!

Visit https://github.com/rheehose/grandlight for more information.
""")
