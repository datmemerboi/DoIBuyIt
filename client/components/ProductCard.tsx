import React from "react";

import Button from "@/components/Button";

interface ProductCardProps {
  title: string;
  brand: string;
  vendor: string;
  price: number;
  image?: string;
}

const cardStyle: string =
  "w-11/12 bg-white lg:w-3/12 lg:bg-white sm:w-3/12 sm:bg-red-100 md:w-3/12 md:bg-yellow-200 bg-gray-100 rounded-lg shadow-lg p-4 m-4 flex flex-col";
const imageContainerStyle: string =
  "object-contain flex justify-center align-center w-full h-44";
const cardImageStyle: string = "object-contain lg:h-full";
const textContainerStyle: string = "flex flex-col";
const productTitleStyle: string = "text-base font-bold md:text-xl";
const productVendorStyle: string = "text-m text-gray-500";
const productPriceStyle: string = "p-2 text-2xl font-medium";

export default function ProductCard({
  title,
  price,
  brand,
  vendor,
  image
}: ProductCardProps) {
  const renderVendor = () => <p className={productVendorStyle}>@ {vendor}</p>;
  // TODO: Show cheaper vendor
  const renderPrice = () => {
    if (price) {
      // TODO: Indicate vendor-price rise/fall
      return <p className={productPriceStyle}>${price}</p>;
    }
  };
  const renderImage = () => {
    if (image && image !== "") {
      return (
        <div className={imageContainerStyle}>
          <img src={image} alt={title} className={cardImageStyle} />
        </div>
      );
    }
  };
  const renderText = () => (
    <div className={textContainerStyle}>
      <h3 className={productTitleStyle}>{title}</h3>
      {renderPrice()}
      <p className={productVendorStyle}>{brand}</p>
    </div>
  );
  return (
    <div className={cardStyle}>
      {renderImage()}
      {renderText()}
      {renderVendor()}
      <Button text={"Open this product"} wide={true} />
    </div>
  );
}
