"""
Advanced GrandLight Example - Login Form

This example demonstrates building a beautiful glassmorphic login form
with validation, theming, and interactive feedback.
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
    GlassEffect,
)


def create_login_form():
    """Create a glassmorphic login form application."""

    # Create window with a purple-blue gradient
    window = Window(
        title="GrandLight Login",
        size=Size(500, 600),
        background_gradient=["#4158D0", "#C850C0", "#FFCC70"],
    )

    # Main login panel
    login_panel = GlassPanel(
        size=Size(400, 450), effect=GlassTheme.light(), padding=40
    )
    window.center_component(login_panel)

    # Logo/Title
    title = GlassLabel(
        text="🔐 Secure Login",
        position=Position(0, 0),
        size=Size(320, 60),
        font_size=28,
        font_weight="bold",
        text_color=(60, 60, 80, 255),
        text_align="center",
        background=True,
        effect=GlassTheme.frosted(),
    )
    login_panel.add(title)

    # Welcome message
    welcome = GlassLabel(
        text="Welcome back! Please login to your account.",
        position=Position(0, 80),
        size=Size(320, 30),
        font_size=13,
        text_color=(100, 100, 120, 255),
        text_align="center",
        background=False,
    )
    login_panel.add(welcome)

    # Username label
    username_label = GlassLabel(
        text="Username",
        position=Position(0, 130),
        size=Size(320, 25),
        font_size=12,
        font_weight="bold",
        text_color=(80, 80, 100, 255),
        background=False,
    )
    login_panel.add(username_label)

    # Username input
    username_input = GlassInput(
        placeholder="Enter your username",
        position=Position(0, 160),
        size=Size(320, 45),
        effect=GlassTheme.light(),
        focus_effect=GlassTheme.colorful((150, 150, 255)),
        font_size=14,
    )
    login_panel.add(username_input)

    # Password label
    password_label = GlassLabel(
        text="Password",
        position=Position(0, 220),
        size=Size(320, 25),
        font_size=12,
        font_weight="bold",
        text_color=(80, 80, 100, 255),
        background=False,
    )
    login_panel.add(password_label)

    # Password input
    password_input = GlassInput(
        placeholder="Enter your password",
        position=Position(0, 250),
        size=Size(320, 45),
        effect=GlassTheme.light(),
        focus_effect=GlassTheme.colorful((150, 150, 255)),
        font_size=14,
    )
    login_panel.add(password_input)

    # Login button
    login_button = GlassButton(
        text="Login",
        position=Position(0, 320),
        size=Size(320, 50),
        effect=GlassTheme.colorful((100, 150, 255)),
        hover_effect=GlassTheme.frosted(),
        font_size=16,
        text_color=(255, 255, 255, 255),
        on_click=lambda e: print("🔓 Logging in..."),
    )
    login_panel.add(login_button)

    # Forgot password link (using label)
    forgot_link = GlassLabel(
        text="Forgot password?",
        position=Position(0, 380),
        size=Size(320, 25),
        font_size=11,
        text_color=(100, 150, 255, 255),
        text_align="center",
        background=False,
    )
    login_panel.add(forgot_link)

    # Register panel
    register_panel = GlassPanel(
        position=Position(50, 520),
        size=Size(400, 60),
        effect=GlassTheme.dark(),
        padding=15,
    )

    register_label = GlassLabel(
        text="Don't have an account?",
        position=Position(0, 0),
        size=Size(200, 30),
        font_size=12,
        text_color=(220, 220, 230, 255),
        background=False,
    )
    register_panel.add(register_label)

    register_button = GlassButton(
        text="Sign Up",
        position=Position(220, 0),
        size=Size(110, 30),
        effect=GlassTheme.colorful((200, 100, 255)),
        font_size=12,
        text_color=(255, 255, 255, 255),
        on_click=lambda e: print("📝 Opening registration..."),
    )
    register_panel.add(register_button)

    window.add(login_panel)
    window.add(register_panel)

    return window


def create_dashboard():
    """Create a glassmorphic dashboard example."""

    window = Window(
        title="GrandLight Dashboard",
        size=Size(1200, 800),
        background_gradient=["#0F2027", "#203A43", "#2C5364"],
    )

    # Header
    header = GlassPanel(
        position=Position(20, 20),
        size=Size(1160, 80),
        effect=GlassTheme.dark(),
        padding=20,
    )

    header_title = GlassLabel(
        text="Dashboard",
        position=Position(0, 0),
        size=Size(400, 40),
        font_size=24,
        font_weight="bold",
        text_color=(255, 255, 255, 255),
        background=False,
    )
    header.add(header_title)

    # Stat cards
    stat_cards = [
        ("📊 Total Users", "12,543", (100, 150, 255)),
        ("💰 Revenue", "$45,231", (100, 200, 130)),
        ("📈 Growth", "+23.5%", (255, 180, 100)),
        ("⭐ Rating", "4.8/5.0", (255, 150, 200)),
    ]

    for i, (title, value, color) in enumerate(stat_cards):
        card = GlassPanel(
            position=Position(20 + i * 295, 120),
            size=Size(280, 140),
            effect=GlassTheme.colorful(color),
            padding=20,
        )

        card_title = GlassLabel(
            text=title,
            position=Position(0, 0),
            size=Size(240, 30),
            font_size=14,
            text_color=(255, 255, 255, 200),
            background=False,
        )
        card.add(card_title)

        card_value = GlassLabel(
            text=value,
            position=Position(0, 50),
            size=Size(240, 60),
            font_size=32,
            font_weight="bold",
            text_color=(255, 255, 255, 255),
            background=False,
        )
        card.add(card_value)

        window.add(card)

    window.add(header)

    return window


def main():
    """Main entry point."""
    print("\n" + "=" * 70)
    print("  GrandLight Advanced Examples")
    print("  Login Form & Dashboard Demos")
    print("=" * 70 + "\n")

    # Create login form
    print("🔐 Creating login form...")
    login_app = create_login_form()
    print(f"   ✅ Login form ready: {login_app.size.width}x{login_app.size.height}")
    print(f"   📦 Components: {sum(1 + len(c.children) if hasattr(c, 'children') else 1 for c in login_app.children)}")

    # Create dashboard
    print("\n📊 Creating dashboard...")
    dashboard_app = create_dashboard()
    print(f"   ✅ Dashboard ready: {dashboard_app.size.width}x{dashboard_app.size.height}")
    print(f"   📦 Components: {sum(1 + len(c.children) if hasattr(c, 'children') else 1 for c in dashboard_app.children)}")

    print("\n" + "=" * 70)
    print("These examples demonstrate:")
    print("  ✨ Form layouts with labels and inputs")
    print("  🎨 Custom color themes for components")
    print("  📱 Responsive component positioning")
    print("  🖱️  Interactive hover and focus states")
    print("  🌈 Beautiful gradient backgrounds")
    print("=" * 70 + "\n")

    print("To run: login_app.run() or dashboard_app.run()")
    print("(Full rendering coming in future releases)\n")


if __name__ == "__main__":
    main()
