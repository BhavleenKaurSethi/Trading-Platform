import React, { useState } from 'react';
import { Input, Button, Space } from 'antd';
import axios from 'axios';

const ReportingSharePrice = () => {
  const [shareId, setShareId] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);
    try {
      const response = await axios.get(
        'https://backend-7fft7bnqha-ts.a.run.app/report/2',
        {
          params: {
            share_id: shareId,
          },
        }
      );
      setImageUrl(response.data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <Space.Compact
          size="large"
          style={{
            marginBottom: '20px',
            display: 'flex',
            justifyContent: 'center',
            width: '60%',
          }}
        >
          <Input
            placeholder="share id"
            style={{ width: '25%' }}
            value={shareId}
            onChange={(e) => setShareId(e.target.value)}
          />
          <Button
            type="primary"
            onClick={handleDownload}
            loading={loading}
            style={{ width: '25%' }}
          >
            Display Image
          </Button>
        </Space.Compact>
      </div>
      <div style={{ textAlign: 'center' }}>
        {loading ? (
          <p>Loading image...</p>
        ) : (
          imageUrl && (
            <img
              src={imageUrl}
              alt="Description"
              style={{ maxWidth: '100%' }}
            />
          )
        )}
      </div>
    </>
  );
};

export default ReportingSharePrice;
