@app.route("/products", methods=["GET"])
def list_products():
    """Returns a list of Products"""
    app.logger.info("Request to list Products...")

    products = []
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        app.logger.info("Find by name: %s", name)
        products = Product.find_by_name(name)
    elif available:
        app.logger.info("Find by available: %s", available)
        # create bool from string
        available_value = available.lower() in ["true", "yes", "1"]
        products = Product.find_by_availability(available_value)
    else:
        app.logger.info("Find all")
        products = Product.all()

    results = [product.serialize() for product in products]
    app.logger.info("[%s] Products returned", len(results))
    return results, status.HTTP_200_OK
