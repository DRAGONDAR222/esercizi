export default function App() {
  const items = ["Mela", "Banana", "Arancia"];

  return (
    <ul>
      {items.map((frutto, i) => (
        <li key={i}>{frutto}</li>
      ))}
    </ul>
  );
}
