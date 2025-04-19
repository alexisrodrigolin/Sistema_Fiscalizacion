"use client"

import { useState, useEffect, useMemo } from "react"
import { DatePickerWithRange } from "@/components/date-range-picker"
import { SalesOverview } from "@/components/sales-overview"
import { SalesChart } from "@/components/sales-chart"
import { SalesTable } from "@/components/sales-table"
import { subDays } from "date-fns"
import type { DateRange } from "react-day-picker"
import { getDailySales } from "@/lib/data"
import { DailySales } from "@/lib/database-schema"

export function SalesDashboard() {
  // Memoize today's date so it doesn't change on every render
  const today = useMemo(() => new Date(), [])

  // Default to today's date only (not a range)
  const [dateRange, setDateRange] = useState<DateRange | undefined>({
    from: today,
    to: today,
  })

  const [salesData, setSalesData] = useState<DailySales[]>([])
  const [last7DaysData, setLast7DaysData] = useState<DailySales[]>([])
  const [last30DaysData, setLast30DaysData] = useState<DailySales[]>([])
  const [loading, setLoading] = useState(true)

  // Fetch data based on selected date range
  useEffect(() => {
    async function fetchData() {
      setLoading(true)

      if (!dateRange?.from) {
        // If no date range is selected, don't fetch data
        setSalesData([])
        setLoading(false)
        return
      }

      // Use the selected date range
      const startDate = dateRange.from.toISOString().split('T')[0]
      // If it's a single date (from === to) or no end date, use the start date as end date
      const endDate = (dateRange.to || dateRange.from).toISOString().split('T')[0]

      console.log('Fetching data for range:', { startDate, endDate })

      try {
        const data = await getDailySales(startDate, endDate)
        console.log('Fetched data:', data)
        setSalesData(data)
      } catch (error) {
        console.error("Error fetching sales data:", error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [dateRange])

  // Always fetch the last 7 days data separately for the chart
  useEffect(() => {
    async function fetchLast7DaysData() {
      const last7DaysStart = subDays(new Date(), 6) // 6 days ago + today = 7 days
      const today = new Date()

      const startDate = last7DaysStart.toISOString().split('T')[0]
      const endDate = today.toISOString().split('T')[0]

      console.log('Fetching last 7 days data:', { startDate, endDate })

      try {
        const data = await getDailySales(startDate, endDate)
        console.log('Fetched last 7 days data:', data)
        setLast7DaysData(data)
      } catch (error) {
        console.error("Error fetching last 7 days data:", error)
      }
    }

    fetchLast7DaysData()
  }, [])

  // Always fetch the last 30 days data for the table
  useEffect(() => {
    async function fetchLast30DaysData() {
      const last30DaysStart = subDays(new Date(), 29)
      const today = new Date()

      const startDate = last30DaysStart.toISOString().split('T')[0]
      const endDate = today.toISOString().split('T')[0]

      console.log('Fetching last 30 days data:', { startDate, endDate })

      try {
        const data = await getDailySales(startDate, endDate)
        console.log('Fetched last 30 days data:', data)
        setLast30DaysData(data)
      } catch (error) {
        console.error("Error fetching last 30 days data:", error)
      }
    }

    fetchLast30DaysData()
  }, [])

  // Calculate totals for the filtered period
  const totalSales = salesData.reduce((sum, item) => 
    sum + item.invoiced_total + item.non_invoiced_total, 0)
  const invoicedSales = salesData.reduce((sum, item) => sum + item.invoiced_total, 0)
  const nonInvoicedSales = salesData.reduce((sum, item) => sum + item.non_invoiced_total, 0)
  const cancelledSales = salesData.reduce((sum, item) => sum + item.cancelled_total, 0)
  const cancelledTransactions = salesData.reduce((sum, item) => sum + item.cancelled_transactions, 0)

  // Calculate payment method totals
  const cashTotal = salesData.reduce((sum, item) => sum + item.cash_total, 0)
  const cardTotal = salesData.reduce((sum, item) => sum + item.card_total, 0)
  const virtualTotal = salesData.reduce((sum, item) => sum + item.virtual_total, 0)
  const cashTransactions = salesData.reduce((sum, item) => sum + item.cash_transactions, 0)
  const cardTransactions = salesData.reduce((sum, item) => sum + item.card_transactions, 0)
  const virtualTransactions = salesData.reduce((sum, item) => sum + item.virtual_transactions, 0)

  // Calculate average daily sales
  const avgDailySales = salesData.length > 0 ? totalSales / salesData.length : 0

  // Find highest sales day
  const highestSalesDay = salesData.length > 0
    ? salesData.reduce((prev, current) => 
        (prev.invoiced_total + prev.non_invoiced_total > current.invoiced_total + current.non_invoiced_total) 
          ? prev 
          : current)
    : null

  console.log('Calculated values:', {
    totalSales,
    invoicedSales,
    nonInvoicedSales,
    cancelledSales,
    cancelledTransactions,
    cashTotal,
    cardTotal,
    virtualTotal,
    cashTransactions,
    cardTransactions,
    virtualTransactions,
    avgDailySales,
    highestSalesDay,
    salesDataLength: salesData.length
  })

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <h1 className="text-3xl font-bold tracking-tight">Sales Dashboard</h1>
        <DatePickerWithRange dateRange={dateRange} setDateRange={setDateRange} />
      </div>

      <SalesOverview
        totalSales={totalSales}
        facturatedSales={invoicedSales}
        nonFacturatedSales={nonInvoicedSales}
        cancelledSales={cancelledSales}
        cancelledTransactions={cancelledTransactions}
        avgDailySales={avgDailySales}
        highestSalesDay={highestSalesDay}
        dateRange={dateRange}
        cashTotal={cashTotal}
        cardTotal={cardTotal}
        virtualTotal={virtualTotal}
        cashTransactions={cashTransactions}
        cardTransactions={cardTransactions}
        virtualTransactions={virtualTransactions}
      />

      <div className="w-full">
        <SalesChart data={last7DaysData} />
      </div>

      <SalesTable data={last30DaysData} />
    </div>
  )
}
