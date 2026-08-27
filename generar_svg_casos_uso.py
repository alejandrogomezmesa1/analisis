import csv
import os
import re

csv_file = "/Users/alejo/Proyectos/MapaMental/Tablero Kanban + Matriz HU (Agosto 21)) - Story Mapping.csv"
output_dir = "/Users/alejo/Proyectos/MapaMental/diagramas_casos_uso_svg"
os.makedirs(output_dir, exist_ok=True)

subprocesses = []

with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = list(csv.reader(f))
    headers = reader[5]
    
    start_col = 0
    for i, h in enumerate(headers):
        if h.strip() == "ROLES":
            start_col = i
            break
            
    for col in range(start_col, len(headers)):
        name = headers[col].strip()
        if not name:
            continue
            
        actions = []
        for r in range(6, len(reader)):
            if col < len(reader[r]):
                val = reader[r][col].strip()
                if val and not val.isdigit():
                    clean_val = val.replace('"', '').replace('\n', ' ').strip()
                    
                    # Filter out "Consultar estado de la cuenta" from ACCESO
                    if name.upper() == "ACCESO" and "consultar estado de la cuenta" in clean_val.lower():
                        continue
                        
                    # Filter out redundant "Registrar salida de inventario" from INSUMOS
                    if name.upper() == "INSUMOS" and clean_val.lower() == "registrar salida de inventario":
                        continue
                        
                    actions.append(clean_val)
                    


        if actions:
            subprocesses.append({
                "title": name,
                "actions": actions
            })

