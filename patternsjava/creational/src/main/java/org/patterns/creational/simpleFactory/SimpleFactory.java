package org.patterns.creational.simpleFactory;

// Simple Factory
// The simple factory is a way to abstract the object creation process.
// It's a relatively simple a pattern, but can go a long way to help make the
// design of a system flexible (especially combined with interfaces).

/**
 * simple product catalog item
 */
interface Product {
    public double getPrice();

    public String getName();
}

/**
 * Example implementation of a product
 */
class GroceryStoreProduct implements Product {
    double price;
    String name;

    public GroceryStoreProduct(double price, String name) {
        this.price = price;
        this.name = name;
    }

    @Override
    public double getPrice() {
        return this.price;

    }

    @Override
    public String getName() {
        return this.name;

    }

    @Override
    public String toString() {
        return String.format("Product: %s, Price: %.2f\n", this.getName(), this.getPrice());
    }
}

class ProductFactory {
    public static Product createProduct(double price, String name) {
        return new GroceryStoreProduct(price, name);
    }
}


public class SimpleFactory {
    public static void main(String[] args) {
        // create a product without having to include the class in our main function
        Product lettuce = ProductFactory.createProduct(3.99, "Lettuce");
        System.out.println("My grocery store catalog");
        System.out.println(lettuce);
    }
}
