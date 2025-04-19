export interface UserConfig {
  username: string;
  password: string;
  supabaseUrl: string;
  supabaseKey: string;
  databaseName: string;
}

export const users: UserConfig[] = [
  {
    username: "bin1282",
    password: "Super-1618",
    supabaseUrl: "https://usbhajiuifdwmbekrkln.supabase.co",
    supabaseKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzYmhhaml1aWZkd21iZWtya2xuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5ODI0NjEsImV4cCI6MjA2MDU1ODQ2MX0.xky26OY0WJzhKjOPALQnarGlpehVHJL5_HGzaVJdatA",
    databaseName: "SuperBIN"
  },
  {
    username: "Carolina1148",
    password: "Carolina-2025",
    supabaseUrl: "https://your-project-2.supabase.co",
    supabaseKey: "your-anon-key-2",
    databaseName: "SuperCAROLINA"
  },
  {
    username: "admin",
    password: "adminpass",
    supabaseUrl: "https://your-main-project.supabase.co",
    supabaseKey: "your-main-anon-key",
    databaseName: "Admin Central"
  }
];

export function getUser(username: string, password: string): UserConfig | null {
  if (password) {
    // Si se proporciona contraseña, verificar ambos
    return users.find(user => user.username === username && user.password === password) || null;
  }
  // Si no se proporciona contraseña, buscar solo por nombre de usuario
  return users.find(user => user.username === username) || null;
} 