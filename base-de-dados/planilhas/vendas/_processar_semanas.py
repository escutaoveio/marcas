"""
Processa S23 e S24 CSV e gera os agregados para o dashboard.
Cada linha do CSV tem 3 blocos de canais diferentes lado a lado.
"""
import csv
import sys
from collections import defaultdict

def parse_value(s):
    if not s or s.strip() in ('-', '', 'Valor total', 'Valor unitário'):
        return 0.0
    s = s.strip().replace('.', '').replace(',', '.')
    try:
        return float(s)
    except:
        return 0.0

def parse_qty(s):
    if not s or s.strip() in ('-', '', 'Quantidade'):
        return 0
    try:
        v = s.strip().replace(',', '.')
        return int(float(v))
    except:
        return 0

BRAND_KEYWORDS = {
    'LT SHINE': ['LT SHINE', 'GRANNISTONE', 'PELÍCULA LÍQUIDA', 'MICROCIMENTO', 'MARMORITE', 'PRIMER UNIVERSAL LT',
                 'VERNIZ BICOMPONENTE', 'CERA ATÓXICA', 'PASTA METALIZADA', 'PISO LÍQUIDO', 'ACQUA SHINE',
                 'PIGMENTO UMA GOTA', 'REVESTIMENTO CONCRETO APARENTE', 'PRIMER GRANNISTONE', 'LT300'],
    'ELASTMENT': ['ELASTMENT', 'SOS UMIDADE', 'MANTA LÍQUIDA', 'MANTA CIMENTÍCIA', 'MANTA LIQUIDA', 'RUFO LÍQUIDO',
                  'CHAPISCO FLEX', 'CIMENTO QUEIMADO ELASTMENT', 'CIMENTO ELÁSTICO', 'DRYMANTA', 'REJUNTE ELÁSTICO',
                  'MEMBRANA DE CURA', 'PROTETOR DE ARMADURA', 'RAPID CURE', 'FITA MULTIUSO LÍQUIDA SOS TELHAS',
                  'CHAPISCO FLEX RESINA', 'POLÍMERO ACRÍLICO', 'ELASTMENT SMART CIMENTO', 'CIMENTO ADDITIVE',
                  'SOS GESSO PERFECT', 'ADITIVO RETARDANTE', 'SOS CONCRETO IMPERMEABILIZANTE'],
    'SMART': ['SMART RESINA', 'SMART COLOR', 'TINTA ELÁSTICA SMART', 'ZERO TRINCA', 'MASSA FINA SECA',
              'CONCRE FAST', 'ULTRAGRIP', 'MASSA FLEX TAPA TUDO', 'SELANTE ACRÍLICO ZERO TRINCA',
              'MASSA POLIMERICA CIMENTO', 'IMPERMEABILIZANTE SOS CONCRETO', 'PRIMER PROMOTOR DE ADERÊNCIA ULTRAGRIP',
              'CONCRETO ESTRUTURAL INDUSTRIAL', 'SMART COAT', 'MASSA TAPA TUDO', 'CHAPISKOLA', 'CONCRE FAST'],
    'HOLD STONE': ['HOLD STONE', 'RESINA PARA PEDRAS', 'FIXADOR DE PEDRAS', 'GARDEN COLOR STONE',
                   'CLEAN TOOL', 'FIX STONE', 'RESINA PRO 5L', 'COLOR STONE'],
    'CRISTAL': ['NEX FLOOR', 'UMI BLOCK CRISTAL', 'PROTELHA', 'TIRA TINTAS CRISTAL', 'SKIN COLOR CRISTAL',
                'SHAMPOO PARA TELHAS', 'TINTA REMOVÍVEL SKIN COLOR', 'POWER SHOWER', 'REJUNTE ACRÍLICO PULO'],
    'DRYLEVIS': ['CIMENTO EGÍPCIO', 'CIMENTO EGIPCIO', 'CIMENTO SULFOALUMINOSO', 'ESPUMA TURBO DW240',
                 'SELANTE PARA JUNTAS', 'SOS GESSO HIDROFUGANTE', 'HIDROFUGANTE PARA GESSO', 'DRYTHERM',
                 'BISNAGA ZEROTRINCA', 'KIT SOS UMIDADE', 'SOS GESSO - HIDROFUGANTE', 'SOS TELHAS FITA',
                 'DRYLEVIS', 'DW240'],
}

