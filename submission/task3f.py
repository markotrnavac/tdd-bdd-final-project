def test_query_by_availability(self):
    """It should Query Products by availability"""
    products = self._create_products(10)
    available_products = [product for product in products if product.available is True]
    available_count = len(available_products)        
    # test for available
    response = self.client.get(
        BASE_URL, query_string={"available": "true"}
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    self.assertEqual(len(data), available_count)
    # check the data just to be sure
    for product in data:
        self.assertEqual(product["available"], True)
