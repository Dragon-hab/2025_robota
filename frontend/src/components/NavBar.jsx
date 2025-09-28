export default function NavBar({ user, onLogout }) {
  return (
    <nav className="flex justify-between items-center bg-gray-800 text-white px-4 py-2">
      <h1 className="font-bold">Event Platform</h1>
      <div>
        {user ? (
          <button onClick={onLogout} className="hover:underline">
            Вихід
          </button>
        ) : (
          <span>Гість</span>
        )}
      </div>
    </nav>
  );
}