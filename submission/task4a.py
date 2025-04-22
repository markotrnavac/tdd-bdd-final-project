@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    """
    Reads a Product
    This endpoint will read a single Product based on the id provided in 
    the query parameter
    """
    app.logger.info("Request to Read a Product with id [%s]", product_id)
    
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    
    app.logger.info("Returning product: %s", product.name)
    return product.serialize(), status.HTTP_200_OK
