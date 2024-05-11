# Create your tests here.
from tests.domain.entities.test_Produto import *
from tests.domain.entities.test_Categoria import *
from tests.db.test_CategoriaDaoOrm import *
from tests.db.test_ProdutoDaoOrm import *
from tests.web.TestCategoriaView import *
from tests.web.TestCategoriaDetalhesView import *
from tests.web.TestProdutoByCategoriaView import *
from tests.web.TestProdutoDetalhesView import *
