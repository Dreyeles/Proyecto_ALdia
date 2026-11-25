import re

html_path = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\diapositivas_analisis_datos_web.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the entire CSS variables block and top-toolbar / components styling
old_style_marker = "/* ==========================================================================\n       THEME VARIABLES - TURQUESA MÉDICO / TECH & CIAN NEÓN\n       ========================================================================== */"

new_styles = """/* ==========================================================================
       THEME VARIABLES - ALDÍA BRAND (OFFICIAL DEFAULT)
       ========================================================================== */
    :root, body.theme-aldia {
      --bg-dark: #fff6e0;          /* Background Cream #FFF6E0 */
      --bg-card: #ffffff;          /* Slide Canvas Pure White */
      --bg-card-hover: #fffdf5;
      --bg-box: #fffdf7;          /* Box Warm White */
      --border-card: #0f3d2e;      /* Forest Slate */
      --border-subtle: #d2ddd8;    /* Subtle border */
      --border-glow: rgba(15, 61, 46, 0.15);
      
      --toolbar-bg: #ffd54a;       /* Header Hero Yellow */
      --toolbar-border: #0f3d2e;
      --toolbar-text: #0f3d2e;
      --btn-bg: #ffffff;
      --btn-text: #0f3d2e;
      --btn-hover-bg: #0f3d2e;
      --btn-hover-text: #ffd54a;
      --btn-active-bg: #c93a22;
      --btn-active-text: #ffffff;

      --cyan-neon: #0f3d2e;        /* Dark Forest Slate */
      --teal-primary: #ffd54a;     /* Hero Yellow */
      --teal-dark: #0a291f;
      --accent-coral: #c93a22;     /* Terracotta Red CTA */
      --accent-amber: #d97706;     /* Amber */
      --accent-blue: #1db46a;      /* Growth Green */

      --text-main: #0f3d2e;        /* Forest Slate */
      --text-muted: #4a5c54;       /* Slate Muted */
      --text-dim: #71857d;

      --table-th-bg: #0f3d2e;
      --table-th-text: #ffd54a;
      --table-td-bg: #ffffff;
      --table-td-border: #e6edea;

      --drawer-bg: rgba(255, 255, 255, 0.98);
      --drawer-border: #0f3d2e;
      --drawer-text: #0f3d2e;

      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --slide-width: 1280px;
      --slide-height: 720px;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-pill: 9999px;

      --shadow-card: 0 14px 35px rgba(15, 61, 46, 0.08);
      --shadow-neon: 0 4px 14px rgba(201, 58, 34, 0.2);
    }

    /* Dark Forest Mode */
    body.theme-aldia-dark {
      --bg-dark: #071f17;
      --bg-card: #0f3225;
      --bg-card-hover: #154232;
      --bg-box: #0a261c;
      --border-card: #1f5e46;
      --border-subtle: #194b38;
      --border-glow: rgba(255, 213, 74, 0.3);
      
      --toolbar-bg: #0a261c;
      --toolbar-border: #1f5e46;
      --toolbar-text: #ffd54a;
      --btn-bg: #154232;
      --btn-text: #ffffff;
      --btn-hover-bg: #ffd54a;
      --btn-hover-text: #071f17;
      --btn-active-bg: #c93a22;
      --btn-active-text: #ffffff;

      --cyan-neon: #ffd54a;
      --teal-primary: #1db46a;
      --teal-dark: #0f766e;
      --accent-coral: #f87171;
      --accent-amber: #ffd54a;
      --accent-blue: #38bdf8;

      --text-main: #f8fafc;
      --text-muted: #cbd5e1;
      --text-dim: #94a3b8;

      --table-th-bg: #071f17;
      --table-th-text: #ffd54a;
      --table-td-bg: #0f3225;
      --table-td-border: #1f5e46;

      --drawer-bg: rgba(7, 31, 23, 0.98);
      --drawer-border: #ffd54a;
      --drawer-text: #f8fafc;
    }

    /* Tech Cyber Mode */
    body.theme-cyber {
      --bg-dark: #030d12;
      --bg-card: #081b24;
      --bg-card-hover: #0c2633;
      --bg-box: rgba(3, 13, 18, 0.65);
      --border-card: #133e4f;
      --border-subtle: #0d2833;
      --border-glow: rgba(45, 212, 191, 0.35);

      --toolbar-bg: rgba(8, 27, 36, 0.95);
      --toolbar-border: #133e4f;
      --toolbar-text: #f8fafc;
      --btn-bg: rgba(19, 62, 79, 0.4);
      --btn-text: #f8fafc;
      --btn-hover-bg: #14b8a6;
      --btn-hover-text: #030d12;
      --btn-active-bg: #2dd4bf;
      --btn-active-text: #030d12;

      --cyan-neon: #2dd4bf;
      --teal-primary: #14b8a6;
      --teal-dark: #0f766e;
      --accent-coral: #f43f5e;
      --accent-amber: #fbbf24;
      --accent-blue: #38bdf8;

      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;

      --table-th-bg: rgba(19, 62, 79, 0.6);
      --table-th-text: #2dd4bf;
      --table-td-bg: rgba(3, 13, 18, 0.4);
      --table-td-border: rgba(19, 62, 79, 0.3);

      --drawer-bg: rgba(4, 18, 25, 0.98);
      --drawer-border: #2dd4bf;
      --drawer-text: #e2e8f0;
    }"""

