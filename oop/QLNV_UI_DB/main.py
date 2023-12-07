from model import CongTy
from form import QlnvApp
if __name__ == '__main__':
    cty = CongTy('CT1', tenCty='Cong Ty 1')
    cty.loadDatabase()
    app = QlnvApp(cty)
    app.run()