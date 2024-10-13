"use client";

import { ConfigProvider, theme } from "antd";

export default function ThemeWrapper({ children }) {
  const { darkAlgorithm, compactAlgorithm } = theme;
  return (
    <ConfigProvider
      theme={{
        algorithm: compactAlgorithm,
      }}
    >
      {children}
    </ConfigProvider>
  );
}
