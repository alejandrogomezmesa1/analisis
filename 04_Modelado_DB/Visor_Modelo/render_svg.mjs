// Convierte un archivo DOT en SVG con Graphviz (viz.js). Uso: node render_svg.mjs entrada.dot salida.svg
import { instance } from '@viz-js/viz';
import fs from 'fs';
const [inp, out] = process.argv.slice(2);
const viz = await instance();
const r = viz.render(fs.readFileSync(inp, 'utf8'), { format: 'svg' });
if (r.status !== 'success') { console.error(r.errors); process.exit(1); }
fs.writeFileSync(out, r.output);
