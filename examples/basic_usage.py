"""
Complete GrandLight Demo Application

This example demonstrates a full-featured glassmorphic application
using all available GrandLight components.
"""

from grandlight import (
    Window,
    GlassPanel,
    GlassButton,
    GlassLabel,
    GlassInput,
    Position,
    Size,
    EventType,
    GlassTheme,
)


def create_demo_app():
    """Create and configure the demo application."""

    # Create the main window with a gradient background
    window = Window(
        title="GrandLight Demo - Glassmorphism UI Library",
        size=Size(900, 700),
        background_gradient=["#667eea", "#764ba2", "#f093fb", "#4facfe"],
        fps=60,
    )

    # Create main panel (centered)
    main_panel = GlassPanel(
        size=Size(600, 500), effect=GlassTheme.light(), padding=30
    )

    # Center the main panel
    window.center_component(main_panel)

    # Add title label
    title = GlassLabel(
        text="Welcome to GrandLight",
        position=Position(0, 0),
        size=Size(540, 60),
        font_size=32,
        font_weight="bold",
        text_color=(50, 50, 70, 255),
        text_align="center",
        background=True,
        effect=GlassTheme.frosted(),
    )
    main_panel.add(title)

    # Add subtitle
    subtitle = GlassLabel(
        text="A Modern Glassmorphism GUI Library for Python",
        position=Position(0, 80),
        size=Size(540, 40),
        font_size=16,
        text_color=(80, 80, 100, 255),
        text_align="center",
        background=False,
    )
    main_panel.add(subtitle)

    # Create input field
    name_input = GlassInput(
        placeholder="Enter your name...",
        position=Position(0, 150),
        size=Size(540, 50),
        effect=GlassTheme.light(),
        focus_effect=GlassTheme.frosted(),
        font_size=16,
    )
    main_panel.add(name_input)

    # Create a row of themed buttons
    button_y = 230

    # Primary button - Blue theme
    btn_primary = GlassButton(
        text="Get Started",
        position=Position(0, button_y),
        size=Size(170, 50),
        effect=GlassTheme.colorful((100, 150, 255)),
        hover_effect=GlassTheme.frosted(),
        font_size=15,
        on_click=lambda e: print("🚀 Getting started with GrandLight!"),
    )
    main_panel.add(btn_primary)

    # Success button - Green theme
    btn_success = GlassButton(
        text="Documentation",
        position=Position(185, button_y),
        size=Size(170, 50),
        effect=GlassTheme.colorful((100, 200, 130)),
        hover_effect=GlassTheme.frosted(),
        font_size=15,
        on_click=lambda e: print("📚 Opening documentation..."),
    )
    main_panel.add(btn_success)

    # Warning button - Orange theme
    btn_warning = GlassButton(
        text="Examples",
        position=Position(370, button_y),
        size=Size(170, 50),
        effect=GlassTheme.colorful((255, 180, 100)),
        hover_effect=GlassTheme.frosted(),
        font_size=15,
        on_click=lambda e: print("💡 Loading examples..."),
    )
    main_panel.add(btn_warning)

    # Create feature showcase panel
    features_panel = GlassPanel(
        position=Position(0, 310),
        size=Size(540, 150),
        effect=GlassTheme.dark(),
        padding=20,
    )
    main_panel.add(features_panel)

    # Feature labels
    features = [
        "✨ Glassmorphism Design",
        "🎨 Multiple Themes",
        "⚡ High Performance",
        "🔧 Easy to Use",
        "🌈 Beautiful Effects",
        "🚀 Modern Python",
    ]

    for i, feature in enumerate(features):
        row = i // 3
        col = i % 3

        feature_label = GlassLabel(
            text=feature,
            position=Position(col * 180, row * 50),
            size=Size(170, 40),
            font_size=13,
            text_color=(255, 255, 255, 230),
            background=False,
        )
        features_panel.add(feature_label)

    # Add footer
    footer = GlassLabel(
        text="Created by Rheehose (Rhee Creative) © 2008-2026",
        position=Position(0, 450),
        size=Size(540, 30),
        font_size=11,
        text_color=(100, 100, 120, 200),
        text_align="center",
        background=False,
    )
    main_panel.add(footer)

    # Add the main panel to window
    window.add(main_panel)

    return window


def main():
    """Main entry point."""
    print("\n" + "=" * 70)
    print("  GrandLight Demo - Glassmorphism GUI Library")
    print("  Created by Rheehose (Rhee Creative)")
    print("=" * 70 + "\n")

    print("🎨 Creating glassmorphic application...")
    print("✨ Initializing components...")
    print("🌈 Applying glass effects...\n")

    # Create the demo application
    app = create_demo_app()

    print("✅ Application ready!")
    print("\nThis is a conceptual demo showcasing GrandLight's component structure.")
    print("In a full implementation, this would open a window with:")
    print("  • Beautiful gradient background")
    print("  • Glassmorphic panels with blur effects")
    print("  • Interactive buttons with hover states")
    print("  • Text input with focus effects")
    print("  • Smooth animations and transitions\n")

    print("📊 Application Stats:")
    print(f"  Window Size: {app.size.width}x{app.size.height}")
    print(f"  Total Components: {len(app.children) + sum(len(c.children) if hasattr(c, 'children') else 0 for c in app.children)}")
    print(f"  Target FPS: {app.fps}")

    print("\n🎯 Component Hierarchy:")
    print("  └── Window")
    for i, child in enumerate(app.children):
        is_last = i == len(app.children) - 1
        prefix = "    └──" if is_last else "    ├──"
        print(f"{prefix} {child.__class__.__name__}")

        if hasattr(child, "children"):
            for j, grandchild in enumerate(child.children):
                is_last_gc = j == len(child.children) - 1
                gc_prefix = "        └──" if is_last_gc else "        ├──"
                print(f"{gc_prefix} {grandchild.__class__.__name__}: {getattr(grandchild, 'text', 'N/A')}")

    print("\n" + "=" * 70)
    print("To run the actual window, call: app.run()")
    print("(Full rendering implementation coming soon!)")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
