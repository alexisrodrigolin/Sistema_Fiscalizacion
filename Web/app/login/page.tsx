"use client"

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { getUser } from '@/lib/auth-config'
import { initializeSupabaseClient } from '@/lib/supabase'
import Cookies from 'js-cookie'

export default function LoginPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setIsLoading(true)

    try {
      const user = getUser(username, password)
      if (!user) {
        setError('Usuario o contraseña incorrectos')
        setIsLoading(false)
        return
      }

      // Store user info in cookies (will expire in 7 days)
      Cookies.set('currentUser', JSON.stringify({
        username: user.username,
        databaseName: user.databaseName
      }), { expires: 7 })

      // Initialize Supabase client with user credentials
      const supabaseClient = initializeSupabaseClient(user)
      
      // Test the connection
      const { error: supabaseError } = await supabaseClient.from('daily_sales').select('count').single()
      
      if (supabaseError && supabaseError.code !== 'PGRST116') {
        console.error('Supabase connection error:', supabaseError)
        setError('Error al conectar con la base de datos')
        setIsLoading(false)
        return
      }

      // Force a router refresh to update the middleware state
      router.refresh()
      
      // Redirect to dashboard
      router.push('/')
    } catch (error) {
      console.error('Login error:', error)
      setError('Error al iniciar sesión')
      setIsLoading(false)
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <div className="w-full max-w-md space-y-8 rounded-lg bg-white p-6 shadow-lg">
        <div>
          <h2 className="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">
            Iniciar sesión
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4 rounded-md shadow-sm">
            <div>
              <label htmlFor="username" className="sr-only">
                Usuario
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6"
                placeholder="Usuario"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                disabled={isLoading}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Contraseña
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                disabled={isLoading}
              />
            </div>
          </div>

          {error && (
            <div className="text-center text-sm text-red-600">
              {error}
            </div>
          )}

          <div>
            <button
              type="submit"
              className="group relative flex w-full justify-center rounded-md bg-primary px-3 py-2 text-sm font-semibold text-white hover:bg-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-50 disabled:cursor-not-allowed"
              disabled={isLoading}
            >
              {isLoading ? 'Iniciando sesión...' : 'Iniciar sesión'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
} 