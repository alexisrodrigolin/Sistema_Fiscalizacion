import { getCurrentSupabase } from './supabase'
import { Sales, Products, Categories } from './supabase'
import { DailySales } from './database-schema'

// Fetch sales data from Supabase
export async function getSalesData(startDate: string, endDate: string) {
  const { supabase } = getCurrentSupabase()
  
  const { data, error } = await supabase
    .from('sales')
    .select(`
      *,
      products (
        name,
        category
      )
    `)
    .gte('date', startDate)
    .lte('date', endDate)
    .order('date', { ascending: true })

  if (error) {
    console.error('Error fetching sales data:', error)
    throw error
  }

  return data
}

// Fetch products data from Supabase
export async function getProducts() {
  const { supabase } = getCurrentSupabase()

  const { data, error } = await supabase
    .from('products')
    .select('*')
    .order('name')

  if (error) {
    console.error('Error fetching products:', error)
    throw error
  }

  return data
}

// Fetch categories data from Supabase
export async function getCategories() {
  const { supabase } = getCurrentSupabase()

  const { data, error } = await supabase
    .from('categories')
    .select('*')
    .order('name')

  if (error) {
    console.error('Error fetching categories:', error)
    throw error
  }

  return data
}

// Insert new sale
export async function insertSale(sale: any) {
  const { supabase } = getCurrentSupabase()

  const { data, error } = await supabase
    .from('sales')
    .insert([sale])
    .select()

  if (error) {
    console.error('Error inserting sale:', error)
    throw error
  }

  return data[0]
}

// Update product stock
export async function updateProductStock(productId: string, newStock: number) {
  const { supabase } = getCurrentSupabase()

  const { data, error } = await supabase
    .from('products')
    .update({ stock: newStock })
    .eq('id', productId)
    .select()

  if (error) {
    console.error('Error updating product stock:', error)
    throw error
  }

  return data[0]
}

// Fetch daily sales data from Supabase
export async function getDailySales(startDate: string, endDate: string) {
  const { supabase } = getCurrentSupabase()
  console.log('Querying with dates:', { startDate, endDate })

  const { data, error } = await supabase
    .from('daily_sales')
    .select('*')
    .gte('date', startDate)
    .lte('date', endDate)
    .order('date', { ascending: true })

  if (error) {
    console.error('Error fetching daily sales data:', error)
    throw error
  }

  // Ensure all required fields are present, defaulting to 0 or empty string for missing fields
  const processedData = data.map(item => ({
    id: Number(item.id) || 0,
    date: String(item.date) || '',
    invoiced_total: Number(item.invoiced_total) || 0,
    non_invoiced_total: Number(item.non_invoiced_total) || 0,
    invoiced_transactions: Number(item.invoiced_transactions) || 0,
    non_invoiced_transactions: Number(item.non_invoiced_transactions) || 0,
    cancelled_total: Number(item.cancelled_total) || 0,
    cancelled_transactions: Number(item.cancelled_transactions) || 0,
    cash_total: Number(item.cash_total) || 0,
    card_total: Number(item.card_total) || 0,
    virtual_total: Number(item.virtual_total) || 0,
    cash_transactions: Number(item.cash_transactions) || 0,
    card_transactions: Number(item.card_transactions) || 0,
    virtual_transactions: Number(item.virtual_transactions) || 0,
    created_at: item.created_at ? String(item.created_at) : undefined,
  }))

  console.log('Processed data from Supabase:', processedData)
  return processedData
}

// Insert new daily sales record
export async function insertDailySales(sale: Omit<DailySales, 'id' | 'created_at'>) {
  const { supabase } = getCurrentSupabase()

  const { data, error } = await supabase
    .from('daily_sales')
    .insert([sale])
    .select()

  if (error) {
    console.error('Error inserting daily sales:', error)
    throw error
  }

  return data[0]
}

// Update daily sales record
export async function updateDailySales(date: string, sale: Partial<DailySales>) {
  const { supabase } = getCurrentSupabase()

  const { data, error } = await supabase
    .from('daily_sales')
    .update(sale)
    .eq('date', date)
    .select()

  if (error) {
    console.error('Error updating daily sales:', error)
    throw error
  }

  return data[0]
}
