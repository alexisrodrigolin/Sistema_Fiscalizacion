"use client"

import { format } from "date-fns"
import { ArrowDownIcon, ArrowUpIcon, BarChart, DollarSign, FileCheck, FileX, XCircle, CreditCard, Wallet, Smartphone } from "lucide-react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { DailySales } from "@/lib/database-schema"

interface SalesOverviewProps {
  totalSales: number
  facturatedSales: number
  nonFacturatedSales: number
  cancelledSales: number
  cancelledTransactions: number
  avgDailySales: number
  highestSalesDay: DailySales | null
  dateRange?: { from: Date; to?: Date }
  cashTotal: number
  cardTotal: number
  virtualTotal: number
  cashTransactions: number
  cardTransactions: number
  virtualTransactions: number
}

export function SalesOverview({
  totalSales,
  facturatedSales,
  nonFacturatedSales,
  cancelledSales,
  cancelledTransactions,
  avgDailySales,
  highestSalesDay,
  dateRange,
  cashTotal,
  cardTotal,
  virtualTotal,
  cashTransactions,
  cardTransactions,
  virtualTransactions,
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

  // Calculate percentages
  const facturationPercentage = totalSales > 0 ? Math.round((facturatedSales / totalSales) * 100) : 0
  const nonFacturationPercentage = totalSales > 0 ? Math.round((nonFacturatedSales / totalSales) * 100) : 0
  const cancelledPercentage = totalSales > 0 ? Math.round((cancelledSales / totalSales) * 100) : 0
  const cashPercentage = totalSales > 0 ? Math.round((cashTotal / totalSales) * 100) : 0
  const cardPercentage = totalSales > 0 ? Math.round((cardTotal / totalSales) * 100) : 0
  const virtualPercentage = totalSales > 0 ? Math.round((virtualTotal / totalSales) * 100) : 0

  return (
    <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-8">
      {/* Total Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-900 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-white text-sm font-medium">
            TOTAL SALES REVENUE
            <DollarSign className="h-4 w-4 text-white/80" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${totalSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <p className="text-xs text-zinc-500">Combined invoiced and non-invoiced sales</p>
          <p className="text-xs text-zinc-500 mt-1">{getDateDisplayText()}</p>
        </CardContent>
      </Card>

      {/* Cash Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-100 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-zinc-900 text-sm font-medium">
            CASH SALES
            <Wallet className="h-4 w-4 text-zinc-700" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${cashTotal.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-zinc-600">{cashPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">{cashTransactions.toLocaleString()} cash transactions</p>
        </CardContent>
      </Card>

      {/* Card Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-100 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-zinc-900 text-sm font-medium">
            CARD SALES
            <CreditCard className="h-4 w-4 text-zinc-700" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${cardTotal.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-zinc-600">{cardPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">{cardTransactions.toLocaleString()} card transactions</p>
        </CardContent>
      </Card>

      {/* Virtual Pay Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-100 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-zinc-900 text-sm font-medium">
            VIRTUAL PAY
            <Smartphone className="h-4 w-4 text-zinc-700" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${virtualTotal.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-zinc-600">{virtualPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">{virtualTransactions.toLocaleString()} virtual transactions</p>
        </CardContent>
      </Card>

      {/* Invoiced Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-100 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-zinc-900 text-sm font-medium">
            INVOICED SALES
            <FileCheck className="h-4 w-4 text-zinc-700" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${facturatedSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-zinc-600">{facturationPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">Sales with formal invoices issued</p>
        </CardContent>
      </Card>

      {/* Non-Invoiced Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-100 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-zinc-900 text-sm font-medium">
            NON-INVOICED SALES
            <FileX className="h-4 w-4 text-zinc-700" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${nonFacturatedSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-zinc-600">{nonFacturationPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">Sales without formal invoices</p>
        </CardContent>
      </Card>

      {/* Average Daily Revenue Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-zinc-100 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-zinc-900 text-sm font-medium">
            AVERAGE DAILY REVENUE
            <BarChart className="h-4 w-4 text-zinc-700" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${avgDailySales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            {percentChange > 0 ? (
              <ArrowUpIcon className="mr-1 h-3 w-3 text-emerald-600" />
            ) : (
              <ArrowDownIcon className="mr-1 h-3 w-3 text-red-600" />
            )}
            <span className={`text-xs ${percentChange > 0 ? "text-emerald-600" : "text-red-600"}`}>
              {Math.abs(percentChange)}% from previous period
            </span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">Mean daily sales for selected period</p>
        </CardContent>
      </Card>

      {/* Cancelled Sales Card */}
      <Card className="overflow-hidden border shadow-sm card-hover lg:col-span-2">
        <CardHeader className="bg-red-500 pb-2">
          <CardTitle className="flex flex-row items-center justify-between space-y-0 text-white text-sm font-medium">
            CANCELLED SALES
            <XCircle className="h-4 w-4 text-white/80" />
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <div className="text-2xl font-bold text-zinc-900">
            ${cancelledSales.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </div>
          <div className="flex items-center pt-1">
            <span className="text-xs text-red-600">{cancelledPercentage}% of total sales</span>
          </div>
          <p className="text-xs text-zinc-500 mt-1">{cancelledTransactions.toLocaleString()} cancelled transactions</p>
        </CardContent>
      </Card>
    </div>
  )
}
