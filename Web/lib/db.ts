// Example database connection using Prisma ORM
// This file is commented out for preview purposes
// You would need to install @prisma/client and set up your schema.prisma file

// import { PrismaClient } from "@prisma/client"

// Create a singleton instance of PrismaClient
// const globalForPrisma = global as unknown as { prisma: PrismaClient }
// export const prisma = globalForPrisma.prisma || new PrismaClient()
// if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma

import { format } from "date-fns"

// Mock data generation for preview
function generateMockSalesData(startDate: Date, endDate: Date) {
  const days = []
  const currentDate = new Date(startDate)

  while (currentDate <= endDate) {
    const dayOfWeek = currentDate.getDay()
    const isWeekend = dayOfWeek === 0 || dayOfWeek === 6

    const baseTransactions = isWeekend
      ? Math.floor(Math.random() * (250 - 180 + 1) + 180)
      : Math.floor(Math.random() * (200 - 120 + 1) + 120)

    const avgTransactionValue = Math.floor(Math.random() * (60 - 30 + 1) + 30)

    // Split between facturated and non-facturated
    const facturationRatio = Math.floor(Math.random() * (85 - 65 + 1) + 65) / 100 // Between 65% and 85% is facturated
    const facturatedTransactions = Math.round(baseTransactions * facturationRatio)
    const nonFacturatedTransactions = baseTransactions - facturatedTransactions

    const facturatedTotal = Math.round(facturatedTransactions * avgTransactionValue * 100) / 100
    const nonFacturatedTotal = Math.round(nonFacturatedTransactions * avgTransactionValue * 100) / 100
    const total = facturatedTotal + nonFacturatedTotal

    days.push({
      id: `sale-${format(currentDate, "yyyyMMdd")}`,
      date: format(currentDate, "yyyy-MM-dd"),
      total,
      facturatedTotal,
      nonFacturatedTotal,
      transactions: baseTransactions,
      facturatedTransactions,
      nonFacturatedTransactions,
      salesDepartments: [
        {
          department: { name: "Groceries" },
          amount: Math.round(total * 0.42 * 100) / 100,
        },
        {
          department: { name: "Electronics" },
          amount: Math.round(total * 0.28 * 100) / 100,
        },
        {
          department: { name: "Home Goods" },
          amount: Math.round(total * 0.18 * 100) / 100,
        },
        {
          department: { name: "Clothing" },
          amount: Math.round(total * 0.12 * 100) / 100,
        },
      ],
    })

    currentDate.setDate(currentDate.getDate() + 1)
  }

  return days
}

// Example function to fetch sales data - returns mock data for preview
export async function getSalesData(startDate: Date, endDate: Date) {
  // In a real implementation, this would query the database:
  // return await prisma.sales.findMany({...})

  // For preview, return mock data:
  return generateMockSalesData(startDate, endDate)
}

// Example function to create a new sales record - mocked for preview
export async function createSalesRecord(data: {
  date: Date
  total: number
  facturatedTotal: number
  nonFacturatedTotal: number
  transactions: number
  facturatedTransactions: number
  nonFacturatedTransactions: number
  storeId: string
  departmentSales: Array<{
    departmentId: string
    amount: number
  }>
}) {
  // In a real implementation, this would create a record:
  // return await prisma.sales.create({...})

  // For preview, just return the data:
  return {
    id: `sale-${format(data.date, "yyyyMMdd")}`,
    date: data.date,
    total: data.total,
    facturatedTotal: data.facturatedTotal,
    nonFacturatedTotal: data.nonFacturatedTotal,
    transactions: data.transactions,
    facturatedTransactions: data.facturatedTransactions,
    nonFacturatedTransactions: data.nonFacturatedTransactions,
    storeId: data.storeId,
    salesDepartments: data.departmentSales.map((dept) => ({
      departmentId: dept.departmentId,
      amount: dept.amount,
      department: { name: `Department ${dept.departmentId}` },
    })),
  }
}
