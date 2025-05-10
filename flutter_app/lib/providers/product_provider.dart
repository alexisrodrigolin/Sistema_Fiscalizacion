import 'package:flutter/foundation.dart';
import '../helpers/database_helper.dart';

class ProductProvider with ChangeNotifier {
  List<Map<String, dynamic>> _products = [];
  Map<String, dynamic>? _selectedProduct;

  List<Map<String, dynamic>> get products => _products;
  Map<String, dynamic>? get selectedProduct => _selectedProduct;

  Future<void> searchProducts(String query) async {
    try {
      _products = await DatabaseHelper.instance.searchProduct(query);
      notifyListeners();
    } catch (e) {
      print('Search error: $e');
    }
  }

  Future<bool> updateProduct(Map<String, dynamic> product) async {
    try {
      final result = await DatabaseHelper.instance.updateProduct(product);
      if (result > 0) {
        await searchProducts(product['plu']);
        return true;
      }
      return false;
    } catch (e) {
      print('Update error: $e');
      return false;
    }
  }

  Future<bool> insertProduct(Map<String, dynamic> product) async {
    try {
      final result = await DatabaseHelper.instance.insertProduct(product);
      if (result > 0) {
        await searchProducts(product['plu']);
        return true;
      }
      return false;
    } catch (e) {
      print('Insert error: $e');
      return false;
    }
  }

  void selectProduct(Map<String, dynamic> product) {
    _selectedProduct = product;
    notifyListeners();
  }

  void clearSelection() {
    _selectedProduct = null;
    notifyListeners();
  }
}
