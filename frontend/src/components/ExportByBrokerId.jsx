import React, { useState } from 'react';
import { Input, Space, Button } from 'antd';
import axios from 'axios';

const ExportByBrokerId = () => {
  const [broker_id, setBrokerId] = useState(null);
  const [loading, setLoading] = useState(false);

  const filename = 'trade_filtered_by_broker_id.csv';

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.get(
        'https://backend-7fft7bnqha-ts.a.run.app/export/2',
        {
          params: {
            broker_id: broker_id ? broker_id : undefined,
          },
        }
      );

      const downloadUrl = response.data;

      // Trigger the download using the URL returned by the backend
      const anchor = document.createElement('a');
      anchor.href = downloadUrl;
      anchor.setAttribute('download', filename); // Set the filename
      document.body.appendChild(anchor);
      anchor.click();
      document.body.removeChild(anchor); // Clean up the DOM
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center' }}>
      <Space.Compact
        size="large"
        style={{
          width: '60%',
          marginBottom: '20px',
          display: 'flex',
          justifyContent: 'center',
        }}
      >
        <Input
          placeholder="broker id"
          style={{ width: '25%' }}
          value={broker_id}
          onChange={(e) => setBrokerId(e.target.value)}
        />
        <Button
          type="primary"
          onClick={handleDownload}
          loading={loading}
          style={{ width: '25%' }}
        >
          Download CSV
        </Button>
      </Space.Compact>
      {loading && <div>downloading...</div>}
    </div>
  );
};

export default ExportByBrokerId;
