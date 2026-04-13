import re

with open('f:/DAV UNI PROJECT/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hero 🤖 block
content = re.sub(
    r'<div class="hero-icon">🤖</div>',
    r'<img src="https://davuniversity.org/src2/img/basic/logohead.png?v=1" alt="DAV Logo" class="hero-logo">',
    content
)

# Replace the chat header avatar 🤖 block
content = re.sub(
    r'<div class="chat-avatar">🤖</div>',
    r'<div class="chat-avatar"><img src="https://davuniversity.org/src2/img/basic/logohead.png?v=1" style="width:100%; object-fit:contain;" alt="DAV"></div>',
    content
)

minimal_css = """  <style>
    /* ─── RESET & ROOT (MINIMAL MODERN LIGHT) ───────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --blue-main:    #0B3D91;
      --blue-accent:  #1E5AB6;
      --bg-color:     #FBFCFE;
      --panel-bg:     rgba(255, 255, 255, 0.95);
      --panel-border: rgba(0, 0, 0, 0.06);
      --text-main:    #1E293B;
      --text-muted:   #64748B;
      --transition:   0.25s ease-out;
    }

    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background: var(--bg-color);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* ─── NAV ────────────────────────────────────────────── */
    nav {
      position: sticky; top: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 16px 48px;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--panel-border);
    }
    nav img { height: 38px; }
    .nav-badge {
      display: flex; align-items: center; gap: 8px;
      font-size: 13px; color: var(--text-main); font-weight: 500;
      background: #F1F5F9;
      padding: 6px 14px; border-radius: 8px;
      border: 1px solid var(--panel-border);
    }
    .nav-badge .dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: #10B981;
    }

    /* ─── HERO ───────────────────────────────────────────── */
    .hero {
      position: relative; z-index: 1;
      min-height: 75vh;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center; padding: 60px 20px 40px;
    }
    .hero-logo {
      height: 70px;
      margin-bottom: 32px;
    }
    .hero h1 {
      font-size: clamp(32px, 5vw, 56px);
      font-weight: 700; line-height: 1.15;
      color: var(--blue-main);
      letter-spacing: -0.02em;
      margin-bottom: 16px;
    }
    .hero p { 
      font-size: 18px; color: var(--text-muted); 
      max-width: 560px; line-height: 1.6; 
    }

    /* Hero chips */
    .suggestions {
      display: flex; flex-wrap: wrap; gap: 12px;
      justify-content: center; margin-top: 40px; max-width: 720px;
    }
    .chip {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 10px 20px; border-radius: 8px;
      border: 1px solid var(--panel-border);
      background: #FFFFFF;
      color: var(--text-main); font-size: 14px; font-weight: 500;
      cursor: pointer; transition: var(--transition); white-space: nowrap;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .chip:hover {
      background: var(--blue-main);
      color: #FFFFFF;
      border-color: var(--blue-main);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(11,61,145,0.15);
    }
    .chip i { font-size: 13px; opacity: 0.8; }

    /* ─── MAP ─────────────────────────────────────────────── */
    .map-section { position: relative; z-index: 1; padding: 0 48px 60px; }
    .map-label {
      font-size: 13px; font-weight: 600;
      text-transform: uppercase; letter-spacing: 1px;
      color: var(--text-muted); margin-bottom: 16px;
      display: flex; align-items: center; gap: 8px;
    }
    .map-label i { color: var(--blue-main); }
    .map {
      width: 100%; height: 320px;
      border-radius: 16px;
      border: 1px solid var(--panel-border);
    }

    /* ─── FOOTER ──────────────────────────────────────────── */
    footer {
      text-align: center; padding: 24px;
      font-size: 13px; color: var(--text-muted);
      border-top: 1px solid var(--panel-border);
      background: #FFFFFF;
    }

    /* ─── CHAT BUTTON ─────────────────────────────────────── */
    .chat-btn {
      position: fixed; bottom: 32px; right: 32px; z-index: 1000;
      width: 64px; height: 64px; border-radius: 16px; /* Smooth rounded square */
      background: var(--blue-main); border: none; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      font-size: 24px; color: white;
      box-shadow: 0 4px 20px rgba(11,61,145,0.25);
      transition: var(--transition);
    }
    .chat-btn:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(11,61,145,0.3); }
    .chat-btn .badge {
      position: absolute; top: -6px; right: -6px;
      width: 20px; height: 20px;
      background: #EF4444; border-radius: 50%;
      color: white; font-size: 11px; font-weight: 600;
      display: flex; align-items: center; justify-content: center;
      border: 2px solid var(--bg-color);
    }

    /* ─── CHAT BOX ────────────────────────────────────────── */
    .chat-box {
      position: fixed; bottom: 110px; right: 32px;
      width: 400px; height: 600px; z-index: 999;
      display: none; flex-direction: column;
      border-radius: 20px; overflow: hidden;
      background: var(--panel-bg);
      backdrop-filter: blur(16px);
      border: 1px solid var(--panel-border);
      box-shadow: 0 12px 40px rgba(0,0,0,0.08);
      transform-origin: bottom right;
    }
    .chat-box.open    { display: flex; animation: slideUp 0.3s ease-out both; }
    .chat-box.closing { animation: slideDown 0.25s ease-in both; }
    @keyframes slideUp { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
    @keyframes slideDown { from{opacity:1;transform:translateY(0)} to{opacity:0;transform:translateY(20px)} }

    /* Chat header */
    .chat-header {
      display: flex; align-items: center; gap: 14px;
      padding: 20px; flex-shrink: 0;
      background: #FFFFFF;
      border-bottom: 1px solid var(--panel-border);
    }
    .chat-avatar {
      width: 44px; height: 44px;
      background: #FFFFFF; border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      padding: 4px; border: 1px solid var(--panel-border);
    }
    .chat-header-info { flex: 1; }
    .chat-header-info strong { font-size: 16px; display: block; color: var(--text-main); font-weight: 600; }
    .chat-header-info span  { font-size: 13px; color: var(--text-muted); }
    .chat-close {
      background: transparent; border: none;
      color: var(--text-muted); width: 32px; height: 32px;
      border-radius: 8px; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: var(--transition); font-size: 16px;
    }
    .chat-close:hover { background: #F1F5F9; color: var(--text-main); }

    /* Messages */
    .messages {
      flex: 1; padding: 20px;
      overflow-y: auto; background: transparent;
      display: flex; flex-direction: column; gap: 14px;
    }
    .messages::-webkit-scrollbar { width: 4px; }
    .messages::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 4px; }

    /* Bubbles */
    .msg {
      max-width: 85%; padding: 12px 16px; border-radius: 12px;
      font-size: 14.5px; line-height: 1.6; word-break: break-word;
    }
    .msg.user  { align-self: flex-end; background: var(--blue-main); color: white; border-bottom-right-radius: 4px; }
    .msg.bot   { align-self: flex-start; background: #FFFFFF; border: 1px solid var(--panel-border); color: var(--text-main); border-bottom-left-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.02); }
    .msg.bot .msg-meta {
      display: flex; align-items: center; gap: 6px;
      margin-bottom: 6px; font-size: 12px; color: var(--text-muted); font-weight: 500;
    }
    .msg-link {
      display: inline-flex; align-items: center; gap: 6px;
      margin-top: 10px; font-size: 13px; color: var(--blue-accent); font-weight: 500;
      text-decoration: none; padding: 6px 12px; 
      background: #F1F5F9; border-radius: 6px; transition: var(--transition);
    }
    .msg-link:hover { background: #E2E8F0; }

    /* Typing dots */
    .typing {
      align-self: flex-start;
      background: #FFFFFF; border: 1px solid var(--panel-border);
      padding: 16px; border-radius: 12px; border-bottom-left-radius: 4px;
      display: flex; align-items: center; gap: 6px;
    }
    .typing span {
      width: 6px; height: 6px; background: var(--text-muted);
      border-radius: 50%; opacity: 0.4;
      animation: blink 1.4s infinite both;
    }
    .typing span:nth-child(2) { animation-delay: 0.2s; }
    .typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes blink { 0%,100%{opacity:0.2} 20%{opacity:1} }

    /* Quick chips */
    .quick-chips {
      display: flex; flex-wrap: wrap; gap: 8px;
      padding: 12px 20px; flex-shrink: 0;
      background: transparent;
    }
    .quick-chip {
      padding: 8px 14px; border-radius: 6px;
      border: 1px solid var(--panel-border);
      background: #FFFFFF; box-shadow: 0 1px 2px rgba(0,0,0,0.02);
      color: var(--text-main); font-size: 13px; font-weight: 500;
      cursor: pointer; transition: var(--transition);
    }
    .quick-chip:hover { border-color: var(--blue-main); color: var(--blue-main); }

    /* Input area */
    .input-area {
      display: flex; align-items: flex-end; gap: 10px;
      padding: 16px 20px; flex-shrink: 0;
      background: #FFFFFF;
      border-top: 1px solid var(--panel-border);
    }
    .input-area input {
      flex: 1; background: #F8FAFC;
      border: 1px solid #E2E8F0; border-radius: 8px;
      padding: 12px 16px; color: var(--text-main); font-size: 14.5px;
      outline: none; transition: var(--transition);
      min-height: 44px;
    }
    .input-area input::placeholder { color: #94A3B8; }
    .input-area input:focus { border-color: var(--blue-accent); background: #FFFFFF; }

    .icon-btn {
      width: 44px; height: 44px; border-radius: 8px; border: none;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      font-size: 18px; flex-shrink: 0; transition: var(--transition);
    }
    .send-btn  { background: var(--blue-main); color: white; }
    .send-btn:hover { background: var(--blue-accent); }
    .voice-btn { background: transparent; border: 1px solid #E2E8F0; color: var(--text-muted); }
    .voice-btn:hover { background: #F1F5F9; color: var(--text-main); }
    .voice-btn.recording { background: #FEF2F2; color: #EF4444; border-color: #EF4444; }

    @media(max-width:480px) {
      .chat-box { width: calc(100vw - 32px); right: 16px; bottom: 100px; height: 500px; }
      nav { padding: 16px 20px; }
      .map-section { padding: 0 20px 40px; }
      .chat-btn { right: 16px; bottom: 16px; width: 56px; height: 56px; }
    }
  </style>"""

content = re.sub(r'<style>.*?</style>', minimal_css, content, flags=re.DOTALL)

# Add bot generic logic modifications (removing emoji from code adding message)
content = content.replace('<i class="fas fa-robot"></i> DAV Assistant', '<img src="https://davuniversity.org/src2/img/basic/logohead.png?v=1" style="width:50px; object-fit:contain; margin-right:4px;" alt="DAV"> Assistant')

with open('f:/DAV UNI PROJECT/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
