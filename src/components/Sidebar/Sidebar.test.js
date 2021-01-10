// React imports
import React from "react";
import { render, screen, within } from "@testing-library/react";
import "@testing-library/jest-dom/extend-expect";

// Module imports
import Sidebar from "./Sidebar";

describe("Sidebar", () => {
  test("Render test for the sidebar. It should render list 5 items", () => {
    render(<Sidebar />);

    // Retrieve all list items
    const list = screen.getByRole("list");
    const { getAllByRole } = within(list);
    const listItems = getAllByRole("listitem");

    // Assertions
    expect(listItems.length).toBe(4);
    expect(screen.getByRole("list")).toBeInTheDocument();
  });

  test("Toggle test for the sidebar", () => {});

  test("Checks if the appropriate text areas are in the document ", () => {
    render(<Sidebar />);
    expect(screen.getByText("Dashboard")).toBeInTheDocument();
    expect(screen.getByText("Settings")).toBeInTheDocument();
    expect(screen.getByText("Agents")).toBeInTheDocument();
    expect(screen.getByText("Favorite")).toBeInTheDocument();
  });
});
