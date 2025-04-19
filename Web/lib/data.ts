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

  // Ensure all required fields are present, defaulting to 0 for cancelled fields if missing
  const processedData = data.map(item => ({
    ...item,
    cancelled_total: item.cancelled_total || 0,
    cancelled_transactions: item.cancelled_transactions || 0,
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
