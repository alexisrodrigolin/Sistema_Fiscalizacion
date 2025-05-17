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
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between px-4">
        <Link href="/" className="flex items-center gap-2">
          <ShoppingCart className="h-6 w-6 text-blue-600" />
          <div className="flex flex-col">
            <span className="font-bold text-xl hidden sm:block">RetailPulse</span>
            <span className="font-bold text-lg block sm:hidden">RP</span>
            <span className="text-xs text-muted-foreground hidden sm:block">Database: {databaseName}</span>
          </div>
        </Link>
        <div className="flex items-center gap-2 sm:gap-4">
          <div className="text-sm text-muted-foreground hidden sm:block">
            User: {userName}
          </div>
          <div className="text-sm text-muted-foreground block sm:hidden">
            {userName}
          </div>
          <button
            onClick={handleLogout}
            className="bg-red-600 hover:bg-red-700 text-white px-3 sm:px-4 py-2 rounded-lg text-sm font-medium transition-colors"
          >
            Sign Out
          </button>
        </div>
      </div>
    </header>
  )
}
