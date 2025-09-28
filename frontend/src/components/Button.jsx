export default function Button({ children, onClick, disabled }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className="px-4 py-2 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded shadow 
                 hover:from-blue-600 hover:to-indigo-700 disabled:from-gray-400 disabled:to-gray-500"
    >
      {children}
    </button>
  );
}
