import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { SupabaseProvider } from '@/components/providers/supabase-provider'
import { ThemeProvider } from '@/components/theme-provider'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'RetailPulse',
  description: 'Modern retail management dashboard',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider
          attribute="class"
          defaultTheme="light"
          enableSystem={false}
          disableTransitionOnChange
        >
          <SupabaseProvider>
            <div className="min-h-screen bg-background">
              {/* Main content */}
              <main className="container px-4 py-6">
                {children}
              </main>
            </div>
          </SupabaseProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}
