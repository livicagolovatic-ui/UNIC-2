// Placa informativă pentru sediul GAL: un slide de 70 × 50 cm, fundalul = modelul AFIR curățat (SVG), textele în Calibri.
// Rulare: node placa_pptx.js _build/placa_layout.json   (cere pptxgenjs: npm install pptxgenjs, sau NODE_PATH către el)
const fs = require('fs');
const pptxgen = require('pptxgenjs');

const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const IN = (pt) => pt / 72;                 // modelul e la scara 1:1, în puncte PDF
// Distanța de la marginea de sus a casetei (fără margini interioare) la linia de bază, în multipli ai corpului literei.
// Măsurat pe randarea LibreOffice cu Carlito (metric identic cu Calibri): 1,00 em. PowerPoint așază primul rând cu câteva
// sutimi de em mai sus; 0,928 ține ambele randări la sub 1 pt (sub 0,4 mm pe placă) de linia punctată din model.
const ASC = parseFloat(process.env.PLACA_ASC || '0.928');

const pres = new pptxgen();
pres.defineLayout({ name: 'PLACA_70x50', width: IN(spec.width_pt), height: IN(spec.height_pt) });
pres.layout = 'PLACA_70x50';
pres.title = 'Placă informativă – sediul GAL Napoca Porolissum';
pres.author = 'Asociația GAL Napoca Porolissum';
pres.subject = 'PS 2023-2027, LEADER – Educație pentru mediu în teritoriul GAL Napoca Porolissum – micro-granturi pentru mediu';

const slide = pres.addSlide();
slide.background = { color: 'FFFFFF' };
slide.addImage({ path: spec.svg, x: 0, y: 0, w: IN(spec.width_pt), h: IN(spec.height_pt),
                 altText: 'Model AFIR „Placă FEADR LEADER” V3', objectName: 'Model AFIR (nu se modifică)' });

const hex = (c) => c.map((v) => Math.round(v * 255).toString(16).padStart(2, '0')).join('').toUpperCase();
spec.items.forEach((it, i) => {
  const top = it.y - ASC * it.size;
  slide.addText(it.text, {
    x: IN(it.x), y: IN(top), w: IN(it.w + it.size * 0.6), h: IN(it.size * 1.3),
    fontFace: 'Calibri', fontSize: it.size, bold: it.bold, color: hex(it.color),
    margin: 0, align: 'left', valign: 'top', wrap: false, fit: 'none', isTextBox: true,
    objectName: `Camp ${it.camp} ${i + 1}`,
  });
});

pres.writeFile({ fileName: spec.out }).then(() => console.log('pptx', spec.out));
