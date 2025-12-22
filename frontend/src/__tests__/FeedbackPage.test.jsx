import { render, screen, fireEvent } from "@testing-library/react";
import FeedbackPage from "../pages/FeedbackPage";

test("FeedbackPage: не додає відгук якщо поле пусте", () => {
  render(<FeedbackPage />);

  // натискаємо "Надіслати" без тексту
  fireEvent.click(screen.getByRole("button", { name: /надіслати/i }));

  // Повідомлення про успіх НЕ має з'явитися
  expect(screen.queryByText(/дякуємо/i)).not.toBeInTheDocument();
});
