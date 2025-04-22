def test_update_product(self):
        """It should Update an existing Product"""
        # create a product to update
        test_product = ProductFactory()
        response = self.client.post(BASE_URL, json=test_product.serialize())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # update the product
        new_product = response.get_json()
        new_product["description"] = "unknown"
        response = self.client.put(f"{BASE_URL}/{new_product['id']}", json=new_product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_product = response.get_json()
        self.assertEqual(updated_product["description"], "unknown")

    def test_update_product_not_found(self):
        """It should Update an existing Product"""
        # create a product to update
        new_product = ProductFactory()
        response = self.client.put(f"{BASE_URL}/{new_product.id}", json=new_product.serialize())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
