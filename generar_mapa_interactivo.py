import csv
import json
import os
import re

svg_dir = "/Users/alejo/Proyectos/MapaMental/diagramas_casos_uso_svg"
output_html = "/Users/alejo/Proyectos/MapaMental/mapa_interactivo.html"

# Grouping Subprocesses by Macro-Process
macro_processes = {
    "Configuración y Seguridad": [
        "ROLES", "PERMISOS", "USUARIOS", "ACCESO"
    ],
    "Compras e Inventario": [
        "CATEGORIA DE INSUMOS", "INSUMOS", "PROVEEDORES", "COMPRAS"
    ],
    "Producción y Recetas": [
        "EMPLEADOS", "CATEGORIA PRODUCTOS", "PRODUCTOS", 
        "FICHA TECNICA \"PRODUCTO\"", "PRODUCTO TERMINADO", "PRODUCCION"
    ],
    "Servicios y Operación": [
        "CATEGORIA DE SERVICIOS", "SERVICIO", "CALENDARIO"
    ],
    "Clientes y Ventas": [
        "CLIENTES", "SUSCRIPCIONES"
    ],
    "Logística y Domicilios": [
        "RUTA Y DOMICILIARIOS", "MONITOREO DE ENTREGA \"TIEMPO REAL\"", "INCIDENCIAS"
    ],
    "Analítica y Métricas": [
        "DASHBOARD"
    ]
}

# Read SVG contents for all 23 subprocesses
svg_map = {}

