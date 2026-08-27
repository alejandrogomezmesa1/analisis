import os

with open("/Users/alejo/Proyectos/MapaMental/arbol_problemas.svg", "r", encoding="utf-8") as f:
    orig_content = f.read()

defs_end = orig_content.find("</defs>") + 7
preamble = orig_content[:defs_end]

medios_marker = '''
    <marker id="aM" viewBox="0 0 20 20" refX="18" refY="10" markerWidth="10" markerHeight="10" orient="auto">
      <path d="M1,1 L18,10 L1,19 z" fill="#0288D1"/>
    </marker>
  </defs>'''

preamble = preamble.replace("</defs>", medios_marker)

svg = []
svg.append(preamble)

svg.append('''

  <!-- ================= LOGO ================= -->
  <rect x="904" y="120" width="144" height="144" rx="30" fill="#2E7D32"/>
  <text x="976" y="196" text-anchor="middle" dominant-baseline="central"
        font-family="BricolageBold, sans-serif" font-size="88" fill="#ffffff">J</text>

  <text x="1070" y="232" font-family="BricolageBold, sans-serif" font-size="96"
        letter-spacing="2" fill="#1a1a1a">JACKSOFT</text>
  <text x="1070" y="296" font-family="Outfit, sans-serif" font-size="28"
        letter-spacing="8" fill="#8a8a8a">LA COCA DE JACKS SAS</text>

  <!-- ================= FINES (VERDE POSITIVO) ================= -->

  <!-- Conexiones indirectos -> directos -->
  <path d="M450,572 L450,650 L660,650 L660,728" fill="none" stroke="#43A047" stroke-width="5" marker-end="url(#aG)"/>
  <path d="M976,572 L976,650 L660,650 L660,728" fill="none" stroke="#43A047" stroke-width="5" marker-end="url(#aG)"/>
  <path d="M1502,572 L1502,650 L1820,650 L1820,728" fill="none" stroke="#43A047" stroke-width="5" marker-end="url(#aG)"/>
  <path d="M2028,572 L2028,650 L1820,650 L1820,728" fill="none" stroke="#43A047" stroke-width="5" marker-end="url(#aG)"/>

  <!-- Fila indirectos (Resultados específicos esperados) -->
  <g class="txt" font-size="22" text-anchor="middle" dominant-baseline="central">
    <rect x="220"  y="420" width="460" height="152" rx="28" fill="#2E7D32"/><text x="450" y="498" fill="#ffffff">VALIDACIÓN RÁPIDA DE PAGOS</text>
    <rect x="746"  y="420" width="460" height="152" rx="28" fill="#2E7D32"/><text x="976" y="498" fill="#ffffff">CONTROL DE ROTACIÓN DE COCAS</text>
    <rect x="1272" y="420" width="460" height="152" rx="28" fill="#2E7D32"/><text x="1502" y="498" fill="#ffffff">VENTAS DENTRO DE COBERTURA</text>
    <rect x="1798" y="420" width="460" height="152" rx="28" fill="#2E7D32"/><text x="2028" y="498" fill="#ffffff">ACTIVACIÓN OPORTUNA DE PLANES</text>
  </g>

  <!-- Fila directos (Fines principales) -->
  <g class="txt" font-size="28" text-anchor="middle" dominant-baseline="central">
    <rect x="220"  y="740" width="880" height="170" rx="30" fill="#2E7D32"/><text x="660" y="825" fill="#ffffff">REDUCCIÓN DE ERRORES Y DEMORAS OPERATIVAS</text>
    <rect x="1380" y="740" width="880" height="170" rx="30" fill="#2E7D32"/><text x="1820" y="825" fill="#ffffff">INCREMENTO DE VENTAS Y FIDELIZACIÓN</text>
  </g>

  <!-- Conexiones directos -> arbol -->
  <path d="M660,910 L660,985 L1170,985 L1170,1080" fill="none" stroke="#43A047" stroke-width="5" marker-end="url(#aG)"/>
  <path d="M1820,910 L1820,985 L1310,985 L1310,1080" fill="none" stroke="#43A047" stroke-width="5" marker-end="url(#aG)"/>

  <!-- ================= ARBOL (CENTRO) ================= -->

  <!-- Copa (Follaje verde) -->
  <ellipse cx="1240" cy="1400" rx="460" ry="220" fill="#2E7D32"/>
  <ellipse cx="1000" cy="1200" rx="260" ry="200" fill="#388E3C"/>
  <ellipse cx="1480" cy="1200" rx="260" ry="200" fill="#388E3C"/>
  <ellipse cx="1240" cy="1320" rx="430" ry="240" fill="#388E3C"/>
  <ellipse cx="840"  cy="1360" rx="210" ry="160" fill="#43A047"/>
  <ellipse cx="1640" cy="1360" rx="210" ry="160" fill="#43A047"/>
  <ellipse cx="1240" cy="1190" rx="300" ry="190" fill="#43A047"/>
  <ellipse cx="1240" cy="1180" rx="180" ry="120" fill="#66BB6A"/>

  <!-- Ramas -->
  <path d="M1240,1510 C1120,1440 1040,1380 1000,1300" fill="none" stroke="#6D4C41" stroke-width="26" stroke-linecap="round"/>
  <path d="M1240,1510 C1360,1440 1440,1380 1480,1300" fill="none" stroke="#6D4C41" stroke-width="26" stroke-linecap="round"/>
  <path d="M1240,1505 C1240,1420 1230,1360 1215,1280" fill="none" stroke="#6D4C41" stroke-width="22" stroke-linecap="round"/>

  <!-- Tronco -->
  <path d="M1144,1490 C1140,1580 1136,1600 1132,1640 L1132,2000 C1132,2030 1180,2050 1240,2050 C1300,2050 1348,2030 1348,2000 L1348,1640 C1344,1600 1340,1580 1336,1490 C1280,1520 1200,1520 1144,1490 Z"
        fill="#795548"/>

  <!-- Caja Objetivo Central -->
  <rect x="680" y="1570" width="1120" height="185" rx="34" fill="#1B5E20" stroke="#43A047" stroke-width="4"/>
  <text x="1240" class="txt" font-size="24" text-anchor="middle" dominant-baseline="central" fill="#ffffff">
    <tspan x="1240" y="1635">OPTIMIZAR LA OPERACIÓN DE LA COCA DE JACKS S.A.S.</tspan>
    <tspan x="1240" y="1695">MEDIANTE SOLUCIÓN TECNOLÓGICA INTEGRAL</tspan>
  </text>

  <!-- Raices -->
  <path d="M1240,2050 C1150,2120 820,2220 500,2340" fill="none" stroke="#795548" stroke-width="40" stroke-linecap="round"/>
  <path d="M1240,2050 C1330,2120 1660,2220 1980,2340" fill="none" stroke="#795548" stroke-width="40" stroke-linecap="round"/>
  <path d="M1240,2050 C1230,2120 1225,2220 1230,2350" fill="none" stroke="#795548" stroke-width="34" stroke-linecap="round"/>
  <path d="M1240,2050 C1250,2120 1255,2220 1250,2350" fill="none" stroke="#795548" stroke-width="34" stroke-linecap="round"/>
  <path d="M1240,2055 C1100,2140 900,2210 700,2320" fill="none" stroke="#8D6E63" stroke-width="22" stroke-linecap="round"/>
  <path d="M1240,2055 C1380,2140 1580,2210 1780,2320" fill="none" stroke="#8D6E63" stroke-width="22" stroke-linecap="round"/>

  <!-- ================= MEDIOS / ACCIONES (AZUL / TURQUESA) ================= -->

  <!-- Conexiones raices -> medios directos (apuntando hacia arriba hacia el tronco/objetivo) -->
  <path d="M500,2390 L500,2355" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M1240,2390 L1240,2355" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M1980,2390 L1980,2355" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>

  <!-- Fila medios directos -->
  <g class="txt" text-anchor="middle" dominant-baseline="central">
    <rect x="220"  y="2390" width="560" height="180" rx="30" fill="#0288D1"/>
    <text x="500" fill="#ffffff" font-size="22">
      <tspan x="500" y="2458">PASARELA DE PAGOS</tspan>
      <tspan x="500" y="2514">AUTOMATIZADA</tspan>
    </text>
    <rect x="960"  y="2390" width="560" height="180" rx="30" fill="#0288D1"/>
    <text x="1240" fill="#ffffff" font-size="21">
      <tspan x="1240" y="2458">CONTROL DIGITAL DE INVENTARIO</tspan>
      <tspan x="1240" y="2514">Y ROTACIÓN DE ENVASES</tspan>
    </text>
    <rect x="1700" y="2390" width="560" height="180" rx="30" fill="#0288D1"/>
    <text x="1980" fill="#ffffff" font-size="21">
      <tspan x="1980" y="2458">GEORREFERENCIACIÓN Y</tspan>
      <tspan x="1980" y="2514">COBERTURA LOGÍSTICA</tspan>
    </text>
  </g>

  <!-- Conexiones medios directos -> indirectos -->
  <path d="M500,2690 L500,2635 L380,2635 L380,2570" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M500,2690 L500,2635 L724,2635 L724,2570" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M1240,2690 L1240,2635 L1068,2635 L1068,2570" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M1240,2690 L1240,2635 L1412,2635 L1412,2570" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M1980,2690 L1980,2635 L1756,2635 L1756,2570" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>
  <path d="M1980,2690 L1980,2635 L2100,2635 L2100,2570" fill="none" stroke="#0288D1" stroke-width="5" marker-end="url(#aM)"/>

  <!-- Fila medios indirectos / acciones -->
  <g class="txt" font-size="16" text-anchor="middle" dominant-baseline="central">
    <rect x="220"  y="2700" width="320" height="152" rx="28" fill="#0288D1"/><text x="380" y="2776" fill="#ffffff">PASARELA DE PAGO INTEGRADA</text>
    <rect x="564"  y="2700" width="320" height="152" rx="28" fill="#0288D1"/><text x="724" y="2776" fill="#ffffff">VALIDACIÓN AUTOMÁTICA DE PAGOS</text>
    <rect x="908"  y="2700" width="320" height="152" rx="28" fill="#0288D1"/><text x="1068" y="2776" fill="#ffffff">SEGUIMIENTO DIGITAL A COCAS</text>
    <rect x="1252" y="2700" width="320" height="152" rx="28" fill="#0288D1"/><text x="1412" y="2776" fill="#ffffff">CÁLCULO AUTOMÁTICO DE CUPOS</text>
    <rect x="1596" y="2700" width="320" height="152" rx="28" fill="#0288D1"/><text x="1756" y="2776" fill="#ffffff">ZONAS GEORREFERENCIADAS</text>
    <rect x="1940" y="2700" width="320" height="152" rx="28" fill="#0288D1"/><text x="2100" y="2776" fill="#ffffff">PLANIFICACIÓN Y FESTIVOS</text>
  </g>

  <!-- ================= FLECHAS LATERALES ================= -->

  <!-- FINES (arriba) -->
  <path d="M2420,930 L2420,620" fill="none" stroke="#2E7D32" stroke-width="6" marker-end="url(#aG)"/>
  <text x="2325" y="775" transform="rotate(-90 2325 775)" fill="#2E7D32" font-size="64"
        text-anchor="middle" dominant-baseline="central" letter-spacing="6">FINES</text>

  <!-- MEDIOS (abajo) -->
  <path d="M2420,2810 L2420,2530" fill="none" stroke="#0288D1" stroke-width="6" marker-end="url(#aM)"/>
  <text x="2325" y="2670" transform="rotate(-90 2325 2670)" fill="#0288D1" font-size="64"
        text-anchor="middle" dominant-baseline="central" letter-spacing="6">MEDIOS</text>

  <!-- ================= PIE ================= -->
  <line x1="840" y1="3040" x2="1640" y2="3040" stroke="#e0e0e0" stroke-width="3"/>
  <text x="1240" y="3140" font-family="OutfitBold, sans-serif" font-size="58" text-anchor="middle"
        dominant-baseline="central" fill="#333333">Figura 2. Modelo Árbol de Objetivos</text>

</svg>
''')

output_path = "/Users/alejo/Proyectos/MapaMental/arbol_objetivos.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Perfect Árbol de Objetivos SVG created at {output_path}")
