import React, { useState } from 'react';
import {
  LaptopOutlined,
  NotificationOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme, Typography } from 'antd';
import QueryBrokers from './components/QueryBrokers';
import QueryShares from './components/QueryShares';
import QueryTrades from './components/QueryTrades';
import QueryBySearch from './components/QueryBySearch';
import ExportByShareId from './components/ExportByShareId';
import ExportByBrokerId from './components/ExportByBrokerId';
import ExportByDateRange from './components/ExportByDateRange';
import ReportingNumberOfTrades from './components/ReportingNumberOfTrades';
import ReportingSharePrice from './components/ReportingSharePrice';
import ReportingProportionOfTrades from './components/ReportingProportionOfTrades';

const { Title } = Typography;

const App = () => {
  const componentMapping = {
    queryBrokers: <QueryBrokers />,
    queryShares: <QueryShares />,
    queryTrades: <QueryTrades />,
    queryBySearch: <QueryBySearch />,
    exportByShareId: <ExportByShareId />,
    exportByBrokerId: <ExportByBrokerId />,
    exportByDateRange: <ExportByDateRange />,
    reportingNumberOfTrades: <ReportingNumberOfTrades />,
    reportingSharePrice: <ReportingSharePrice />,
    reportingProportionOfTrades: <ReportingProportionOfTrades />,
  };
  const [activeMenuItem, setActiveMenuItem] = useState(null);

  const { Header, Content, Footer, Sider } = Layout;

  const items = [
    {
      icon: <UserOutlined />,
      label: 'Query',
      children: [
        { key: 'queryBrokers', label: 'List all Brokers' },
        { key: 'queryShares', label: 'List all Shares' },
        { key: 'queryTrades', label: 'List all Trades' },
        { key: 'queryBySearch', label: 'Search for trade' },
      ],
    },
    {
      icon: <LaptopOutlined />,
      label: 'Export',
      children: [
        { key: 'exportByShareId', label: 'Fetch Trades by Share_id' },
        { key: 'exportByBrokerId', label: 'Fetch Trades by Broker_id' },
        { key: 'exportByDateRange', label: 'Fetch Trades by date_range' },
      ],
    },
    {
      icon: <NotificationOutlined />,
      label: 'Reporting',
      children: [
        {
          key: 'reportingNumberOfTrades',
          label: 'Number of trades per broker',
        },
        {
          key: 'reportingSharePrice',
          label: 'Share price history',
        },
        {
          key: 'reportingProportionOfTrades',
          label: ' Trades proportion on exchange',
        },
      ],
    },
  ];

  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const handleMenuItemClick = (e) => {
    setActiveMenuItem(e.key);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header
        style={{
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <Title level={2} style={{ color: '#ffffff' }}>
          Trading Platform
        </Title>
      </Header>
      <Content
        style={{
          padding: '0 50px',
        }}
      >
        <Breadcrumb
          style={{
            margin: '16px 0',
          }}
        >
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb>
        <Layout
          style={{
            padding: '24px 0',
            background: colorBgContainer,
            height: '95%',
          }}
        >
          <Sider
            style={{
              background: colorBgContainer,
            }}
            width={260}
          >
            <Menu
              mode="inline"
              selectedKeys={[activeMenuItem]}
              items={items}
              onClick={handleMenuItemClick}
              style={{
                height: '100%',
              }}
            />
          </Sider>
          <Content
            style={{
              padding: '0 24px',
              minHeight: 500,
            }}
          >
            {componentMapping[activeMenuItem]}
          </Content>
        </Layout>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        Trading Platform ©2023 Created by FDM
      </Footer>
    </Layout>
  );
};
export default App;
