import { format } from "date-fns"
import { ArrowDownIcon, ArrowUpIcon, BarChart, DollarSign, FileCheck, FileX } from "lucide-react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { DailySales } from "@/lib/database-schema"

interface SalesOverviewProps {
  totalSales: number
  facturatedSales: number
  nonFacturatedSales: number
  avgDailySales: number
  highestSalesDay: DailySales | null
  dateRange?: { from: Date; to?: Date }
}

export function SalesOverview({
  totalSales,
  facturatedSales,
  nonFacturatedSales,
  avgDailySales,
  highestSalesDay,
  dateRange,
}: SalesOverviewProps) {
  // Calculate percentage change (mock data for demonstration)
  const percentChange = 12.5

  // Format the date display text based on whether it's a range or single date
  const getDateDisplayText = () => {
    if (!dateRange?.from) return "Select a date"

    if (dateRange.to && dateRange.from.getTime() !== dateRange.to.getTime()) {
      return `For period ${format(dateRange.from, "MMM d")} - ${format(dateRange.to, "MMM d, yyyy")}`
    }

    return `For ${format(dateRange.from, "MMMM d, yyyy")}`
  }

  // Calculate facturated percentage
  const facturationPercentage = totalSales > 0 ? Math.round((facturatedSales / totalSales) * 100) : 0

  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      <Card className="overflow-hidden border shadow-md card-hover">
        <CardHeader className="gradient-bg-1 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-white text-sm font-medium">
            TOTAL SALES REVENUE
            <DollarSign className="h-4 w-4 text-white/80" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold">
            ${totalSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <p className="text-xs text-muted-foreground">Combined invoiced and non-invoiced sales</p>
          <p className="text-xs text-muted-foreground mt-1">{getDateDisplayText()}</p>
        </CardContent>
      </Card>

      <Card className="overflow-hidden border shadow-md card-hover">
        <CardHeader className="gradient-bg-2 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-white text-sm font-medium">
            INVOICED SALES
            <FileCheck className="h-4 w-4 text-white/80" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold">
            ${facturatedSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-theme-secondary">{facturationPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-muted-foreground mt-1">Sales with formal invoices issued</p>
        </CardContent>
      </Card>

      <Card className="overflow-hidden border shadow-md card-hover">
        <CardHeader className="gradient-bg-3 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-white text-sm font-medium">
            NON-INVOICED SALES
            <FileX className="h-4 w-4 text-white/80" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold">
            ${nonFacturatedSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-muted-foreground">{100 - facturationPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-muted-foreground mt-1">Sales without formal invoices</p>
        </CardContent>
      </Card>

      <Card className="overflow-hidden border shadow-md card-hover">
        <CardHeader className="gradient-bg-4 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-white text-sm font-medium">
            AVERAGE DAILY REVENUE
            <BarChart className="h-4 w-4 text-white/80" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold">
            ${avgDailySales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            {percentChange > 0 ? (
              <ArrowUpIcon className="mr-1 h-3 w-3 text-theme-secondary" />
            ) : (
              <ArrowDownIcon className="mr-1 h-3 w-3 text-red-500" />
            )}
            <span className={`text-xs ${percentChange > 0 ? "text-theme-secondary" : "text-red-500"}`}>
              {Math.abs(percentChange)}% from previous period
            </span>
          </div>
          <p className="text-xs text-muted-foreground mt-1">Mean daily sales for selected period</p>
        </CardContent>
      </Card>
    </div>
  )
}
