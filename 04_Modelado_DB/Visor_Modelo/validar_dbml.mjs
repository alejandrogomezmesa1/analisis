// Valida la sintaxis DBML de un bd.uml (sin los bloques Records, que el parser no soporta).
// Uso: node validar_dbml.mjs ruta/bd.uml
import pkg from '@dbml/core';
import fs from 'fs';
const { Parser } = pkg;
const f = process.argv[2];
const s = fs.readFileSync(f, 'utf8').replace(/^Records[^{]*\{[\s\S]*?^\}/gm, '');
try {
  const sch = new Parser().parse(s, 'dbmlv2').schemas[0];
  const anchas = sch.tables.filter(t => t.fields.length > 12).map(t => `${t.name} (${t.fields.length})`);
  console.log(`OK ${f}: ${sch.tables.length} tablas, ${sch.refs.length} relaciones, ${sch.tableGroups.length} grupos` +
              (anchas.length ? ` · ATENCIÓN, más de 12 columnas: ${anchas.join(', ')}` : ' · todas con 12 columnas o menos'));
} catch (e) {
  console.log('ERROR', JSON.stringify(e.diags ? e.diags.map(d => [d.message, d.location && d.location.start]) : e.message).slice(0, 800));
  process.exit(1);
}
