import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
// import 'package:flutter_app/providers/auth_provider.dart'; // Si lo necesitaras de nuevo
import 'package:flutter_app/providers/product_provider.dart'; // Corregido
// import 'package:flutter_app/screens/login_screen.dart';    // Si lo necesitaras de nuevo
// import 'package:flutter_app/screens/home_screen.dart';     // Si lo necesitaras de nuevo
import 'package:flutter_app/screens/config_screen.dart';    // Corregido

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        // ChangeNotifierProvider(create: (_) => AuthProvider()),
        ChangeNotifierProvider(create: (_) => ProductProvider()), 
      ],
      child: MaterialApp(
        title: 'PriceSync App', 
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: ConfigScreen(), 
      ),
    );
  }
}
