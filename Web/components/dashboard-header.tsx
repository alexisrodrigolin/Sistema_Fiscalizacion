"use client"

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import Cookies from 'js-cookie'
import { ShoppingCart } from "lucide-react"
import Link from "next/link"
import { logout } from '@/lib/supabase'

export function DashboardHeader() {
  const [userName, setUserName] = useState<string>('')
  const [databaseName, setDatabaseName] = useState<string>('')
  const router = useRouter()

  useEffect(() => {
    const currentUser = Cookies.get('currentUser')
    if (currentUser) {
      const { username, databaseName } = JSON.parse(currentUser)
      setUserName(username)
      setDatabaseName(databaseName)
    }
  }, [])

  const handleLogout = () => {
    logout()
    Cookies.remove('currentUser')
    router.refresh()
    router.push('/login')
  }

  return (
    <header className="border-b bg-white shadow-sm">
      <div className="container mx-auto flex h-16 items-center px-4 sm:px-6">
        <Link href="/" className="flex items-center gap-2">
          <ShoppingCart className="h-6 w-6 text-blue-600" />
          <span className="font-bold text-gray-900">SuperMarket Analytics</span>
        </Link>
        <div className="ml-auto flex items-center gap-4">
          <p className="text-sm text-gray-600">
            Usuario: <span className="font-medium">{userName}</span> | Base de datos: <span className="font-medium">{databaseName}</span>
          </p>
          <button
            onClick={handleLogout}
            className="rounded-md bg-red-600 px-4 py-2 text-sm font-semibold text-white hover:bg-red-700 transition-colors"
          >
            Cerrar sesión
          </button>
        </div>
      </div>
    </header>
  )
}
