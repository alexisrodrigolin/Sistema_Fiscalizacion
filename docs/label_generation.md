# Label Generation Documentation

## Overview

The label generation system in PriceSyncer allows users to create and print product labels with various layouts and special offer configurations.

## Label Types

1. **Quick Labels**
   - Standard product labels
   - Basic product information
   - Barcode
   - Price

2. **Special Offer Labels**
   - 1x1 Offers
   - 2x1 Offers
   - 4x1 Offers

## Label Components

### Standard Label Layout
```
+------------------------+
|      Product Name      |
|                        |
|      $XX.XX           |
|                        |
| [Barcode]             |
|                        |
| Product Code          |
+------------------------+
```

### Special Offer Layout
```
+------------------------+
|        OFERTA         |
|                        |
|   Product Name        |
|                        |
|   Now: $XX.XX        |
|   Before: $XX.XX     |
|                        |
|   Price per unit      |
|   Product Code        |
+------------------------+
```

## Technical Implementation

### Label Generation Process

1. **Data Collection**
   ```python
   def obtener_productos_seleccionados():
       # Collect selected products
       # Validate data
       # Format for label generation
   ```

2. **PDF Generation**
   ```python
   def eti(productos):
       # Create PDF canvas
       # Set up page layout
       # Generate labels
       # Save PDF
   ```

3. **Barcode Generation**
   ```python
   def generar_codigo_barras(codigo):
       # Generate barcode
       # Save as image
       # Return image path
   ```

### Configuration Options

1. **Page Layout**
   - A4 size
   - Landscape/Portrait
   - Margins
   - Label spacing

2. **Font Settings**
   - Title font
   - Price font
   - Description font
   - Code font

3. **Label Dimensions**
   - Width
   - Height
   - Border
   - Padding

## Special Features

### Price Formatting
- Automatic currency symbol
- Decimal places
- Thousands separator
- Price per unit calculation

### Barcode Support
- EAN-13
- UPC-A
- EAN-8
- Code128 (fallback)

### Special Offers
- Multiple quantity options
- Price calculations
- Before/After price display
- Unit price calculation

## Error Handling

1. **Input Validation**
   - Product data completeness
   - Price format
   - Barcode validity
   - Quantity validation

2. **Generation Errors**
   - PDF creation
   - Barcode generation
   - File system access
   - Printer communication

## Best Practices

1. **Label Design**
   - Clear hierarchy
   - Readable fonts
   - Proper spacing
   - Consistent layout

2. **Performance**
   - Batch processing
   - Image optimization
   - Memory management
   - File cleanup

3. **User Experience**
   - Preview option
   - Error messages
   - Progress indication
   - Print confirmation

## Configuration Options

### Label Templates
```python
label_templates = {
    'standard': {
        'title_size': 12,
        'price_size': 20,
        'code_size': 6,
        'margin': 1,
        'spacing': 0.5
    },
    'offer': {
        'title_size': 22,
        'price_size': 30,
        'code_size': 8,
        'margin': 1,
        'spacing': 0.5
    }
}
```

### Barcode Settings
```python
barcode_settings = {
    'ean13': {
        'width': 2.5,
        'height': 0.5,
        'font_size': 6
    },
    'code128': {
        'width': 3.0,
        'height': 0.5,
        'font_size': 6
    }
}
```

## Known Issues

1. **Performance**
   - Large batch processing
   - Memory usage
   - PDF generation time

2. **Compatibility**
   - Printer drivers
   - PDF viewers
   - Barcode scanners

3. **Layout**
   - Font scaling
   - Text wrapping
   - Image positioning

## Future Improvements

1. **Features**
   - Custom templates
   - Batch processing
   - Preview system
   - Print queue

2. **Performance**
   - Parallel processing
   - Caching
   - Optimization

3. **Compatibility**
   - More barcode types
   - Additional printers
   - Cross-platform support 