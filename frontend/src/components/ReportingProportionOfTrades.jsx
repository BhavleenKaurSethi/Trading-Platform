import React, { useState } from 'react';
import axios from 'axios';

const ReportingProportionOfTrades = () => {
  const [imageUrl, setImageUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.get(
        'https://backend-7fft7bnqha-ts.a.run.app/report/3'
      );
      setImageUrl(response.data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    handleDownload();
  }, []);

  return (
    <div style={{ display: 'flex', justifyContent: 'center' }}>
      {loading ? (
        <p>Loading image...</p>
      ) : (
        <img src={imageUrl} alt="Description" style={{ maxWidth: '100%' }} />
      )}
    </div>
  );
};

export default ReportingProportionOfTrades;
