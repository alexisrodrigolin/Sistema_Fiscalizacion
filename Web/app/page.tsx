import { DashboardHeader } from "@/components/dashboard-header"
import { SalesDashboard } from "@/components/sales-dashboard"

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <DashboardHeader />
      <main className="flex-1 p-6 container mx-auto">
        <SalesDashboard />
      </main>
    </div>
  )
}
