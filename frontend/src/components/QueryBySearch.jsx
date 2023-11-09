import React, { useState } from 'react';
import { Table, Input, Space, DatePicker, Button } from 'antd';
import axios from 'axios';

const QueryBySearch = () => {
  const [share_id, setShareId] = useState(null);
  const [broker_id, setBrokerId] = useState(null);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);

    try {
      const response = await axios.get(
        'https://backend-7fft7bnqha-ts.a.run.app/query/4',
        {
          params: {
            share_id: share_id ? share_id : undefined,
            broker_id: broker_id ? broker_id : undefined,
            date_range_min: startDate
              ? startDate.format('YYYY-MM-DD')
              : undefined,
            date_range_max: endDate ? endDate.format('YYYY-MM-DD') : undefined,
          },
        }
      );

      setData(response.data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  const columns = data[0]?.map((columnName) => ({
    title: columnName,
    dataIndex: columnName,
    key: columnName,
    className: 'center-text',
  }));

  const dataSource = data.slice(1).map((row) => {
    const rowData = {};
    columns?.forEach((column, index) => {
      rowData[column.dataIndex] = row[index];
    });
    return rowData;
  });

  return (
    <div style={{ textAlign: 'center' }}>
      <Space.Compact
        size="large"
        style={{ width: '80%', marginBottom: '20px' }}
      >
        <Input
          placeholder="share id"
          style={{ width: '20%' }}
          value={share_id}
          onChange={(e) => setShareId(e.target.value)}
        />
        <Input
          placeholder="broker id"
          style={{ width: '20%' }}
          value={broker_id}
          onChange={(e) => setBrokerId(e.target.value)}
        />
        <DatePicker
          onChange={(date, dateString) => setStartDate(date)}
          placeholder="start date"
          style={{ width: '20%' }}
        />
        <DatePicker
          onChange={(date, dateString) => setEndDate(date)}
          placeholder="end date"
          style={{ width: '20%' }}
        />
        <Button type="primary" onClick={handleSearch} style={{ width: '20%' }}>
          Search
        </Button>
      </Space.Compact>
      {loading ? (
        <div>Loading...</div>
      ) : (
        data.length > 0 && <Table dataSource={dataSource} columns={columns} />
      )}
    </div>
  );
};

export default QueryBySearch;
