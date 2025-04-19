import { createClient } from '@supabase/supabase-js'
import type { UserConfig } from './auth-config'
import { redirect } from 'next/navigation'
import Cookies from 'js-cookie'

let currentSupabaseClient: ReturnType<typeof createClient> | null = null;
let currentUser: UserConfig | null = null;

// Función para guardar la configuración del usuario
function saveUserConfig(user: UserConfig) {
  if (typeof window !== 'undefined') {
    Cookies.set('supabaseUser', JSON.stringify(user), { expires: 7 });
  }
}

// Función para cargar la configuración del usuario
function loadUserConfig(): UserConfig | null {
  if (typeof window !== 'undefined') {
    const savedUser = Cookies.get('supabaseUser');
    return savedUser ? JSON.parse(savedUser) : null;
  }
  return null;
}

// Inicializar el cliente al cargar la página
if (typeof window !== 'undefined') {
  const savedUser = loadUserConfig();
  if (savedUser) {
    currentUser = savedUser;
    currentSupabaseClient = createClient(savedUser.supabaseUrl, savedUser.supabaseKey);
  }
}

export function initializeSupabaseClient(user: UserConfig) {
  if (currentUser?.username === user.username) {
    return currentSupabaseClient;
  }

  currentSupabaseClient = createClient(user.supabaseUrl, user.supabaseKey);
  currentUser = user;
  saveUserConfig(user);
  
  return currentSupabaseClient;
}

export function isAuthenticated() {
  return !!(currentSupabaseClient && currentUser);
}

export function getCurrentSupabase() {
  if (!currentSupabaseClient || !currentUser) {
    const savedUser = loadUserConfig();
    if (savedUser) {
      currentUser = savedUser;
      currentSupabaseClient = createClient(savedUser.supabaseUrl, savedUser.supabaseKey);
      return { 
        supabase: currentSupabaseClient, 
        user: currentUser 
      };
    }
    redirect('/login');
  }
  return { 
    supabase: currentSupabaseClient, 
    user: currentUser 
  };
}

export function logout() {
  currentSupabaseClient = null;
  currentUser = null;
  if (typeof window !== 'undefined') {
    Cookies.remove('supabaseUser');
  }
}

// Types for our database tables
export type Sales = {
  id: string
  date: string
  product_id: string
  quantity: number
  price: number
  total: number
  created_at: string
}

export type Products = {
  id: string
  name: string
  category: string
  price: number
  stock: number
  created_at: string
}

export type Categories = {
  id: string
  name: string
  created_at: string
} 