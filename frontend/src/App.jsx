import { useState } from "react";
import EventsPage from "./pages/EventsPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import FeedbackPage from "./pages/FeedbackPage";
import NavBar from "./components/NavBar";

export default function App() {
  const [user, setUser] = useState(null);
  const [page, setPage] = useState("login");

  function renderPage() {
    if (!user) {
      return page === "register"
        ? <RegisterPage onRegister={setUser} />
        : <LoginPage onLogin={setUser} />;
    }
    if (page === "events") return <EventsPage />;
    if (page === "feedback") return <FeedbackPage />;
    return <EventsPage />;
  }

  return (
    <div>
      <NavBar user={user} onLogout={() => setUser(null)} />
      <div className="p-4">
        <div className="flex gap-4 mb-4">
          {!user && (
            <>
              <button onClick={() => setPage("login")} className="underline">Вхід</button>
              <button onClick={() => setPage("register")} className="underline">Реєстрація</button>
            </>
          )}
          {user && (
            <>
              <button onClick={() => setPage("events")} className="underline">Події</button>
              <button onClick={() => setPage("feedback")} className="underline">Відгуки</button>
            </>
          )}
        </div>
        {renderPage()}
      </div>
    </div>
  );
}
