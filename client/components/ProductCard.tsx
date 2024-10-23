import React from "react";
import Image from "next/image";

import Button from "@/components/Button";

interface ProductCardProps {
  title: string;
  description: string;
  price?: number;
  image?: string;
}

const cardStyle: string =
  "w-11/12 lg:w-4/12 lg:bg-blue-100 sm:w-3/12 sm:bg-red-100 md:w-5/12 md:bg-yellow-200 bg-gray-100 rounded-lg shadow-lg p-4 m-4 flex flex-col";
const imageContainerStyle: string = "object-contain";
const cardImageStyle: string = "object-contain w-11/12";
const textContainerStyle: string = "flex flex-col";
const productTitleStyle: string = "text-xl font-bold";
const productDescriptionStyle: string = "text-m text-gray-500";
const productPriceStyle: string = "p-2 text-2xl font-medium";

export default function ProductCard({
  title,
  price,
  description
}: ProductCardProps) {
  const renderPrice = () => {
    if (price) {
      return <p className={productPriceStyle}>${price}</p>;
    }
  };
  const renderText = () => (
    <div className={textContainerStyle}>
      <h3 className={productTitleStyle}>{title}</h3>
      {renderPrice()}
      <p className={productDescriptionStyle}>{description}</p>
      <Button text={"Open this product"} wide={true} />
    </div>
  );
  return (
    <div className={cardStyle}>
      <div className={imageContainerStyle}>
        {/* <Image
          fill={true}
          src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
          alt="Example"
          className={cardImageStyle}
        /> */}
      </div>
      {renderText()}
    </div>
  );
}
