import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  // Get the pathname of the request
  const path = request.nextUrl.pathname

  // Define public paths that don't require authentication
  const isPublicPath = path === '/login'

  // Get the user from cookies
  const currentUser = request.cookies.get('currentUser')

  // Redirect logic
  if (!isPublicPath && !currentUser) {
    // Redirect to login if trying to access protected route without being logged in
    const response = NextResponse.redirect(new URL('/login', request.url))
    response.cookies.delete('currentUser') // Clear any invalid cookies
    return response
  }

  if (isPublicPath && currentUser) {
    // Redirect to home if trying to access login while being logged in
    return NextResponse.redirect(new URL('/', request.url))
  }

  return NextResponse.next()
}

// Configure the paths that should be protected by the middleware
export const config = {
  matcher: [
    /*
     * Match all request paths except:
     * 1. /api routes
     * 2. /_next (Next.js internals)
     * 3. /fonts (inside /public)
     * 4. /icons (inside /public)
     * 5. all files inside /public (e.g. /favicon.ico)
     */
    '/((?!api|_next|fonts|icons|[\\w-]+\\.\\w+).*)',
  ],
} 