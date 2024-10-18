import React from "react";
import Head from "next/head";

import Input from "@/components/Input";
import ProductCard from "@/components/ProductCard";

const App: React.FC = () => {
  // const { Search } = Input;
  // const { Meta } = Card;

  // const items: MenuProps["items"] = [
  //   {
  //     key: "1",
  //     label: "Woolworths"
  //   },
  //   {
  //     key: "2",
  //     label: "Coles"
  //   }
  // ];

  return (
    <>
      <Head>
        <title>Do I Buy It??</title>
      </Head>

      <div className="flex flex-col flex-wrap justify-center">
        <div className="flex flex-row justify-center">
          <Input type="main-search" placeholder="Search for product..." />
        </div>

        <ProductCard title="abc" description="lorem ipsum" price={35} />
      </div>
    </>
    /* <Search
          size="large"
          addonBefore="Do I Buy"
          placeholder="Search Here"
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
      </Flex>
      <ProductCard title={"ABC"} description={"def lorem ipsum"} /> */
  );
};

export default App;
