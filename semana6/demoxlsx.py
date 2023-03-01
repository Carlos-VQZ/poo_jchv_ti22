
import pandas as pd

datos = {'SKU': ['172211', '172213', '172215', '172216'],
        'producto': ['gansito', 'nito', 'panque', 'alitas'],
        'Unidad de medida': ['gramos', 'gramos', 'gramos', 'gramos'],}
df = pd.DataFrame(datos)
df.to_excel('productos.xlsx', index=False)