# Find from old_style_marker down to *, *::before
pattern_var = re.compile(r'/\* ==========================================================================\s+THEME VARIABLES.*?(?=\*,\s*\*::before)', re.DOTALL)
if pattern_var.search(content):
    content = pattern_var.sub(new_styles + "\n\n    ", content, count=1)
    print("Replaced CSS variables.")
else:
    print("Could not find theme variables block!")

# Replace .top-toolbar styles
content = re.sub(
    r'\.top-toolbar\s*\{[^}]*\}',
    """.top-toolbar {
      height: 52px;
      background: var(--toolbar-bg);
      border-bottom: 2px solid var(--toolbar-border);
      color: var(--toolbar-text);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      z-index: 100;
      flex-shrink: 0;
    }""",
    content
)

# Replace .project-badge
content = re.sub(
    r'\.project-badge\s*\{[^}]*\}',
    """.project-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--toolbar-text);
      background: rgba(15, 61, 46, 0.08);
      border: 1px solid var(--toolbar-border);
      padding: 0.25rem 0.75rem;
      border-radius: var(--radius-pill);
      letter-spacing: 0.02em;
    }""",
    content
)

# Replace .btn-tool
content = re.sub(
    r'\.btn-tool\s*\{[^}]*\}',
    """.btn-tool {
      background: var(--btn-bg);
      border: 1px solid var(--toolbar-border);
      color: var(--btn-text);
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }""",
    content
)

content = re.sub(
    r'\.btn-tool:hover\s*\{[^}]*\}',
    """.btn-tool:hover {
      background: var(--btn-hover-bg);
      color: var(--btn-hover-text);
      border-color: var(--toolbar-border);
    }""",
    content
)

content = re.sub(
    r'\.btn-tool\.active\s*\{[^}]*\}',
    """.btn-tool.active {
      background: var(--btn-active-bg);
      color: var(--btn-active-text);
      border-color: var(--btn-active-bg);
      font-weight: 800;
    }""",
    content
)

# Replace .timer-display
content = re.sub(
    r'\.timer-display\s*\{[^}]*\}',
    """.timer-display {
      font-family: var(--font-mono);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--toolbar-text);
      background: rgba(255, 255, 255, 0.6);
      padding: 0.3rem 0.8rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--toolbar-border);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }""",
    content
)

# Replace .content-box
content = re.sub(
    r'\.content-box\s*\{[^}]*\}',
    """.content-box {
      background: var(--bg-box);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.35rem;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: border-color 0.2s, box-shadow 0.2s;
    }""",
    content
)

# Replace .kpi-table th and td
content = re.sub(
    r'\.kpi-table th\s*\{[^}]*\}',
    """.kpi-table th {
      background: var(--table-th-bg);
      color: var(--table-th-text);
      padding: 0.75rem 0.85rem;
      text-align: left;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      border-bottom: 1px solid var(--border-card);
    }""",
    content
)

content = re.sub(
    r'\.kpi-table td\s*\{[^}]*\}',
    """.kpi-table td {
      padding: 0.7rem 0.85rem;
      border-bottom: 1px solid var(--table-td-border);
      color: var(--text-muted);
      background: var(--table-td-bg);
    }""",
    content
)

# Replace speaker drawer
content = re.sub(
    r'\.speaker-drawer\s*\{[^}]*\}',
    """.speaker-drawer {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 250px;
      background: var(--drawer-bg);
      backdrop-filter: blur(16px);
      border-top: 3px solid var(--drawer-border);
      box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.25);
      transform: translateY(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 999;
      display: flex;
      flex-direction: column;
    }""",
    content
)

content = re.sub(
    r'\.drawer-body\s*\{[^}]*\}',
    """.drawer-body {
      flex: 1;
      padding: 1.25rem 1.75rem;
      overflow-y: auto;
      font-size: 0.95rem;
      line-height: 1.6;
      color: var(--drawer-text);
      font-family: var(--font-sans);
    }""",
    content
)

# Replace themes array in JS
content = re.sub(
    r"const themes = \['theme-default', 'theme-cyber', 'theme-light'\];",
    "const themes = ['theme-aldia', 'theme-aldia-dark', 'theme-cyber'];",
    content
)

content = re.sub(
    r"document\.body\.classList\.remove\('theme-cyber', 'theme-light'\);",
    "document.body.classList.remove('theme-aldia', 'theme-aldia-dark', 'theme-cyber');",
    content
)

content = re.sub(
    r"if \(themes\[currentThemeIdx\] !== 'theme-default'\) \{\s*document\.body\.classList\.add\(themes\[currentThemeIdx\]\);\s*\}",
    "document.body.classList.add(themes[currentThemeIdx]);",
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated HTML slides with AlDia brand theme successfully!")

