import * as Dialog from '@radix-ui/react-dialog';
import { ScrollArea } from '@radix-ui/react-scroll-area';
import { createFileRoute } from '@tanstack/react-router'
import { useState } from 'react';

export const Route = createFileRoute('/chat')({
  component: Chatbot,
})

function Chatbot() {
  const [messages, setMessages] = useState<{ id: string; text: string; type: "user" | "bot" }[]>([]);
  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages((prev) => [...prev, { id: crypto.randomUUID(), text: input, type: "user" }]);
    setMessages((prev) => [...prev, { id: crypto.randomUUID(), text: "こんにちは！", type: "bot" }]);
    setInput("");
  };

  return (
    <Dialog.Root>
      <Dialog.Trigger className="fixed bottom-4 right-4 p-3 bg-blue-600 text-white rounded-full">💬</Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black opacity-50" />
        <Dialog.Content className="fixed bottom-16 right-4 w-80 bg-white shadow-lg p-4 rounded-lg">
          <ScrollArea className="h-64 overflow-y-auto border p-2">
            {messages.map((msg) => (
              <div key={msg.id} className={`p-2 rounded-md my-1 ${msg.type === "user" ? "bg-blue-500 text-white self-end" : "bg-gray-300 text-black"}`}>
                {msg.text}
              </div>
            ))}
          </ScrollArea>
          <div className="flex gap-2 mt-4">
            <input className="border flex-1 p-2 rounded" value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={(e) => e.key === "Enter" && sendMessage()} />
            <button type="button" className="bg-blue-600 text-white p-2 rounded" onClick={sendMessage}>送信</button>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}