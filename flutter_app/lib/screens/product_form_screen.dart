import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/product_provider.dart';

class ProductFormScreen extends StatefulWidget {
  final Map<String, dynamic>? product;

  const ProductFormScreen({super.key, this.product});

  @override
  State<ProductFormScreen> createState() => _ProductFormScreenState();
}

class _ProductFormScreenState extends State<ProductFormScreen> {
  final _formKey = GlobalKey<FormState>();
  final _pluController = TextEditingController();
  final _plu2Controller = TextEditingController();
  final _priceController = TextEditingController();
  final _brandController = TextEditingController();
  final _descriptionController = TextEditingController();
  final _typeController = TextEditingController();
  final _quantityController = TextEditingController();
  final _unitController = TextEditingController();
  final _departmentController = TextEditingController();
  final _aisleController = TextEditingController();
  final _costController = TextEditingController();
  final _ivaController = TextEditingController();
  final _profitController = TextEditingController();
  final _quantity1Controller = TextEditingController();
  final _price1Controller = TextEditingController();
  final _quantity2Controller = TextEditingController();
  final _price2Controller = TextEditingController();
  final _quantity3Controller = TextEditingController();
  final _price3Controller = TextEditingController();

  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    if (widget.product != null) {
      _pluController.text = widget.product!['plu'] ?? '';
      _plu2Controller.text = widget.product!['plu2'] ?? '';
      _priceController.text = widget.product!['price']?.toString() ?? '';
      _brandController.text = widget.product!['brand'] ?? '';
      _descriptionController.text = widget.product!['description'] ?? '';
      _typeController.text = widget.product!['type'] ?? '';
      _quantityController.text = widget.product!['quantity']?.toString() ?? '';
      _unitController.text = widget.product!['unit'] ?? '';
      _departmentController.text = widget.product!['department'] ?? '';
      _aisleController.text = widget.product!['aisle'] ?? '';
      _costController.text = widget.product!['cost']?.toString() ?? '';
      _ivaController.text = widget.product!['iva']?.toString() ?? '';
      _profitController.text = widget.product!['profit']?.toString() ?? '';
      _quantity1Controller.text =
          widget.product!['quantity1']?.toString() ?? '';
      _price1Controller.text = widget.product!['price1']?.toString() ?? '';
      _quantity2Controller.text =
          widget.product!['quantity2']?.toString() ?? '';
      _price2Controller.text = widget.product!['price2']?.toString() ?? '';
      _quantity3Controller.text =
          widget.product!['quantity3']?.toString() ?? '';
      _price3Controller.text = widget.product!['price3']?.toString() ?? '';
    }
  }

  @override
  void dispose() {
    _pluController.dispose();
    _plu2Controller.dispose();
    _priceController.dispose();
    _brandController.dispose();
    _descriptionController.dispose();
    _typeController.dispose();
    _quantityController.dispose();
    _unitController.dispose();
    _departmentController.dispose();
    _aisleController.dispose();
    _costController.dispose();
    _ivaController.dispose();
    _profitController.dispose();
    _quantity1Controller.dispose();
    _price1Controller.dispose();
    _quantity2Controller.dispose();
    _price2Controller.dispose();
    _quantity3Controller.dispose();
    _price3Controller.dispose();
    super.dispose();
  }

  Future<void> _saveProduct() async {
    if (_formKey.currentState!.validate()) {
      setState(() => _isLoading = true);

      final product = {
        'plu': _pluController.text,
        'plu2': _plu2Controller.text,
        'price': double.tryParse(_priceController.text) ?? 0.0,
        'brand': _brandController.text,
        'description': _descriptionController.text,
        'type': _typeController.text,
        'quantity': double.tryParse(_quantityController.text) ?? 0.0,
        'unit': _unitController.text,
        'department': _departmentController.text,
        'aisle': _aisleController.text,
        'cost': double.tryParse(_costController.text) ?? 0.0,
        'iva': double.tryParse(_ivaController.text) ?? 0.0,
        'profit': double.tryParse(_profitController.text) ?? 0.0,
        'quantity1': int.tryParse(_quantity1Controller.text) ?? 0,
        'price1': double.tryParse(_price1Controller.text) ?? 0.0,
        'quantity2': int.tryParse(_quantity2Controller.text) ?? 0,
        'price2': double.tryParse(_price2Controller.text) ?? 0.0,
        'quantity3': int.tryParse(_quantity3Controller.text) ?? 0,
        'price3': double.tryParse(_price3Controller.text) ?? 0.0,
      };

      final productProvider =
          Provider.of<ProductProvider>(context, listen: false);
      final success = widget.product != null
          ? await productProvider.updateProduct(product)
          : await productProvider.insertProduct(product);

      setState(() => _isLoading = false);

      if (success && mounted) {
        Navigator.of(context).pop();
      } else if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Error saving product')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.product != null ? 'Edit Product' : 'New Product'),
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Form(
                key: _formKey,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    TextFormField(
                      controller: _pluController,
                      decoration: const InputDecoration(labelText: 'PLU'),
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter a PLU';
                        }
                        return null;
                      },
                    ),
                    TextFormField(
                      controller: _plu2Controller,
                      decoration: const InputDecoration(labelText: 'PLU 2'),
                    ),
                    TextFormField(
                      controller: _priceController,
                      decoration: const InputDecoration(labelText: 'Price'),
                      keyboardType: TextInputType.number,
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter a price';
                        }
                        if (double.tryParse(value) == null) {
                          return 'Please enter a valid number';
                        }
                        return null;
                      },
                    ),
                    TextFormField(
                      controller: _brandController,
                      decoration: const InputDecoration(labelText: 'Brand'),
                    ),
                    TextFormField(
                      controller: _descriptionController,
                      decoration:
                          const InputDecoration(labelText: 'Description'),
                      maxLines: 2,
                    ),
                    TextFormField(
                      controller: _typeController,
                      decoration:
                          const InputDecoration(labelText: 'Type/Sabor'),
                    ),
                    TextFormField(
                      controller: _quantityController,
                      decoration: const InputDecoration(labelText: 'Quantity'),
                      keyboardType: TextInputType.number,
                    ),
                    TextFormField(
                      controller: _unitController,
                      decoration: const InputDecoration(labelText: 'Unit'),
                    ),
                    TextFormField(
                      controller: _departmentController,
                      decoration:
                          const InputDecoration(labelText: 'Department'),
                    ),
                    TextFormField(
                      controller: _aisleController,
                      decoration: const InputDecoration(labelText: 'Aisle'),
                    ),
                    TextFormField(
                      controller: _costController,
                      decoration: const InputDecoration(labelText: 'Cost'),
                      keyboardType: TextInputType.number,
                    ),
                    TextFormField(
                      controller: _ivaController,
                      decoration: const InputDecoration(labelText: 'IVA'),
                      keyboardType: TextInputType.number,
                    ),
                    TextFormField(
                      controller: _profitController,
                      decoration: const InputDecoration(labelText: 'Profit %'),
                      keyboardType: TextInputType.number,
                    ),
                    const Divider(),
                    const Text('Price by Quantity',
                        style: TextStyle(fontSize: 18)),
                    Row(
                      children: [
                        Expanded(
                          child: TextFormField(
                            controller: _quantity1Controller,
                            decoration:
                                const InputDecoration(labelText: 'Quantity 1'),
                            keyboardType: TextInputType.number,
                          ),
                        ),
                        Expanded(
                          child: TextFormField(
                            controller: _price1Controller,
                            decoration:
                                const InputDecoration(labelText: 'Price 1'),
                            keyboardType: TextInputType.number,
                          ),
                        ),
                      ],
                    ),
                    Row(
                      children: [
                        Expanded(
                          child: TextFormField(
                            controller: _quantity2Controller,
                            decoration:
                                const InputDecoration(labelText: 'Quantity 2'),
                            keyboardType: TextInputType.number,
                          ),
                        ),
                        Expanded(
                          child: TextFormField(
                            controller: _price2Controller,
                            decoration:
                                const InputDecoration(labelText: 'Price 2'),
                            keyboardType: TextInputType.number,
                          ),
                        ),
                      ],
                    ),
                    Row(
                      children: [
                        Expanded(
                          child: TextFormField(
                            controller: _quantity3Controller,
                            decoration:
                                const InputDecoration(labelText: 'Quantity 3'),
                            keyboardType: TextInputType.number,
                          ),
                        ),
                        Expanded(
                          child: TextFormField(
                            controller: _price3Controller,
                            decoration:
                                const InputDecoration(labelText: 'Price 3'),
                            keyboardType: TextInputType.number,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 20),
                    ElevatedButton(
                      onPressed: _saveProduct,
                      child: const Text('Save'),
                    ),
                  ],
                ),
              ),
            ),
    );
  }
}
