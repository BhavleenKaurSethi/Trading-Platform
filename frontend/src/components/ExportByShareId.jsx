import React from 'react';

const ExportByShareId = () => {
  const handleDownload = (url, filename) => {
    // Create a new anchor element
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = filename;
    document.body.appendChild(anchor);
    anchor.click(); // Trigger the download
    document.body.removeChild(anchor); // Clean up
  };

  // URL and filename you get from the backend
  const url =
    'https://storage.googleapis.com/trading_platform/csv/trade_filtered_by_date_range.csv?Expires=1699541976&GoogleAccessId=storage%40trading-platform-404001.iam.gserviceaccount.com&Signature=gt%2FaH3XqoaXbxC3tZQa42lFUZ4%2B9u8IS4UoQR49P72%2FdFZCAaaOUADgjhvuL6ofOPbtQryTyU6p0aigFg2cdARZfSQGrAvcbIQNsYBUjPmArRXaC%2FFXmyAIr5t9eA1e3EVXhfsDYQnr2clXyKExUiEVFsNqgOORDeLEGkL%2FKtE4d4znXWCoA2kfgUKOBCnN7EWuBs1M4KeEUbiL5GbjgIJrBNyg8PEyN9wsQ%2FY4OaC2VbkoRCsuMw103IZkUT32FzAcgx%2FbM5l3aHto3bty7QZrfuKmQGmFRyAyGYeNBPjLLc%2B5AhtnJmjcYlwpLElMn8czSWXaYoxe536ERFN2GIA%3D%3D';
  const filename = 'trade_filtered_by_share_id.csv';

  return (
    <div>
      <button onClick={() => handleDownload(url, filename)}>
        Download CSV
      </button>
    </div>
  );
};
export default ExportByShareId;
