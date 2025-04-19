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
        setError('Invalid username or password')
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
      if (!supabaseClient) {
        setError('Error initializing client')
        setIsLoading(false)
        return
      }
      
      // Test the connection
      const { error: supabaseError } = await supabaseClient.from('daily_sales').select('count').single()
      
      if (supabaseError && supabaseError.code !== 'PGRST116') {
        console.error('Supabase connection error:', supabaseError)
        setError('Database connection error')
        setIsLoading(false)
        return
      }

      // Force a router refresh to update the middleware state
      router.refresh()
      
      // Redirect to dashboard
      router.push('/')
    } catch (error) {
      console.error('Login error:', error)
      setError('Login error')
      setIsLoading(false)
    }
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-primary/10 via-white to-primary/5">
      <div className="mb-12 text-center">
        <h1 className="text-7xl font-extrabold text-primary mb-4 bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary/70">
          RetailPulse
        </h1>
        <p className="text-xl text-gray-600 font-medium">
          Your Retail Management Platform
        </p>
      </div>
      <div className="w-full max-w-md space-y-8 rounded-xl bg-white/80 backdrop-blur-sm p-8 shadow-xl border border-primary/10">
        <div>
          <h2 className="text-center text-3xl font-bold tracking-tight text-gray-900">
            Sign In
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4 rounded-md shadow-sm">
            <div>
              <label htmlFor="username" className="sr-only">
                Username
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="relative block w-full rounded-lg border-0 p-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                disabled={isLoading}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="relative block w-full rounded-lg border-0 p-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6"
                placeholder="Password"
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
              className="group relative flex w-full justify-center rounded-lg bg-primary px-4 py-3 text-sm font-semibold text-white hover:bg-primary/90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
              disabled={isLoading}
            >
              {isLoading ? 'Signing in...' : 'Sign In'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
} 