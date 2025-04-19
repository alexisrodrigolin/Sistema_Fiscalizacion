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
import { ChevronDown, Download, Search } from "lucide-react"
import { DailySales } from "@/lib/database-schema"

interface SalesTableProps {
  data: DailySales[]
}

export function SalesTable({ data }: SalesTableProps) {
  const [searchTerm, setSearchTerm] = useState("")
  const [visibleColumns, setVisibleColumns] = useState({
    date: true,
    total: true,
    invoiced: true,
    nonInvoiced: true,
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

  return (
    <Card className="border shadow-md">
      <CardHeader className="bg-gradient-to-r from-theme-primary/5 to-theme-secondary/5">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <CardTitle className="text-theme-dark">Sales Transactions</CardTitle>
            <CardDescription>Detailed daily sales information</CardDescription>
          </div>
          <div className="flex items-center gap-2">
            <div className="relative">
              <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                type="search"
                placeholder="Search by date..."
                className="pl-8 w-[200px] sm:w-[300px]"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="outline" className="ml-auto">
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
                  checked={visibleColumns.transactions}
                  onCheckedChange={() => toggleColumn("transactions")}
                >
                  Transactions
                </DropdownMenuCheckboxItem>
              </DropdownMenuContent>
            </DropdownMenu>
            <Button variant="outline" size="icon">
              <Download className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </CardHeader>
      <CardContent className="p-0">
        <div className="rounded-md">
          <Table>
            <TableHeader className="bg-muted/50">
              <TableRow>
                {visibleColumns.date && <TableHead>Date</TableHead>}
                {visibleColumns.total && <TableHead className="text-right">Total Sales</TableHead>}
                {visibleColumns.invoiced && <TableHead className="text-right">Invoiced</TableHead>}
                {visibleColumns.nonInvoiced && <TableHead className="text-right">Non-Invoiced</TableHead>}
                {visibleColumns.transactions && <TableHead className="text-right">Transactions</TableHead>}
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredData.length > 0 ? (
                filteredData.map((item, index) => (
                  <TableRow key={index} className="hover:bg-muted/30 transition-colors">
                    {visibleColumns.date && (
                      <TableCell className="font-medium">{format(new Date(item.date), "MMMM d, yyyy")}</TableCell>
                    )}
                    {visibleColumns.total && (
                      <TableCell className="text-right text-theme-primary font-medium">
                        ${(item.invoiced_total + item.non_invoiced_total).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                      </TableCell>
                    )}
                    {visibleColumns.invoiced && (
                      <TableCell className="text-right text-theme-secondary font-medium">
                        ${item.invoiced_total.toLocaleString("en-US", {
                          minimumFractionDigits: 2,
                          maximumFractionDigits: 2,
                        })}
                      </TableCell>
                    )}
                    {visibleColumns.nonInvoiced && (
                      <TableCell className="text-right text-theme-accent font-medium">
                        ${item.non_invoiced_total.toLocaleString("en-US", {
                          minimumFractionDigits: 2,
                          maximumFractionDigits: 2,
                        })}
                      </TableCell>
                    )}
                    {visibleColumns.transactions && (
                      <TableCell className="text-right">
                        {(item.invoiced_transactions + item.non_invoiced_transactions).toLocaleString()}
                        <span className="text-xs text-muted-foreground ml-1">
                          ({item.invoiced_transactions}/{item.non_invoiced_transactions})
                        </span>
                      </TableCell>
                    )}
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell
                    colSpan={Object.values(visibleColumns).filter(Boolean).length}
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
