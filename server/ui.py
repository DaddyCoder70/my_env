def get_terminal_html():
    """Returns a state-of-the-art, high-end institutional whitepaper for Team unSuppotrtive."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ai trader | Institutional Whitepaper</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #030303;
            --paper: #080808;
            --accent-pink: #ff007f;
            --accent-crimson: #bc0000;
            --accent-gold: #c5a059;
            --text: #ffffff;
            --text-dim: #777777;
            --border: rgba(255, 255, 255, 0.05);
            --glass: blur(30px) saturate(200%);
            --grid: rgba(255, 255, 255, 0.02);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            background: var(--bg); color: var(--text); line-height: 1.6; overflow-x: hidden; 
            font-family: 'Inter', sans-serif;
            background-attachment: fixed;
        }

        /* Large Grid & Grain Base */
        body::before {
            content: ''; position: fixed; inset: 0;
            background-image: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
            background-size: 80px 80px; pointer-events: none; z-index: 0;
        }
        body::after {
            content: ''; position: fixed; inset: 0;
            background: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
            opacity: 0.04; pointer-events: none; z-index: 1000;
        }

        #progress-bar { position: fixed; top: 0; left: 0; width: 0%; height: 2px; background: var(--accent-pink); z-index: 3000; }

        header {
            height: 100px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between;
            padding: 0 5%; background: rgba(3, 3, 3, 0.85); backdrop-filter: var(--glass); position: sticky; top: 0; z-index: 2000;
        }

        .logo { font-family: 'DM Serif Display', serif; font-size: 2.2rem; display: flex; align-items: baseline; letter-spacing: -2px; }
        .logo span { color: var(--accent-pink); font-size: 1rem; font-family: 'JetBrains Mono'; margin-left: 12px; font-weight: 500; opacity: 0.6; }
        .status-tag { font-family: 'JetBrains Mono'; font-size: 0.6rem; color: var(--accent-gold); border: 1px solid var(--accent-gold); padding: 4px 10px; border-radius: 2px; margin-left: 20px; text-transform: uppercase; letter-spacing: 2px; }

        .nav-links a { font-family: 'JetBrains Mono'; font-size: 0.7rem; text-transform: uppercase; color: var(--text); text-decoration: none; margin-left: 40px; letter-spacing: 2px; opacity: 0.5; transition: 0.4s; }
        .nav-links a:hover { opacity: 1; color: var(--accent-pink); text-shadow: 0 0 10px var(--accent-pink); }

        /* Simplified Hero - Formal Doc Style */
        .hero { 
            position: relative; min-height: 40vh; display: flex; align-items: center; padding: 100px 8% 50px;
            border-bottom: 1px solid var(--border); background: var(--paper);
        }
        
        .hero-content { max-width: 900px; position: relative; z-index: 1; }
        .hero-label { font-family: 'JetBrains Mono'; color: var(--accent-crimson); font-size: 0.7rem; letter-spacing: 12px; margin-bottom: 25px; display: block; opacity: 0.8; }
        .hero h1 { font-family: 'DM Serif Display', serif; font-size: 4.5rem; line-height: 1.1; margin-bottom: 30px; letter-spacing: -2px; color: #fff; }
        .hero h1 span { color: var(--accent-pink); font-style: normal; }
        .hero p { font-size: 1.2rem; color: var(--text-dim); font-weight: 300; max-width: 700px; line-height: 1.6; }

        /* New Asymmetrical Content Grid */
        .doc-body { width: 100%; display: grid; grid-template-columns: 350px 1fr; gap: 120px; padding: 150px 8%; align-items: start; max-width: 1600px; margin: 0 auto; }
        
        .sidebar { position: sticky; top: 150px; }
        .sidebar h2 { font-family: 'DM Serif Display', serif; font-size: 3.5rem; margin-bottom: 25px; line-height: 1.1; }
        .sidebar p { color: var(--text-dim); font-size: 1rem; margin-bottom: 60px; }
        
        .blueprint-info { font-family: 'JetBrains Mono'; font-size: 0.6rem; color: var(--text-dim); line-height: 2; border-top: 1px solid var(--border); padding-top: 30px; }
        .blueprint-info b { color: var(--accent-gold); }

        /* Content Sections */
        section { margin-bottom: 150px; scroll-margin-top: 150px; }
        section h3 { font-family: 'JetBrains Mono'; font-size: 0.6rem; color: var(--accent-pink); letter-spacing: 6px; text-transform: uppercase; margin-bottom: 45px; display: flex; align-items: center; }
        section h3::after { content: ''; flex: 1; height: 1px; background: var(--border); margin-left: 30px; }
        
        .editorial-text { font-size: 1.3rem; font-weight: 300; margin-bottom: 50px; line-height: 1.6; color: rgba(255,255,255,0.85); }
        .editorial-text b { color: #fff; font-weight: 600; font-family: 'DM Serif Display', serif; font-size: 1.6rem; }

        .spec-container { display: grid; grid-template-columns: 1fr; gap: 40px; }
        .spec-box { background: var(--paper); border: 1px solid var(--border); padding: 50px; position: relative; transition: 0.5s; overflow: hidden; }
        .spec-box:hover { border-color: var(--accent-pink); background: rgba(255, 255, 255, 0.01); }
        .spec-box::before { content: ''; position: absolute; top: -100px; right: -100px; width: 200px; height: 200px; background: radial-gradient(circle, var(--accent-pink) 0%, transparent 70%); opacity: 0; transition: 0.5s; }
        .spec-box:hover::before { opacity: 0.05; }
        
        .spec-box h4 { font-family: 'DM Serif Display', serif; font-size: 2.2rem; margin-bottom: 20px; color: var(--text); }
        .spec-box p { color: var(--text-dim); font-size: 1rem; }

        /* Leaderboard */
        .board-wrap { border: 1px solid var(--border); background: var(--paper); position: relative; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 30px; font-family: 'JetBrains Mono'; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 3px; border-bottom: 1px solid var(--border); color: var(--text-dim); }
        td { padding: 35px 30px; border-bottom: 1px solid var(--border); font-size: 1.1rem; vertical-align: middle; }
        .rank-icon { width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
        tr:hover td { background: rgba(255,255,255,0.01); }

        /* Code Block Enhancement */
        .technical-block { background: #000; border: 1px solid var(--accent-crimson); padding: 60px; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; position: relative; border-radius: 2px; }
        .block-label { position: absolute; top: -11px; left: 40px; background: #000; padding: 0 20px; font-size: 0.6rem; color: var(--accent-crimson); letter-spacing: 5px; font-weight: 700; }
        .pk { color: var(--accent-pink); } .cc { color: #353535; font-style: italic; } .fn { color: var(--accent-gold); }

        footer { border-top: 1px solid var(--border); padding: 120px 8%; display: flex; justify-content: space-between; align-items: baseline; font-family: 'JetBrains Mono'; font-size: 0.7rem; color: var(--text-dim); }
        .footer-logo { font-family: 'DM Serif Display'; font-size: 2rem; color: var(--text); }

        @media (max-width: 1200px) {
            .doc-body { grid-template-columns: 1fr; }
            .hero h1 { font-size: 7rem; }
        }
    </style>
</head>
<body>
    <div id="progress-bar"></div>

    <header>
        <div class="logo">Ai trader <span>FINAL</span> <div class="team-meta">UNSUPOTRTIVE_CORE</div></div>
        <div class="nav-links">
            <a href="https://github.com/DaddyCoder70/my_env" target="_blank">GITHUB</a>
            <a href="#how">PROTOCOL</a>
            <a href="#bench">BENCHMARKS</a>
        </div>
    </header>

    <div class="hero">
        <div class="hero-content">
            <span class="hero-label">ENVIRONMENT_AUTH_SUCCESSFUL</span>
            <h1>Ai trader <span>by Team unSuppotrtive</span></h1>
            <p>Institutional-grade evaluation environment for benchmarking LLM agents against real-world market dynamics with deterministic guardrails.</p>
        </div>
    </div>

    <div class="doc-body">
        <div class="sidebar">
            <h2>The Strategic Core</h2>
            <p>Documentation of our high-conviction decision architecture.</p>
            <div class="blueprint-info">
                // SYSTEM: <b>AITRADE_KERNEL</b><br>
                // TARGET: <b>MAX_TREND_CAPTURE</b><br>
                // NOISE_CLAMP: <b>ENABLED (0.2%)</b><br>
                // PERSISTENCE_LOCK: <b>ACTIVE</b>
            </div>
        </div>

        <div class="main-content">
            <section id="how">
                <h3>01 // Global Connectivity</h3>
                <div class="editorial-text">
                    Ai trader utilizes a <b>Tactical Gateway</b> for LLM agents. Every decision vector is validated against institutional trend schemas to ensure absolute market discipline.
                </div>
                
                <div class="technical-block" style="margin-bottom: 40px;">
                    <div class="block-label">QUICK_START_SDK.PY</div>
                    <div class="cc"># Connect from Python using Official SDK</div>
                    <div><span class="pk">from</span> aitrade <span class="pk">import</span> AiTradeAction, AiTradeEnv</div>
                    <br>
                    <div><span class="pk">with</span> <span class="fn">AiTradeEnv.from_env</span>(<span class="pk">"harsh063423/my_env"</span>) <span class="pk">as</span> env:</div>
                    <div style="padding-left: 20px;">result = <span class="pk">await</span> env.<span class="fn">step</span>(<span class="tk">AiTradeAction</span>(message=<span class="pk">"..."</span>))</div>
                    <br>
                    <div class="cc"># Or connect to a verified local server</div>
                    <div>env = <span class="fn">AiTradeEnv</span>(base_url=<span class="pk">"http://localhost:8000"</span>)</div>
                </div>

                <div class="technical-block" style="margin-bottom: 60px;">
                    <div class="block-label">CONTRIBUTE_TERMINAL.SH</div>
                    <div class="cc"># Submit improvements via HF Hub</div>
                    <div>openenv fork <span class="tk">harsh063423/my_env</span> --repo-id <span class="cc">&lt;your-username&gt;/&lt;your-repo-name&gt;</span></div>
                    <br>
                    <div class="cc"># Commit and PUSH</div>
                    <div><span class="pk">cd</span> &lt;forked-repo&gt;</div>
                    <div>openenv push <span class="tk">harsh063423/my_env</span> --create-pr</div>
                </div>

                <div class="spec-container">
                    <div class="spec-box">
                        <h4>Direct Uplink</h4>
                        <p>Establish high-fidelity connections via the <code>AiTradeEnv</code> SDK. Each session is uniquely cryptographed for institutional security.</p>
                    </div>
                </div>
            </section>

            <section id="bench">
                <h3>02 // Performance Index</h3>
                <div class="board-wrap">
                    <table>
                        <thead>
                            <tr>
                                <th>POS</th>
                                <th>MODEL ARCHITECTURE</th>
                                <th>PROVIDER</th>
                                <th>LEVEL</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><div class="rank-icon">🥇</div></td>
                                <td><b>GPT-OSS 120B</b></td>
                                <td style="opacity: 0.6; font-family: 'JetBrains Mono'; font-size: 0.7rem;">OSS_PRO</td>
                                <td style="color: var(--accent-pink); font-family: 'JetBrains Mono';">S_TIER (0.94)</td>
                            </tr>
                            <tr>
                                <td><div class="rank-icon">🥈</div></td>
                                <td>GROQ COMPOUND MINI</td>
                                <td style="opacity: 0.6; font-family: 'JetBrains Mono'; font-size: 0.7rem;">GROQ_CORP</td>
                                <td style="color: var(--accent-crimson); font-family: 'JetBrains Mono';">A_TIER (0.88)</td>
                            </tr>
                            <tr>
                                <td><div class="rank-icon">🥉</div></td>
                                <td>MOONSHOT KIMI K2</td>
                                <td style="opacity: 0.6; font-family: 'JetBrains Mono'; font-size: 0.7rem;">MOON_AI</td>
                                <td style="opacity: 0.5; font-family: 'JetBrains Mono';">B_TIER (0.82)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <section id="arch">
                <h3>03 // Kernel Architecture</h3>
                <div class="editorial-text">
                    Our <b>Persistence Engine</b> is the mechanical core of the suite. It explicitly prevents directional "flickering" unless the trend reaches a multi-sigma exhaustion point.
                </div>
                <div class="technical-block">
                    <div class="block-label">KERNEL_CORE_GUARD.PY</div>
                    <div class="cc"># Institutional Signal Guard</div>
                    <div><span class="pk">def</span> <span class="fn">apply_guardrail</span>(order, state):</div>
                    <div style="padding-left: 20px;"><span class="pk">if</span> state.in_buffer: <span class="pk">return</span> <span class="pk">"HOLD"</span></div>
                    <div style="padding-left: 20px;"><span class="pk">if</span> order != state.last_order:</div>
                    <div style="padding-left: 40px;"><span class="pk">if not</span> state.is_reversal:</div>
                    <div style="padding-left: 60px;"><span class="pk">return</span> state.last_order</div>
                    <div style="padding-left: 20px;"><span class="pk">return</span> order</div>
                </div>
            </section>
        </div>
    </div>

    <footer>
        <div class="footer-logo">Ai trader.</div>
        <div style="text-align: right;">
            TEAM UNSUPOTRTIVE // 2026<br>
            <span style="opacity: 0.4;">UPLINK SECURE / ENCRYPTION ACTIVE</span>
        </div>
    </footer>

    <script>
        window.onscroll = function() {
            let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            let scrolled = (winScroll / height) * 100;
            document.getElementById("progress-bar").style.width = scrolled + "%";
        };
    </script>
</body>
</html>
"""
