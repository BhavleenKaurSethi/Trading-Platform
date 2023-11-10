import React, { useState } from 'react';
import axios from 'axios';

const ReportingNumberOfTrades = () => {
  const [imageUrl, setImageUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.get(
        'https://backend-7fft7bnqha-ts.a.run.app/report/1'
      );
      setImageUrl(response.data); // Assuming response.data is the image URL
    } catch (error) {
      console.error('Error:', error);
      // You can set an error message here if needed
    } finally {
      setLoading(false);
    }
  };

  // Call handleDownload when the component mounts
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

export default ReportingNumberOfTrades;
