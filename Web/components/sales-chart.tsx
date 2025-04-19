"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { format } from "date-fns"
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
  type TooltipProps,
} from "recharts"
import type { NameType, ValueType } from "recharts/types/component/DefaultTooltipContent"
import { DailySales } from "@/lib/database-schema"

interface SalesChartProps {
  data: DailySales[]
}

export function SalesChart({ data }: SalesChartProps) {
  // Format data for the chart
  const chartData = data.map((item) => ({
    date: format(new Date(item.date), "MMM dd"),
    Total: item.invoiced_total + item.non_invoiced_total,
    Invoiced: item.invoiced_total,
    "Non-Invoiced": item.non_invoiced_total,
  }))

  // Custom tooltip
  const CustomTooltip = ({ active, payload, label }: TooltipProps<ValueType, NameType>) => {
    if (active && payload && payload.length) {
      return (
        <div className="rounded-lg border bg-background p-2 shadow-sm">
          <div className="font-bold">{label}</div>
          <div className="text-theme-primary">
            Total: ${payload[0].value?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
          </div>
          <div className="text-theme-secondary">
            Invoiced: ${payload[1].value?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
          </div>
          <div className="text-theme-accent">
            Non-Invoiced: ${payload[2].value?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
          </div>
        </div>
      )
    }
    return null
  }

  return (
    <Card className="overflow-hidden border shadow-md card-hover">
      <CardHeader className="bg-gradient-to-r from-theme-primary/10 to-theme-secondary/10 pb-6">
        <CardTitle className="text-xl text-theme-dark">Daily Sales (Last 7 Days)</CardTitle>
        <CardDescription>Total, invoiced, and non-invoiced sales</CardDescription>
      </CardHeader>
      <CardContent className="pl-2 pt-6">
        <div className="h-[300px]">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={chartData}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
              <XAxis
                dataKey="date"
                tick={{ fontSize: 12 }}
                tickLine={false}
                axisLine={false}
                className="text-xs text-muted-foreground"
              />
              <YAxis
                tick={{ fontSize: 12 }}
                tickLine={false}
                axisLine={false}
                className="text-xs text-muted-foreground"
                tickFormatter={(value) => `$${value}`}
              />
              <Tooltip content={<CustomTooltip />} />
              <Legend />
              <Line
                type="monotone"
                dataKey="Total"
                stroke="#4f46e5"
                strokeWidth={2}
                dot={{ r: 4, fill: "#4f46e5", stroke: "#4f46e5" }}
                activeDot={{ r: 6, fill: "#4f46e5", stroke: "#ffffff" }}
              />
              <Line
                type="monotone"
                dataKey="Invoiced"
                stroke="#10b981"
                strokeWidth={2}
                dot={{ r: 4, fill: "#10b981", stroke: "#10b981" }}
              />
              <Line
                type="monotone"
                dataKey="Non-Invoiced"
                stroke="#f59e0b"
                strokeWidth={2}
                dot={{ r: 4, fill: "#f59e0b", stroke: "#f59e0b" }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  )
}
