import 'package:flutter/material.dart';

class ConfigScreen extends StatelessWidget {
  const ConfigScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Configurations'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                'Configuration Settings',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 20),
              // Add your configuration widgets here
              // For example:
              ListTile(
                leading: const Icon(Icons.settings_backup_restore),
                title: const Text('Server Address'),
                subtitle: const Text('Not configured'),
                trailing: IconButton(
                  icon: const Icon(Icons.edit),
                  onPressed: () {
                    // TODO: Implement server address configuration
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                          content: Text('Edit Server Address Tapped')),
                    );
                  },
                ),
              ),
              ListTile(
                leading: const Icon(Icons.print),
                title: const Text('Default Printer'),
                subtitle: const Text('Not selected'),
                trailing: IconButton(
                  icon: const Icon(Icons.edit),
                  onPressed: () {
                    // TODO: Implement printer selection
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text('Edit Printer Tapped')),
                    );
                  },
                ),
              ),
              // Add more configuration options as needed
            ],
          ),
        ),
      ),
    );
  }
}
