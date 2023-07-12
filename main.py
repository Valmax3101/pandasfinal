import pandas as pd
from data.platosRestaurante import platosPopulares

tablaPlatos= pd.DataFrame(platosPopulares)
print(tablaPlatos)