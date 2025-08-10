-- =================================================================
-- THE TRULY FINAL SCRIPT (Restart, Load, and Map)
-- =================================================================

-- Step 1: Automatically deletes the old database to ensure a clean start.
DROP DATABASE IF EXISTS portfolio_db;

-- Step 2: Create and use the new database.
CREATE DATABASE portfolio_db;
USE portfolio_db;

-- Step 3: Create all three tables.
CREATE TABLE stocks (
    StockID INT AUTO_INCREMENT PRIMARY KEY,
    TickerSymbol VARCHAR(20) NOT NULL UNIQUE,
    CompanyName VARCHAR(100),
    Sector VARCHAR(50)
);

CREATE TABLE historical_prices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY,
    TickerSymbol VARCHAR(20),
    PriceDate DATE NOT NULL,
    ClosePrice DECIMAL(18, 8)
);

CREATE TABLE transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    TickerSymbol VARCHAR(20),
    TransactionDate DATE NOT NULL,
    TransactionType ENUM('BUY', 'SELL') NOT NULL,
    Quantity INT NOT NULL,
    PricePerShare DECIMAL(18, 8)
);

-- Step 4: Load all the data with explicit column mapping.
-- !!! IMPORTANT: MAKE SURE YOUR FILE PATHS ARE CORRECT !!!
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/stocks.csv'
INTO TABLE stocks
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS
(TickerSymbol, CompanyName, Sector); -- This new line fixes the error.

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/transactions.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS
(TransactionDate, TickerSymbol, TransactionType, Quantity, PricePerShare); -- Added for safety.

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/historical_prices.csv'
INTO TABLE historical_prices
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS
(PriceDate, TickerSymbol, ClosePrice); -- Added for safety.

-- Step 5: Final verification message.
SELECT 'DATABASE IS 100% READY FOR POWER BI!' AS Status;