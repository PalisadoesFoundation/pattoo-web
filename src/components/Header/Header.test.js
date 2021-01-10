// React imports
import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom/extend-expect";

// Module imports
import Header from "./Header";

describe("Test Suite for the Header Component", () => {
  test("Render test for the Header Component", () => {
    render(<Header />);
    expect(screen.getByRole("banner")).toBeInTheDocument();
    expect(screen.getByRole("heading")).toBeInTheDocument();
  });
});
