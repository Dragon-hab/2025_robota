import { render, screen } from "@testing-library/react";
import EventsPage from "../pages/EventsPage";

test("EventsPage: рендерить список подій", () => {
  render(<EventsPage />);
  expect(screen.getByText(/Конференція/i)).toBeInTheDocument();
});
