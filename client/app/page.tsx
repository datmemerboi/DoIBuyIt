import React from "react";

import Input from "@/components/Input";
import ProductCard from "@/components/ProductCard";

const productCardsContainer = "flex flex-row flex-wrap justify-center";

const App: React.FC = async () => {
  let prodReq = await fetch("http://localhost:8080/products");
  let products = await prodReq.json();

  return (
    <div>
      <div className="flex flex-col flex-wrap justify-center">
        <div className="flex flex-row justify-center">
          <Input type="main-search" placeholder="Search for product..." />
        </div>

        <div className={productCardsContainer}>
          {products.map((product) => (
            <ProductCard
              key={product.barcode}
              title={product.name}
              vendor="Woolworths"
              brand={product.brand}
              price={35.01}
              image={product.image}
            />
          ))}
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
export const metadata = {
  title: "Do I Buy It?",
  description: "A simple price comparison site"
};