def wrap_text(text, max_chars=22):
    words = text.split(' ')
    lines = []
    current_line = []
    current_len = 0
    for w in words:
        if current_len + len(w) > max_chars and current_line:
            lines.append(" ".join(current_line))
            current_line = [w]
            current_len = len(w)
        else:
            current_line.append(w)
            current_len += len(w) + 1
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def generate_svg_diagram(sp):
    raw_title = sp["title"]
    clean_title = raw_title.replace('"', '').strip()
    actions = sp["actions"]
    
    # Custom layout for ACCESO
    if clean_title.upper() == "ACCESO":
        width = 950
        height = 550
        actor_x = 70
        actor_y = 275

        svg = []
        svg.append(f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">')
        svg.append('''
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333333" />
    </marker>
  </defs>
  <style>
    .bg { fill: #ffffff; }
    .box { fill: #ffffff; stroke: #333333; stroke-width: 1.5; }
    .actor { fill: none; stroke: #333333; stroke-width: 2; }
    .actor-text { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #333333; text-anchor: middle; }
    .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; fill: #111111; text-anchor: middle; }
    .oval { fill: #ffffff; stroke: #333333; stroke-width: 1.5; }
    .uc-text { font-family: Arial, sans-serif; font-size: 12px; fill: #222222; text-anchor: middle; dominant-baseline: middle; }
    .solid-line { stroke: #333333; stroke-width: 1.5; }
    .dashed-line { stroke: #555555; stroke-width: 1.2; stroke-dasharray: 4,4; marker-end: url(#arrow); }
    .rel-text { font-family: Arial, sans-serif; font-size: 11px; fill: #444444; text-anchor: middle; dominant-baseline: middle; }
  </style>
  <rect width="100%" height="100%" class="bg" />
  <rect x="160" y="30" width="760" height="490" class="box" />
  <text x="540" y="65" class="title">ACCESO</text>
''')
        # Actor
        svg.append(f'  <circle cx="{actor_x}" cy="{actor_y - 35}" r="18" class="actor" />')
        svg.append(f'  <line x1="{actor_x}" y1="{actor_y - 17}" x2="{actor_x}" y2="{actor_y + 25}" class="actor" />')
        svg.append(f'  <line x1="{actor_x - 25}" y1="{actor_y - 5}" x2="{actor_x + 25}" y2="{actor_y - 5}" class="actor" />')
        svg.append(f'  <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x - 20}" y2="{actor_y + 60}" class="actor" />')
        svg.append(f'  <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x + 20}" y2="{actor_y + 60}" class="actor" />')
        svg.append(f'  <text x="{actor_x}" y="{actor_y + 80}" class="actor-text">Admin</text>')

        def draw_oval(cx, cy, text, rx=85, ry=26):
            lines = wrap_text(text)
            svg.append(f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="oval" />')
            line_height = 13
            start_y = cy - ((len(lines) - 1) * line_height / 2)
            for idx, line in enumerate(lines):
                ly = start_y + (idx * line_height)
                svg.append(f'  <text x="{cx}" y="{ly}" class="uc-text">{line}</text>')

        hub_x, hub_y = 270, 275
        login_x, login_y = 510, 275
        valid_x, valid_y = 770, 275
        recup_x, recup_y = 510, 130
        close_x, close_y = 770, 410

        draw_oval(hub_x, hub_y, "Acceso al sistema", rx=80, ry=28)
        draw_oval(login_x, login_y, "Iniciar sesión", rx=85, ry=28)
        draw_oval(valid_x, valid_y, "Validar credenciales", rx=85, ry=28)
        draw_oval(recup_x, recup_y, "Recuperar / restablecer contraseña", rx=95, ry=28)
        draw_oval(close_x, close_y, "Cerrar sesión", rx=80, ry=28)

        svg.append(f'  <line x1="{actor_x + 30}" y1="{actor_y}" x2="{hub_x - 80}" y2="{hub_y}" class="solid-line" />')
        svg.append(f'  <line x1="{hub_x + 80}" y1="{hub_y}" x2="{login_x - 85}" y2="{login_y}" class="dashed-line" />')
        svg.append(f'  <text x="{(hub_x + login_x)/2}" y="{hub_y - 10}" class="rel-text">&lt;&lt;include&gt;&gt;</text>')

        svg.append(f'  <line x1="{login_x + 85}" y1="{login_y}" x2="{valid_x - 85}" y2="{valid_y}" class="dashed-line" />')
        svg.append(f'  <text x="{(login_x + valid_x)/2}" y="{login_y - 10}" class="rel-text">&lt;&lt;include&gt;&gt;</text>')

        svg.append(f'  <line x1="{recup_x - 70}" y1="{recup_y + 20}" x2="{hub_x + 40}" y2="{hub_y - 25}" class="dashed-line" />')
        svg.append(f'  <text x="{(recup_x + hub_x)/2 - 10}" y="{(recup_y + hub_y)/2 - 10}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')

        svg.append(f'  <line x1="{close_x - 60}" y1="{close_y - 20}" x2="{login_x + 60}" y2="{login_y + 20}" class="dashed-line" />')
        svg.append(f'  <text x="{(close_x + login_x)/2}" y="{(close_y + login_y)/2 - 8}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')

        svg.append('</svg>')
        return "\n".join(svg)

    # Custom layout for DASHBOARD
    if clean_title.upper() == "DASHBOARD":
        create_action = None
        search_action = None
        right_actions = []
        for name in actions:
            name_lower = name.lower()
            if name_lower.startswith("exportar"):
                create_action = name
            elif name_lower.startswith("filtrar"):
                search_action = name
            else:
                right_actions.append(name)

        num_right = len(right_actions)
        min_height = 650
        item_step = 55
        content_height = max(min_height, num_right * item_step + 180)
        
        width = 950
        height = content_height

        actor_x = 70
        actor_y = height / 2

        pkg_x = 160
        pkg_y = 30
        pkg_w = 760
        pkg_h = height - 60

        hub_x = 280
        hub_y = height / 2

        top_x = 520
        top_y = 110

        bottom_x = 520
        bottom_y = height - 110

        svg = []
        svg.append(f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">')
        svg.append('''
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333333" />
    </marker>
  </defs>
  <style>
    .bg { fill: #ffffff; }
    .box { fill: #ffffff; stroke: #333333; stroke-width: 1.5; }
    .actor { fill: none; stroke: #333333; stroke-width: 2; }
    .actor-text { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #333333; text-anchor: middle; }
    .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; fill: #111111; text-anchor: middle; }
    .oval { fill: #ffffff; stroke: #333333; stroke-width: 1.5; }
    .uc-text { font-family: Arial, sans-serif; font-size: 12px; fill: #222222; text-anchor: middle; dominant-baseline: middle; }
    .solid-line { stroke: #333333; stroke-width: 1.5; }
    .dashed-line { stroke: #555555; stroke-width: 1.2; stroke-dasharray: 4,4; marker-end: url(#arrow); }
    .rel-text { font-family: Arial, sans-serif; font-size: 11px; fill: #444444; text-anchor: middle; dominant-baseline: middle; }
  </style>
  <rect width="100%" height="100%" class="bg" />
''')
        svg.append(f'  <rect x="{pkg_x}" y="{pkg_y}" width="{pkg_w}" height="{pkg_h}" class="box" />')
        svg.append(f'  <text x="{pkg_x + pkg_w/2}" y="{pkg_y + 35}" class="title">{clean_title}</text>')

        svg.append(f'  <circle cx="{actor_x}" cy="{actor_y - 35}" r="18" class="actor" />')
        svg.append(f'  <line x1="{actor_x}" y1="{actor_y - 17}" x2="{actor_x}" y2="{actor_y + 25}" class="actor" />')
        svg.append(f'  <line x1="{actor_x - 25}" y1="{actor_y - 5}" x2="{actor_x + 25}" y2="{actor_y - 5}" class="actor" />')
        svg.append(f'  <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x - 20}" y2="{actor_y + 60}" class="actor" />')
        svg.append(f'  <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x + 20}" y2="{actor_y + 60}" class="actor" />')
        svg.append(f'  <text x="{actor_x}" y="{actor_y + 80}" class="actor-text">Admin</text>')

        def draw_oval(cx, cy, text, rx=85, ry=25):
            lines = wrap_text(text)
            svg.append(f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="oval" />')
            line_height = 13
            start_y = cy - ((len(lines) - 1) * line_height / 2)
            for idx, line in enumerate(lines):
                ly = start_y + (idx * line_height)
                svg.append(f'  <text x="{cx}" y="{ly}" class="uc-text">{line}</text>')

        draw_oval(hub_x, hub_y, "Dashboard", rx=80, ry=28)
        svg.append(f'  <line x1="{actor_x + 30}" y1="{actor_y}" x2="{hub_x - 80}" y2="{hub_y}" class="solid-line" />')

        if create_action:
            draw_oval(top_x, top_y, create_action, rx=85, ry=25)
            svg.append(f'  <line x1="{top_x - 60}" y1="{top_y + 20}" x2="{hub_x + 50}" y2="{hub_y - 20}" class="dashed-line" />')
            svg.append(f'  <text x="{(top_x + hub_x)/2}" y="{(top_y + hub_y)/2 - 10}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')

        if search_action:
            draw_oval(bottom_x, bottom_y, search_action, rx=110, ry=28)
            svg.append(f'  <line x1="{bottom_x - 80}" y1="{bottom_y - 20}" x2="{hub_x + 50}" y2="{hub_y + 20}" class="dashed-line" />')
            svg.append(f'  <text x="{(bottom_x + hub_x)/2}" y="{(bottom_y + hub_y)/2 + 10}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')

        right_x = 770
        if num_right > 0:
            start_y = 110
            end_y = height - 110
            step_y = (end_y - start_y) / max(1, num_right - 1) if num_right > 1 else (start_y + end_y)/2
            
            for idx, act_name in enumerate(right_actions):
                ry = start_y + (idx * step_y) if num_right > 1 else (start_y + end_y)/2
                draw_oval(right_x, ry, act_name, rx=85, ry=25)
                svg.append(f'  <line x1="{right_x - 85}" y1="{ry}" x2="{hub_x + 80}" y2="{hub_y}" class="dashed-line" />')
                
                t = 0.25
                lx = (right_x - 85) + t * ((hub_x + 80) - (right_x - 85))
                ly = ry + t * (hub_y - ry)
                svg.append(f'  <text x="{lx}" y="{ly - 6}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')

        svg.append('</svg>')
        return "\n".join(svg)

    # Standard layout for all other subprocesses
    elif clean_title.upper() == "CALENDARIO":
        hub_name = "Gestión de calendario"
    elif clean_title.upper() == "MONITOREO DE ENTREGA TIEMPO REAL":
        hub_name = "Monitoreo de entregas"
    elif clean_title.upper().startswith("CATEGORIA"):
        hub_name = f"Gestión de {clean_title.lower()}"
    elif clean_title.upper().startswith("FICHA"):
        hub_name = "Gestión de fichas técnicas"
    elif clean_title.upper().startswith("RUTA"):
        hub_name = "Gestión de rutas y domiciliarios"
    else:
        hub_name = f"Gestión de {clean_title.lower()}"

    central_action = None
    create_action = None
    search_action = None
    right_actions = []
    
    for name in actions:
        if name.lower().startswith("listar"):
            central_action = name
            break
    if not central_action:
        for name in actions:
            if name.lower().startswith("consultar") or name.lower().startswith("generar reportes"):
                central_action = name
                break

    for name in actions:
        if name == central_action:
            continue
        name_lower = name.lower()
        if not create_action and (name_lower.startswith("crear") or name_lower.startswith("registrar") or name_lower.startswith("exportar") or name_lower.startswith("parametrizar") or name_lower.startswith("cotizar")):
            create_action = name
        elif not search_action and (name_lower.startswith("buscar") or name_lower.startswith("filtrar")):
            search_action = name
        else:
            right_actions.append(name)

    num_right = len(right_actions)
    
    min_height = 650
    item_step = 55
    content_height = max(min_height, num_right * item_step + 180)
    
    width = 950
    height = content_height

    actor_x = 70
    actor_y = height / 2

    pkg_x = 160
    pkg_y = 30
    pkg_w = 760
    pkg_h = height - 60

    hub_x = 280
    hub_y = height / 2

    central_x = 520
    central_y = height / 2

    top_x = 520
    top_y = 110

    bottom_x = 520
    bottom_y = height - 110

    svg = []
    svg.append(f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">')
    
    svg.append('''
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333333" />
    </marker>
  </defs>
  <style>
    .bg { fill: #ffffff; }
    .box { fill: #ffffff; stroke: #333333; stroke-width: 1.5; }
    .actor { fill: none; stroke: #333333; stroke-width: 2; }
    .actor-text { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #333333; text-anchor: middle; }
    .title { font-family: Arial, sans-serif; font-size: 20px; font-weight: bold; fill: #111111; text-anchor: middle; }
    .oval { fill: #ffffff; stroke: #333333; stroke-width: 1.5; }
    .uc-text { font-family: Arial, sans-serif; font-size: 12px; fill: #222222; text-anchor: middle; dominant-baseline: middle; }
    .solid-line { stroke: #333333; stroke-width: 1.5; }
    .dashed-line { stroke: #555555; stroke-width: 1.2; stroke-dasharray: 4,4; marker-end: url(#arrow); }
    .rel-text { font-family: Arial, sans-serif; font-size: 11px; fill: #444444; text-anchor: middle; dominant-baseline: middle; }
  </style>
  <rect width="100%" height="100%" class="bg" />
''')

    svg.append(f'  <rect x="{pkg_x}" y="{pkg_y}" width="{pkg_w}" height="{pkg_h}" class="box" />')
    svg.append(f'  <text x="{pkg_x + pkg_w/2}" y="{pkg_y + 35}" class="title">{clean_title}</text>')

    svg.append(f'  <circle cx="{actor_x}" cy="{actor_y - 35}" r="18" class="actor" />')
    svg.append(f'  <line x1="{actor_x}" y1="{actor_y - 17}" x2="{actor_x}" y2="{actor_y + 25}" class="actor" />')
    svg.append(f'  <line x1="{actor_x - 25}" y1="{actor_y - 5}" x2="{actor_x + 25}" y2="{actor_y - 5}" class="actor" />')
    svg.append(f'  <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x - 20}" y2="{actor_y + 60}" class="actor" />')
    svg.append(f'  <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x + 20}" y2="{actor_y + 60}" class="actor" />')
    svg.append(f'  <text x="{actor_x}" y="{actor_y + 80}" class="actor-text">Admin</text>')

    def draw_oval(cx, cy, text, rx=85, ry=25):
        lines = wrap_text(text)
        svg.append(f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="oval" />')
        line_height = 13
        start_y = cy - ((len(lines) - 1) * line_height / 2)
        for idx, line in enumerate(lines):
            ly = start_y + (idx * line_height)
            svg.append(f'  <text x="{cx}" y="{ly}" class="uc-text">{line}</text>')

    draw_oval(hub_x, hub_y, hub_name, rx=80, ry=28)
    draw_oval(central_x, central_y, central_action, rx=90, ry=28)

    svg.append(f'  <line x1="{actor_x + 30}" y1="{actor_y}" x2="{hub_x - 80}" y2="{hub_y}" class="solid-line" />')
    svg.append(f'  <line x1="{hub_x + 80}" y1="{hub_y}" x2="{central_x - 90}" y2="{central_y}" class="dashed-line" />')
    svg.append(f'  <text x="{(hub_x + central_x)/2}" y="{hub_y - 10}" class="rel-text">&lt;&lt;include&gt;&gt;</text>')

    if create_action and create_action != central_action:
        draw_oval(top_x, top_y, create_action, rx=85, ry=25)
        svg.append(f'  <line x1="{top_x - 60}" y1="{top_y + 20}" x2="{hub_x + 40}" y2="{hub_y - 25}" class="dashed-line" />')
        svg.append(f'  <text x="{(top_x + hub_x)/2 - 10}" y="{(top_y + hub_y)/2 - 10}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')
        svg.append(f'  <line x1="{top_x}" y1="{top_y + 25}" x2="{central_x}" y2="{central_y - 28}" class="dashed-line" />')
        svg.append(f'  <text x="{top_x + 35}" y="{(top_y + central_y)/2}" class="rel-text">&lt;&lt;include&gt;&gt;</text>')

    if search_action and search_action != central_action and search_action != create_action:
        draw_oval(bottom_x, bottom_y, search_action, rx=105, ry=28)
        svg.append(f'  <line x1="{bottom_x - 60}" y1="{bottom_y - 20}" x2="{hub_x + 40}" y2="{hub_y + 25}" class="dashed-line" />')
        svg.append(f'  <text x="{(bottom_x + hub_x)/2 - 10}" y="{(bottom_y + hub_y)/2 + 10}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')
        svg.append(f'  <line x1="{bottom_x}" y1="{bottom_y - 25}" x2="{central_x}" y2="{central_y + 28}" class="dashed-line" />')
        svg.append(f'  <text x="{bottom_x + 35}" y="{(bottom_y + central_y)/2}" class="rel-text">&lt;&lt;include&gt;&gt;</text>')

    right_x = 770
    if num_right > 0:
        start_y = 110
        end_y = height - 110
        step_y = (end_y - start_y) / max(1, num_right - 1) if num_right > 1 else (start_y + end_y)/2
        
        for idx, act_name in enumerate(right_actions):
            ry = start_y + (idx * step_y) if num_right > 1 else (start_y + end_y)/2
            draw_oval(right_x, ry, act_name, rx=85, ry=25)
            
            svg.append(f'  <line x1="{right_x - 85}" y1="{ry}" x2="{central_x + 90}" y2="{central_y}" class="dashed-line" />')
            
            t = 0.22
            lx = (right_x - 85) + t * ((central_x + 90) - (right_x - 85))
            ly = ry + t * (central_y - ry)
            svg.append(f'  <text x="{lx}" y="{ly - 6}" class="rel-text">&lt;&lt;extends&gt;&gt;</text>')

    svg.append('</svg>')
    return "\n".join(svg)

for sp in subprocesses:
    svg_content = generate_svg_diagram(sp)
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', sp["title"]) + ".svg"
    path = os.path.join(output_dir, safe_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Regenerated SVG: {safe_name}")

print("All SVG diagrams updated successfully!")