for macro, sub_list in macro_processes.items():
    for sub in sub_list:
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', sub) + ".svg"
        path = os.path.join(svg_dir, safe_name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                svg_map[sub] = f.read()
        else:
            print(f"Warning: SVG not found for {sub} at {path}")

# Build interactive HTML Dashboard
html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mapa Interactivo de Procesos y Casos de Uso</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #0f172a;
      --card-bg: rgba(30, 41, 59, 0.7);
      --border-color: rgba(255, 255, 255, 0.1);
      --accent-blue: #38bdf8;
      --accent-purple: #a855f7;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }}

    body {{
      background: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    header {{
      background: rgba(15, 23, 42, 0.8);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      padding: 18px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
    }}

    header h1 {{
      font-size: 20px;
      font-weight: 700;
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .subtitle {{
      font-size: 13px;
      color: var(--text-muted);
    }}

    .container {{
      display: flex;
      flex: 1;
      height: calc(100vh - 70px);
    }}

    /* Sidebar / Navigation */
    .sidebar {{
      width: 340px;
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      border-right: 1px solid var(--border-color);
      padding: 20px;
      overflow-y: auto;
    }}

    .macro-group {{
      margin-bottom: 20px;
    }}

    .macro-title {{
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-blue);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .sub-item {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 14px;
      margin-bottom: 6px;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sub-item:hover, .sub-item.active {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--accent-blue);
      color: var(--text-main);
      transform: translateX(4px);
    }}

    .sub-item .count {{
      font-size: 11px;
      background: rgba(255, 255, 255, 0.1);
      padding: 2px 6px;
      border-radius: 10px;
    }}

    /* Main View Canvas */
    .main-canvas {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      position: relative;
      background: radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.05) 0%, transparent 60%);
    }}

    .viewer-card {{
      background: #ffffff;
      border-radius: 12px;
      width: 100%;
      height: 100%;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .viewer-header {{
      background: #f1f5f9;
      padding: 12px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #e2e8f0;
      color: #0f172a;
    }}

    .viewer-header h2 {{
      font-size: 16px;
      font-weight: 600;
    }}

    .viewer-body {{
      flex: 1;
      overflow: auto;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
      background: #ffffff;
    }}

    .placeholder-state {{
      text-align: center;
      color: var(--text-muted);
    }}

    .placeholder-state svg {{
      width: 64px;
      height: 64px;
      margin-bottom: 16px;
      opacity: 0.5;
    }}

    /* Interactive Macro Map SVG View */
    .macro-map-container {{
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    /* Zoom Controls */
    .controls {{
      display: flex;
      gap: 8px;
    }}

    .btn {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      color: #334155;
      transition: background 0.2s;
    }}

    .btn:hover {{
      background: #f8fafc;
    }}
  </style>
</head>
<body>

  <header>
    <div>
      <h1>Mapa Interactivo de Procesos y Casos de Uso</h1>
      <div class="subtitle">Sistema Operativo de Gestión Alimentaria</div>
    </div>
    <div class="controls">
      <button class="btn" onclick="showMacroMap()">Ver Mapa General de Procesos</button>
    </div>
  </header>

  <div class="container">
    <!-- Sidebar Navigation -->
    <div class="sidebar">
'''

for macro, sub_list in macro_processes.items():
    html_content += f'''
      <div class="macro-group">
        <div class="macro-title">
          <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
          {macro}
        </div>
'''
    for sub in sub_list:
        clean_sub = sub.replace('"', '')
        html_content += f'''
        <div class="sub-item" onclick="openDiagram('{clean_sub}')" id="btn-{clean_sub.replace(' ', '_')}">
          <span>{clean_sub}</span>
          <span class="count">UML</span>
        </div>
'''
    html_content += '      </div>'

# Master Interactive Macro-Process SVG
master_svg = '''
<svg width="850" height="500" viewBox="0 0 850 500" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Actor Admin -->
  <g transform="translate(60, 220)">
    <circle cx="0" cy="-35" r="18" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="0" y1="-17" x2="0" y2="25" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="-25" y1="-5" x2="25" y2="-5" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="0" y1="25" x2="-20" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="0" y1="25" x2="20" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="0" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#f8fafc" text-anchor="middle">Administrador</text>
  </g>

  <!-- Title Boundary Box -->
  <rect x="170" y="30" width="640" height="440" rx="16" fill="rgba(30, 41, 59, 0.5)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="2"/>
  <text x="490" y="65" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#38bdf8" text-anchor="middle">SISTEMA GENERAL DE PROCESOS</text>

  <!-- Lines connecting Admin to Processes -->
  <line x1="90" y1="220" x2="230" y2="110" stroke="#475569" stroke-width="2"/>
  <line x1="90" y1="220" x2="230" y2="190" stroke="#475569" stroke-width="2"/>
  <line x1="90" y1="220" x2="230" y2="270" stroke="#475569" stroke-width="2"/>
  <line x1="90" y1="220" x2="230" y2="350" stroke="#475569" stroke-width="2"/>
  <line x1="90" y1="220" x2="230" y2="420" stroke="#475569" stroke-width="2"/>

  <!-- Macro Process Nodes (Clickable) -->
  <g class="macro-node" cursor="pointer" onclick="openDiagram('ROLES')">
    <rect x="230" y="90" width="260" height="45" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" filter="url(#shadow)"/>
    <text x="360" y="118" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#f8fafc" text-anchor="middle">1. Configuración y Usuarios</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('COMPRAS')">
    <rect x="230" y="170" width="260" height="45" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2" filter="url(#shadow)"/>
    <text x="360" y="198" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#f8fafc" text-anchor="middle">2. Compras e Inventario</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('PRODUCCION')">
    <rect x="230" y="250" width="260" height="45" rx="10" fill="#1e293b" stroke="#22c55e" stroke-width="2" filter="url(#shadow)"/>
    <text x="360" y="278" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#f8fafc" text-anchor="middle">3. Producción y Cocina</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('CLIENTES')">
    <rect x="230" y="330" width="260" height="45" rx="10" fill="#1e293b" stroke="#eab308" stroke-width="2" filter="url(#shadow)"/>
    <text x="360" y="358" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#f8fafc" text-anchor="middle">4. Clientes y Suscripciones</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('RUTA Y DOMICILIARIOS')">
    <rect x="230" y="400" width="260" height="45" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="2" filter="url(#shadow)"/>
    <text x="360" y="428" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#f8fafc" text-anchor="middle">5. Logística y Domicilios</text>
  </g>

  <!-- Right side Subprocess Quick Links -->
  <g class="macro-node" cursor="pointer" onclick="openDiagram('DASHBOARD')">
    <rect x="540" y="250" width="230" height="45" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2" filter="url(#shadow)"/>
    <text x="655" y="278" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#38bdf8" text-anchor="middle">6. Dashboard & Analítica</text>
  </g>
</svg>
'''

html_content += f'''
    </div>

    <!-- Main Canvas View -->
    <div class="main-canvas">
      <div class="viewer-card">
        <div class="viewer-header">
          <h2 id="diagram-title">Mapa General de Procesos</h2>
          <div class="controls">
            <span style="font-size: 12px; color: #64748b;">Haz clic en cualquier subproceso del menú izquierdo para explorar</span>
          </div>
        </div>
        <div class="viewer-body" id="diagram-container">
          <div class="macro-map-container">
            {master_svg}
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Embedded SVG store
    const svgStore = {json.dumps(svg_map, ensure_ascii=False)};
    const masterMap = `{master_svg}`;

    function openDiagram(subName) {{
      const container = document.getElementById('diagram-container');
      const title = document.getElementById('diagram-title');
      
      // Update active state in sidebar
      document.querySelectorAll('.sub-item').forEach(el => el.classList.remove('active'));
      const activeBtn = document.getElementById('btn-' + subName.replace(/ /g, '_'));
      if (activeBtn) activeBtn.classList.add('active');

      if (svgStore[subName]) {{
        title.innerText = 'Diagrama de Casos de Uso: ' + subName;
        container.innerHTML = svgStore[subName];
      }} else {{
        title.innerText = subName;
        container.innerHTML = '<div class="placeholder-state"><p>Diagrama no encontrado.</p></div>';
      }}
    }}

    function showMacroMap() {{
      const container = document.getElementById('diagram-container');
      const title = document.getElementById('diagram-title');
      document.querySelectorAll('.sub-item').forEach(el => el.classList.remove('active'));
      title.innerText = 'Mapa General de Procesos';
      container.innerHTML = '<div class="macro-map-container">' + masterMap + '</div>';
    }}
  </script>
</body>
</html>
'''

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Interactive Dashboard created at {output_html}")
