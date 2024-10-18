import React from "react";

interface ButtonProps {
  text: string;
  onClick?: () => void;
  wide?: boolean;
}

const buttonStyle: string =
  "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded";

export default function Button({ text, onClick, wide }: ButtonProps) {
  return (
    <button
      className={[buttonStyle, wide ? "w-full" : ""].join(" ")}
      onClick={onClick}
    >
      {text}
    </button>
  );
}
