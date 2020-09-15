from .Kinda import Kinda
from .model import db

def insert_data():
    k1 = Kinda('食物')
    k2 = Kinda('交通')
    k3 = Kinda('娛樂')
    k4 = Kinda('購物')
    k5 = Kinda('醫藥')
    k6 = Kinda('生活開銷')
    k7 = Kinda('定存')
    k8 = Kinda('收入')

    db.session.add_all([k1, k2, k3, k4, k5, k6, k7, k8])
    db.session.commit()
