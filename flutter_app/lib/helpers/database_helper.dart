import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  DatabaseHelper._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('pricesync.db');
    return _database!;
  }

  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(
      path,
      version: 1,
      onCreate: _createDB,
    );
  }

  Future<void> _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plu TEXT UNIQUE,
        plu2 TEXT,
        price REAL,
        brand TEXT,
        description TEXT,
        type TEXT,
        quantity REAL,
        unit TEXT,
        department TEXT,
        aisle TEXT,
        cost REAL,
        iva REAL,
        profit REAL,
        quantity1 INTEGER,
        price1 REAL,
        quantity2 INTEGER,
        price2 REAL,
        quantity3 INTEGER,
        price3 REAL,
        last_modified TEXT
      )
    ''');

    await db.execute('''
      CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        is_admin INTEGER
      )
    ''');
  }

  // Product operations
  Future<int> insertProduct(Map<String, dynamic> product) async {
    final db = await database;
    return await db.insert('products', product);
  }

  Future<int> updateProduct(Map<String, dynamic> product) async {
    final db = await database;
    return await db.update(
      'products',
      product,
      where: 'plu = ?',
      whereArgs: [product['plu']],
    );
  }

  Future<List<Map<String, dynamic>>> searchProduct(String query) async {
    final db = await database;
    return await db.query(
      'products',
      where: 'plu LIKE ? OR description LIKE ? OR brand LIKE ?',
      whereArgs: ['%$query%', '%$query%', '%$query%'],
    );
  }

  // User operations
  Future<bool> validateUser(String username, String password) async {
    final db = await database;
    final result = await db.query(
      'users',
      where: 'username = ? AND password = ?',
      whereArgs: [username, password],
    );
    return result.isNotEmpty;
  }

  Future<bool> isAdmin(String username) async {
    final db = await database;
    final result = await db.query(
      'users',
      where: 'username = ? AND is_admin = 1',
      whereArgs: [username],
    );
    return result.isNotEmpty;
  }
}
