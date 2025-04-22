@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_products(product_id):
    """
    Delete a Product
    This endpoint will delete a Product based the id specified in the path
    """
    app.logger.info("Request to Delete a product with id [%s]", product_id)
    product = Product.find(product_id)
    if product:
        product.delete()
        return "", status.HTTP_204_NO_CONTENT
    return "", status.HTTP_404_NOT_FOUND
