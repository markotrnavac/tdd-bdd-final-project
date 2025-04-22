def test_list_all_products(self):
        """It should list all products from the database"""
        products = Product.all()
        self.assertEqual(len(products), 0)
        for _ in range(5):
            product = ProductFactory()
            product.create()
        products = Product.all()
        self.assertEqual(len(products), 5)
