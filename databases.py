from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(Name, Price, Picture_link, Description):
	product_object = Product(
		Name = Name,
		Price = Price,
		Picture_link = Picture_link,
		Description = Description)
	session.add(product_object)
	session.commit()


def edit_product(id, Name):
	product_object = session.query(Product)
	filter_by(id=id).first()
	product_object.Name = Name
	session.commit()


def delete_product(their_id):
	session.query(Product).filter_by(id = their_id).delete()
	session.commit()


def query_all():
	products = session.query(Product).all()
	return products


def query_by_id(their_id):
	product = session.query(Product).filter_by(id = their_id).first()
	return product

def add_to_cart(productID):
	product=Cart(ProductID=productID)
	session.add(product)
	session.commit()


	
# add_product("Noa's Pouch","$20,000","pouch.jpg","The original pouch that Noa wore in her clip 'Pouch'")
# delete_product(1)