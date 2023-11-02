import { React, useEffect, useState } from 'react';
import { Table } from 'antd';
import axios from 'axios';

const QueryBrokers = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    try {
      const response = await axios.get('http://localhost:8000/query/1');
      setData(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  }

  if (data.length === 0) {
    return <div>Loading...</div>;
  }

  const columns = data[0].map((columnName) => ({
    title: columnName,
    dataIndex: columnName,
    key: columnName,
    className: 'center-text',
  }));

  const dataSource = data.slice(1).map((row) => {
    const rowData = {};
    columns.forEach((column, index) => {
      rowData[column.dataIndex] = row[index];
    });
    return rowData;
  });

  return <Table dataSource={dataSource} columns={columns} />;
};

export default QueryBrokers;
