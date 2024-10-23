import React from "react";
import Head from "next/head";

import Input from "@/components/Input";
import ProductCard from "@/components/ProductCard";

const productCardsContainer = "flex flex-row flex-wrap justify-center";

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
    <div>
      <Head>
        <title>Do I Buy It??</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>

      <div className="flex flex-col flex-wrap justify-center">
        <div className="flex flex-row justify-center">
          <Input type="main-search" placeholder="Search for product..." />
        </div>

        <div className={productCardsContainer}>
          <ProductCard title="abc" description="lorem ipsum" price={35.01} />
          <ProductCard title="abc" description="lorem ipsum" price={35.50} />
          <ProductCard title="abc" description="lorem ipsum" price={35.00} />
          <ProductCard title="abc" description="lorem ipsum" price={35.12} />
        </div>
      </div>
    </div>
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
