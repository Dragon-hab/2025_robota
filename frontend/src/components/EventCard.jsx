export default function EventCard({ title, date, location, onDetailsClick }) {
  return (
    <div className="border p-4 rounded shadow hover:shadow-lg transition bg-gradient-to-br from-blue-50 to-white">
      <h2 className="text-lg font-bold text-blue-700">{title}</h2>
      <p className="text-sm text-gray-600">{date}</p>
      <p className="text-sm text-gray-600">{location}</p>
      <button
        onClick={onDetailsClick}
        className="mt-2 text-blue-600 hover:text-blue-800 font-semibold"
      >
        Детальніше
      </button>
    </div>
  );
}