import React, { useState } from 'react';
import { DatePicker, Space, Button } from 'antd';
import axios from 'axios';

const ExportByBrokerId = () => {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [loading, setLoading] = useState(false);

  const filename = 'trade_filtered_by_broker_id.csv';

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.get(
        'https://backend-7fft7bnqha-ts.a.run.app/export/3',
        {
          params: {
            date_range_min: startDate
              ? startDate.format('YYYY-MM-DD')
              : undefined,
            date_range_max: endDate ? endDate.format('YYYY-MM-DD') : undefined,
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
          display: 'flex',
          justifyContent: 'center',
          width: '80%',
          marginBottom: '20px',
        }}
      >
        <DatePicker
          onChange={(date, dateString) => setStartDate(date)}
          placeholder="start date"
          style={{ width: '30%' }}
        />
        <DatePicker
          onChange={(date, dateString) => setEndDate(date)}
          placeholder="end date"
          style={{ width: '30%' }}
        />
        <Button
          type="primary"
          onClick={handleDownload}
          loading={loading}
          style={{ width: '20%' }}
        >
          Download CSV
        </Button>
      </Space.Compact>
      {loading && <div>downloading...</div>}
    </div>
  );
};

export default ExportByBrokerId;
