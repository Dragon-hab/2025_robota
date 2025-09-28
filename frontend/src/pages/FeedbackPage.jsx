import { useState, useEffect } from "react";
import Button from "../components/Button";

export default function FeedbackPage() {
  const [feedback, setFeedback] = useState("");
  const [status, setStatus] = useState(null);
  const [allFeedback, setAllFeedback] = useState([]);

  useEffect(() => {
    // 🔹 Тимчасові заглушки (приклади відгуків)
    setAllFeedback([
      { id: 1, text: "Дуже сподобалася подія, все було на високому рівні!" },
      { id: 2, text: "Було цікаво, але хотілося б більше практики." },
      { id: 3, text: "Дякую організаторам, чекаю наступного заходу!" }
    ]);
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    if (!feedback.trim()) return;
    const newFeedback = { id: Date.now(), text: feedback };
    setAllFeedback([newFeedback, ...allFeedback]);
    setStatus("✅ Дякуємо за ваш відгук!");
    setFeedback("");
  }

  return (
    <div className="p-6 max-w-md mx-auto bg-white shadow rounded">
      <h2 className="text-xl font-bold mb-4 text-indigo-700">Залиште відгук</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <textarea
          placeholder="Ваш відгук..."
          value={feedback}
          onChange={(e) => setFeedback(e.target.value)}
          className="border p-2 rounded h-28 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        />
        <Button>Надіслати</Button>
      </form>

      {status && <p className="mt-4 text-green-600 font-semibold">{status}</p>}

      <div className="mt-6">
        <h3 className="font-bold text-blue-600 mb-2">Відгуки інших учасників:</h3>
        <ul className="space-y-2">
          {allFeedback.map((f) => (
            <li key={f.id} className="p-3 bg-gradient-to-r from-blue-50 to-indigo-50 border rounded shadow-sm">
              {f.text}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
