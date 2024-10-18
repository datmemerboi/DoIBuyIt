import React from "react";

interface InputProps {
  type: string;
  placeholder?: string;
}

export default function Input({ type, placeholder }: InputProps) {
  const regularInputStyle: string =
    "width-1 p-2 m-2 border-2 border-gray-300 rounded-md";

  const mainSearchStyle: string =
    "w-9/12 p-8 m-2 border-b-8 border-gray-400 bg-transparent font-bold text-2xl";

  return (
    <>
      <input
        type={type}
        className={type === "main-search" ? mainSearchStyle : regularInputStyle}
        placeholder={placeholder ?? "Enter text here"}
      />
    </>
  );
}
