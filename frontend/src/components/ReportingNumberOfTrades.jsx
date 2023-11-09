import React from 'react';

const ReportingNumberOfTrades = () => {
  const imageUrl =
    'https://storage.googleapis.com/trading_platform/charts/trades_per_broker.png?Expires=1699542129&GoogleAccessId=storage%40trading-platform-404001.iam.gserviceaccount.com&Signature=WLFgVbS2yUfr%2FUc%2B49UNAHNQ%2B5QcaV4vBxoIh31zpHeQvyjCNTfXl0y4uY1ONSCiUd5ryfXKnxTb4DD4bt7zFHfXYERpz4BN9XSmF3AfFJMkTtbUmGR6VZ%2FFnji0ogXW1byuM0zEpHPGOR47stQkc1TypZ45w0fPgrneW4hpwcZXNrz0cJrUMCgk57UYs%2F11JjbsUnObWe8PCvKsa6FPXctwmOJKZSWuPSGqIsdYwThSHpTvdspRASqGnI8vrO9UL7pGxgguZ9FEIjrWHBmabuPT5E5TmRS9RY2NmZUbhtlQiOwmkLdHyGH0Y8fdVtCyxFUdadL9h73GQ%2B1loaSnrg%3D%3D';

  return (
    <div className="App">
      <h1>Image from URL</h1>
      <img src={imageUrl} alt="Description" style={{ maxWidth: '100%' }} />
    </div>
  );
};

export default ReportingNumberOfTrades;
