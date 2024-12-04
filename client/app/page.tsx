import React from "react";

import Input from "@/components/Input";
import ProductCard from "@/components/ProductCard";

const productCardsContainer = "flex flex-row flex-wrap justify-center";

type Price = {
  product: {
    barcode: string;
    name: string;
    brand: string;
    image: string;
  };
  price: string | number;
  viewed_date: string;
  tentative_end_date: string;
  cost_per_unit: number;
  cost_per_unit_measure: string;
  vendor_product: string;
};

const App: React.FC = async () => {
  let prices: Price[] = [];
  try {
    let prodReq = await fetch("http://localhost:8080/prices?format=json");
    let pricesPage = await prodReq.json();
    prices = pricesPage.results;
  } catch (error) {
    console.error(error);
  }

  return (
    <div>
      <div className="flex flex-col flex-wrap justify-center">
        <div className="flex flex-row justify-center">
          <h1 className="text-4xl font-bold">Do I Buy It?</h1>
        </div>
        {/* <div className="flex flex-row justify-center">
          <Input type="main-search" placeholder="Search for product..." />
        </div> */}

        <div className={productCardsContainer}>
          {prices.length &&
            prices.map((priceObj) => (
              <ProductCard
                key={priceObj.product.barcode}
                title={priceObj.product.name}
                vendor="Woolworths"
                brand={priceObj.product.brand}
                price={priceObj.price > 0 ? priceObj.price : "N/A"}
                image={priceObj.product.image}
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
