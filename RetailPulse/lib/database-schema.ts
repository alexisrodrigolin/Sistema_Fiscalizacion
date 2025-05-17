export interface DailySales {
  id: number
  date: string
  invoiced_total: number
  non_invoiced_total: number
  invoiced_transactions: number
  non_invoiced_transactions: number
  cancelled_total: number
  cancelled_transactions: number
  cash_total: number
  card_total: number
  virtual_total: number
  cash_transactions: number
  card_transactions: number
  virtual_transactions: number
  created_at?: string
} 