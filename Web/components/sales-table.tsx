"use client"

import { useState } from "react"
import { format } from "date-fns"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ChevronDown, Download, Search, ChevronRight, CreditCard, Wallet, Smartphone } from "lucide-react"
import { DailySales } from "@/lib/database-schema"
import React from "react"

interface SalesTableProps {
  data: DailySales[]
}

export function SalesTable({ data }: SalesTableProps) {
  const [searchTerm, setSearchTerm] = useState("")
  const [expandedRow, setExpandedRow] = useState<number | null>(null)
  const [visibleColumns, setVisibleColumns] = useState({
    date: true,
    total: true,
    invoiced: true,
    nonInvoiced: true,
    cancelled: true,
    transactions: true,
  })

  // Filter data based on search term
  const filteredData = data.filter((item) =>
    format(new Date(item.date), "MMMM d, yyyy").toLowerCase().includes(searchTerm.toLowerCase()),
  )

  const toggleColumn = (column: keyof typeof visibleColumns) => {
    setVisibleColumns((prev) => ({
      ...prev,
      [column]: !prev[column],
    }))
  }

  const handleRowClick = (index: number) => {
    setExpandedRow(expandedRow === index ? null : index)
  }

  return (
    <Card className="border shadow-md">
      <CardHeader className="bg-gradient-to-r from-theme-primary/5 to-theme-secondary/5">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <CardTitle className="text-theme-dark">Sales Transactions</CardTitle>
            <CardDescription>Detailed daily sales information</CardDescription>
          </div>
          <div className="flex flex-col sm:flex-row items-center gap-2">
            <div className="relative w-full sm:w-auto">
              <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                type="search"
                placeholder="Search by date..."
                className="pl-8 w-full sm:w-[200px]"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <div className="flex items-center gap-2 w-full sm:w-auto">
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="outline" className="w-full sm:w-auto">
                    Columns <ChevronDown className="ml-2 h-4 w-4" />
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuCheckboxItem checked={visibleColumns.date} onCheckedChange={() => toggleColumn("date")}>
                    Date
                  </DropdownMenuCheckboxItem>
                  <DropdownMenuCheckboxItem checked={visibleColumns.total} onCheckedChange={() => toggleColumn("total")}>
                    Total Sales
                  </DropdownMenuCheckboxItem>
                  <DropdownMenuCheckboxItem
                    checked={visibleColumns.invoiced}
                    onCheckedChange={() => toggleColumn("invoiced")}
                  >
                    Invoiced Sales
                  </DropdownMenuCheckboxItem>
                  <DropdownMenuCheckboxItem
                    checked={visibleColumns.nonInvoiced}
                    onCheckedChange={() => toggleColumn("nonInvoiced")}
                  >
                    Non-Invoiced Sales
                  </DropdownMenuCheckboxItem>
                  <DropdownMenuCheckboxItem
                    checked={visibleColumns.cancelled}
                    onCheckedChange={() => toggleColumn("cancelled")}
                  >
                    Cancelled Sales
                  </DropdownMenuCheckboxItem>
                  <DropdownMenuCheckboxItem
                    checked={visibleColumns.transactions}
                    onCheckedChange={() => toggleColumn("transactions")}
                  >
                    Transactions
                  </DropdownMenuCheckboxItem>
                </DropdownMenuContent>
              </DropdownMenu>
              <Button variant="outline" size="icon" className="w-full sm:w-auto">
                <Download className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </CardHeader>
      <CardContent className="p-0">
        <div className="rounded-md overflow-x-auto">
          <Table>
            <TableHeader className="bg-muted/50">
              <TableRow>
                <TableHead className="w-[30px]"></TableHead>
                {visibleColumns.date && <TableHead>Date</TableHead>}
                {visibleColumns.total && <TableHead className="text-right">Total Sales</TableHead>}
                {visibleColumns.invoiced && <TableHead className="text-right">Invoiced</TableHead>}
                {visibleColumns.nonInvoiced && <TableHead className="text-right">Non-Invoiced</TableHead>}
                {visibleColumns.cancelled && <TableHead className="text-right">Cancelled</TableHead>}
                {visibleColumns.transactions && <TableHead className="text-right">Transactions</TableHead>}
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredData.length > 0 ? (
                filteredData.map((item, index) => (
                  <React.Fragment key={item.id}>
                    <TableRow 
                      className="hover:bg-muted/30 transition-colors cursor-pointer"
                      onClick={() => handleRowClick(index)}
                    >
                      <TableCell className="w-[30px]">
                        <ChevronRight 
                          className={`h-4 w-4 transition-transform ${expandedRow === index ? 'rotate-90' : ''}`} 
                        />
                      </TableCell>
                      {visibleColumns.date && (
                        <TableCell className="font-medium whitespace-nowrap">
                          {format(new Date(item.date), "MMMM d, yyyy")}
                        </TableCell>
                      )}
                      {visibleColumns.total && (
                        <TableCell className="text-right text-theme-primary font-medium whitespace-nowrap">
                          ${(item.invoiced_total + item.non_invoiced_total).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                        </TableCell>
                      )}
                      {visibleColumns.invoiced && (
                        <TableCell className="text-right text-theme-secondary font-medium whitespace-nowrap">
                          ${item.invoiced_total.toLocaleString("en-US", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2,
                          })}
                        </TableCell>
                      )}
                      {visibleColumns.nonInvoiced && (
                        <TableCell className="text-right text-theme-accent font-medium whitespace-nowrap">
                          ${item.non_invoiced_total.toLocaleString("en-US", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2,
                          })}
                        </TableCell>
                      )}
                      {visibleColumns.cancelled && (
                        <TableCell className="text-right text-red-500 whitespace-nowrap">
                          ${item.cancelled_total.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                          <span className="text-xs text-muted-foreground ml-1">
                            ({item.cancelled_transactions.toLocaleString()})
                          </span>
                        </TableCell>
                      )}
                      {visibleColumns.transactions && (
                        <TableCell className="text-right whitespace-nowrap">
                          {(item.invoiced_transactions + item.non_invoiced_transactions).toLocaleString()}
                          <span className="text-xs text-muted-foreground ml-1">
                            ({item.invoiced_transactions}/{item.non_invoiced_transactions})
                          </span>
                        </TableCell>
                      )}
                    </TableRow>
                    {expandedRow === index && (
                      <TableRow key={`${item.id}-expanded`} className="bg-muted/20">
                        <TableCell colSpan={Object.values(visibleColumns).filter(Boolean).length + 1}>
                          <div className="py-4 px-6">
                            <h4 className="text-sm font-medium mb-3">Payment Method Breakdown</h4>
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                              <div className="flex items-center justify-between p-3 rounded-lg bg-cyan-50">
                                <div className="flex items-center gap-2">
                                  <Wallet className="h-4 w-4 text-cyan-600" />
                                  <div>
                                    <p className="text-sm font-medium text-cyan-600">Cash</p>
                                    <p className="text-xs text-muted-foreground">{item.cash_transactions} transactions</p>
                                  </div>
                                </div>
                                <p className="text-sm font-medium text-cyan-600">
                                  ${item.cash_total.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                                </p>
                              </div>
                              <div className="flex items-center justify-between p-3 rounded-lg bg-purple-50">
                                <div className="flex items-center gap-2">
                                  <CreditCard className="h-4 w-4 text-purple-600" />
                                  <div>
                                    <p className="text-sm font-medium text-purple-600">Card</p>
                                    <p className="text-xs text-muted-foreground">{item.card_transactions} transactions</p>
                                  </div>
                                </div>
                                <p className="text-sm font-medium text-purple-600">
                                  ${item.card_total.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                                </p>
                              </div>
                              <div className="flex items-center justify-between p-3 rounded-lg bg-pink-50">
                                <div className="flex items-center gap-2">
                                  <Smartphone className="h-4 w-4 text-pink-600" />
                                  <div>
                                    <p className="text-sm font-medium text-pink-600">Virtual Pay</p>
                                    <p className="text-xs text-muted-foreground">{item.virtual_transactions} transactions</p>
                                  </div>
                                </div>
                                <p className="text-sm font-medium text-pink-600">
                                  ${item.virtual_total.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                                </p>
                              </div>
                            </div>
                          </div>
                        </TableCell>
                      </TableRow>
                    )}
                  </React.Fragment>
                ))
              ) : (
                <TableRow>
                  <TableCell
                    colSpan={Object.values(visibleColumns).filter(Boolean).length + 1}
                    className="h-24 text-center"
                  >
                    No results found.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  )
}
