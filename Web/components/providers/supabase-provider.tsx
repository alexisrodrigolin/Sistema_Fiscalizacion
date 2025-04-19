"use client"

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Cookies from 'js-cookie'
import { getUser } from '@/lib/auth-config'
import { initializeSupabaseClient } from '@/lib/supabase'

export function SupabaseProvider({ children }: { children: React.ReactNode }) {
  const router = useRouter()

  useEffect(() => {
    const currentUserCookie = Cookies.get('currentUser')
    if (!currentUserCookie) {
      router.push('/login')
      return
    }

    try {
      const { username } = JSON.parse(currentUserCookie)
      // Recuperamos las credenciales completas del usuario
      const user = getUser(username, '') // Password is not needed here since we'll search by username only
      if (!user) {
        console.error('User not found in configuration')
        Cookies.remove('currentUser')
        router.push('/login')
        return
      }

      // Inicializamos el cliente de Supabase
      initializeSupabaseClient(user)
    } catch (error) {
      console.error('Error initializing Supabase client:', error)
      Cookies.remove('currentUser')
      router.push('/login')
    }
  }, [router])

  return <>{children}</>
} 