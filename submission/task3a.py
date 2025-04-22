def test_get_product(self):
        """It should Read a Product"""
        test_product = self._create_products(1)[0]
        URL = f"{BASE_URL}/{test_product.id}"
        response = self.client.get(URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(data['name'], test_product.name)

    def test_get_product_not_found(self):
        """It should not Get a Product thats not found"""
        response = self.client.get(f"{BASE_URL}/0")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = response.get_json()
        self.assertIn("was not found", data["message"])