BRAND_DIRECT = {
    'DRYLEVIS': 'DRYLEVIS', 'DRY LEVIS': 'DRYLEVIS', ' DRYLEVIS': 'DRYLEVIS',
    'ELASTMENT': 'ELASTMENT',
    'SMART': 'SMART', 'SMART CIMENTO': 'SMART',
    'LT SHINE': 'LT SHINE', 'LT SHINER': 'LT SHINE', 'LT Shiner': 'LT SHINE',
    'HOLD STONE': 'HOLD STONE',
    'CRISTAL': 'CRISTAL',
}

def infer_brand(desc, marca=''):
    m = marca.strip().upper()
    if m in BRAND_DIRECT:
        return BRAND_DIRECT[m]
    d = desc.upper()
    for brand, kws in BRAND_KEYWORDS.items():
        if any(kw.upper() in d for kw in kws):
            return brand
    return 'TERCEIROS'

def normalize_channel(loja):
    if not loja:
        return None
    lu = loja.upper().strip()
    if not lu or lu == '-':
        return None

    # EOV channels
    if 'EOV' in lu or 'EOV' in lu:
        if 'MERCADO LIVRE' in lu and 'CONSTRULIVRE' not in lu:
            return 'Mercado Livre'
        if 'SHOPEE' in lu and 'CONSTRULIVRE' not in lu:
            return 'Shopee'
        if 'WAKE' in lu:
            return 'Wake'
        if 'MAGALU' in lu:
            return 'Magalu'
        if 'TIK' in lu or 'TIKTOK' in lu:
            return 'TikTok'

    if 'COMERCIAL INTERNO' in lu:
        return 'Comercial Interno'

    # Construlivre channels
    if 'CONSTRULIVRE' in lu:
        if 'MERCADO LIVRE' in lu:
            return 'ML - Construlivre'
        if 'SHOPEE' in lu:
            return 'Shopee - Construlivre'
        return 'ML - Construlivre'

    # Shopee Novo (conta separada)
    if lu == 'SHOPEE NOVO':
        return 'Shopee Novo'

    # Obramil channels
    if 'OBRAMIL' in lu:
        if 'MERCADO LIVRE' in lu:
            return 'ML - Obramil'
        if 'MAGALU' in lu:
            return 'Magalu - Obramil'
        return 'ML - Obramil'

    if 'TRAY' in lu:
        return 'Tray'
    if 'MAGALU' in lu:
        return 'Magalu'

    return loja.strip()

def process_csv(filepath, encoding='utf-8'):
    channels = defaultdict(lambda: {'val': 0.0, 'qty': 0, 'orders': set()})
    brands = defaultdict(lambda: {'val': 0.0, 'qty': 0})
    products = defaultdict(lambda: {'val': 0.0, 'qty': 0, 'brand': '', 'channels': defaultdict(lambda: {'val': 0.0, 'qty': 0})})

    row_count = 0
    with open(filepath, encoding=encoding, errors='replace') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)  # skip header

        for row in reader:
            row_count += 1
            blocks = []

            # Block 1: cols 0-13
            if len(row) > 10 and row[5].strip() and row[3].strip() not in ('', 'Situação'):
                desc = row[5].strip()
                qty = parse_qty(row[7]) if len(row) > 7 else 0
                val = parse_value(row[9]) if len(row) > 9 else 0
                loja = row[10].strip() if len(row) > 10 else ''
                marca = row[13].strip() if len(row) > 13 else ''
                num = row[0].strip() if row else ''
                if val > 0:
                    blocks.append({'desc': desc, 'qty': qty, 'val': val, 'loja': loja, 'marca': marca, 'num': num})

            # Block 2: cols 15-24
            if len(row) > 24 and row[19].strip():
                desc = row[19].strip()
                qty = parse_qty(row[21]) if len(row) > 21 else 0
                val = parse_value(row[23]) if len(row) > 23 else 0
                loja = row[24].strip() if len(row) > 24 else ''
                if val > 0 and desc not in ('Descrição', ''):
                    blocks.append({'desc': desc, 'qty': qty, 'val': val, 'loja': loja, 'marca': '', 'num': ''})

            # Block 3: cols 27-36
            if len(row) > 36 and row[31].strip():
                desc = row[31].strip()
                qty = parse_qty(row[33]) if len(row) > 33 else 0
                val = parse_value(row[35]) if len(row) > 35 else 0
                loja = row[36].strip() if len(row) > 36 else ''
                if val > 0 and desc not in ('Descrição', ''):
                    blocks.append({'desc': desc, 'qty': qty, 'val': val, 'loja': loja, 'marca': '', 'num': ''})

            for b in blocks:
                ch = normalize_channel(b['loja'])
                brand = infer_brand(b['desc'], b['marca'])

                if ch:
                    channels[ch]['val'] += b['val']
                    channels[ch]['qty'] += b['qty']
                    if b['num']:
                        channels[ch]['orders'].add(b['num'])

                brands[brand]['val'] += b['val']
                brands[brand]['qty'] += b['qty']

                prod_key = b['desc'].strip()
                products[prod_key]['val'] += b['val']
                products[prod_key]['qty'] += b['qty']
                if not products[prod_key]['brand']:
                    products[prod_key]['brand'] = brand
                if ch:
                    products[prod_key]['channels'][ch]['val'] += b['val']
                    products[prod_key]['channels'][ch]['qty'] += b['qty']

    print(f"  -> {row_count} linhas processadas", file=sys.stderr)
    return channels, brands, products

