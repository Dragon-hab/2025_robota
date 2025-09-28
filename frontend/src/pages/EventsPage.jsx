import { useEffect, useState } from "react";
import EventCard from "../components/EventCard";

export default function EventsPage() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // 🔹 Тестові дані (замість бекенду)
    setEvents([
      { id: 1, title: "Конференція AI 2025", start_at: "2025-10-10 10:00", location: "Київ" },
      { id: 2, title: "Meetup з веброзробки", start_at: "2025-11-05 18:00", location: "Львів" },
      { id: 3, title: "Hackathon 2025", start_at: "2025-12-01 09:00", location: "Одеса" }
    ]);
  }, []);

  return (
    <div className="p-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {events.map((event) => (
        <EventCard
          key={event.id}
          title={event.title}
          date={event.start_at}
          location={event.location}
          onDetailsClick={() => alert(`Подія: ${event.title}`)}
        />
      ))}
    </div>
  );
}
