// This is a representation of the database schema
// You would implement this in your actual database system

/*
Table: sales
- id: UUID (primary key)
- date: DATE
- total: DECIMAL(10,2)
- transactions: INTEGER
- store_id: UUID (foreign key to stores table)
- created_at: TIMESTAMP
- updated_at: TIMESTAMP

Table: sales_departments
- id: UUID (primary key)
- sale_id: UUID (foreign key to sales table)
- department_id: UUID (foreign key to departments table)
- amount: DECIMAL(10,2)
- created_at: TIMESTAMP
- updated_at: TIMESTAMP

Table: departments
- id: UUID (primary key)
- name: VARCHAR(100)
- description: TEXT
- created_at: TIMESTAMP
- updated_at: TIMESTAMP

Table: stores
- id: UUID (primary key)
- name: VARCHAR(100)
- location: VARCHAR(255)
- created_at: TIMESTAMP
- updated_at: TIMESTAMP

Table: products
- id: UUID (primary key)
- name: VARCHAR(100)
- description: TEXT
- price: DECIMAL(10,2)
- department_id: UUID (foreign key to departments table)
- created_at: TIMESTAMP
- updated_at: TIMESTAMP

Table: sales_products
- id: UUID (primary key)
- sale_id: UUID (foreign key to sales table)
- product_id: UUID (foreign key to products table)
- quantity: INTEGER
- price_at_sale: DECIMAL(10,2)
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
*/

export type DailySales = {
  id: string
  date: string
  invoiced_total: number
  non_invoiced_total: number
  invoiced_transactions: number
  non_invoiced_transactions: number
  created_at: string
}

// SQL to create the table in Supabase:
/*
create table daily_sales (
  id uuid default uuid_generate_v4() primary key,
  date date not null unique,
  invoiced_total decimal(10,2) not null,
  non_invoiced_total decimal(10,2) not null,
  invoiced_transactions integer not null,
  non_invoiced_transactions integer not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
*/