def fmt(v):
    return f"R$ {v:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def pct(v, total):
    if total == 0: return '0,0%'
    return f"{v/total*100:.1f}%"

def delta_str(v_new, v_old):
    if v_old == 0:
        return "NOVO"
    d = (v_new - v_old) / v_old * 100
    sign = '+' if d > 0 else ''
    return f"{sign}{d:.1f}%"

def fix_double_encoding(s):
    """Fix UTF-8-over-latin-1 double encoding: read as UTF-8, encode back to latin-1, decode as UTF-8"""
    if not s:
        return s
    try:
        return s.encode('latin-1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s

def process_csv_with_fix(filepath, encoding='utf-8', fix_encoding=False):
    """Wrapper that applies double-encoding fix to string fields."""
    channels = defaultdict(lambda: {'val': 0.0, 'qty': 0, 'orders': set()})
    brands = defaultdict(lambda: {'val': 0.0, 'qty': 0})
    products = defaultdict(lambda: {'val': 0.0, 'qty': 0, 'brand': '', 'channels': defaultdict(lambda: {'val': 0.0, 'qty': 0})})

    row_count = 0
    with open(filepath, encoding=encoding, errors='replace') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)

        for row in reader:
            if fix_encoding:
                row = [fix_double_encoding(c) for c in row]
            row_count += 1
            blocks = []

            if len(row) > 10 and row[5].strip() and row[3].strip() not in ('', 'Situacao', 'Situação'):
                desc = row[5].strip()
                qty = parse_qty(row[7]) if len(row) > 7 else 0
                val = parse_value(row[9]) if len(row) > 9 else 0
                loja = row[10].strip() if len(row) > 10 else ''
                marca = row[13].strip() if len(row) > 13 else ''
                num = row[0].strip() if row else ''
                if val > 0:
                    blocks.append({'desc': desc, 'qty': qty, 'val': val, 'loja': loja, 'marca': marca, 'num': num})

            if len(row) > 24 and row[19].strip():
                desc = row[19].strip()
                qty = parse_qty(row[21]) if len(row) > 21 else 0
                val = parse_value(row[23]) if len(row) > 23 else 0
                loja = row[24].strip() if len(row) > 24 else ''
                if val > 0 and desc not in ('Descricao', 'Descrição', ''):
                    blocks.append({'desc': desc, 'qty': qty, 'val': val, 'loja': loja, 'marca': '', 'num': ''})

            if len(row) > 36 and row[31].strip():
                desc = row[31].strip()
                qty = parse_qty(row[33]) if len(row) > 33 else 0
                val = parse_value(row[35]) if len(row) > 35 else 0
                loja = row[36].strip() if len(row) > 36 else ''
                if val > 0 and desc not in ('Descricao', 'Descrição', ''):
                    blocks.append({'desc': desc, 'qty': qty, 'val': val, 'loja': loja, 'marca': '', 'num': ''})

            for b in blocks:
                ch = normalize_channel(b['loja'])
                brand = infer_brand(b['desc'], b['marca'])

                if ch:
                    channels[ch]['val'] += b['val']
                    channels[ch]['qty'] += b['qty']
                    if b['num']:
                        channels[ch]['orders'].add(b['num'])

                brands[brand]['val'] += b['val']
                brands[brand]['qty'] += b['qty']

                prod_key = b['desc'].strip()
                products[prod_key]['val'] += b['val']
                products[prod_key]['qty'] += b['qty']
                if not products[prod_key]['brand']:
                    products[prod_key]['brand'] = brand
                if ch:
                    products[prod_key]['channels'][ch]['val'] += b['val']
                    products[prod_key]['channels'][ch]['qty'] += b['qty']

    print(f"  -> {row_count} linhas processadas", file=sys.stderr)
    return channels, brands, products

