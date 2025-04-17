# PriceSyncer

PriceSyncer is a comprehensive price management and label printing system designed for retail environments. It provides a user-friendly interface for managing product prices, generating labels, and handling special offers.

## Features

- User authentication system with different access levels
- Product price management
- Label generation and printing
- Special offer management (1x1, 2x1, 4x1 offers)
- Barcode generation
- Database integration
- Configuration management

## System Requirements

- Python 3.x
- Required Python packages:
  - tkinter
  - ttkbootstrap
  - reportlab
  - barcode
  - win32com (for Windows systems)

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Login
- Launch the application
- Enter username and password
- Different access levels:
  - Admin: Full access to all features
  - Regular user: Limited access to price management and label printing

### Price Management
- Access the price management interface
- Enter product details:
  - Code
  - PLU
  - Price
  - Brand
  - Description
  - Type/Flavor
  - Quantity
  - Unit
  - Department
  - Aisle
  - Cost
  - VAT
  - Profit margin

### Label Generation
- Select products for label printing
- Choose label type:
  - Quick label
  - Special offers (1x1, 2x1, 4x1)
- Generate and print labels

### Configuration
- Access configuration settings (admin only)
- Modify:
  - Entry password
  - Admin password
  - Database settings
  - Font settings

## File Structure

- `mainPrice.py`: Main application file
- `priceB.py`: Backend logic and database connection
- `README.md`: This documentation file

## Technical Details

### Main Components

1. **Main Application Class**
   - Handles GUI initialization
   - Manages user interface components
   - Controls application flow

2. **Price Management**
   - Product data entry
   - Price calculation
   - Data validation
   - Database integration

3. **Label Generation**
   - PDF generation
   - Barcode creation
   - Label layout management
   - Special offer formatting

4. **Configuration Management**
   - User authentication
   - System settings
   - Database configuration

### Database Integration

The application connects to a database to:
- Store product information
- Manage user accounts
- Track price changes
- Store configuration settings

### Security Features

- Password protection
- User access levels
- Data validation
- Error handling

## Error Handling

The application includes comprehensive error handling for:
- Database connection issues
- Invalid user input
- System configuration problems
- Label generation errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact the development team or open an issue in the repository. 