import { render, screen, fireEvent } from "@testing-library/react";
import LoginPage from "../pages/LoginPage";

test("LoginPage: логін викликає onLogin при введених email+password", () => {
  const onLogin = vi.fn();
  render(<LoginPage onLogin={onLogin} />);

  fireEvent.change(screen.getByPlaceholderText("Email"), { target: { value: "a@b.com" } });
  fireEvent.change(screen.getByPlaceholderText("Пароль"), { target: { value: "123456" } });

  fireEvent.click(screen.getByRole("button", { name: /увійти/i }));
  expect(onLogin).toHaveBeenCalled();
});
