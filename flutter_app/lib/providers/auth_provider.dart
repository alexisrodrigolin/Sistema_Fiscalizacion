import 'package:flutter/foundation.dart';
import '../helpers/database_helper.dart';

class AuthProvider with ChangeNotifier {
  bool _isAuthenticated = false;
  bool _isAdmin = false;
  String? _currentUser;

  bool get isAuthenticated => _isAuthenticated;
  bool get isAdmin => _isAdmin;
  String? get currentUser => _currentUser;

  Future<bool> login(String username, String password) async {
    try {
      final isValid =
          await DatabaseHelper.instance.validateUser(username, password);
      if (isValid) {
        _isAuthenticated = true;
        _currentUser = username;
        _isAdmin = await DatabaseHelper.instance.isAdmin(username);
        notifyListeners();
        return true;
      }
      return false;
    } catch (e) {
      print('Login error: $e');
      return false;
    }
  }

  void logout() {
    _isAuthenticated = false;
    _isAdmin = false;
    _currentUser = null;
    notifyListeners();
  }
}
