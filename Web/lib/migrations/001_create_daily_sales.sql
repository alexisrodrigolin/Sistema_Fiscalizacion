-- Drop the table if it exists
DROP TABLE IF EXISTS daily_sales;

-- Create daily_sales table
CREATE TABLE daily_sales (
    id BIGSERIAL PRIMARY KEY,
    date DATE NOT NULL,
    invoiced_total DECIMAL(10,2) NOT NULL DEFAULT 0,
    non_invoiced_total DECIMAL(10,2) NOT NULL DEFAULT 0,
    invoiced_transactions INTEGER NOT NULL DEFAULT 0,
    non_invoiced_transactions INTEGER NOT NULL DEFAULT 0,
    cancelled_total DECIMAL(10,2) NOT NULL DEFAULT 0,
    cancelled_transactions INTEGER NOT NULL DEFAULT 0,
    cash_total DECIMAL(10,2) NOT NULL DEFAULT 0,
    card_total DECIMAL(10,2) NOT NULL DEFAULT 0,
    virtual_total DECIMAL(10,2) NOT NULL DEFAULT 0,
    cash_transactions INTEGER NOT NULL DEFAULT 0,
    card_transactions INTEGER NOT NULL DEFAULT 0,
    virtual_transactions INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
    UNIQUE(date)
);

-- Create index on date for faster queries
CREATE INDEX idx_daily_sales_date ON daily_sales(date);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = TIMEZONE('utc'::text, NOW());
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create trigger to automatically update updated_at
CREATE TRIGGER update_daily_sales_updated_at
    BEFORE UPDATE ON daily_sales
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Insert sample data for the last 30 days
INSERT INTO daily_sales (
    date, 
    invoiced_total, 
    non_invoiced_total, 
    invoiced_transactions, 
    non_invoiced_transactions, 
    cancelled_total, 
    cancelled_transactions,
    cash_total,
    card_total,
    virtual_total,
    cash_transactions,
    card_transactions,
    virtual_transactions
)
VALUES 
    -- Today
    (CURRENT_DATE, 0.00, 2000.00, 0, 100, 260.00, 20, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- Yesterday
    (CURRENT_DATE - INTERVAL '1 day', 1500.00, 500.00, 75, 25, 180.00, 15, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 2 days ago
    (CURRENT_DATE - INTERVAL '2 days', 1800.00, 200.00, 90, 10, 150.00, 12, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 3 days ago
    (CURRENT_DATE - INTERVAL '3 days', 1600.00, 400.00, 80, 20, 200.00, 16, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 4 days ago
    (CURRENT_DATE - INTERVAL '4 days', 1400.00, 600.00, 70, 30, 220.00, 18, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 5 days ago
    (CURRENT_DATE - INTERVAL '5 days', 1200.00, 800.00, 60, 40, 240.00, 19, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 6 days ago
    (CURRENT_DATE - INTERVAL '6 days', 1000.00, 1000.00, 50, 50, 260.00, 21, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 7 days ago
    (CURRENT_DATE - INTERVAL '7 days', 800.00, 1200.00, 40, 60, 280.00, 23, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 8 days ago
    (CURRENT_DATE - INTERVAL '8 days', 600.00, 1400.00, 30, 70, 300.00, 25, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 9 days ago
    (CURRENT_DATE - INTERVAL '9 days', 400.00, 1600.00, 20, 80, 320.00, 27, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 10 days ago
    (CURRENT_DATE - INTERVAL '10 days', 200.00, 1800.00, 10, 90, 340.00, 29, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 11-20 days ago (similar pattern with variations)
    (CURRENT_DATE - INTERVAL '11 days', 1700.00, 300.00, 85, 15, 200.00, 16, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '12 days', 1500.00, 500.00, 75, 25, 220.00, 18, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '13 days', 1300.00, 700.00, 65, 35, 240.00, 20, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '14 days', 1100.00, 900.00, 55, 45, 260.00, 22, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '15 days', 900.00, 1100.00, 45, 55, 280.00, 24, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '16 days', 700.00, 1300.00, 35, 65, 300.00, 26, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '17 days', 500.00, 1500.00, 25, 75, 320.00, 28, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '18 days', 300.00, 1700.00, 15, 85, 340.00, 30, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '19 days', 100.00, 1900.00, 5, 95, 360.00, 32, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '20 days', 0.00, 2000.00, 0, 100, 380.00, 34, 600.00, 1000.00, 400.00, 30, 50, 20),
    -- 21-30 days ago (reverse pattern)
    (CURRENT_DATE - INTERVAL '21 days', 200.00, 1800.00, 10, 90, 360.00, 32, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '22 days', 400.00, 1600.00, 20, 80, 340.00, 30, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '23 days', 600.00, 1400.00, 30, 70, 320.00, 28, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '24 days', 800.00, 1200.00, 40, 60, 300.00, 26, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '25 days', 1000.00, 1000.00, 50, 50, 280.00, 24, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '26 days', 1200.00, 800.00, 60, 40, 260.00, 22, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '27 days', 1400.00, 600.00, 70, 30, 240.00, 20, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '28 days', 1600.00, 400.00, 80, 20, 220.00, 18, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '29 days', 1800.00, 200.00, 90, 10, 200.00, 16, 600.00, 1000.00, 400.00, 30, 50, 20),
    (CURRENT_DATE - INTERVAL '30 days', 2000.00, 0.00, 100, 0, 180.00, 14, 600.00, 1000.00, 400.00, 30, 50, 20)
ON CONFLICT (date) DO NOTHING; 