"use client";

import React from "react";
import {
  Button,
  ConfigProvider,
  Space,
  Input,
  ColorPicker,
  Divider,
  theme,
  Dropdown,
  MenuProps,
  Typography
} from "antd";

const App: React.FC = () => {
  const { Search } = Input;

  const items: MenuProps["items"] = [
    {
      key: "1",
      label: "Woolworths"
    },
    {
      key: "2",
      label: "Coles"
    }
  ];

  return (
    <Space>
      <Search
        addonBefore="Do I Buy"
        placeholder="Cadbury Dairy Milk 400g"
        allowClear
        onSearch={(value) => console.log(value)}
      />
      <Dropdown
        menu={{
          items,
          selectable: true,
          defaultSelectedKeys: ["1"]
        }}
      >
        <Typography.Link>
          <Space>Any Store?</Space>
        </Typography.Link>
      </Dropdown>
    </Space>
  );
};

export default App;
