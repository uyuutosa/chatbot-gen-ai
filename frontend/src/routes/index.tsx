import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  component: Index,
});

function Index() {
  return (
    <div className="p-2">
      <h3>Welcome Home!</h3>
      <h1 className="bg-teal-400">Vite + React</h1>
      <div className="bg-blue-500 text-white p-4">Hello, Tailwind CSS!</div>
    </div>
  );
}