print("Processando S23...", file=sys.stderr)
base_path = r'c:\Users\GustavoSantos\Desktop\IVA QUÍMICA\base-de-dados\planilhas\vendas'
s23_ch, s23_br, s23_pr = process_csv_with_fix(f'{base_path}\\S23_canais-de-vendas.csv', 'utf-8-sig', fix_encoding=True)

print("Processando S24...", file=sys.stderr)
s24_ch, s24_br, s24_pr = process_csv_with_fix(f'{base_path}\\S24_canais-de-vendas.csv', 'utf-8', fix_encoding=False)

s23_total = sum(v['val'] for v in s23_ch.values())
s24_total = sum(v['val'] for v in s24_ch.values())
s23_units = sum(v['qty'] for v in s23_pr.values())
s24_units = sum(v['qty'] for v in s24_pr.values())
s23_orders = sum(len(v['orders']) for v in s23_ch.values())
s24_orders = sum(len(v['orders']) for v in s24_ch.values())

print("\n" + "="*70)
print(f"SEMANA 23 -- 01/06 ate 04/06/2026 (4 dias, parcial)")
print(f"  Total: {fmt(s23_total)} | {s23_units} un | ~{s23_orders} pedidos unicos (EOV)")
print("="*70)

print("\n[CANAIS S23]")
for ch, d in sorted(s23_ch.items(), key=lambda x: -x[1]['val']):
    n = len(d['orders'])
    print(f"  {ch:<35} {fmt(d['val']):>15}  {d['qty']:>5} un  {n:>4} ped  {pct(d['val'],s23_total):>6}")

print("\n[MARCAS S23]")
for br, d in sorted(s23_br.items(), key=lambda x: -x[1]['val']):
    print(f"  {br:<20} {fmt(d['val']):>15}  {d['qty']:>5} un  {pct(d['val'],s23_total):>6}")

print("\n" + "="*70)
print(f"SEMANA 24 -- 05/06 ate 11/06/2026 (7 dias, semana completa)")
print(f"  Total: {fmt(s24_total)} | {s24_units} un | ~{s24_orders} pedidos unicos (EOV)")
print(f"  D vs S23: {delta_str(s24_total, s23_total)}")
print("="*70)

print("\n[CANAIS S24]")
for ch, d in sorted(s24_ch.items(), key=lambda x: -x[1]['val']):
    n = len(d['orders'])
    s23v = s23_ch.get(ch, {}).get('val', 0)
    print(f"  {ch:<35} {fmt(d['val']):>15}  {d['qty']:>5} un  {n:>4} ped  {pct(d['val'],s24_total):>6}  D {delta_str(d['val'], s23v)}")

print("\n[MARCAS S24]")
for br, d in sorted(s24_br.items(), key=lambda x: -x[1]['val']):
    s23v = s23_br.get(br, {}).get('val', 0)
    s23q = s23_br.get(br, {}).get('qty', 0)
    print(f"  {br:<20} {fmt(d['val']):>15}  {d['qty']:>5} un  {pct(d['val'],s24_total):>6}  D {delta_str(d['val'], s23v)}")

print("\n[TOP 30 PRODUTOS S24]")
top30 = sorted(s24_pr.items(), key=lambda x: -x[1]['val'])[:30]
for i, (prod, d) in enumerate(top30, 1):
    s23v = s23_pr.get(prod, {}).get('val', 0)
    s23q = s23_pr.get(prod, {}).get('qty', 0)
    print(f"  {i:>2}. {prod[:55]:<55} | {d['brand']:<12} | {d['qty']:>5} un | {fmt(d['val']):>14} | D {delta_str(d['val'], s23v)}")
    # Show channels for this product
    for ch, cd in sorted(d['channels'].items(), key=lambda x: -x[1]['val'])[:3]:
        print(f"        {ch:<33} {fmt(cd['val']):>13} ({cd['qty']} un)")

print("\n[HISTÓRICO JUN — S23+S24 somados]")
jun_total = s23_total + s24_total
print(f"  Total Junho (estimado): {fmt(jun_total)}")

print("\n[TICKET MÉDIO S24]")
if s24_orders > 0:
    ticket = s24_total / s24_orders
    print(f"  {fmt(ticket)} por pedido EOV")
